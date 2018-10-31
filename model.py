
import sys
import argparse

from rfclassifier import RFClassifier
import data_prep
import data_init
import feature_selection as fs


def run_analysis(data_df, col_list, min_redshift, max_redshift, subsample = None, oneall = None):
    """
    This is the main driver for the model. 
    :param data_df: dataframe with all data returned from collect_data function
    :param col_list: array of column names (features) on which to run the model
    :param min_redshift: minimum redshift to consider (exclusive)
    :param max_redshift: maximum redshift to consider (inclusive)
    :param subsample: claimed type group to subsample, must be one of the keys in the cat_code map, will be reduced
    to either the number of II P or the 'Other' category if doing oneall
    :param oneall: the transient class to classify against all others. Does One vs All classification on this specific
    claimed type group. Must be a claimed type group from the cat_code map. 
    """
    X, y = data_prep.prep_data(data_df, 
                     col_list, 
                     min_redshift, 
                     max_redshift, 
                     subsample,
                     oneall)
    # fs.get_mutual_information(X,y)
    # fs.get_feature_correlation(X,y)
    
    print("Rows run through classifier in training data: " + str(X.shape[0]))
    X_train, X_test, y_train, y_test = data_prep.split_train_test(X, y)

    rfclassifier = RFClassifier(X_train, X_test, y_train, y_test)
    clf, predictions = rfclassifier.run_rm()
    # rfclassifier.get_feature_importance(clf, X_train)
    print(rfclassifier.get_performance(y_test, predictions))
    return clf, X_train, X_test, y_test, predictions

def main():
    parser = argparse.ArgumentParser(description='Classify transients')
    parser.add_argument('-file_name', metavar='N', type=str,
                        help='REQUIRED: Data FITS file name, relative to this directory')
    parser.add_argument('-col_list', metavar='N', type=str,
                        help='List of strings by which to columns (features) will be filtered on. For example, passing in [PS1, ALLWISE] means the program will keep all columns that contain PS1 or ALLWISE in the column name.')
    parser.add_argument('-min_rs', metavar='N', type=str,
                        help='REQUIRED: Minimum redshift, exclusive')    
    parser.add_argument('-max_rs', metavar='N', type=str,
                        help='REQUIRED: Maximum redshift, inclusive')   
    parser.add_argument('-subsample', metavar='N', type=str,
                        help='OPTIONAL: Number to subsample over-represented classes to. For example, pass in 100 if you want all transients to have 100 or less samples.')   
    parser.add_argument('-oneall', metavar='N', type=str,
                        help='OPTIONAL: Transient type to do one versus all classification on. For example pass in Ia if you want to do Ia versus Other classification. Must be valid VALUE in data_maps.groupings.')  

    args = parser.parse_args()

    data_df = data_init.collect_data(args.file_name)
    
    
    # data_df.drop(labels = ['AllWISE_IsVar'], axis='columns', inplace = True)
    if args.col_list is not None:
        col_list = [col for col in list(data_df) if str(args.col_list) in col and 'Err' not in col]
    else:
        col_list = None
        print("Column list is empty")
    oneall = str(args.oneall) if args.oneall is not None else None
    subsample = str(args.subsample) if args.subsample is not None else None



    clf, X_train, X_test, y_test, predictions = run_analysis(data_df = data_df,
                            col_list = col_list,  
                            min_redshift = float(args.min_rs), 
                            max_redshift = float(args.max_rs),
                            subsample = subsample,
                            oneall = oneall)

if __name__ == '__main__':
    main()









