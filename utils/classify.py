import numpy as np
import sys
from os import listdir
from scipy import misc
import os
import pickle
from datetime import datetime

if __name__ == "__main__":

    # Check if classifier has been saved to disk yet
    try:
        knn = pickle.load(open('utils/clf.pickle', 'rb'))
    except FileNotFoundError:
        print('knn not generated yet!')
        sys.exit(0)

    path = 'imgs/'
    correct_path='correct_imgs/'
    cur_date = datetime.now().strftime('%a-%b-%d')
    for f in listdir(path):
        cur_img = misc.imread(path+f).reshape(1, -1)[:,::knn.skip]

        if knn.predict(cur_img) != 1:
            # Remove image if not word of the day
            # print('{} incorrect, removed.'.format(path+f))
            os.remove(path+f)
        # else:
        #     # Move file to 'correct images' directory!
        #     os.rename(path+f, correct_path+f)
        #     print('{} was a codeword image! moved to {}'.format(path+f, '../'+correct_path+cur_date+f))
