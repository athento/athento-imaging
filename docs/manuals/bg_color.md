#bg_color.py

This script allows to clean an image with noisy background (ie: coloured 
background).


###Requirements

    - OpenCV
    - argparse
    - os
    - threshold


###Common arguments

    - input_file: input file, can be a file path or an image (np array).
    - thresh_val: list of values used to threshold.
    - window_size: size of the window used to blur. As this values increases so
                    does the blur.

                  
###Use in CLI

    python remove_bg_color.py -i myImage.png 
    python remove_bg_color.py -i myImage.png -t X, where X is the threshold value. 
    python remove_bg_color.py -i myImage.png -w X, where X is the size of the 
                                                    window used in the Gaussian Blur.

As usual, you can use any combination of parameters that you may need.


###Import        
        
To import this function into your application, you must include the following 
line at the beginning:

    ```from bg_color import clean```


###Functions

####check_arguments(input_file, window_size)

Checks that input_file exists and that window_size is greater than 0 and an 
even number. Launches exceptions if any argument is not valid.

Returns:
    
    0 if everything works ok.


####clean(input_file, thresh_val =  [225, 220, 215, 210, 205, 200], window_size = 3)

Transforms the input file to gray-scale and applies a Gaussian Blur to the image.
In the end, it applies each thresh_val to the image to get different versions of 
the threshold source image.

Returns:
    
    A list of images cleaned with all values in thresh_val.