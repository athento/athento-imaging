#Athento-Imaging Summary

Athento-Imaging is a Python library designed to implement simple computer
vision operations. This package aims to perform the quality of an image as this
is a crucial factor in OCR.

To perform this operations, I have been using OpenCV, which you can download and
learn some of it from [OpenCV.org](http://www.opencv.org)

This file provides a quick overview of each module, describing in a few words
 the operations performed in each module. A complete description for each
 module and it's functions can be found in the manuals:

- [area_analysis](manuals/area_analysis.md)
- [bg_color](manuals/bg_color.md)
- [contours](manuals/contours.md)
- [ftm_pyramid](manuals/ftm_pyramid.md)
- [lines_detection](manuals/lines_detection.md)
- [salt_pepper](manuals/salt_pepper.md)
- [threshold](manuals/threshold.md)


##Summary

Each module name identifies the kind of operation that can be performed with the
 functions within the modules:

- **analysis_table**: sample module provided as an example of use of the whole
module. Provides an analysis of features used on real documents.

- **area_analysis**: performs a gray intensity analysis of the image and provides
a simple model.

- **bg_color**: uses a combination of Gaussian blur and thresholding to remove
noisy colored backgrounds.

- **contours**: analyzes the image looking for blocks of pixels and corners to
 perform an analysis of the template of the document instead of it's content.

- **ftm_pyramid**: performs a template matching operation using an approximation
with pyramids to improve it's performance.

- **img_utils**: module with auxiliary functions used in the whole application.

- **lines_detection**: analyzes the image looking for lines in it. It may remove
them, draw them or return some info about the lines. Lines are detected using
 the HoughLines/HoughLinesP functions.

- **salt_pepper**: transforms the image into grayscale and performs a complete
erode operation. This is used to improve the quality of the text when it has
much “salt and pepper” noise.

- **threshold**: performs different thresholds to an image (adaptive, or simple
plus variations).


##Testing

There are a few additional functions within each module, those are the "check
functions", which are written exclusively to get a cleaner code and allow us to
define and work with exceptions clearly.

As those functions do not perform any computer vision operation I'm not going to
explain much about them, you can check them directly in the code, and as you can
see they check the argument values.

If everything is ok (each argument has a correct value) the check functions
return 0.

There are also unit tests designed with doctest, the tests checks:

- A correct case, which an image extracted from the resources folder.
- A test for each possible exception in the function.

To test the modules (assuming you are already in the *athentoimaging* folder):

        python -m doctest *.py

You can also test each module separately:

        python -m doctest my_module.py
