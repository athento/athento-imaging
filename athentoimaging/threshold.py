import cv2 as cv
import argparse
import os
import img_utils as iu

"""
This script shows the results of applying threshold values to the input image
and ask the user whether he wants to save the outputted image or not. Also, it
can be used in the CLI.
"""


def adaptive_gaussian_apply(input_file, max_val=255, thresh_type=0,
                            block_size=11, c=5):
    check_threshold(max_val)
    check_thresh_type(thresh_type)
    check_block_size(block_size)
    check_c(c)

    image = iu.get_image(input_file, 0)

    return cv.adaptiveThreshold(image, max_val, cv.ADAPTIVE_THRESH_MEAN_C,
                                thresh_type, block_size, c)


def adaptive_mean_apply(input_file, max_val=255, thresh_type=0,
                        block_size=11, c=5):

    check_threshold(max_val)
    check_thresh_type(thresh_type)
    check_block_size(block_size)
    check_c(c)

    image = iu.get_image(input_file, 0)

    return cv.adaptiveThreshold(image, max_val, cv.ADAPTIVE_THRESH_MEAN_C,
                                thresh_type, block_size, c)


def apply(input_file, thresh_val=200, new_value=255, thresh_type=0):

    # Checking arguments and raising expected exceptions
    check_threshold(thresh_val)
    check_threshold(new_value)
    check_thresh_type(thresh_type)

    image = iu.get_image(input_file, 0)

    th, img_thresh = cv.threshold(image, thresh_val, new_value, thresh_type)

    return img_thresh


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


def check_thresh_type(value):

    if int(value) < 0 or int(value) > 4:
        raise ValueError("Threshold_type value must be between 0 and 4.")

    return 0


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
