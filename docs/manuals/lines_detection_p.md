#lines_detection_p.py

This script allow to perform several operations in documents that contain lines.
It is based on the Probabilistic Hough Line Transform implemented on OpenCV.

There is no need of a get_line_coordinates in this module as the lines are
already a set of [x1, y1, x2, y2] coordinates.

Requirements:

    - OpenCV
    - numpy

Common parameters:

    - input_file: the path to the image or directly the image to perform lines operations on it.
    - lines: a list of lines.
    - lineX: where X is a number. A single line.
    - width: the width of the line drawn.
    - color: the colour of the line drawn.
    - error: a margin of error of deviation of the lines. Sometimes not every
             pixel on a line is recognized as part of one, resulting in lines
             that may move some coordinates a few pixels even if the line is
              vertical or horizontal. On pixels.
              
To import this functions to your application, you must include the following line
at the beginning of your file:

    ```import lines_detection```

              
####Operations supported:

####def detect_lines(input_file, minLineLength = 30, maxLineGap = 20, rho = 1, theta = np.pi/180, threshold = 200):"

Uses the HoughLines function to detect lines in an image.

Arguments (all the arguments are used in the HoughLinesP call):

    - minLineLength: the minimum  
    - maxLineGap: maximum gap between two points to be considered in the same line. 
    - rho: the resolution of the parameter rho in pixels.
    - theta: the resolution of the parameter theta in radians.
    - threshold: the minimum number of intersections to "detect" a line.
    
Returns:
    
    A list of lines (each line is a set of coordinates).


####delete_lines(input_file, lines, width = 5, color = (255,255,255)):

Deletes the lines received by drawing them in the same color as the document's
background.
    
Returns:
    
    A new image which is the input image with the lines drawn in the selected 
    colour.

    
####delete_all_lines(input_file, width = 5, color = (255, 255, 255)):

Uses the *delete_lines* function in a loop to delete all lines detected until no
more lines can be found in the image. 

Returns:
    
    A new image which is the input image with the lines drawn in the selected 
    colour.
    

####distance(line1, line2):

Calculates the absolute distance between two lines that must be parallels.

Returns:
    
    A list of two elements [x,y], which are the distance in pixels between two
    coordinates of the lines.

    
####distance_mean(lines):

Calculates the mean distance between a set of lines.

Returns:

    The mean of the distance between each line.


####draw_lines(input_file, lines, width=5, color=(0,0,255)):

Draws the lines into the input image in the selected colour.
    
Returns:

    A new image which is the input image with the input lines drawn on it in the
    selected colour.
   
    
####line_count(lines, error = 5):

Counts the total of lines, and checks how many horizontal and vertical lines are.
A line is considered horizontal or vertical if it's coordinates (Y or X 
respectively) is constant (+- error argument value).
    
Returns:

    [total, num_vertical_lines, num_horizontal_lines]


####parallels(line1, line2, error = 5):

Checks if two lines are parallels, within an expected margin of error in pixels.

Returns:

    True or false.


###Testing

There are a few more functions in the *lines_detection* module, those are the
"check functions", which are written exclusively to get a cleaner code and allow
us to define and work with exceptions quickly.

As those functions do not perform any computer vision operation I'm not going to
explain much about them, you can check them directly in the code, and as you can
see they check the argument values.

If everything is ok (each argument has a correct value) returns 0.

Else returns exception (usually ValueError or IOError)