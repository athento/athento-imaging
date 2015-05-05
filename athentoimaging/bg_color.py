import argparse
import cv2 as cv
import threshold as th
import os
import img_utils as iu
import numpy as np

"""
This script allows to clean an image with noisy background (ie: coloured
background).
"""

test_image = os.path.abspath(os.path.join(os.path.dirname("__file__"),
                                          "../resources/", "test_image.png"))


def adaptive_gaussian_clean(input_file, kernel_size=3, block_size=11, c=5):
    """
    >>> isinstance(adaptive_gaussian_clean(test_image), np.ndarray)
    True

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

    >>> adaptive_gaussian_clean(test_image, kernel_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Window size value must be greater than 0.

    >>> adaptive_gaussian_clean(test_image, kernel_size=2)
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
    check_kernel_size(kernel_size)
    check_block_size(block_size)
    check_c(c)

    # Loading image
    image = iu.get_image(input_file)

    # Removing noise by blurring and adaptive thresholding
    image = cv.GaussianBlur(image, (kernel_size, kernel_size), 0)

    return th.adaptive_threshold_apply(image, block_size=block_size, c=c, cv_threshold=cv.ADAPTIVE_THRESH_MEAN_C)


def adaptive_mean_clean(input_file, kernel_size=3, block_size=11, c=5):
    """
    >>> isinstance(adaptive_mean_clean(test_image), np.ndarray)
    True

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

    >>> adaptive_mean_clean(test_image, kernel_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Window size value must be greater than 0.

    >>> adaptive_mean_clean(test_image, kernel_size=2)
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
    check_kernel_size(kernel_size)
    check_block_size(block_size)
    check_c(c)

    # Loading the image
    image = iu.get_image(input_file)

    # Removing noise by blurring and thresholding
    image = cv.GaussianBlur(image, (kernel_size, kernel_size), 0)

    return th.adaptive_threshold_apply(image, block_size=block_size, c=c, cv_threshold=cv.ADAPTIVE_THRESH_MEAN_C)


def clean(input_file, thresh_val=200, kernel_size=3):
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

    >>> clean(test_image, kernel_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Window size value must be greater than 0.

    >>> clean(test_image, kernel_size=2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Window size value must be odd.
    """

    # Checking arguments and raising expected exceptions
    check_threshold(thresh_val)
    check_kernel_size(kernel_size)

    # Loading the image
    image = iu.get_image(input_file, 0)

    # Removing noise by blurring and thresholding
    image = cv.GaussianBlur(image, (kernel_size, kernel_size), 0)

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


def check_kernel_size(kernel_size):
    if kernel_size < 0:
        raise ValueError("Window size value must be greater than 0.")

    if kernel_size % 2 == 0:
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
        ap.add_argument("-w", "--kernelsize",
                        help="Odd value, size of the kernel used in the \
                        Gaussian Blur.")
        ap.add_argument("-b", "--blocksize",
                        help="Size of the block of neighbours used in adaptive \
                             thresholding")
        ap.add_argument("-c", "--constraint",
                        help="Constraint to substract of the neighbours mean.")
        args = vars(ap.parse_args())


        # Loading values
        input_file = args["input"]
        thresh_val = args["threshold"]
        kernel_size = args["kernelsize"]
        block_size = args["blocksize"]
        constraint = args["constraint"]

        
        # Setting values:
        if thresh_val is None:
            thresh_val = 200
        
        if kernel_size is None:
            kernel_size = 3

        if block_size is None:
            block_size = 11

        if constraint is None:
            constraint = 5

        cv.imshow("Adaptive Gaussian Threshold",
                  adaptive_gaussian_clean(input_file, kernel_size, block_size,
                                          constraint)
                  )
        cv.waitKey()

        cv.imshow("Adaptive Mean Threshold",
                  adaptive_mean_clean(input_file, kernel_size, block_size,
                                      constraint)
                  )
        cv.waitKey()

        cv.imshow("Classical Thresholding", clean(input_file, thresh_val,
                                                  kernel_size)
                  )
        cv.waitKey()

        cv.destroyAllWindows()
