import cv2 as cv
import numpy as np
import os
import math
import img_utils as iu

"""
This script contains auxilary functions to be used during development.
"""

def pyramid_clean(input_file):

    image = iu.get_image(input_file)

    image = cv.pyrDown(image)
    image = cv.pyrUp(image)

    return image


def file_exists(input_file):

    if input_file == '':
        raise IOError("The input file can't be ''.")
    if input_file is None:
        raise IOError("The input file can't be a None object")

    return os.path.isfile(input_file)


def get_image(input_file, mode=1):

    image = input_file

    if isinstance(input_file, np.ndarray) is False:
        if file_exists(image) is False:
            raise IOError("Input file not found.")
        image = cv.imread(input_file, mode)

    if mode == 0 and len(image.shape) > 2:
        image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    return image


def split_image(input_file, split_x=3, split_y=2):

    image = get_image(input_file)

    x = image.shape[1]
    inc_x = math.floor(x/split_x)

    y = image.shape[0]
    inc_y = math.floor(y/split_y)

    results = []

    for column in range(0, split_x):
        current_x = column*inc_x
        next_x = current_x+inc_x
        if next_x > x:
            next_x = x

        for row in range(0, split_y):
            current_y = row*inc_y
            next_y = current_y+inc_y
            if next_y > y:
                next_y = y

            aux1 = [current_y, next_y]
            aux2 = [current_x, next_x]
            results = [[aux1, aux2]] + results

    return results


def save_img(image, output_name, question):

    if image is None:
        raise IOError("Input image is None.")

    if question == '':
        raise ValueError("The value of the question can't be ''.")

    if question is None:
        raise ValueError("The question can't be a None object.")

    if output_name == '':
        raise ValueError("The value of the output name can't be ''.")

    if output_name is None:
        raise ValueError("The output name can't be a None object.")

    #CHANGE THE NEXT FEW LINES TO CHANGE THE INPUT SYSTEM
    ans = input(question)

    # Checks that the input is within the correct values
    ans_list = ["y", "yes", "n", "no", "Y", "YES", "N", "NO"]
    while ans not in ans_list:
        ans = input(question)

    #END CHANGES

    # Saving the image
    if ans[0] == 'y' or ans[0] == 'Y':
        print "Saving..."
        cv.imwrite(output_name, image)
        print "Saved as {0}.".format(output_name)

    return 0

def check_color(color):

    if len(color) == 3:
        if (color[0] < 0 or color[0] > 255 or color[1] < 0 or color[1] > 255 or
                color[2] < 0 or color[2] > 255):
            raise ValueError("Color value must be: (0-255, 0-255, 0-255).")
    else:
        raise ValueError("Color value must be: (0-255, 0-255, 0-255).")
    return 0