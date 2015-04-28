import area_analysis as aa
import lines_detection as ld
import contours as cc
import time
import img_utils as iu
import cv2 as cv


def analyze_all(files, min_length=1000, line_length=1000, line_error=5):

    results = []

    for i in files:
        print "Processing ", i
        results = results + \
                  [get_analysis_results(i, min_length, line_length, line_error)]

    return results



def get_analysis_results(input_file, min_dim=1000, line_length=1000, line_error=15):

    original = iu.get_image(input_file)

    #aux = iu.pyramid_clean(original)

    cleaned = cc.delete_border_noise(original)

    contours = cc.detect_contours(cleaned, min_dimension=min_dim)
    contours = cc.get_squares(contours)

    blank = original
    blank[:] = 255

    contours_lines = cc.draw_contours(blank, contours, thickness=10)
    filled = cc.draw_contours(blank, contours, thickness=-1)

    lines = ld.detect_lines(contours_lines)

    if len(contours) > 0:
        dimension = []
        area = []
        #coordinates = []
        squares = len(contours)
        for c in contours:
            dimension = dimension + [cc.get_contour_dimension(c)]
            area = area + [cc.get_contour_area(c)]
            #coordinates = coordinates + [aa.get_contour_coord(c)]

    else:
        dimension = -1
        area = -1
        squares = 0
        #coordinates = -1

    gray_analysis = aa.get_gray_intensity_analysis(filled, 2, 2)

    if lines is not None:
        counts = ld.line_count(lines, line_length, line_error)
        if counts[0] < 200:
            distance_mean = ld.distance_mean(lines, line_length)
    else:
        counts = -1
        distance_mean = -1

    model = aa.get_model(filled)

    corners = cc.detect_corners(contours_lines)

    cv.imshow("", cc.draw_corners(contours_lines, corners))
    cv.waitKey()
    cv.destroyAllWindows()


    num_corners = len(corners)

    results = [input_file,
               sum(dimension),
               sum(area),
               squares,
               #coordinates,
               gray_analysis,
               counts,
               distance_mean,
               model,
               num_corners
               ]

    return results


def show_table(table):

    index = ["File", "Type", "Estimated contour dimension",
             "Estimated document area", "Number of squares",
             "Gray intensity", "Number of lines (T-V-H)",
             "Distance mean between lines", "Model",
             "Number of corners"]

    first_line = ""

    for i in index:
        first_line = first_line + i + ","

    print first_line

    types = ["PC", "D", "D", "FT", "FT", "PC", "D", "D", "PC", "D", "D", "FT",
             "FT", "FT", "FT", "PC", "D", "D", "FT", "FT"]

    for n, i in enumerate(table):
        line = str(i[0]) + "," + types[n] + "," + str(i[1]) + "," + str(i[2]) + \
               "," + str(i[3]) + "," + str(i[4]) + "," + str(i[5]) + "," + \
               str(i[6]) + "," + str(i[7]) + "," + str(i[8])
        print line

    return 0

if __name__ == '__main__':

    start = time.time()
    files = ["../../../../page-02.png", "../../../../page-03.png",
             "../../../../page-04.png", "../../../../page-05.png",
             "../../../../page-06.png", "../../../../page-12.png",
             "../../../../page-13.png", "../../../../page-14.png",
             "../../../../page-23.png", "../../../../page-24.png",
             "../../../../page-25.png", "../../../../page-27.png",
             "../../../../page-28.png", "../../../../page-35.png",
             "../../../../page-36.png", "../../../../page-42.png",
             "../../../../page-43.png", "../../../../page-44.png",
             "../../../../page-45.png", "../../../../page-46.png"]

    #files = ["../../../../page-24.png"]

    #D --> DNI
    #PC --> Permiso de conducir
    #FT --> Ficha tecnica
    types = ["PC", "D", "D", "FT", "FT", "PC", "D", "D", "PC", "D", "D", "FT",
             "FT", "D", "D", "FT", "FT", "PC", "D", "D", "FT", "FT"]

    show_table(analyze_all(files))
    

    print time.time()-start
