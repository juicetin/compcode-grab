from sklearn.model_selection import StratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import numpy as np

def strat_kfold(imgs, labels):
    skf = StratifiedKFold(n_splits=5)
    skf.get_n_splits(imgs, labels)
    for train_index, test_index in skf.split(imgs, labels):
        knn = KNeighborsClassifier()
        knn.fit(imgs[train_index], labels[train_index])
        label_preds = knn.predict(imgs[test_index])
        acc = accuracy_score(labels[test_index], label_preds)
        print(acc)

def test_downsample_images(imgs, labels):
    """
    Checks how many features can be cut out and still correctly
    predict the cash cow images.
    Looks like skipping every 4995 *may* work
    """
    for skip in np.arange(5, 5005, 5):
        strat_kfold(imgs[:,::skip], labels)
