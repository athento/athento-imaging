#lines_detection.py

This script allows to perform several operations in documents that contain lines.
It is based on the Standard Hough Line Transform implemented on OpenCV.


###Requirements

    - OpenCV
    - numpy
    - os


###Common arguments

    - input_file: the path to the image or directly the image to perform lines operations on it.
    - lines: a list of lines.
    - lineX: where X is a number. A single line.
    - line_length: the length of each line of the image.
    - width: the width of the line drawn.
    - color: the colour of the line drawn.
    - error: a margin of error of deviation of the lines. Sometimes not every
             pixel on a line is recognized as part of one, resulting in lines
             that may move some coordinates a few pixels even if the line is
              vertical or horizontal. On pixels.
         
           
###Import
              
To import this functions to your application, you must include the following line
at the beginning of your file:

    ```import lines_detection```

              
###Functions

####detect_lines(input_file, min_val=50, max_val=200, aperture_size=3, rho = 1, theta = np.pi/180, threshold = 200)

Uses the HoughLines function to detect lines in an image.

Arguments (rho, theta and threshold are used in the HoughLines call):

    - min_val: if intensity gradient lesser than min_val, the point is not an edge.
    - max_val: if intensity gradient greater than max_val, the point is an edge.
    - aperture_size: size of Sobel kernel used for find image gradients.
    - rho: the resolution of the parameter rho in pixels.
    - theta: the resolution of the parameter theta in radians.
    - threshold: the minimum number of intersections to "detect" a line.
    
Returns:
    
    A list of lines (each line is a set of coordinates).


####delete_lines(input_file, lines, line_length = 1000, width = 5, color = (255,255,255)):

Deletes the lines received by drawing them in the same color as the document's
background.
    
Returns:
    
    A new image which is the input image with the lines drawn in the selected 
    colour.

    
####delete_all_lines(input_file, rho=1, theta=np.pi/180, threshold=200, line_length = 1000, width = 5, color = (255, 255, 255)):

Uses the *delete_lines* function in a loop to delete all lines detected until no
more lines can be found in the image with *detect_lines*. 

Returns:
    
    A new image which is the input image with the lines drawn in the selected 
    colour.


####distance(line1, line2, line_length = 1000):

Calculates the absolute distance between two lines that must be parallels.

Returns:
    
    A list of two elements [x,y], which are the distance in pixels between two
    coordinates of the lines.

    
####distance_mean(lines, line_length = 1000):

Calculates the mean distance between a set of lines.

Returns:

    The mean of the distance between each line.


####draw_lines(input_file, lines, line_length = 1000, width=5, color=(0,0,255)):

Draws the lines into the input image in the selected colour.
    
Returns:

    A new image which is the input image with the input lines drawn on it in the
    selected colour.
    

####get_line_coordinates(line, line_length = 1000):

Calculates the coordinates of the line received given a line length.
    
Returns:

    [x1, y1, x2, y2] a set of coordinates that represents the line.
   
    
####line_count(lines, line_length = 1000, error = 5):

Counts the total of lines, and checks how many horizontal and vertical lines are.
A line is considered horizontal or vertical if it's coordinates (Y or X 
respectively) is constant (+- error argument value).
    
Returns:

    [total, num_vertical_lines, num_horizontal_lines]


####parallels(line1, line2, line_length = 1000, error = 5):

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