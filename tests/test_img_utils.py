import pytest
import os
import athentoimaging.img_utils as iu
import cv2 as cv


class Test_SaveImg:

    test_image = cv.imread(os.path.abspath(os.path.join(os.path.dirname(
                            "__file__"), "resources/", "test_image.png")))

    """
    This test might have to be overwritten during final implementation on the
    product as the input sistem probably won't be the same.

    #Everything works ok
    def test_save_img_good(self):
        assert iu.save_img(self.test_image, "output name", "My Question") == 0
    """

    #Error if input image is None
    def test_save_img_none(self):
        with pytest.raises(IOError) as exc:
            iu.save_img(None, "output", "My Question")
        assert exc.value.message == "Input image is None."

    #Error if question is ''
    def test_save_img_question_void(self):
        with pytest.raises(ValueError) as exc:
            iu.save_img(self.test_image, "output", "")
        assert exc.value.message == "The value of the question can't be ''."

    #Error if question is None object
    def test_save_img_question_none(self):
        with pytest.raises(ValueError) as exc:
            iu.save_img(self.test_image, "output", None)
        assert exc.value.message == "The question can't be a None object."

    #Error if output name is ''
    def test_save_img_output_void(self):
        with pytest.raises(ValueError) as exc:
            iu.save_img(self.test_image, '', "My Question")
        assert exc.value.message == "The value of the output name can't be ''."

    #Error if output name is None object
    def test_save_img_output_none(self):
        with pytest.raises(ValueError) as exc:
            iu.save_img(self.test_image, None, "My Question")
        assert exc.value.message == "The output name can't be a None object."