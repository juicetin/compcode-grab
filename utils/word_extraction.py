from PIL import Image
from scipy.misc import imsave
import numpy as np
from pytesseract import image_to_string
from re import search as regexp_search

import pdb

black = np.array([0,0,0])
white = np.array([255,255,255])

def crop_non_word(im):
    bounds = (210, 190, 890, 330)
    return im.crop(bounds).save('tmp.png')

def binarize_pixel(pixel):
    if (pixel < 105).all() == True:
        return black
    else:
        return white

def monochrome(im):
    new_im = np.array(im)
    for row in range(new_im.shape[0]):
        for col in range(new_im.shape[1]):
            new_im[row][col] = binarize_pixel(new_im[row][col])

    return new_im

def retrieve_word_from_processed_image(im):
    word = image_to_string(im)
    # TODO when this fails, error should be caught, and 
    # original supposedly correct image instead put into
    # the incorrect pile
    return regexp_search("[a-zA-Z]+", word).group()

def get_word(img_path):
    # Crop image down to the word area
    im = Image.open(img_path)
    crop_non_word(im)

    # Process to black and white
    im = Image.open('tmp.png')
    bw_im = monochrome(im)
    imsave('bw_tmp.png', bw_im)

    im = Image.open('bw_tmp.png')
    return retrieve_word_from_processed_image(im)
