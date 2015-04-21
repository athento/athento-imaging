import argparse
import cv2 as cv
import threshold as th
import os
import img_utils as iu

"""
This script allows to clean an image with noisy background (ie: coloured
background).
"""


def clean(input_file, thresh_val = [225, 220, 215, 210, 205, 200],
                        window_size = 3):
      
        # Ensures that window_size parameter is integer
        window_size = int(window_size)

        # Checking arguments and raising expected exceptions
        check_arguments(window_size)

        # Loading the image
        image = iu.get_image(input_file)
        
        # Gray-scale and Gaussian Blur
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        image = cv.GaussianBlur(image, (window_size, window_size), 0)

        # Applying threshold list
        results = th.apply(image, thresh_val)

        return results


def check_arguments(window_size):
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
                thresh_val = [225, 220, 215, 210, 205, 200]
        else:
                thresh_val = [thresh_val]
        
        if window_size is None:
            window_size = 3
        
        clean(input_file, thresh_val, window_size)

