from sklearn.feature_selection import mutual_info_classif
import pandas as pd


def get_mutual_information(X,y):
	mi = mutual_info_classif(X,y)
	# print(list(X))
	print(mi)

def get_feature_correlation(X,y):
	print(X.corr())
	X.corr().to_csv("Feature_Correlation.csv")