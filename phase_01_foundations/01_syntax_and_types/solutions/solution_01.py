"""
Solution 01 — Syntax & Data Types
"""
from typing import Any


def format_product(name: str, price: float, discount: float) -> str:
    discounted = price * (1 - discount)
    pct = discount * 100
    return f"{name}: €{price:.2f} → €{discounted:.2f} ({pct:.1f}% off)"


def invert_dict(d: dict[str, int]) -> dict[int, str]:
    return {v: k for k, v in d.items()}


def flatten_nested(nested: list[list[Any]]) -> list[Any]:
    return [item for sublist in nested for item in sublist]


def first_and_last(items: list[Any]) -> tuple[Any, Any]:
    first, *_, last = items
    return first, last


def safe_divide(a: float, b: float) -> float | None:
    if b == 0:
        return None
    return a / b


def add_tag(tags: list[str] | None, new_tag: str) -> list[str]:
    if tags is None:
        tags = []
    tags.append(new_tag)
    return tags
