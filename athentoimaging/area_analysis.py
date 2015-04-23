import cv2 as cv
import argparse
import numpy as np
import img_utils as iu
import threshold as th
import math


def detect_contours(input_file, thresh_val=127):

    gray = iu.get_image(input_file, 0)

    #Threshold to delete noise
    thresh = th.apply(gray, thresh_val, thresh_type=1)
    thresh = thresh[0]

    #Dilate and blur to improve the contours
    thresh = cv.dilate(thresh, kernel=(5, 5), iterations=5)
    thresh = cv.blur(thresh, (5, 5))

    #Pyramid transformations to remove some extra noise
    thresh = cv.pyrDown(thresh)
    thresh = cv.pyrUp(thresh)

    contours, h = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    return contours


def get_squares(contours, min_length=1000):

    results = []

    for cnt in contours:
        approx = cv.approxPolyDP(cnt, 0.01*cv.arcLength(cnt, True), True)
        if len(approx) == 4 and abs(get_contour_dimension(approx)) > min_length:
            results = [approx] + results

    return results


def draw_contours(input_file, contours):

    image = iu.get_image(input_file)

    if contours is None:
        raise ValueError("Contour can't be none, must be list")

    for cnt in contours:
        cv.drawContours(image, [cnt], 0, (255, 0, 0), 0)

    return image


def get_square_number(contours, min_length=1000):
    return len(get_squares(contours, min_length))


def get_contour_area(contour):
    return math.floor(cv.contourArea(contour))


def get_contour_coord(contour):
    return contour


def get_contour_dimension(contour, closed=1):
    return math.floor(cv.arcLength(contour, closed))


def get_gray_intensity(image):
    if not isinstance(image, np.ndarray):
        raise IOError("Image must be numpy array.")
    return math.floor(np.mean(image))


def get_gray_intensity_analysis(input_file, split_x=3, split_y=2):

    image = iu.get_image(input_file)

    results = []

    coordinates = crop_image(image, split_x, split_y)

    for i, coord in enumerate(coordinates):
        x1, x2 = coord[1]
        y1, y2 = coord[0]

        crop = image[x1:x2, y1:y2]
        if crop is None or crop == []:
            print "Unexpected error while cropping the image."

        intensity = get_gray_intensity(crop)
        results = [intensity] + results

    return results


def crop_image(input_file, split_x=3, split_y=2):

    image = iu.get_image(input_file)

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


if __name__ == '__main__':
    #CLI arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required="True",
                    help="Path to the input image.")
    ap.add_argument("-m", "--minlength",
                    help="Minimum perimeter length wanted.")
    args = vars(ap.parse_args())

    #Loading values
    input_file = args["input"]
    min_length = args["minlength"]

    if min_length is None:
        min_length = 100

    contours = detect_contours(input_file)
    contours = get_squares(contours)
    print get_contour_dimension(contours[0])
    print get_contour_area(contours[0])
    print get_square_number(contours, min_length)
    print get_contour_coord(contours[0])
    print get_gray_intensity_analysis(input_file, 5, 3)

    cv.imshow("", draw_contours(input_file, contours))
    cv.waitKey()
    cv.destroyAllWindows()