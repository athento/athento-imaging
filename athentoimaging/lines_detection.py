import cv2 as cv
import numpy as np
import os
import img_utils as iu


"""
This script contains basic functions to implement line detection in images
using the HoughLines function.
"""


test_image = os.path.abspath(os.path.join(os.path.dirname("__file__"),
                                              "../resources/", "lines.jpg"))


def delete_all_lines(input_file,
                     min_val=50, max_val=200, aperture_size=3,
                     rho=1, theta=np.pi/180, threshold=200,
                     line_length=1000, width=5, color=(255, 255, 255)):
    """
    >>> lines = detect_lines(test_image)
    >>> isinstance(delete_all_lines(test_image), np.ndarray)
    True

    >>> delete_all_lines(None, lines)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> delete_all_lines("", lines)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> delete_all_lines("fakeRoute", lines)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.

    >>> delete_all_lines(test_image, min_val=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Min_val value must be between 0 and 255.

    >>> delete_all_lines(test_image, max_val=300)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Max_val value must be between 0 and 255.

    >>> delete_all_lines(test_image, min_val=100, max_val=30)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Min_val value must be lesser than max_val.

    >>> delete_all_lines(test_image, aperture_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Aperture_size value must be greater than 0.

    >>> delete_all_lines(test_image, rho=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Rho value must be greater than 0.

    >>> delete_all_lines(test_image, theta=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Theta value must be greater than 0.

    >>> delete_all_lines(test_image, threshold=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Threshold value must be greater than 0.

    >>> delete_all_lines(test_image, line_length=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Line_length value must be greater than 0.

    >>> delete_all_lines(test_image, width=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Width value must be greater than 0.

    >>> delete_all_lines(test_image, color=(-10, 0, 0))
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Color value must be: (0-255, 0-255, 0-255).
    """

    image = iu.get_image(input_file)

    check_canny_args(min_val, max_val, aperture_size)
    check_houghlines_args(rho, theta, threshold)
    check_line_length(line_length)
    check_width(width)
    check_color(color)

    lines = detect_lines(image,
                         min_val, max_val, aperture_size,
                         rho, theta, threshold)

    while lines is not None:
        image = delete_lines(image, lines, line_length, width, color)
        lines = detect_lines(image, rho, theta, threshold)

    return image


def delete_lines(image, lines, line_length=1000, width=5,
                 color=(255, 255, 255)):
    """
    >>> lines = detect_lines(test_image)
    >>> isinstance(delete_lines(test_image, lines), np.ndarray)
    True

    >>> delete_lines(None, lines)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> delete_lines("", lines)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> delete_lines("fakeRoute", lines)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.

    >>> delete_lines(test_image, None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Lines can't be None.

    >>> delete_lines(test_image, lines, line_length=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Line_length value must be greater than 0.

    >>> delete_lines(test_image, lines, width=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Width value must be greater than 0.

    >>> delete_lines(test_image, lines, color=(-10, 0, 0))
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Color value must be: (0-255, 0-255, 0-255).
    """

    check_lines(lines)
    check_line_length(line_length)
    check_width(width)
    check_color(color)

    return draw_lines(image, lines, line_length, width, color)


def detect_lines(input_file,
                 min_val=50, max_val=200, aperture_size=3,
                 rho=1, theta=np.pi/180, threshold=200):
    """
    >>> isinstance(detect_lines(test_image), np.ndarray)
    True

    >>> detect_lines(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> detect_lines("")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> detect_lines("fakeRoute")
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.

    >>> detect_lines(test_image, min_val=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Min_val value must be between 0 and 255.

    >>> detect_lines(test_image, max_val=300)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Max_val value must be between 0 and 255.

    >>> detect_lines(test_image, aperture_size=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Aperture_size value must be greater than 0.

    >>> detect_lines(test_image, rho=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Rho value must be greater than 0.

    >>> detect_lines(test_image, theta=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Theta value must be greater than 0.

    >>> detect_lines(test_image, threshold=-3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Threshold value must be greater than 0.
    """

    if min_val < max_val:
        image = iu.get_image(input_file, 0)
        check_canny_args(min_val, max_val, aperture_size)
        check_houghlines_args(rho, theta, threshold)

        edges = cv.Canny(image, min_val, max_val, aperture_size)
        lines = cv.HoughLines(edges, rho, theta, threshold)
    else:
        lines = None
    return lines


def distance(line1, line2, line_length=1000):
    """
    >>> lines = detect_lines(test_image)
    >>> line1 = lines[0][0]
    >>> line2 = lines[0][1]
    >>> isinstance(distance(line1, line2), (int, list))
    True

    >>> distance(line1, None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Line must be a line, is None.

    >>> distance(None, line2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Line must be a line, is None.

    >>> distance(line1, line2, line_length=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Line_length value must be greater than 0.
    """

    # Checking arguments
    check_line(line1)
    check_line(line2)
    check_line_length(line_length)

    # Checks if both lines are parallels, if so, returns the distance between
    # them for both axis: [dist_x, dist_y]
    res = -1
    if parallels(line1, line2):
        l1_x1, l1_y1, l1_x2, l1_y2 = get_line_coordinates(line1, line_length)
        l2_x1, l2_y1, l2_x2, l2_y2 = get_line_coordinates(line2, line_length)
        res = [abs(l1_x1 - l2_x1), abs(l1_y1 - l2_y1)]

    return res


def distance_mean(lines, line_length=1000):
    """
    >>> lines = detect_lines(test_image)
    >>> dist = distance_mean(lines)
    >>> isinstance(dist[0], int) and isinstance(dist[1], int)
    True

    >>> distance_mean(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Lines can't be None.

    >>> distance_mean(lines, line_length=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Line_length value must be greater than 0.
    """

    # Checking arguments
    check_lines(lines)
    check_line_length(line_length)

    n_lines = np.size(lines)
    total = [0, 0]

    # Examins each line to get the distance to all the lines and calculates the
    # average.
    for i, l1 in enumerate(lines[0]):
        for j, l2 in enumerate(lines[0][i:]):
            d = distance(l1, l2, line_length)
            if d != -1:
                total[0] += d[0]
                total[1] += d[1]

    return [total[0]/n_lines, total[1]/n_lines]


def draw_lines(input_file, lines, line_length=1000, width=5, color=(0, 0, 255)):
    """
    >>> lines = detect_lines(test_image)
    >>> isinstance(draw_lines(test_image, lines), np.ndarray)
    True

    >>> draw_lines(None, lines)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be a None object

    >>> draw_lines("", lines)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: The input file can't be ''.

    >>> draw_lines("fakeRoute", lines)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    IOError: Input file not found.

    >>> draw_lines(test_image, None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Lines can't be None.

    >>> draw_lines(test_image, lines, line_length=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Line_length value must be greater than 0.

    >>> draw_lines(test_image, lines, width=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Width value must be greater than 0.

    >>> draw_lines(test_image, lines, color=(-10, 0, 0))
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Color value must be: (0-255, 0-255, 0-255).
    """

    # Checking arguments
    check_lines(lines)
    check_line_length(line_length)
    check_width(width)
    check_color(color)

    # Loading the image
    image = iu.get_image(input_file)

    if np.size(lines) == 1:
        x1, y1, x2, y2 = get_line_coordinates(lines, line_length)
        cv.line(image, (x1, y1), (x2, y2), color, width)

    else:
        for l in lines[0]:
            x1, y1, x2, y2 = get_line_coordinates(l, line_length)
            p1 = (x1, y1)
            p2 = (x2, y2)
            cv.line(image, p1, p2, color, width)

    return image


def get_line_coordinates(line, line_length=1000):
    """
    >>> lines = detect_lines(test_image)
    >>> line = lines[0][0]
    >>> isinstance(get_line_coordinates(line), list)
    True

    >>> get_line_coordinates(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Line must be a line, is None.

    >>> get_line_coordinates(line, line_length=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Line_length value must be greater than 0.
    """

    # Checking arguments
    check_line(line)
    check_line_length(line_length)

    # Calculating line coordinates
    rho, theta = line
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + line_length*(-b))
    y1 = int(y0 + line_length*a)
    x2 = int(x0 - line_length*(-b))
    y2 = int(y0 - line_length*a)

    return [x1, y1, x2, y2]


def line_count(lines, line_length=1000, error=5):
    """
    >>> lines = detect_lines(test_image)
    >>> isinstance(line_count(lines), list)
    True

    >>> line_count(None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Lines can't be None.

    >>> line_count(lines, line_length=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Line_length value must be greater than 0.

    >>> line_count(lines, error=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Error value must be positive (0 included).
    """

    # Checking arguments
    check_lines(lines)
    check_line_length(line_length)
    check_error(error)

    total = 0
    v_lines = 0
    h_lines = 0

    # Checks the lines and compares their coordinates to get the number of
    # horizontal and vertical lines (+- error margin)
    if np.size(lines[0]) == 1:
        x1, y1, x2, y2 = get_line_coordinates(lines, line_length)
        if x1 in range(x2-error, x2+error):
            v_lines += 1
        elif y1 in range(y2-error, y2+error):
            h_lines += 1
        total += 1

    else:
        for l in lines[0]:
            x1, y1, x2, y2 = get_line_coordinates(l, line_length)
            if x1 in range(x2-error, x2+error):
                v_lines += 1
            elif y1 in range(y2-error, y2+error):
                h_lines += 1
            total += 1

    return [total, v_lines, h_lines]


def parallels(line1, line2, line_length=1000, error=5):
    """
    >>> lines = detect_lines(test_image)
    >>> line1 = lines[0][0]
    >>> line2 = lines[0][1]
    >>> isinstance(parallels(line1, line2), bool)
    True

    >>> parallels(None, line1)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Line must be a line, is None.

    >>> parallels(line2, None)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Line must be a line, is None.

    >>> parallels(line1, line2, line_length=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Line_length value must be greater than 0.

    >>> parallels(line1, line2, error=-10)
    Traceback (most recent call last):
      File "<stdin>", line 1, in ?
    ValueError: Error value must be positive (0 included).
    """

    # Checking arguments
    check_line(line1)
    check_line(line2)
    check_line_length(line_length)
    check_error(error)

    # Getting line coords
    l1_x1, l1_y1, l1_x2, l1_y2 = get_line_coordinates(line1, line_length)
    l2_x1, l2_y1, l2_x2, l2_y2 = get_line_coordinates(line2, line_length)

    return (l1_x1 - l2_x1 in range((l1_x2 - l2_x2 - error),
                                   (l1_x2 - l2_x2 + error))) and \
           (l1_y1 - l2_y1 in range((l1_y2 - l2_y2 - error),
                                   (l1_y2 - l2_y2 + error)))


# CHECKING ARGUMENTS


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


def check_color(color):

    if len(color) == 3:
        if (color[0] < 0 or color[0] > 255 or color[1] < 0 or color[1] > 255 or
                color[2] < 0 or color[2] > 255):
            raise ValueError("Color value must be: (0-255, 0-255, 0-255).")
    else:
        raise ValueError("Color value must be: (0-255, 0-255, 0-255).")
    return 0


def check_error(error):

    if error < 0:
        raise ValueError("Error value must be positive (0 included).")
    return 0


def check_houghlines_args(rho, theta, threshold):

    if rho < 0:
        raise ValueError("Rho value must be greater than 0.")

    if theta < 0:
        raise ValueError("Theta value must be greater than 0.")

    if threshold < 0:
        raise ValueError("Threshold value must be greater than 0.")
    return 0


def check_line(line):

    if line is None:
        raise ValueError("Line must be a line, is None.")
    if np.size(line) != 2:
        raise ValueError("Wrong format on line, line must be [rho, theta].")
    return 0


def check_line_length(line_length):

    if line_length <= 0:
        raise ValueError("Line_length value must be greater than 0.")
    return 0


def check_lines(lines):

    if lines is None:
        raise ValueError("Lines can't be None.")
    return 0


def check_width(width):

    if width < 0:
        raise ValueError("Width value must be greater than 0.")
    return 0