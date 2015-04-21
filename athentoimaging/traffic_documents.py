import cv2 as cv
import threshold as th
import argparse
import numpy as np
import lines_detection as ld

def detect_license(input_file, threshold=254):

    # Loading the image
    image = input_file
    if isinstance(image, str):
        image = cv.imread(input_file)

    image = cv.pyrDown(image)
    image = cv.pyrUp(image)

    #kernel = np.ones((5,5), 'uint8')
    #dilated = cv.dilate(image, kernel, 1)

    image = th.apply(image, threshold)
    image = image[0]

    lines = ld.detect_lines(image)
    print ld.line_count(lines)
    cv.imshow("", ld.draw_lines(image, lines))
    cv.waitKey()

    img_th = th.apply(image, threshold)

    cv.imshow("", img_th[0])
    cv.waitKey()


if __name__ == '__main__':
    #CLI arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required="True",
                    help="Path to the input image.")
    ap.add_argument("-t", "--threshold",
                    help="Path to the template image.")
    args = vars(ap.parse_args())

    #Loading values
    input_file = args["input"]
    threshold = args["threshold"]

    if threshold is None:
        threshold = 254

    detect_license(input_file, threshold)