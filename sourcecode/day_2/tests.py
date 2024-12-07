import pytest

from sourcecode.day_2.solution import _check_report_data_consistency

test_data = {
    'happy_path': [[7, 6, 4, 2, 1], [1, 3, 6, 7, 9]],
    'negative_path': [[9, 7, 6, 2, 1], [1, 3, 2, 4, 5]]
}


class TestCalculateTotalDistance:
    @pytest.mark.parametrize("report_data", test_data['happy_path'])
    def test_get_safety_flag_for_happy_path(self, report_data):
        assert _check_report_data_consistency(report_data) is True

    @pytest.mark.parametrize("report_data", test_data['negative_path'])
    def test_get_safety_flag_for_negative_path(self, report_data):
        assert _check_report_data_consistency(report_data) is False
