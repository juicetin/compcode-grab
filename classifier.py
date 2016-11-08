from os.path import isfile, join
from os import listdir
from scipy import misc
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

def img_features_from_dir(path):
    imgs = []
    for f in listdir(path):
        imgs.append(misc.imread(path+f))

    return np.array(imgs)

def gen_img_and_labels(imgs, label):
    return imgs.reshape(imgs.shape[0], -1), np.full(imgs.shape[0], label, dtype=np.int64)

def reduce_img_features(imgs, skip):
    return imgs[:,::skip]

# pull features of images
correct_imgs = img_features_from_dir('correct_imgs/')
incorrect_imgs = img_features_from_dir('incorrect_imgs/')

# flatten and assign labels
correct_imgs, correct_labels = gen_img_and_labels(correct_imgs, 1)
incorrect_imgs, incorrect_labels = gen_img_and_labels(incorrect_imgs, 0)

# merge image lists
imgs = np.concatenate((correct_imgs, incorrect_imgs))
imgs = reduce_img_features(imgs, 5)
labels = np.concatenate((correct_labels, incorrect_labels))

knn = KNeighborsClassifier(1)
knn.fit(imgs, labels)

