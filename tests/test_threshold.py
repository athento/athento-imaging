import pytest
import os
from athentoimaging.threshold import apply
import cv2 as cv


class Test_TH:

    test_image = os.path.abspath(os.path.join(os.path.dirname(
                            "__file__"), "resources/", "test_image.png"))


    #Single threshold value, everything works ok
    def test_th_single_th(self):
        result = apply(self.test_image, 150)
        assert isinstance(result, list) and result is not None

    #Multi threshold values, everything works ok
    def test_th_multi_th(self):
        result = apply(self.test_image, [220, 230, 250])
        assert isinstance(result, list) and result is not None

    #Error if input image is None
    def test_th_img_none(self):
        with pytest.raises(IOError) as exc:
            apply(None, 150)
        assert exc.value.message == "Input file can't be None."

    #Error if threshold value is negative (only values between 0 and 255)
    def test_th_negative_thresh(self):
        with pytest.raises(ValueError) as exc:
            apply(self.test_image, -230)
        assert exc.value.message == "All threshold values must be between 0 and 255"

    #Error if threshold value is over 255 (only values between 0 and 255)
    def test_th_over_thresh(self):
        with pytest.raises(ValueError) as exc:
            apply(self.test_image, 270)
        assert exc.value.message == "All threshold values must be between 0 and 255"