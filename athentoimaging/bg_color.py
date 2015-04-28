import argparse
import cv2 as cv
import threshold as th
import os
import img_utils as iu

"""
This script allows to clean an image with noisy background (ie: coloured
background).
"""


def clean(input_file, thresh_val=200, window_size=3):

    # Checking arguments and raising expected exceptions
    check_threshold(thresh_val)
    check_window_size(window_size)

    # Loading the image
    image = iu.get_image(input_file, 0)
        
    # Gray-scale and Gaussian Blur
    image = cv.GaussianBlur(image, (window_size, window_size), 0)

    # Applying threshold list
    results = th.apply(image, thresh_val)

    return results


def adaptive_mean_clean(input_file, window_size=3, block_size=11, c=5):

    check_window_size(window_size)
    check_block_size(block_size)
    check_c(c)

    image = iu.get_image(input_file)

    image = cv.GaussianBlur(image, (window_size, window_size), 0)

    results = th.adaptive_mean_apply(image, block_size, c)

    return results


def adaptive_gaussian_clean(input_file, window_size=3, block_size=11, c=5):

    check_window_size(window_size)
    check_block_size(block_size)
    check_c(c)

    image = iu.get_image(input_file)

    image = cv.GaussianBlur(image, (window_size, window_size), 0)

    results = th.adaptive_gaussian_apply(image, block_size, c)

    return results


# CHECKING ARGUMENTS


def check_block_size(block_size):
    if block_size < 0:
        raise ValueError("Window size value must be greater than 0")

    if block_size % 2 == 0:
        raise ValueError("Window size value must be odd.")
    return 0


def check_c(c):

    if not isinstance(c, int):
        raise IOError("Constraint must be integer")

    return 0


def check_threshold(value):

    if int(value) < 0 or int(value) > 255:
        raise ValueError("All threshold values must be between 0 and 255")

    return 0


def check_window_size(window_size):
    if window_size < 0:
        raise ValueError("Window size value must be greater than 0")

    if window_size % 2 == 0:
        raise ValueError("Window size value must be odd.")
    return 0


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

