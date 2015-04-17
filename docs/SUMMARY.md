#PyDocCV Summary

PyDocCV is a set of Python modules designed to implement simple computer vision
operations. This package aims to perform the quality of an image as this is a
crucial factor in OCR.

To perform this operations, I have been using OpenCV, which you can download and
learn some of it from [OpenCV.org](http://www.opencv.org)

This file provides a quick overview of each module, describing in a few words the
operations performed in each module. A complete description for each module and
it's functions can be found in the manuals:

- [bg_color](manuals/bg_color.md)
- [ftm_pyramid](anuals/ftm_pyramid.md)
- [lines_detection](manuals/lines_detection.md)
- [lines_detection_p](manuals/lines_detection_p.md)
- [salt_pepper](manuals/salt_pepper.md)
- [threshold](manuals/threshold.md)


##Summary

Each module name identifies the kind of operation that can be performed with the
 functions within the modules:

- **bg_color**:  transforms the image into grayscale and applies a series
 of threshold values to the image if none is indicated by parameter.

- **ftm_pyramid**: performs a template matching operation using an approximation
with pyramids to improve it's performance.

- **lines_detection**: analyses the image looking for lines in it. It may remove
them, draw them or return some info about the lines. Lines are detected using the 
HoughLines function.

- **lines_detection_p**: equivalent to lines_detection but using a probabilistic
approach.  Lines are detected using the HoughLinesP function.
    
- **salt_pepper**: transforms the image into grayscale and performs a complete 
erode operation. This is used to improve the quality of the text when it has 
much “salt and pepper” noise.

- **threshold**: applies a series of threshold values to an input image.


##Use in CLI

Some of the functions described below may be used directly in the CLI. In order 
to know how to properly use the commands, open a terminal and navigate to the 
*pydoccv* folder and type:

    ```python my_module.py -h```
    
Where my_module may be any of the module names listed before.
