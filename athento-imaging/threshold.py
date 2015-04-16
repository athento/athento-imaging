import cv2 as cv
import argparse
import os


"""
This script shows the results of applying threshold values to the input image
and ask the user whether he wants to save the outputted image or not. Also, it
can be used in the CLI.
"""


def apply(input_file, thresh_values=[250, 245, 240, 230, 225, 220]):

    # If thresh is not a list of values transform it.
    if not isinstance(thresh_values, list):
        thresh_values = [thresh_values]

    # Checking arguments and raising expected exceptions
    check_arguments(input_file, thresh_values)

    # Loading the image
    image = input_file
    if isinstance(image, str):
        image = cv.imread(input_file)

    results = []

    for i in thresh_values:
        th, img_thresh = cv.threshold(image, float(i), 255, cv.THRESH_BINARY)
        results = results + [img_thresh]

    return results


def check_arguments(input_file, thresh_values):

    if input_file == '':
        raise IOError("Input file can't be ''.")

    if input_file is None:
        raise IOError("Input file can't be None.")

    if isinstance(input_file, str) and os.path.isfile(input_file) is False:
        raise IOError("Input file not found.")

    for i, value in enumerate(thresh_values):
        if int(value) < 0 or int(value) > 255:
            raise ValueError("All threshold values must be between 0 and 255")

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
                thresh_val = [250, 245, 240, 230, 225, 220]
        
        apply(input_file, thresh_val)
