import area_analysis as aa
import contours as cc
import img_utils as iu
import numpy as np
import argparse
import time

"""
This module is not intended to work as a part of a production environment.
It will be used to test some of the functions developed in the other modules.
However images used on this table will not be provided in the repository.
"""


def analyze_all(files, min_length=1000):

    results = []

    if not isinstance(files, list):
        files = [files]

    for i in files:
        results = results + [get_analysis(i, min_length)]

    return results


def get_analysis(input_file, min_dim=1000):

    original = iu.get_image(input_file)

    original = iu.pyramid_clean(original)

    cleaned = cc.delete_border_noise(original)

    contours = cc.detect_contours(cleaned)
    contours = cc.delete_small_contours(contours, min_dim)
    contours = cc.get_squares(contours)
    contours = cc.join_contours(contours, min_dist=10)

    blank = np.zeros(original.shape, np.uint8)
    blank[:] = 255
    blank2 = np.zeros(original.shape, np.uint8)
    blank2[:] = 255

    contours_lines = cc.draw_contours(blank, contours, color=(255, 0, 0),
                                      thickness=10)
    filled = cc.draw_contours(blank2, contours, color=(0, 0, 0), thickness=-1)

    if len(contours) > 0:
        dimension = 0
        area = 0
        squares = len(contours)
        for c in contours:
            dimension = dimension + cc.get_contour_dimension(c)
            area = area + cc.get_contour_area(c)

    else:
        dimension = -1
        area = -1
        squares = 0

    model = aa.get_model(filled)

    corners = cc.detect_corners(contours_lines)

    num_corners = len(corners)

    results = [input_file,
               dimension,
               area,
               squares,
               model,
               num_corners
               ]

    return results


def show_table(table, types):

    first_line = "File, Type, Contour dimension, Document area, # of blocks, " \
                 "Model, # of corners"

    print first_line

    for n, i in enumerate(table):
        line = str(i[0]) + "," + types[n] + "," + str(i[1]) + "," + \
               str(i[2]) + "," + str(i[3]) + "," + str(i[4]) + "," + \
               str(i[5])
        print line

    return 0


if __name__ == '__main__':

    start = time.time()

    # CLI arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required="True",
                    help="Path to the input file.")
    ap.add_argument("-t", "--type", required="True",
                    help="Input file type")
    args = vars(ap.parse_args())

    files = args["input"]

    if not isinstance(files, list):
        files = [files]

    types = args["type"]

    if not isinstance(types, list):
        types = [types]

    show_table(analyze_all(files), types)

    print "{0} files analyzed in {1} seconds".format(len(files),
                                                     round(time.time() -
                                                           start, 3))
