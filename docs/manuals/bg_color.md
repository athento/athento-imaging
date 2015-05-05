#bg_color.py

This script allows to clean an image with noisy background (ie: coloured 
background). It is based in the combination of the operations GaussianBlur to 
remove some of the background noise, and after a threshold which will turn the
image into a white and black image.


###Common arguments

These are some of the main arguments used in this module:

    - input_file: input file, can be a file path or an image (np array).
    - thresh_val: list of values used to threshold.
    - kernel_size: size of the window used to blur. As this values increases so
                    does the blur.
    - block_size: size of the block used in adaptive thresholding.
    - c: constraint to diminish the block mean.

                  
###Import        
        
To import this module into your application, you must include the following 
line at the beginning of your own python file:

        import bg_color as bgc


###Functions

In this section you'll find a summary of each function included in this module 
except the *check_argument* functions, which always return either 0 or an 
exception if any parameter is out of it's limits.


- ####adaptive_gaussian_clean(input_file, kernel_size=3, block_size=11, c=5)

    Loads the image, it applies a Gaussian Blur with the kernel_size and after it 
 uses the threshold module to apply a gaussian adaptive threshold.
 
    Returns: a single image, the input_file cleaned.


- ####adaptive_mean_clean(input_file, kernel_size=3, block_size=11, c=5)

    Loads the image, it applies a Gaussian Blur with the kernel_size and after it 
 uses the threshold module to apply a mean adaptive threshold.
 
    Returns: a single image, the input_file cleaned.


- ####clean(input_file, thresh_val=200, kernel_size=3)

    Loads the image, it applies a Gaussian Blur with the kernel_size and after it 
 uses the threshold module to apply threshold.
 
    Returns: a single image, the input_file cleaned.