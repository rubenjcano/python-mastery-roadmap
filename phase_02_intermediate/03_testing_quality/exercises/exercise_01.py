"""
Exercise 01 — Testing & Quality
================================
Write tests for the functions below using pytest.
Run: pytest exercises/exercise_01.py -v

GOAL: achieve 100% branch coverage on all functions below.
"""


# ── Functions to test ─────────────────────────────────────────────────────

def parse_age(value: str) -> int:
    """Parse age from string. Raises ValueError if invalid or out of range."""
    try:
        age = int(value)
    except (ValueError, TypeError):
        raise ValueError(f"Cannot parse age from: {value!r}")
    if not (0 <= age <= 150):
        raise ValueError(f"Age {age} out of valid range 0-150")
    return age


def classify_bmi(weight_kg: float, height_m: float) -> str:
    """Classify BMI. Returns: Underweight / Normal / Overweight / Obese"""
    if height_m <= 0:
        raise ValueError("Height must be positive")
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list."""
    result, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    return result + a[i:] + b[j:]


# ── Write your tests below ─────────────────────────────────────────────────
import pytest

class TestParseAge:
    # TODO: test valid inputs
    # TODO: test non-numeric string raises ValueError
    # TODO: test negative age raises ValueError
    # TODO: test age > 150 raises ValueError
    # TODO: test boundary values (0, 150)
    pass


class TestClassifyBMI:
    # TODO: test each category
    # TODO: test boundary values (exactly 18.5, 25.0, 30.0)
    # TODO: test invalid height
    pass


class TestMergeSorted:
    # TODO: test both empty
    # TODO: test one empty
    # TODO: test equal elements
    # TODO: parametrize multiple cases
    pass
