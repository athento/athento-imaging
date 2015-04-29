import cv2 as cv
import numpy as np
import img_utils as iu
import math


def contours_close(cnt1, cnt2, min_dist=20):

    result = False

    for i in xrange(cnt1.shape[0]):
        for j in xrange(cnt2.shape[0]):
            dist = np.linalg.norm(cnt1[i] - cnt2[j])
            if abs(dist) <= min_dist:
                result = True

    return result


def delete_border_noise(input_file, width=20, color=(255, 255, 255)):

    image = iu.get_image(input_file)

    image = iu.pyramid_clean(image)

    image[0:width, :] = color
    image[:, 0:width] = color
    image[:, -width:] = color
    image[-width:, :] = color

    return image


def delete_small_contours(contours, min_dimension=1000):

    new_contours = []

    for i in contours:
        if get_contour_dimension(i) > min_dimension:
            new_contours.append(i)

    return new_contours


def detect_contours(input_file, thresh_val=255):

    gray = iu.get_image(input_file, 0)

    gray = iu.pyramid_clean(gray)

    th2 = cv.adaptiveThreshold(gray, thresh_val, cv.ADAPTIVE_THRESH_MEAN_C,
                               cv.THRESH_BINARY, 11, 2)

    th2 = cv.erode(th2, kernel=(5, 5), iterations=30)

    th2 = cv.bitwise_not(th2)

    contours, h = cv.findContours(th2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    return contours


def detect_corners(input_file, max_corners=10, min_dist=50, trust_val=0.5):

    image = iu.get_image(input_file)

    contours = detect_contours(image)

    blank = image
    blank[:] = 255

    img = draw_contours(blank, contours, 10, color=(0, 0, 0))

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    corners = cv.goodFeaturesToTrack(img, max_corners, trust_val, min_dist)

    return corners


def draw_contours(input_file, contours, thickness=0, color=(0, 0, 255)):

    image = iu.get_image(input_file)

    if contours is None:
        raise ValueError("Contour can't be none, must be list")

    for cnt in contours:
        cv.drawContours(image, [cnt], 0, color, thickness)

    return image


def draw_corners(input_file, corners, radius=5, color=(0, 0, 255), thickness=-1):

    img = iu.get_image(input_file)

    for i in corners:
        x, y = i.ravel()
        cv.circle(img, (x,y), radius, color, thickness)

    return img


def get_contour_area(contour):
    return math.floor(cv.contourArea(contour))


def get_contour_coord(contour):
    return contour


def get_contour_dimension(contour, closed=1):
    return math.floor(cv.arcLength(contour, closed))


def get_corner_number(input_file, max_corners=10, min_dist=20, trust_val=0.2):
    return len(detect_corners(input_file, max_corners, min_dist, trust_val))


def get_squares(contours, min_length=1000):

    results = []

    for cnt in contours:
        approx = cv.approxPolyDP(cnt, 0.01*cv.arcLength(cnt, True), True)
        if len(approx) >= 4 and abs(get_contour_dimension(approx)) >= min_length:
            results = [approx] + results

    return results


def get_square_number(contours, min_length=1000):
    return len(get_squares(contours, min_length))


def join_contours(contours, min_dist=20):

    # Terrible efficiency

    length = len(contours)
    status = np.zeros((length, 1))
    for i, c1 in enumerate(contours):
        x = i
        for c2 in contours[i+1:]:
            if contours_close(c1, c2, min_dist) is True:
                val = min(status[i], status[x])
                status[x] = status[i] = val
            else:
                if status[x] == status[i]:
                    status[x] = i+1

        unified = []
        maximum = int(status.max())+1
        for i in xrange(maximum):
            pos = np.where(status == i)[0]
            if pos.size != 0:
                cont = np.vstack(contours[i] for i in pos)
                hull = cv.convexHull(cont)
                unified.append(hull)

    return unified