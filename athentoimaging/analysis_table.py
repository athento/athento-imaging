import area_analysis as aa
import contours as cc
import time
import img_utils as iu
import cv2 as cv
import numpy as np

"""
This module is not intended to work as a part of a production environment.
It will be used to test some of the functions developed in the other modules.
However images used on this table will not be provided in the repository.
"""

def analyze_all(files, min_length=1000, line_length=1000, line_error=5):

    results = []

    for i in files:
        #print "Processing ", i
        results = results + \
                  [get_analysis_results(i, min_length, line_length, line_error)]

    return results



def get_analysis_results(input_file, min_dim=1000, line_length=1000, line_error=15):

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

    contours_lines = cc.draw_contours(blank, contours, color=(255, 0, 0), thickness=10)
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


def show_table(table):

    index = ["File",
             "Type",
             "Contour dimension",
             "Document area",
             "# of blocks",
             "Model",
             "# of corners"]

    first_line = ""

    for i in index:
        first_line = first_line + i + ","

    print first_line

    types = ["D",
             "D",
             "D",
             "D",
             "D",
             "D",
             "D",
             "D",
             "FT",
             "FT",
             "FT",
             "FT",
             "FT",
             "FT",
             "FT",
             "FT",
             "PC",
             "PC",
             "PC",
             "PC"
    ]

    for n, i in enumerate(table):
        line = str(i[0]) + "," + \
               types[n] + "," + \
               str(i[1]) + "," + \
               str(i[2]) + "," + \
               str(i[3]) + "," + \
               str(i[4]) + "," + \
               str(i[5]) + "," #+ \
               #str(i[6]) + "," + \
               #str(i[7]) + "," + \
               #str(i[8])
        print line

    return 0

if __name__ == '__main__':

    start = time.time()

    files = ["../../../../page-03.png",
             "../../../../page-04.png",
             "../../../../page-13.png",
             "../../../../page-14.png",
             "../../../../page-24.png",
             "../../../../page-25.png",
             "../../../../page-43.png",
             "../../../../page-44.png",
             "../../../../page-05.png",
             "../../../../page-06.png",
             "../../../../page-27.png",
             "../../../../page-28.png",
             "../../../../page-35.png",
             "../../../../page-36.png",
             "../../../../page-45.png",
             "../../../../page-46.png",
             "../../../../page-02.png",
             "../../../../page-12.png",
             "../../../../page-23.png",
             "../../../../page-42.png",
    ]

    #files = ["../../../../page-04.png"]

    #D --> DNI
    #FT --> Ficha tecnica
    #PC --> Permiso de conducir

    types = ["D",
             "D",
             "D",
             "D",
             "D",
             "D",
             "D",
             "D",
             "FT",
             "FT",
             "FT",
             "FT",
             "FT",
             "FT",
             "FT",
             "FT",
             "PC",
             "PC",
             "PC",
             "PC"
    ]

    show_table(analyze_all(files))
    

    print time.time()-start
