import cv2 as cv
import numpy as np
import img_utils as iu
import math
import os
import argparse

test_image = os.path.abspath(os.path.join(os.path.dirname("__file__"),
                                          "../resources/", "input_ftm.png"))


def get_gray_intensity(input_file):
    """
    >>> isinstance(get_gray_intensity(test_image), float)
    True

    >>> get_gray_intensity(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> get_gray_intensity("")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> get_gray_intensity("fakeRoute")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.
    """
    image = iu.get_image(input_file, 0)

    return math.floor(np.mean(image))


def get_gray_intensity_analysis(input_file, split_x=3, split_y=3):
    """
    >>> isinstance(get_gray_intensity_analysis(test_image), list)
    True

    >>> get_gray_intensity_analysis(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> get_gray_intensity_analysis("")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> get_gray_intensity_analysis("fakeRoute")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.

    >>> get_gray_intensity_analysis(test_image, split_x=-1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: The split value must be greater than 0.

    >>> get_gray_intensity_analysis(test_image, split_y=-1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: The split value must be greater than 0.
    """

    # Cheking arguments
    check_split(split_x)
    check_split(split_y)

    # Loading the image
    image = iu.get_image(input_file)

    results = []

    # Calculating split coords
    coordinates = iu.split_image(image, split_x, split_y)

    # For each split, get it's gray intensity value.
    for i, coord in enumerate(coordinates):
        x1, x2 = coord[1]
        y1, y2 = coord[0]

        crop = image[x1:x2, y1:y2]
        if crop is None or crop == []:
            raise Exception("Unexpected error while cropping the image.")

        intensity = get_gray_intensity(crop)
        results.append(intensity)

    return results


def get_model(input_file, split_x=3, split_y=3):
    """
    >>> isinstance(get_model(test_image), list)
    True

    >>> get_model(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> get_model("")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> get_model("fakeRoute")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.

    >>> get_model(test_image, split_x=-1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: The split value must be greater than 0.

    >>> get_model(test_image, split_y=-1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: The split value must be greater than 0.
    """

    # Loading the image
    image = iu.get_image(input_file)

    mean = math.ceil(np.mean(image))

    results = get_gray_intensity_analysis(input_file, split_x, split_y)

    for i, r in enumerate(results):
        if r <= mean:
            results[i] = 1
        else:
            results[i] = 0

    return results


# CHECKING ARGUMENTS


def check_split(split):

    split = int(split)

    if split < 1:
        raise ValueError("The split value must be greater than 0.")

    return 0


# CLI SETTINGS


if __name__ == '__main__':

        # CLI arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--input", required="True",
                        help="Path to the input file.")
        ap.add_argument("-x", "--splitx",
                        help="Divisions of the image in X axis")
        ap.add_argument("-y", "--splity",
                        help="Divisions of the image in Y axis")
        args = vars(ap.parse_args())

        # Loading values
        input_file = args["input"]
        split_x = args["splitx"]
        split_y = args["splity"]

        # Checking the input values:
        if split_x is None:
                split_x = 3
        if split_y is None:
                split_y = 3

        get_model(input_file, split_x, split_y)
