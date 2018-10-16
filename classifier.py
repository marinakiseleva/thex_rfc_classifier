import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report


class RFClassifier:
    def __init__(self):
        self.clf = RandomForestClassifier(max_depth = 8, random_state = 0, class_weight = "balanced")

    def run_rm(self, X_train, X_test, y_train, y_test):
        self.clf.fit(X_train, y_train)
        predictions = self.clf.predict(X_test)
        return self.clf, predictions

    def get_performance(self, y_test, predictions):
        return classification_report(y_test, predictions)

    def get_feature_importance(self, X_train):
        feature_importances = pd.DataFrame(self.clf.feature_importances_,
                                           index = X_train.columns,
                                           columns=['importance'])
        feature_importances = feature_importances.sort_values('importance', 
                                                              ascending = False)
        return feature_importances

    def get_probabilities(self, class_num):
        """
        Gets probabilities for specific transient class
        :param class_num: the index of the class code corresponding to transient class, from self.clf.classes_
        """
        pps = self.clf.predict_proba(X_test)
        class_probs = []
        for probs in pps:
            for idx, val in enumerate(probs):
                cur_class = self.clf.classes_[idx]
                if cur_class == class_num: 
                    class_probs.append(val)
        return class_probs