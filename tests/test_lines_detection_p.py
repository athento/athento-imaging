import pytest
import os
import athentoimaging.lines_detection_p as ld
import numpy as np

class Test_LD:

        test_image = os.path.abspath(os.path.join(os.path.dirname("__file__"),
                                              "resources/", "lines.jpg"))
        lines = ld.detect_lines(test_image)

    # Tests of detect_line

        def test_detect_lines_good(self):
            r = ld.detect_lines(self.test_image)
            assert len(r) >= 0

        def test_detect_lines_file_void(self):
            with pytest.raises(ValueError) as exc:
                ld.detect_lines('')
            assert exc.value.message == "Input_file must be different than '' " \
                                        "or None."

        def test_detect_lines_file_none(self):
            with pytest.raises(ValueError) as exc:
                ld.detect_lines(None)
            assert exc.value.message == "Input_file must be different than '' " \
                                        "or None."

        def test_detect_lines_file_not_found(self):
            with pytest.raises(IOError) as exc:
                ld.detect_lines("fakePath")
            assert exc.value.message == "Input file not found."

        def test_detect_lines_min_val_negative_error(self):
            with pytest.raises(ValueError) as exc:
                ld.detect_lines(self.test_image, min_val=-200)
            assert exc.value.message == "Min_val value must be between 0 and 255."

        def test_detect_lines_min_val_overflow_error(self):
            with pytest.raises(ValueError) as exc:
                ld.detect_lines(self.test_image, min_val=260, max_val=270)
            assert exc.value.message == "Min_val value must be between 0 and 255."

        def test_detect_lines_max_val_negative_error(self):
            r = ld.detect_lines(self.test_image, min_val=200, max_val=-100)
            assert r is None

        def test_detect_lines_max_val_overflow_error(self):
            with pytest.raises(ValueError) as exc:
                ld.detect_lines(self.test_image, min_val=100, max_val=260)
            assert exc.value.message == "Max_val value must be between 0 and 255."

        def test_detect_lines_min_val_over_max_val(self):
                r = ld.detect_lines(self.test_image, min_val=200, max_val=100)
                assert r is None

        def test_detect_lines_aperture_size_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.detect_lines(self.test_image, aperture_size=-1)
            assert exc.value.message == "Aperture_size value must be greater than 0."

        def test_detect_lines_rho_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.detect_lines(self.test_image, rho=-1)
            assert exc.value.message == "Rho value must be greater than 0."

        def test_detect_lines_theta_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.detect_lines(self.test_image, theta=-1)
            assert exc.value.message == "Theta value must be greater than 0."

        def test_detect_lines_threshold_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.detect_lines(self.test_image, threshold=-1)
            assert exc.value.message == "Threshold value must be greater than 0."

        def test_detect_lines_min_line_length_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.detect_lines(self.test_image, min_line_length=-10)
            assert exc.value.message == "Min_line_length must be greater than 0."

        def test_detect_lines_max_line_gap_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.detect_lines(self.test_image, max_line_gap=-10)
            assert exc.value.message == "Max_line_gap must be greater than 0."

    # Tests of delete_lines

        def test_delete_lines_good(self):
            lines = ld.detect_lines(self.test_image)
            r = ld.delete_lines(self.test_image, lines)
            assert isinstance(r, np.ndarray)

        def test_delete_lines_good(self):
            lines = ld.detect_lines(self.test_image)
            r = ld.delete_lines(self.test_image, lines[0][0])
            assert isinstance(r, np.ndarray)

        def test_delete_lines_lines_none(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_lines(self.test_image, None)
            assert exc.value.message == "Lines can't be None."

        def test_delete__lines_width_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_lines(self.test_image, self.lines, width=-10)
            assert exc.value.message == "Width value must be greater than 0."

        def test_delete_lines_color_error(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_lines(self.test_image, self.lines, color=(260, 0, 0))
            assert exc.value.message == "Color value must be: (0-255, 0-255, 0-255)."

    # Tests of delete_all_lines

        def test_delete_all_lines_good(self):
            assert isinstance(ld.delete_all_lines(self.test_image), np.ndarray)

        def test_delete_all_lines_file_void(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_all_lines('')
            assert exc.value.message == "Input_file must be different than '' " \
                                        "or None."

        def test_delete_all_lines_file_none(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_all_lines(None)
            assert exc.value.message == "Input_file must be different than '' " \
                                        "or None."

        def test_delete_all_lines_file_not_found(self):
            with pytest.raises(IOError) as exc:
                ld.delete_all_lines("fakePath")
            assert exc.value.message == "Input file not found."

        def test_delete_all_lines_min_val_negative_error(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_all_lines(self.test_image, min_val=-200)
            assert exc.value.message == "Min_val value must be between 0 and 255."

        def test_delete_all_lines_min_val_overflow_error(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_all_lines(self.test_image, min_val=260)
            assert exc.value.message == "Min_val value must be between 0 and 255."

        def test_delete_all_lines_max_val_negative_error(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_all_lines(self.test_image, min_val = 100, max_val=-200)
            assert exc.value.message == "Max_val value must be between 0 and 255."

        def test_delete_all_lines_max_val_overflow_error(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_all_lines(self.test_image, min_val=100, max_val=260)
            assert exc.value.message == "Max_val value must be between 0 and 255."

        def test_delete_all_lines_min_val_over_max_val(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_all_lines(self.test_image, min_val=200, max_val=100)
            assert exc.value.message == "Min_val value must be lesser than max_val."

        def test_delete_all_lines_rho_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_all_lines(self.test_image, rho=-1)
            assert exc.value.message == "Rho value must be greater than 0."

        def test_delete_all_lines_theta_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_all_lines(self.test_image, theta=-1)
            assert exc.value.message == "Theta value must be greater than 0."

        def test_delete_all_lines_threshold_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_all_lines(self.test_image, threshold=-1)
            assert exc.value.message == "Threshold value must be greater than 0."

        def test_delete_all_lines_width_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_all_lines(self.test_image, width=-10)
            assert exc.value.message == "Width value must be greater than 0."

        def test_delete_all_lines_color_error(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_all_lines(self.test_image, color=(260, 0, 0))
            assert exc.value.message == "Color value must be: (0-255, 0-255, 0-255)."

        def test_delete_all_lines_min_line_length_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_all_lines(self.test_image, min_line_length=-10)
            assert exc.value.message == "Min_line_length must be greater than 0."

        def test_delete_all_lines_max_line_gap_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.delete_all_lines(self.test_image, max_line_gap=-10)
            assert exc.value.message == "Max_line_gap must be greater than 0."

    # Tests of distance

        def test_distance_good(self):
            result = ld.distance(self.lines[0][0], self.lines[0][1])
            assert isinstance(result[0], int) and isinstance(result[1], int)

        def test_distance_line1_none(self):
            with pytest.raises(ValueError) as exc:
                ld.distance(None, self.lines[0][1])
            assert exc.value.message == "Line must be a line, is None."

        def test_distance_line1_wrong(self):
            with pytest.raises(ValueError) as exc:
                ld.distance([5], self.lines[0][1])
            assert exc.value.message == "Wrong format on line, line must be [rho, theta]."

        def test_distance_line2_none(self):
            with pytest.raises(ValueError) as exc:
                ld.distance(self.lines[0][0], None)
            assert exc.value.message == "Line must be a line, is None."

        def test_distance_line2_wrong(self):
            with pytest.raises(ValueError) as exc:
                ld.distance(self.lines[0][0], [5])
            assert exc.value.message == "Wrong format on line, line must be [rho, theta]."


    # Tests of distance_mean

        def test_distance_mean_good(self):
            result = ld.distance_mean(self.lines)
            assert isinstance(result[0], int) and isinstance(result[1], int)

        def test_distance_mean_single_line(self):
            with pytest.raises(ValueError) as exc:
                ld.distance_mean(self.lines[0][0])
            assert exc.value.message == "Lines must contain at least two lines to proceed."

        def test_distance_mean_lines_none(self):
            with pytest.raises(ValueError) as exc:
                ld.distance_mean(None)
            assert exc.value.message == "Lines can't be None."


    # Tests of draw_lines

        def test_draw_lines_good(self):
            assert isinstance(ld.draw_lines(self.test_image, self.lines), np.ndarray)

        def test_draw_lines_good_single_line(self):
            assert isinstance(ld.draw_lines(self.test_image, self.lines[0][0]), np.ndarray)

        def test_draw_lines_file_void(self):
            with pytest.raises(ValueError) as exc:
                ld.draw_lines('', self.lines)
            assert exc.value.message == "Input_file must be different than '' or None."

        def test_draw_lines_file_none(self):
            with pytest.raises(ValueError) as exc:
                ld.draw_lines(None, self.lines)
            assert exc.value.message == "Input_file must be different than '' or None."

        def test_draw_lines_width_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.draw_lines(self.test_image, self.lines[0][0], width=-10)
            assert exc.value.message == "Width value must be greater than 0."

        def test_draw_lines_colour_wrong_b(self):
            with pytest.raises(ValueError) as exc:
                ld.draw_lines(self.test_image, self.lines[0][0], color=(260, 0, 0))
            assert exc.value.message == "Color value must be: (0-255, 0-255, 0-255)."

    # Tests of line_count

        def test_line_count_single_line(self):
            line = self.lines[0][0]
            result = ld.line_count(line)
            assert result[0] == 1 and result[1] >= 0 and \
                   result[2] >= 0 and result[0] == result[1] + result[2]

        def test_line_count_good(self):
            result = ld.line_count(self.lines)
            assert len(result) == 3 and result[0] >= 0 and result[1] >= 0 and \
                   result[2] >= 0 and result[0] == result[1] + result[2]

        def test_line_count_lines_none(self):
            with pytest.raises(ValueError) as exc:
                ld.line_count(None)
            assert exc.value.message == "Lines can't be None."

        def test_line_count_error_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.line_count(self.lines, error=-10)
            assert exc.value.message == "Error value must be positive " \
                                        "(0 included)."


    # Tests of parallels

        def test_parallels_good(self):
            assert isinstance(ld.parallels(self.lines[0][0], self.lines[0][1]), bool)

        def test_parallels_line1_none(self):
            with pytest.raises(ValueError) as exc:
                ld.parallels(None, self.lines[0][1])
            assert exc.value.message == "Line must be a line, is None."

        def test_parallels_line2_none(self):
            with pytest.raises(ValueError) as exc:
                ld.parallels(self.lines[0][0], None)
            assert exc.value.message == "Line must be a line, is None."

        def test_parallels_line1_wrong(self):
            line1 = [252]
            line2 = [0, 0]
            with pytest.raises(ValueError) as exc:
                ld.parallels(line1, line2)
            assert exc.value.message == "Wrong format on line, line must be " \
                                        "[rho, theta]."

        def test_parallels_line2_wrong(self):
            line1 = [0, 0]
            line2 = [252]
            with pytest.raises(ValueError) as exc:
                ld.parallels(line1, line2)
            assert exc.value.message == "Wrong format on line, line must be " \
                                        "[rho, theta]."

        def test_parallels_error_negative(self):
            with pytest.raises(ValueError) as exc:
                ld.parallels(self.lines[0][0], self.lines[0][1], error=-5)
            assert exc.value.message == "Error value must be positive " \
                                        "(0 included)."
