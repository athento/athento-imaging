import cv2 as cv
import numpy as np
import os
import img_utils as iu


def detect_lines(input_file,
                 min_val=50, max_val=200, aperture_size=3,
                 rho=1, theta=np.pi/180, threshold=200,
                 min_line_length=30, max_line_gap=20):

    if min_val < max_val:

        image = iu.get_image(input_file)

        check_canny_args(min_val, max_val, aperture_size)
        check_houghlines_p_args(rho, theta, threshold,
                              min_line_length, max_line_gap)

        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        edges = cv.Canny(gray, min_val, max_val, aperture_size)
        lines = cv.HoughLinesP(edges, rho, theta, threshold,
                               min_line_length, max_line_gap)
    else:
        lines = None

    return lines


def delete_lines(input_file, lines, width=5, color=(255, 255, 255)):

    image = iu.get_image(input_file)

    check_lines(lines)
    check_width(width)
    check_color(color)

    return draw_lines(image, lines, width, color)


def delete_all_lines(input_file,
                     width=5, color=(255, 255, 255),
                     min_val=50, max_val=200, aperture_size=3,
                     rho=1, theta=np.pi/180, threshold=200,
                     min_line_length=30, max_line_gap=20):

    image = iu.get_image(input_file)

    check_width(width)
    check_color(color)
    check_canny_args(min_val, max_val, aperture_size)
    check_houghlines_p_args(rho, theta, threshold, min_line_length, max_line_gap)

    lines = detect_lines(image, min_val, max_val, aperture_size, rho, theta,
                         threshold, min_line_length, max_line_gap)
    while lines is not None:
        image = delete_lines(image, lines, width, color)
        lines = detect_lines(image, rho, theta, threshold,
                             min_line_length, max_line_gap)

    return image


def distance(line1, line2):

    check_line(line1)
    check_line(line2)

    res = [-1, -1]
    if parallels(line1, line2):
        l1_x1, l1_y1, l1_x2, l1_y2 = line1
        l2_x1, l2_y1, l2_x2, l2_y2 = line2
        res = [abs(l1_x1 - l2_x1), abs(l1_y1 - l2_y1)]

    return res


def distance_mean(lines):

    check_lines(lines)

    if not isinstance(lines, list) and len(lines) > 1:
        raise ValueError("Lines must contain at least two lines to proceed.")

    n_lines = np.size(lines)
    total = [0, 0]
    for i, l1 in enumerate(lines[0]):
        for j, l2 in enumerate(lines[0][i:]):
            d = distance(l1, l2)
            if d != -1:
                total[0] += d[0]
                total[1] += d[1]

    return [total[0]/n_lines, total[1]/n_lines]


def draw_lines(input_file, lines, width=5, color=(0, 0, 255)):

    image = iu.get_image(input_file)

    check_lines(lines)
    check_width(width)
    check_color(color)

    if np.size(lines[0]) == 1:
        x1, y1, x2, y2 = lines
        cv.line(image, (x1, y1), (x2, y2), color, width)
    else:
        for x1, y1, x2, y2 in lines[0]:
            cv.line(image, (x1, y1), (x2, y2), color, width)

    return image


def line_count(lines, error=5):

    check_lines(lines)
    check_error(error)

    total = 0
    v_lines = 0
    h_lines = 0

    if np.size(lines[0]) == 1:
        x1, y1, x2, y2, = lines
        if x1 in range(x2-error, x2+error):
            v_lines += 1
        elif y1 in range(y2-error, y2+error):
            h_lines += 1
        total += 1

    else:
        for x1, y1, x2, y2 in lines[0]:
            if x1 in range(x2-error, x2+error):
                v_lines += 1
            elif y1 in range(y2-error, y2+error):
                h_lines += 1
            total += 1

    return [total, v_lines, h_lines]


def parallels(line1, line2, error=5):

    check_line(line1)
    check_line(line2)
    check_error(error)

    l1_x1, l1_y1, l1_x2, l1_y2 = line1
    l2_x1, l2_y1, l2_x2, l2_y2 = line2

    return (l1_x1 - l2_x1 in range(
        (l1_x2 - l2_x2 - error), (l1_x2 - l2_x2 + error))) \
           and (l1_y1 - l2_y1 in range(
        (l1_y2 - l2_y2 - error), (l1_y2 - l2_y2 + error)))


#Checking arguments

def check_color(color):

    if (color[0] < 0 or color[0] > 255 or color[1] < 0 or color[1] > 255 or
                color[2] < 0 or color[2] > 255):
        raise ValueError("Color value must be: (0-255, 0-255, 0-255).")
    return 0

def check_canny_args(min_val, max_val, aperture_size):

    if min_val < 0 or min_val > 255:
        raise ValueError("Min_val value must be between 0 and 255.")

    if max_val < 0 or max_val > 255:
        raise ValueError("Max_val value must be between 0 and 255.")

    if min_val >= max_val:
        raise ValueError("Min_val value must be lesser than max_val.")

    if aperture_size < 0:
        raise ValueError("Aperture_size value must be greater than 0.")
    return 0


def check_houghlines_p_args(rho, theta, threshold, min_line_length, max_line_gap):

    if rho < 0:
        raise ValueError("Rho value must be greater than 0.")

    if theta < 0:
        raise ValueError("Theta value must be greater than 0.")

    if threshold < 0:
        raise ValueError("Threshold value must be greater than 0.")

    if min_line_length < 0:
        raise ValueError("Min_line_length must be greater than 0.")

    if max_line_gap < 0:
        raise ValueError("Max_line_gap must be greater than 0.")
    return 0


def check_error(error):

    if error < 0:
        raise ValueError("Error value must be positive (0 included).")
    return 0


def check_line(line):

    if line is None:
        raise ValueError("Line must be a line, is None.")
    if np.size(line) != 4:
        raise ValueError("Wrong format on line, line must be [rho, theta].")
    return 0


def check_lines(lines):

    if lines is None:
        raise ValueError("Lines can't be None.")
    return 0


def check_width(width):

    if width < 0:
        raise ValueError("Width value must be greater than 0.")
    return 0
