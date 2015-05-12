import cv2 as cv
import img_utils as iu
import numpy as np
import argparse
import os

"""
This script implement a series of functions to implement the most commonly used
threshold functions in OpenCV.
"""


test_image = os.path.abspath(os.path.join(os.path.dirname("__file__"),
                                          "../resources/", "input_ftm.png"))


def adaptive_threshold(input_file, max_val=255, thresh_type=0, block_size=11,
                       c=5, mode=0):
    """
    >>> isinstance(adaptive_threshold(test_image), np.ndarray)
    True

    >>> isinstance(adaptive_threshold(test_image, mode=1), np.ndarray)
    True

    >>> adaptive_threshold(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> adaptive_threshold("")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> adaptive_threshold("fakeRoute")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.

    >>> adaptive_threshold(test_image, max_val=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> adaptive_threshold(test_image, max_val=260)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> adaptive_threshold(test_image, thresh_type=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Threshold_type value must be between 0 and 4.

    >>> adaptive_threshold(test_image, thresh_type=6)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Threshold_type value must be between 0 and 4.

    >>> adaptive_threshold(test_image, block_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Block size value must be greater than 0.

    >>> adaptive_threshold(test_image, block_size=2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Block size value must be odd.

    >>> adaptive_threshold(test_image, c='a')
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Constraint must be integer.
    >>> adaptive_threshold(test_image, c='a')
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Constraint must be integer.
    >>> adaptive_threshold(test_image, mode=-1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Mode values are: 0 (Gaussian) and 1 (Mean).
    """

    # Checking arguments
    check_threshold(max_val)
    check_thresh_type(thresh_type)
    check_block_size(block_size)
    check_c(c)

    if mode == 0:
        mode = cv.ADAPTIVE_THRESH_GAUSSIAN_C
    elif mode == 1:
        mode = cv.ADAPTIVE_THRESH_MEAN_C
    else:
        raise ValueError("Mode values are: 0 (Gaussian) and 1 (Mean).")

    # Loading image
    image = iu.get_image(input_file, 0)

    return cv.adaptiveThreshold(image, maxValue=max_val, thresholdType=thresh_type,
                                 blockSize=block_size, C=c, adaptiveMethod=mode)


def threshold(input_file, thresh_val=200, new_value=255, thresh_type=0):
    """
    >>> isinstance(threshold(test_image), np.ndarray)
    True

    >>> threshold(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> threshold("")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> threshold("fakeRoute")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.

    >>> threshold(test_image, thresh_val=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> threshold(test_image, thresh_val=260)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> threshold(test_image, new_value=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> threshold(test_image, new_value=260)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> threshold(test_image, thresh_type=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Threshold_type value must be between 0 and 4.

    >>> threshold(test_image, thresh_type=6)
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

        threshold(input_file, thresh_val)
