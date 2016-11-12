from PIL import Image
from scipy.misc import imsave
import numpy as np
from pytesseract import image_to_string
from re import search as regexp_search
import sys

import pdb

black = np.array([0,0,0])
white = np.array([255,255,255])

def crop_non_word(im):
    """
    Crops original sized image to only include roughly the area where the codeword is.
    May need to expand area slightly for longer words, as any longer than about 8 may
    get cut off (though any longer than 8 have yet to be seen based on anecdotal
    evidence)
    """
    bounds = (210, 190, 890, 330)
    return im.crop(bounds).save('tmp.png')

def binarize_pixel(pixel):
    """
    Classifies pixels as black or white
    """
    if (pixel < 105).all() == True:
        return black
    else:
        return white

def monochrome(im):
    """
    Converts an image to all black and white
    """
    new_im = np.array(im)
    for row in range(new_im.shape[0]):
        for col in range(new_im.shape[1]):
            new_im[row][col] = binarize_pixel(new_im[row][col])

    return new_im

def retrieve_word_from_processed_image(im):
    """
    Use OCR to extract word from a processed image
    """
    word = image_to_string(im)
    # TODO when this fails, error should be caught, and 
    # original supposedly correct image instead put into
    # the incorrect pile
    try:
        return regexp_search("[a-zA-Z]+", word).group()
    except AttributeError:
        return None

def get_word(img_path):
    """
    Extracts word given the original screenshot from the TV channel's live stream
    """
    # Crop image down to the word area
    im = Image.open(img_path)
    crop_non_word(im)

    # Process to black and white
    im = Image.open('tmp.png')
    bw_im = monochrome(im)
    imsave('bw_tmp.png', bw_im)

    im = Image.open('bw_tmp.png')
    word = retrieve_word_from_processed_image(im)
    if word == None:
        raise ValueError('No word found in image: [{}]. Most likely incorrect image classification.'.format(img_path))
