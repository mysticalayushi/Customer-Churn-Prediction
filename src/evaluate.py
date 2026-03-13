from sklearn.metrics import accuracy_score, confusion_matrix

def evaluate_model(y_true, y_pred):

    acc = accuracy_score(y_true, y_pred)
    cm = confusion_matrix(y_true, y_pred)

    return acc, cm