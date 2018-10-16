
import sys
import argparse

from classifier import RFClassifier
import data_prep
import data_init


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
    X, y = data_prep.prep_data(data_df, col_list, 
                     min_redshift, 
                     max_redshift, 
                     subsample,
                     oneall)
    print("Rows run through classifier in training data: " + str(X.shape[0]))
    X_train, X_test, y_train, y_test = data_prep.split_train_test(X, y)

    rfclassifier = RFClassifier()
    clf, predictions = rfclassifier.run_rm(X_train, X_test, y_train, y_test)
    # rfclassifier.get_feature_importance(clf, X_train)
    print(rfclassifier.get_performance(y_test, predictions))
    return clf, X_train, X_test, y_test, predictions

def main():
    parser = argparse.ArgumentParser(description='Classify transients')
    parser.add_argument('-file_name', metavar='N', type=str,
                        help='File name, relative to this directory')
    parser.add_argument('-col_list', metavar='N', type=str,
                        help='List of columns')
    parser.add_argument('-min_rs', metavar='N', type=str,
                        help='Minimum redshift')    
    parser.add_argument('-max_rs', metavar='N', type=str,
                        help='Max redshift')   
    parser.add_argument('-subsample', metavar='N', type=str,
                        help='Transient type to subsample on')   
    parser.add_argument('-oneall', metavar='N', type=str,
                        help='Transient type to do one versus all classification on')  

    args = parser.parse_args()


    data_df = data_init.collect_data(args.file_name)

    data_df.drop(labels = ['AllWISE_IsVar'], axis='columns', inplace = True)
    col_list = [col for col in list(data_df) if str(args.col_list) in col and 'Err' not in col]

    print(col_list)

    clf, X_train, X_test, y_test, predictions = run_analysis(data_df = data_df,
                            col_list = col_list,  
                            min_redshift = float(args.min_rs), 
                            max_redshift = float(args.max_rs),
                            subsample = str(args.subsample),
                            oneall = str(args.oneall))

if __name__ == '__main__':
    main()








