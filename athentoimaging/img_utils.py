import cv2 as cv

"""
This script contains auxilary functions to be used during development.
Functions contained in this script probably won't be necessary in the product's
integration.
"""

def save_img(image, output_name, question):

    if image == None:
        raise IOError("Input image is None.")

    if question == '':
        raise ValueError("The value of the question can't be ''.")

    if question == None:
        raise ValueError("The question can't be a None object.")

    if output_name == '':
        raise ValueError("The value of the output name can't be ''.")

    if output_name == None:
        raise ValueError("The output name can't be a None object.")

    #CHANGE THE NEXT FEW LINES TO CHANGE THE INPUT SYSTEM
    ans = input(question)

    # Checks that the input is within the correct values
    ans_list = ["y", "yes", "n", "no", "Y", "YES", "N", "NO"]
    while ans not in ans_list:
        ans = input(question)

    #END CHANGES


    # Saving the thresholded image
    if ans[0] == 'y' or ans[0] == 'Y':
        print "Saving..."
        cv.imwrite(output_name, image)
        print "Saved as {0}.".format(output_name)

    return 0