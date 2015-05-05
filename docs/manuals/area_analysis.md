#area_analysis.py

This module implements operations to get a model of the image dividing it and analyzing each crop's intensity value.


###Common arguments

These are some of the main arguments used in this module:

    - input_file: input file, can be a file path or an image (np array).
    - split_x, split_y: number of divisions to do to the image to process it.


###Import

To import this module into your application, you must include the following 
line at the beginning of your own python file:
    
        import area_analysis as aa
            

###Functions

In this section you'll find a summary of each function included in this module 
except the *check_argument* functions, which always return either 0 or an 
exception if any parameter is out of it's limits.

- ####get_gray_intensity(input_file)

    Returns: the mean piel value of the input_file.

- ####get_gray_intensity_analysis(input_file, split_x=3, split_y=3)

    Divides the input_file in split_x*split_y parts and applies get_gray_intensity in each one.
    
    Returns: a list of the gray intensity value for each split.

- ####get_model(input_file, split_x=3, split_y=3)

    Analyzes the get_gray_intensity_analysis result and compares it to the mean of the whole
    image, if it's darker the split will get a 1, if it's brighter gets a 0.
    
    Returns: same list as get_gray_intensity_analysis but with 1's and 0's as the previous criteria.