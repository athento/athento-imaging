import cv2 as cv
import argparse
import numpy as np
import img_utils as iu
import math


def detect_contours(input_file, thresh_val=255):

    gray = iu.get_image(input_file, 0)
    
    gray = cv.pyrDown(gray)
    gray = cv.pyrUp(gray)
    
    th2 = cv.adaptiveThreshold(gray, thresh_val, cv.ADAPTIVE_THRESH_MEAN_C,
                               cv.THRESH_BINARY, 11, 2)
    
    th2 = cv.erode(th2, kernel=(5, 5), iterations=30)

    th2 = cv.bitwise_not(th2)    

    contours, h = cv.findContours(th2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    
    return contours


def get_squares(contours, min_length=1000):

    results = []

    for cnt in contours:
        approx = cv.approxPolyDP(cnt, 0.01*cv.arcLength(cnt, True), True)
        if len(approx) >= 4 and abs(get_contour_dimension(approx)) >= min_length:
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


def get_gray_intensity_analysis(input_file, split_x=3, split_y=3):

    image = iu.get_image(input_file)

    results = []

    coordinates = iu.split_image(image, split_x, split_y)

    for i, coord in enumerate(coordinates):
        x1, x2 = coord[1]
        y1, y2 = coord[0]

        crop = image[x1:x2, y1:y2]
        if crop is None or crop == []:
            print "Unexpected error while cropping the image."

        intensity = get_gray_intensity(crop)
        results = [intensity] + results

    return results

def get_model(input_file, split_x=3, split_y=3):

    image = iu.get_image(input_file)

    image = cv.pyrDown(image)
    image = cv.pyrUp(image)

    mean = get_gray_intensity(image)
    std = np.std(image)

    coordinates = iu.split_image(image, split_x, split_y)

    results = []

    for i, coord in enumerate(coordinates):
        x1, x2 = coord[1]
        y1, y2 = coord[0]

        crop = image[x1:x2, y1:y2]
        if crop is None or crop == []:
            print "Unexpected error while cropping the image."

        intensity = get_gray_intensity(crop)

        if intensity > 250:
            results = results + [0]
        else:
            results = results + [1]

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
    print get_model(input_file)

    cv.imshow("", draw_contours(input_file, contours))
    cv.waitKey()
    cv.destroyAllWindows()
