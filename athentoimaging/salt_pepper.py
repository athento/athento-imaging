import cv2 as cv
import os
import argparse
import threshold as th
import img_utils as iu

"""
This script cleans an image with salt and pepper noise (ie: text dotted due to
bad pixel definition).
"""


def clean(input_file,  thresh_val = [250, 245, 240, 230, 225, 220], 
                window_size = 5, kernel_size = 5):

    # Ensures that both quality and window_size parameters are integers
    window_size = int(window_size)
    kernel_size = int(kernel_size)

    #Checking arguments and raising expected exceptions
    check_arguments(window_size, kernel_size)

    # Loading the image
    image = iu.get_image(input_file)

    # Applying Grayscale, Gaussian and median blur and erode
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image = cv.GaussianBlur(image, (window_size, window_size), 0)
    image = cv.medianBlur(image, window_size)
    image = cv.erode(image, (kernel_size, kernel_size))

    # Applying threshold list
    results = th.apply(image, thresh_val)

    return results


def check_arguments(window_size, kernel_size):
    if kernel_size < 0:
        raise ValueError("Kernel size value must be greater than 0.")

    if kernel_size % 2 == 0:
        raise ValueError("Kernel size value must be odd.")

    if window_size < 0:
        raise ValueError("Window size value must be greater than 0.")

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
        ap.add_argument("-k", "--kernelsize", 
                        help="Kernel size used in erode operation.")
        ap.add_argument("-w", "--windowsize", 
                        help="Odd value, size of the window used in the \
                        Gaussian Blur.")
        args = vars(ap.parse_args())
        
        # Loading values
        input_file = args["input"]
        kernel_size = args["kernelsize"]
        thresh_val = args["threshold"]
        window_size = args["windowsize"]
        
        # Checking the input values:
        if thresh_val == None:
                thresh_val = [250, 245, 240, 230, 225, 220]
        
        if window_size == None:
                window_size = 5
        
        if kernel_size == None:
                kernel_size = 5
        
        clean(input_file, thresh_val, window_size, kernel_size)
