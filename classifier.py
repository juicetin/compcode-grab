from os.path import isfile, join
from os import listdir
from scipy import misc
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

path = 'correct_imgs/'
imgs = []
for f in listdir('correct_imgs/'):
    imgs.append(misc.imread(path+f))

imgs = np.array(imgs)
imgs = imgs.reshape(imgs.shape[0], -1)
knn = KNeighborsClassifier(1)
