import cv2 as cv
import argparse
import numpy as np
import lines_detection as ld
import img_utils as iu
import threshold as th


def detect_squares(input_file, min_area=1000):

    img = iu.get_image(input_file)
    gray = iu.get_image(input_file, 0)

    thresh = th.apply(gray, 127, thresh_type=1)
    thresh = thresh[0]

    thresh = cv.dilate(thresh, kernel=(5, 5), iterations=5)

    cv.imshow("", thresh)
    cv.waitKey()
    cv.destroyAllWindows()


    thresh = cv.blur(thresh, (5,5))

    cv.imshow("", thresh)
    cv.waitKey()
    cv.destroyAllWindows()

    thresh = cv.pyrDown(thresh)
    thresh = cv.pyrUp(thresh)


    contours, h = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    results = []

    for cnt in contours:
        approx = cv.approxPolyDP(cnt,0.01*cv.arcLength(cnt,True),True)
        if len(approx) == 4 and abs(cv.contourArea(approx)) > min_area:
            results = [approx] + results
            cv.drawContours(img, [cnt], 0, (255, 0, 0), 0)

    cv.imshow("", img)
    cv.waitKey()
    cv.destroyAllWindows()

    return results


def get_square_number(input_file, min_area):
    return len(detect_squares(input_file, min_area))


def get_contour_area(contour):
    return cv.contourArea(contour)


def get_contour_coords(contour):
    return contour


if __name__ == '__main__':
    #CLI arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required="True",
                    help="Path to the input image.")
    ap.add_argument("-m", "--minarea",
                    help="Minimum size wanted.")
    args = vars(ap.parse_args())

    #Loading values
    input_file = args["input"]
    min_area = args["minarea"]

    if min_area is None:
        min_area = 100

    print get_square_number(input_file, min_area)