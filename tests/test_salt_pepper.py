import pytest
import os
from athentoimaging.salt_pepper import clean

class Test_SP:

    test_image = os.path.abspath(os.path.join(os.path.dirname("__file__"),
                                              "resources/", "test_image.png"))

    #Everything works ok
    def test_sp_good(self):
        results = clean(self.test_image, 250, 3, 3)
        assert isinstance(results, list) and results is not None

    #Error if window_size < 0 (only positive odd values admited)
    def test_sp_negative_window(self):
        with pytest.raises(ValueError) as exc:
            clean(self.test_image, 250, -1, 3)
        assert exc.value.message == "Window size value must be greater than 0."


    #Error if kernel_size < 0  (only positive odd values admited)
    def test_sp_negative_kernel(self):
        with pytest.raises(ValueError) as exc:
            clean(self.test_image, 250, 3, -1)
        assert exc.value.message == "Kernel size value must be greater than 0."


    #Error if window_size has a even value (only positive odd values admitted)
    def test_sp_even_window(self):
        with pytest.raises(ValueError) as exc:
            clean(self.test_image, 250, 2, 3)
        assert exc.value.message == "Window size value must be odd."


    #Error if kernel_size has a even value (only positive odd values admitted)
    def test_sp_even_kernel(self):
        with pytest.raises(ValueError) as exc:
            clean(self.test_image, 250, 3, 2)
        assert exc.value.message == "Kernel size value must be odd."

    #Error if input image not found
    def test_sp_input_not_found(self):
        with pytest.raises(IOError) as exc:
            clean("fakeRoute", 250, 3, 3)
        assert exc.value.message == "Input file not found."

    #Error if input image is none
    def test_sp_input_none(self):
        with pytest.raises(IOError) as exc:
            clean(None, 250, 3, 3)
        assert exc.value.message == "Input file can't be None."

    #Error if input image is ''
    def test_sp_input_void(self):
        with pytest.raises(IOError) as exc:
            clean('', 250, 3, 3)
        assert exc.value.message == "Input file can't be ''."