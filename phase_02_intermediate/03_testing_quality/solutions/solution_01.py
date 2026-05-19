"""
Solution 01 — Testing & Quality
"""
import pytest
from exercises.exercise_01 import parse_age, classify_bmi, merge_sorted


class TestParseAge:
    def test_valid_age(self):
        assert parse_age("28") == 28

    def test_boundary_zero(self):
        assert parse_age("0") == 0

    def test_boundary_150(self):
        assert parse_age("150") == 150

    def test_non_numeric_raises(self):
        with pytest.raises(ValueError, match="Cannot parse"):
            parse_age("abc")

    def test_negative_raises(self):
        with pytest.raises(ValueError, match="out of valid range"):
            parse_age("-1")

    def test_over_150_raises(self):
        with pytest.raises(ValueError, match="out of valid range"):
            parse_age("151")

    @pytest.mark.parametrize("value,expected", [
        ("0", 0), ("1", 1), ("99", 99), ("150", 150),
    ])
    def test_parametrized(self, value, expected):
        assert parse_age(value) == expected


class TestClassifyBMI:
    @pytest.mark.parametrize("weight,height,expected", [
        (50, 1.75, "Underweight"),   # BMI ~16.3
        (70, 1.75, "Normal"),        # BMI ~22.9
        (85, 1.75, "Overweight"),    # BMI ~27.8
        (100, 1.75, "Obese"),        # BMI ~32.7
    ])
    def test_categories(self, weight, height, expected):
        assert classify_bmi(weight, height) == expected

    def test_exact_boundary_normal(self):
        # BMI exactly 18.5 → Normal
        weight = 18.5 * (1.0 ** 2)
        assert classify_bmi(weight, 1.0) == "Normal"

    def test_invalid_height(self):
        with pytest.raises(ValueError):
            classify_bmi(70, 0)
        with pytest.raises(ValueError):
            classify_bmi(70, -1)


class TestMergeSorted:
    def test_both_empty(self):
        assert merge_sorted([], []) == []

    def test_first_empty(self):
        assert merge_sorted([], [1, 2, 3]) == [1, 2, 3]

    def test_second_empty(self):
        assert merge_sorted([1, 2], []) == [1, 2]

    @pytest.mark.parametrize("a,b,expected", [
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 1, 2], [1, 3], [1, 1, 1, 2, 3]),
        ([5], [1, 2, 3], [1, 2, 3, 5]),
    ])
    def test_merge(self, a, b, expected):
        assert merge_sorted(a, b) == expected
