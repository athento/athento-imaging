import area_analysis as aa
import lines_detection as ld
import time
import argparse
import cv2 as cv


def analyze_all(files, min_length=1000, line_length=1000, line_error=5):

    results = []

    for i in files:
        print "Processing ", i
        results = results + [get_analysis_results(i, min_length, line_length, line_error)]

    return results



def get_analysis_results(input_file, min_length=1000, line_length=1000, line_error=5):

    contours = aa.detect_contours(input_file)
    contours = aa.get_squares(contours)
    lines = ld.detect_lines(input_file)

    if len(contours) > 0:
        dimension = []
        area = []
        #coordinates = []
        squares = aa.get_square_number(contours, min_length)
        for c in contours:
            dimension = dimension + [aa.get_contour_dimension(c)]
            area = area + [aa.get_contour_area(c)]
            #coordinates = coordinates + [aa.get_contour_coord(c)]

    else:
        dimension = -1
        area = -1
        squares = 0
        coordinates = -1

    gray_analysis = aa.get_gray_intensity_analysis(input_file, 3, 2)

    counts = ld.line_count(lines, line_length, line_error)

    distance_mean = -1
    if counts[0] < 200:
        distance_mean = ld.distance_mean(lines, line_length)

    results = [input_file,
               dimension,
               area,
               squares,
               #coordinates,
               gray_analysis,
               counts,
               distance_mean
               ]

    return results


def show_table(table):

    index = ["File", "Type", "Contour dimension", "Contour area", "Number of squares", "Gray intensity", "Number of lines (T-V-H)", "Distance mean between lines"]

    first_line = ""

    for i in index:
        first_line = first_line + "," + i

    print first_line

    types = ["PC", "D", "D", "FT", "FT", "PC", "D", "D", "PC", "D", "D", "FT", "FT", "D", "D", "FT", "FT", "PC", "D", "D", "FT", "FT"]

    for n, i in enumerate(table):
        line = str(i[0]) + "," + types[n] + "," + str(i[1]) + "," + str(i[2]) + "," + str(i[3]) + "," + str(i[4]) + "," + str(i[5]) + "," + str(i[6])
        print line

    return 0

if __name__ == '__main__':

    start = time.time()
    """
    #CLI arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--input", required="True",
                    help="Path to the input image.")
    ap.add_argument("-m", "--minlength",
                    help="Minimum perimeter length wanted.")
    ap.add_argument("-l", "--linelength",
                    help="Line length wanted.")
    args = vars(ap.parse_args())

    #Loading values
    input_file = args["input"]
    min_length = args["minlength"]
    line_length = args["linelength"]

    if min_length is None:
        min_length = 1000

    if line_length is None:
        line_length = 1000
    """
    files = ["../../../../page-02.png", "../../../../page-03.png", "../../../../page-04.png", "../../../../page-05.png",
             "../../../../page-06.png", "../../../../page-12.png", "../../../../page-13.png", "../../../../page-14.png",
             "../../../../page-23.png", "../../../../page-24.png", "../../../../page-25.png", "../../../../page-27.png",
             "../../../../page-28.png", "../../../../page-31.png", "../../../../page-32.png", "../../../../page-35.png",
             "../../../../page-36.png", "../../../../page-42.png", "../../../../page-43.png",
             "../../../../page-44.png", "../../../../page-45.png", "../../../../page-46.png"]

    #D --> DNI
    #PC --> Permiso de conducir
    #FT --> Ficha tecnica
    types = ["PC", "D", "D", "FT", "FT", "PC", "D", "D", "PC", "D", "D", "FT", "FT", "D", "D", "FT", "FT", "PC", "D", "D", "FT", "FT"]

    show_table(analyze_all(files))

    print time.time()-start