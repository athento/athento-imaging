import cv2 as cv
import threshold as th
import img_utils as iu
import numpy as np
import os
import argparse

"""
This script cleans an image with salt and pepper noise (ie: text dotted due to
bad pixel definition).
"""

test_image = os.path.abspath(os.path.join(os.path.dirname("__file__"),
                                          "../resources/", "test_image.png"))


def clean(input_file,  thresh_val=200, window_size=5, kernel_size=5):
    """
    >>> isinstance(clean(test_image), np.ndarray)
    True

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

    >>> clean(test_image, kernel_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Kernel size value must be greater than 0.

    >>> clean(test_image, kernel_size=2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Kernel size value must be odd.
    """

    # Checking arguments
    check_kernel_size(kernel_size)
    check_threshold(thresh_val)
    check_window_size(window_size)

    # Loading the image
    image = iu.get_image(input_file, 0)

    # Applying Gaussian and median blur and erode
    image = cv.GaussianBlur(image, (window_size, window_size), 0)
    image = cv.medianBlur(image, window_size)
    image = cv.erode(image, (kernel_size, kernel_size))

    return th.threshold(image, thresh_val)


# CHECKING ARGUMENTS


def check_kernel_size(kernel_size):

    if kernel_size < 0:
        raise ValueError("Kernel size value must be greater than 0.")

    if kernel_size % 2 == 0:
        raise ValueError("Kernel size value must be odd.")
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
        ap.add_argument("-k", "--kernel-size",
                        help="Kernel size used in erode operation.")
        ap.add_argument("-w", "--window-size",
                        help="Odd value, size of the window used in the \
                        Gaussian Blur.")
        args = vars(ap.parse_args())
        
        # Loading values
        input_file = args["input"]
        kernel_size = args["kernel-size"]
        thresh_val = args["threshold"]
        window_size = args["window-size"]
        
        # Checking the input values:
        if thresh_val is None:
                thresh_val = 200

        if window_size is None:
                window_size = 5
        
        if kernel_size is None:
                kernel_size = 5
        
        clean(input_file, thresh_val, window_size, kernel_size)
