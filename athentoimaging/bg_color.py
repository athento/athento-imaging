import argparse
import cv2 as cv
import threshold as th
import os
import img_utils as iu

"""
This script allows to clean an image with noisy background (ie: coloured
background).
"""

test_image = os.path.abspath(os.path.join(os.path.dirname("__file__"),
                                          "../resources/", "test_image.png"))


def adaptive_gaussian_clean(input_file, window_size=3, block_size=11, c=5):
    """
    #>>> adaptive_gaussian_clean(test_image,200,3)
    #TODO return np array

    >>> adaptive_gaussian_clean(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> adaptive_gaussian_clean("")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> adaptive_gaussian_clean("fakeRoute")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.

    >>> adaptive_gaussian_clean(test_image, window_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Window size value must be greater than 0.

    >>> adaptive_gaussian_clean(test_image, window_size=2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Window size value must be odd.

    >>> adaptive_gaussian_clean(test_image, block_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Block size value must be greater than 0.

    >>> adaptive_gaussian_clean(test_image, block_size=2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Block size value must be odd.

    >>> adaptive_gaussian_clean(test_image, c='a')
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Constraint must be integer.
    """

    # Checking arguments
    check_window_size(window_size)
    check_block_size(block_size)
    check_c(c)

    # Loading image
    image = iu.get_image(input_file)

    # Removing noise by blurring and adaptive thresholding
    image = cv.GaussianBlur(image, (window_size, window_size), 0)

    return th.adaptive_gaussian_apply(image, block_size, c)


def adaptive_mean_clean(input_file, window_size=3, block_size=11, c=5):
    """
    #>>> adaptive_mean_clean(test_image,200,3)
    #TODO return np array

    >>> adaptive_mean_clean(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> adaptive_mean_clean("")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> adaptive_mean_clean("fakeRoute")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.

    >>> adaptive_mean_clean(test_image, window_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Window size value must be greater than 0.

    >>> adaptive_mean_clean(test_image, window_size=2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Window size value must be odd.

    >>> adaptive_mean_clean(test_image, block_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Block size value must be greater than 0.

    >>> adaptive_mean_clean(test_image, block_size=2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Block size value must be odd.

    >>> adaptive_mean_clean(test_image, c='a')
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Constraint must be integer.
    """

    # Checking arguments
    check_window_size(window_size)
    check_block_size(block_size)
    check_c(c)

    # Loading the image
    image = iu.get_image(input_file)

    # Removing noise by blurring and thresholding
    image = cv.GaussianBlur(image, (window_size, window_size), 0)

    return th.adaptive_mean_apply(image, block_size, c)


def clean(input_file, thresh_val=200, window_size=3):
    """
    #>>> clean(test_image,200,3)
    #TODO return np array

    >>> clean(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> clean("")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> clean("fakeRoute")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.

    >>> clean(test_image, thresh_val=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> clean(test_image, thresh_val=260)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: All threshold values must be between 0 and 255.

    >>> clean(test_image, window_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Window size value must be greater than 0.

    >>> clean(test_image, window_size=2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Window size value must be odd.
    """

    # Checking arguments and raising expected exceptions
    check_threshold(thresh_val)
    check_window_size(window_size)

    # Loading the image
    image = iu.get_image(input_file, 0)

    # Removing noise by blurring and thresholding
    image = cv.GaussianBlur(image, (window_size, window_size), 0)

    return th.apply(image, thresh_val)


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
                        help="Odd value, size of the window used in the \
                        Gaussian Blur.")
        args = vars(ap.parse_args())


        # Loading values
        input_file = args["input"]
        thresh_val = args["threshold"]
        window_size = args["windowsize"]
        
        # Setting values:
        if thresh_val is None:
                thresh_val = 200
        
        if window_size is None:
            window_size = 3
        
        clean(input_file, thresh_val, window_size)

