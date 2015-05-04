import cv2 as cv
import argparse
import os
import img_utils as iu
import numpy as np

"""
This script shows the results of applying threshold values to the input image
and ask the user whether he wants to save the outputted image or not. Also, it
can be used in the CLI.
"""


test_image = os.path.abspath(os.path.join(os.path.dirname("__file__"),
                                          "../resources/", "input_ftm.png"))


def adaptive_gaussian_apply(input_file, max_val=255, thresh_type=0,
                            block_size=11, c=5):
    """
    >>> isinstance(adaptive_gaussian_apply(test_image), np.ndarray)
    True

    >>> adaptive_gaussian_apply(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> adaptive_gaussian_apply("")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> adaptive_gaussian_apply("fakeRoute")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.

    >>> adaptive_gaussian_apply(test_image, max_val=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> adaptive_gaussian_apply(test_image, max_val=260)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> adaptive_gaussian_apply(test_image, thresh_type=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Threshold_type value must be between 0 and 4.

    >>> adaptive_gaussian_apply(test_image, thresh_type=6)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Threshold_type value must be between 0 and 4.

    >>> adaptive_gaussian_apply(test_image, block_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Block size value must be greater than 0.

    >>> adaptive_gaussian_apply(test_image, block_size=2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Block size value must be odd.

    >>> adaptive_gaussian_apply(test_image, c='a')
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Constraint must be integer.
    """

    # Checking arguments
    check_threshold(max_val)
    check_thresh_type(thresh_type)
    check_block_size(block_size)
    check_c(c)

    # Loading image
    image = iu.get_image(input_file, 0)

    return cv.adaptiveThreshold(image, max_val, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                thresh_type, block_size, c)


def adaptive_mean_apply(input_file, max_val=255, thresh_type=0,
                        block_size=11, c=5):
    """
    >>> isinstance(adaptive_mean_apply(test_image), np.ndarray)
    True

    >>> adaptive_mean_apply(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> adaptive_mean_apply("")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> adaptive_mean_apply("fakeRoute")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.

    >>> adaptive_mean_apply(test_image, max_val=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> adaptive_mean_apply(test_image, max_val=260)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> adaptive_mean_apply(test_image, thresh_type=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Threshold_type value must be between 0 and 4.

    >>> adaptive_mean_apply(test_image, thresh_type=6)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Threshold_type value must be between 0 and 4.

    >>> adaptive_mean_apply(test_image, block_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Block size value must be greater than 0.

    >>> adaptive_mean_apply(test_image, block_size=2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Block size value must be odd.

    >>> adaptive_mean_apply(test_image, c='a')
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Constraint must be integer.
    """

    # Checking arguments
    check_threshold(max_val)
    check_thresh_type(thresh_type)
    check_block_size(block_size)
    check_c(c)

    # Loading image
    image = iu.get_image(input_file, 0)

    return cv.adaptiveThreshold(image, max_val, cv.ADAPTIVE_THRESH_MEAN_C,
                                thresh_type, block_size, c)


def apply(input_file, thresh_val=200, new_value=255, thresh_type=0):
    """
    >>> isinstance(apply(test_image), np.ndarray)
    True

    >>> apply(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> apply("")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> apply("fakeRoute")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.

    >>> apply(test_image, thresh_val=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> apply(test_image, thresh_val=260)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> apply(test_image, new_value=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> apply(test_image, new_value=260)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> apply(test_image, thresh_type=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Threshold_type value must be between 0 and 4.

    >>> apply(test_image, thresh_type=6)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Threshold_type value must be between 0 and 4.
    """
    # Checking arguments
    check_threshold(thresh_val)
    check_threshold(new_value)
    check_thresh_type(thresh_type)

    # Loading image
    image = iu.get_image(input_file, 0)

    # Thresholding
    th, img_thresh = cv.threshold(image, thresh_val, new_value, thresh_type)

    return img_thresh


# CHECKING ARGUMENTS


def check_block_size(block_size):

    if block_size < 0:
        raise ValueError("Block size value must be greater than 0.")

    if block_size % 2 == 0:
        raise ValueError("Block size value must be odd.")
    return 0


def check_c(c):

    if not isinstance(c, int):
        raise ValueError("Constraint must be integer.")
    return 0


def check_threshold(value):

    if int(value) < 0 or int(value) > 255:
        raise ValueError("All threshold values must be between 0 and 255.")
    return 0


def check_thresh_type(value):

    if int(value) < 0 or int(value) > 4:
        raise ValueError("Threshold_type value must be between 0 and 4.")
    return 0


# CLI SETTINGS


if __name__ == '__main__':
        
        # CLI arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--input", required="True", 
                        help="Path to the input file.")
        ap.add_argument("-t", "--threshold", 
                        help="Pixel value to threshold.")
        args = vars(ap.parse_args())
        
        # Loading values
        input_file = args["input"]
        thresh_val = args["threshold"]

        # Checking the input values:
        if thresh_val is None:
                thresh_val = 200
        
        apply(input_file, thresh_val)
