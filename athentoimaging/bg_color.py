import cv2 as cv
import threshold as th
import img_utils as iu
import numpy as np
import argparse
import os

"""
This script allows to clean an image with noisy background (ie: coloured
background).
"""

test_image = os.path.abspath(os.path.join(os.path.dirname("__file__"),
                                          "../resources/", "bgcolor.png"))


def remove_bg(input_file, thresh_val=0, window_size=3, block_size=11, c=5,
              mode=0, thresh_type=0):
    """
    >>> isinstance(remove_bg(test_image), np.ndarray)
    True

    >>> isinstance(remove_bg(test_image, mode=1), np.ndarray)
    True

    >>> isinstance(remove_bg(test_image, mode=2), np.ndarray)
    True

    >>> remove_bg(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> remove_bg("")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> remove_bg("fakeRoute")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.

    >>> remove_bg(test_image, window_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Window size value must be greater than 0.

    >>> remove_bg(test_image, window_size=2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Window size value must be odd.

    >>> remove_bg(test_image, block_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Block size value must be greater than 0.

    >>> remove_bg(test_image, block_size=2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Block size value must be odd.

    >>> remove_bg(test_image, c='a')
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Constraint must be integer.

    >>> remove_bg(test_image, thresh_type=-1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Threshold_type value must be between 0 and 4.

    >>> remove_bg(test_image, thresh_type=6)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Threshold_type value must be between 0 and 4.

    >>> remove_bg(test_image, mode=-1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Thres_type value must be between 0 and 2 (0-Adapt-Gauss, 1-Adapt-Mean, 2-Simple).

    >>> remove_bg(test_image, mode=3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Thres_type value must be between 0 and 2 (0-Adapt-Gauss, 1-Adapt-Mean, 2-Simple).
    """

    # Checking arguments
    check_threshold(thresh_val)
    check_window_size(window_size)
    check_block_size(block_size)
    check_c(c)
    check_mode(mode)

    # Loading image
    image = iu.get_image(input_file)

    # Removing noise by blurring and thresholding
    image = cv.GaussianBlur(image, (window_size, window_size), 0)

    result = []

    if mode == 2:
        result = th.threshold(image, thresh_val, thresh_type=thresh_type)
    else:
        result = th.adaptive_threshold(image, block_size=block_size, c=c,
                                       mode=mode, thresh_type=thresh_type)

    return result


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


def check_mode(type):

    if type < 0 or type > 2:
        raise ValueError("Thres_type value must be between 0 and 2 ("
                         "0-Adapt-Gauss, 1-Adapt-Mean, 2-Simple).")
    return 0


def check_threshold(value):

    if int(value) < 0 or int(value) > 255:
        raise ValueError("All threshold values must be between 0 and 255.")

    return 0


def check_thresh_type(value):

    if int(value) < 0 or int(value) > 4:
        raise ValueError("Threshold_type value must be between 0 and 4.")
    return 0


def check_window_size(window_size):
    if window_size < 0:
        raise ValueError("Window size value must be greater than 0.")

    if window_size % 2 == 0:
        raise ValueError("Window size value must be odd.")
    return 0


# CLI SETTINGS


if __name__ == '__main__':

        # CLI arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--input", required="True",
                        help="Path to the input file.")
        ap.add_argument("-t", "--threshold",
                        help="Pixel value to threshold.")
        ap.add_argument("-w", "--windowsize",
                        help="Odd value, size of the kernel used in the \
                        Gaussian Blur.")
        ap.add_argument("-b", "--blocksize",
                        help="Size of the block of neighbours used in adaptive \
                             thresholding")
        ap.add_argument("-c", "--constraint",
                        help="Constraint to substract of the neighbours mean.")
        ap.add_argument("-o", "--option",
                        help="[0-2] depending on the threshold wanted.")
        args = vars(ap.parse_args())

        # Loading values
        input_file = args["input"]
        thresh_val = args["threshold"]
        window_size = args["kernelsize"]
        block_size = args["blocksize"]
        constraint = args["constraint"]
        option = args["option"]

        # Setting values:
        if thresh_val is None:
            thresh_val = 200

        if window_size is None:
            window_size = 3

        if block_size is None:
            block_size = 11

        if constraint is None:
            constraint = 5

        if option is None:
            option = 0

        cv.imshow("Adaptive Gaussian Threshold",
                  remove_bg(input_file, thresh_val, window_size, block_size,
                            constraint, option)
                  )
        cv.waitKey()

        cv.destroyAllWindows()
