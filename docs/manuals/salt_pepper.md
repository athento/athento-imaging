#salt_pepper.py

This script cleans an image with salt and pepper noise (ie: text dotted due to 
bad pixel definition).

Transforms the image into gray-scale and applies a Gaussian Blur + a Median Blur 
to get extra definition to the text. After getting extra pixels for the letters, 
we use the function erode to outline the text in order to improve the quality of 
the data read by OCR.
        
In the end, it applies a series of threshold values (or the ones received by 
parameter) to the modified image and shows them one by one asking the user to 
save the current threshold image.


###Requirements

    - OpenCV
    - argparse
    - os
    - threshold


###Common arguments

    - input_file: input file, can be a file path or an image (np array).
    - thresh_val: list of values used to threshold.
    - quality: quality to use in the pdf_to_png transformation.
    - window_size: size of the window used to blur. As this values increases so
                    does the blur.
    - kernel_size: size of the kernel used to blur. As this values increases so
                    does the blur.


###Use in CLI
    
    python clean_erode.py -i myImage.png 
    python clean_erode.py -i myImage.png -t X, X = threshold value. 
    python clean_erode.py -i myImage.png -k X, X = kernel size used in the erode. 
    python clean_erode.py -i myImage.png -w X, where X is the size of the window
                                                used in the Gaussian Blur.

As usual, you can use any combination of parameters that you may need.


###Import

To import this function into your application, you must include the following 
line at the beginning:

    ```from clean_erode import clean```


###Functions

####clean(input_file,  thresh_val = [250, 245, 240, 230, 225, 220], window_size = 5, kernel_size = 5)

Transforms the image into gray-scale and applies a Gaussian Blur + a Median Blur 
to get extra definition to the text. After getting extra pixels for the letters, 
we use the function erode to outline the text in order to improve the quality of 
the data read by OCR.

In the end, it applies each thresh_val to the image to get different versions of 
the threshold source image.

Returns:
    
    A list of images cleaned with all values in thresh_val.
                
                
####check_arguments(input_file, window_size)

Checks that input_file exists and that window_size is greater than 0 and an 
even number. Launches exceptions if any argument is not valid.

Returns:
    
    0 if everything works ok.

