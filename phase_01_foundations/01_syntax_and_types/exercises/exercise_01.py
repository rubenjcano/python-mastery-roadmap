"""
Exercise 01 — Syntax & Data Types
==================================
Complete all the TODOs below. Run with: python exercise_01.py
"""
from typing import Any


# ── 1. f-strings ───────────────────────────────────────────────────────────
def format_product(name: str, price: float, discount: float) -> str:
    """Return '<name>: €<original> → €<discounted> (X% off)'
    
    Example: format_product("Laptop", 1200.0, 0.15)
    → "Laptop: €1200.00 → €1020.00 (15.0% off)"
    
    Hint: use f-string with :.2f for prices and :.1f% for percentage
    """
    # TODO: implement this
    ...


# ── 2. List / dict manipulation ────────────────────────────────────────────
def invert_dict(d: dict[str, int]) -> dict[int, str]:
    """Swap keys and values.
    
    Example: invert_dict({"a": 1, "b": 2}) → {1: "a", 2: "b"}
    Hint: dict comprehension
    """
    # TODO: implement this
    ...


def flatten_nested(nested: list[list[Any]]) -> list[Any]:
    """Flatten one level of nesting.
    
    Example: flatten_nested([[1, 2], [3, 4], [5]]) → [1, 2, 3, 4, 5]
    Hint: list comprehension with inner loop
    """
    # TODO: implement this
    ...


# ── 3. Unpacking ───────────────────────────────────────────────────────────
def first_and_last(items: list[Any]) -> tuple[Any, Any]:
    """Return (first, last) element using extended unpacking.
    
    Example: first_and_last([1, 2, 3, 4, 5]) → (1, 5)
    Hint: first, *_, last = ...
    """
    # TODO: implement using extended unpacking (one line)
    ...


# ── 4. Type conversion & guards ────────────────────────────────────────────
def safe_divide(a: float, b: float) -> float | None:
    """Divide a by b. Return None instead of raising ZeroDivisionError.
    
    Example: safe_divide(10, 2) → 5.0
             safe_divide(10, 0) → None
    """
    # TODO: implement this
    ...


# ── 5. Mutable default pitfall ─────────────────────────────────────────────
def add_tag(tags: list[str] | None, new_tag: str) -> list[str]:
    """Add new_tag to tags list. If tags is None, create a new list.
    
    This function must NOT share state between calls.
    """
    # TODO: implement correctly (avoid mutable default arg bug)
    ...


# ─── Tests ──────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Testing format_product ===")
    result = format_product("Laptop", 1200.0, 0.15)
    print(result)
    assert result == "Laptop: €1200.00 → €1020.00 (15.0% off)", f"Got: {result}"

    print("\n=== Testing invert_dict ===")
    assert invert_dict({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    print("OK")

    print("\n=== Testing flatten_nested ===")
    assert flatten_nested([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    print("OK")

    print("\n=== Testing first_and_last ===")
    assert first_and_last([1, 2, 3, 4, 5]) == (1, 5)
    print("OK")

    print("\n=== Testing safe_divide ===")
    assert safe_divide(10, 2) == 5.0
    assert safe_divide(10, 0) is None
    print("OK")

    print("\n=== Testing add_tag ===")
    r1 = add_tag(None, "python")
    r2 = add_tag(None, "data")
    assert r1 == ["python"], f"Got: {r1}"
    assert r2 == ["data"], f"Got: {r2}"   # must not contain "python"
    print("OK")

    print("\n✅ All tests passed!")
