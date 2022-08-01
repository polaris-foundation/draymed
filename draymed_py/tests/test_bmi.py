import pytest

import draymed


class TestBmi:
    def assert_correct_decimals(self, value: float) -> None:
        string_value = str(value)
        if "." in string_value:
            decimals = string_value.split(".")[1]
        else:
            decimals = ""
        assert len(decimals) <= draymed.BMI_DECIMAL_PLACES

    def test_zero_division_height(self) -> None:
        height = 0
        weight = 63500
        with pytest.raises(ValueError):
            draymed.bmi(height, weight)

    def test_zero_division_weight(self) -> None:
        height = 1800
        weight = 0
        with pytest.raises(ValueError):
            draymed.bmi(height, weight)

    def test_calculation(self) -> None:
        height = 1800
        weight = 63500

        calculated_bmi = draymed.bmi(height, weight)
        expected_bmi = 19.60

        assert calculated_bmi == expected_bmi

    def test_rounding(self) -> None:
        height = 1800
        weight = 63500

        calculated_bmi = draymed.bmi(height, weight)
        self.assert_correct_decimals(calculated_bmi)
