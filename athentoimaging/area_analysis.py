import cv2 as cv
import numpy as np
import img_utils as iu
import math


def get_gray_intensity(input_file):

    image = iu.get_image(input_file, 0)

    if not isinstance(image, np.ndarray):
        raise IOError("Image must be numpy array.")
    return math.floor(np.mean(image))


def get_gray_intensity_analysis(input_file, split_x=3, split_y=3):

    image = iu.get_image(input_file)

    results = []

    coordinates = iu.split_image(image, split_x, split_y)

    for i, coord in enumerate(coordinates):
        x1, x2 = coord[1]
        y1, y2 = coord[0]

        crop = image[x1:x2, y1:y2]
        if crop is None or crop == []:
            raise Exception("Unexpected error while cropping the image.")

        intensity = get_gray_intensity(crop)
        results = [intensity] + results

    return results


def get_model(input_file, split_x=3, split_y=3):

    image = iu.get_image(input_file)

    image = cv.pyrDown(image)
    image = cv.pyrUp(image)

    coordinates = iu.split_image(image, split_x, split_y)

    results = []

    for i, coord in enumerate(coordinates):
        x1, x2 = coord[1]
        y1, y2 = coord[0]

        crop = image[x1:x2, y1:y2]
        if crop is None or crop == []:
            print "Unexpected error while cropping the image."

        intensity = get_gray_intensity(crop)

        if intensity < 255:
            results = results + [1]
        else:
            results = results + [0]

    return results