#threshold.py

This script applies a series of threshold values to the input image.


###Requirements

    - OpenCV
    - argparse
    - os
    

###Common arguments

    - input_file: input file, can be a file path or an image (np array).
    - thresh_val: list of values used to threshold.


###Use in CLI

    python threshold.py -i myImage.png 
    python threshold.py -i myImage.png -t X, where X is the threshold value


###Import
    
To import this function into your application, you must include the following 
line at the beginning:
    
    ```from threshold import apply```
    

###Functions

####apply(input_file, thresh_values=[250, 245, 240, 230, 225, 220])

Applies each element in thresh_values to perform a threshold operation on the
input file.

Returns:

    A list of images with different thresh_val.


####check_arguments(input_file, thresh_values)

Checks that input_file exists and that each thresh_values element is greater than 
0 and smaller than 256. Launches exceptions if any argument is not valid.

Returns:
    
    0 if everything works ok.
