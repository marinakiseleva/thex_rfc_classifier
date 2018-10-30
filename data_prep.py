import pandas as pd
from sklearn.model_selection import train_test_split

import data_clean
from data_maps import cat_code


def sub_sample(df, count, col_val):
    """
    Sub-samples over-represented class
    :param df: the dataframe to manipulate
    :param count: number to set all classes to; if class has less than this, then just leave it
    """
    subsampled_df = pd.DataFrame()
    t_values = list(df[col_val].unique())
    # iterate through each claimed type group in dataset
    for ctg in t_values:
        cur_ctg = df[df[col_val] == ctg] #rows with this claimed type group
        num_rows = cur_ctg.shape[0] #number of rows
        if num_rows > count:
            # Reduce to the count number
            cur_ctg = cur_ctg.sample(n = count)
        subsampled_df = pd.concat([subsampled_df, cur_ctg])

    return subsampled_df

# def sub_sample(df, oversampled_val, undersampled_val, col_val):
#     """
#     Sub-samples over-represented class
#     :param df: the dataframe to manipulate
#     :param oversampled_val: the value of the class that is over-represented
#     :param col_val: the column name for the value
#     """
#     oversample = df[df[col_val] == oversampled_val]
#     undersample = df[df[col_val] == undersampled_val]
#     if undersample.shape[0] == 0:
#         raise ValueError('The undersampled transient class has no data for this redshift bin/feature set.')
#     keep_oversampled = oversample.sample(n = undersample.shape[0])
#     remaining = df[(df[col_val] != undersampled_val) & (df[col_val] != oversampled_val)]
#     sub_df = pd.concat([keep_oversampled, undersample, remaining])
   
#     return pd.concat([keep_oversampled, undersample, remaining])

def set_up_target(df_rs_band):
    """ 
    Sets up Target dataframe. Converts claimedtype_group strings to numeric codes 
    using cat_code map above
    """
    df_analyze = df_rs_band.copy()
    # Split out claimedtype_group into new dataframe
    y = df_analyze.claimedtype_group.to_frame(name='group')
    # Use category code numbers from cat_code dict, instead of strings
    y['cat_code'] = y.apply(lambda row:  cat_code[row.group] , axis=1)
    y = y.drop('group', axis = 1)
    return y


def set_up_source(df_analyze):
    X = df_analyze.copy()
    X = X.drop(['redshift', 'claimedtype_group'], axis = 1)
        
    return X

def split_train_test(X, y):
    # Split Training and Testing Data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=2)
    return X_train, X_test, y_train, y_test


def filter_columns(df, col_list):
    if col_list is None:
        print("Column list is none")
        col_list = []
        # print(list(df))
        full_list = ["Firefly",  "AllWISE", "Zoo"] # , "NSA", "SCOS"  "LEDA","MPAJHU"
        col_list = [col for col in list(df) if any(col_val in col for col_val in full_list)]
    df = df[col_list + ['redshift', 'claimedtype_group']] # Select features
    return df

def one_all(df, keep_cols, col):
    # print(df[keep_cols].value_counts())
    one = df[df['claimedtype_group'].isin(keep_cols)] #keep unique classes
    rem = df.loc[~df['claimedtype_group'].isin(keep_cols)].copy() #set to other
    rem[col] = 'Other'
    df = pd.concat([one, rem])

    return df

def prep_data(data_df, col_list, min_redshift, max_redshift, subsample = None, oneall = None):
    grouped_df = data_clean.group_cts(data_df) # group claimed types

    valid_df = filter_columns(df = grouped_df.copy(), col_list = col_list)

    
    #  Filter on redshift band
    df_rs_band = valid_df.loc[(valid_df.redshift > min_redshift) & (valid_df.redshift <= max_redshift)] 
    
    # print("Number of rows before dropping null " + str(df_rs_band.shape[0]))
    df_rs_band = df_rs_band.dropna() # Drop NULL before subsampling to ensure equal class distribution 
    # print("Number of rows after dropping null " + str(df_rs_band.shape[0]))

        
    # 1 class, oneall, versus all other classes (grouped into Other)

    if oneall is not None: 
        df_rs_band = one_all(df_rs_band, oneall, 'claimedtype_group')


    if subsample is not None:  #   Subsample Ia down to II P count
        df_rs_band = sub_sample(df = df_rs_band, 
                                count = subsample,
                                # oversampled_val = subsample, 
                                # undersampled_val = 'Ic', 
                                col_val = 'claimedtype_group')  
    # Return source and target split up
    y = set_up_target(df_rs_band)
    X = set_up_source(df_rs_band)
    
    return X, y