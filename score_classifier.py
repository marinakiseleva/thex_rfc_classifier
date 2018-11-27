from sklearn.metrics import precision_recall_fscore_support
import numpy as np
def get_average_correct_probability(clf_classes, prob_dists, y_test):
    """
    Gets the average probability for the transients that were correctly classified.
    Represents the 'peakiness' of classifier.
    :param clf_classes: The classifiers' classes, in the same order they come up in predict_proba
    :param prob_dists: The probability distribution for the test data; results from predict_proba
    :param y_test: The y_test data (actual)
    """ 
    max_correct_probs = [] # Probability for each correctly predicted transient
    for index, dist in enumerate(prob_dists):
        # Each dist has the probability for each class, in classifiers classe
        predicted_max_class_index = np.argmax(dist)
        predicted_max_class = clf_classes[predicted_max_class_index]
        actual_class = y_test.values[index]
        # Check if classifier predicted correctly (using max probability as prediction)
        if actual_class == predicted_max_class:
            max_correct_probs.append(dist[predicted_max_class_index])
        else:
            max_correct_probs.append(0)
    np_max_correct_probs = np.array(max_correct_probs)
    # avg_prob is the average transient probability of correctly predicted transients
    avg_prob = np.average(np_max_correct_probs[np_max_correct_probs>0])
    return avg_prob

def rate_classifier(classes, predictions, prob_dists, y_test):
    """
    Rates classifier by the number of transients, 
    the average recall among classes with recall > 0, 
    and the average correct probability for transients.
    :param classes: classes predicted by classifier (clf.classes_)
    :param predictions: the target predictions 
    :param prob_dists: probability distribution for each test sample (clf.predict_proba(X_test))
    :param y_test: actual transient value for test set
    
    """
    p, r, f, s = precision_recall_fscore_support(y_test, predictions, average=None, labels=np.unique(predictions))
    non0_transient_recalls = r[r>0]
    # Number transients where recall > 0 (Number of transients)
    num_transients = len(non0_transient_recalls) 
    # Avg recall for transients whose recall > 0, not including Other
    for index, class_num in enumerate(classes):
        if class_num == 100 and len(non0_transient_recalls) > index:
            non0_transient_recalls = np.delete(non0_transient_recalls, index)
    avg_recall = np.average(non0_transient_recalls) 


    # Avg correct probability (peakiness)
    avg_cp = get_average_correct_probability(classes, prob_dists, y_test)
    return num_transients, round(avg_recall, 3), round(avg_cp,3)