"""
Exercise 01 — Control Flow & Functions
=======================================
"""
from typing import Generator, Iterator


# ── 1. Comprehensions ──────────────────────────────────────────────────────
def word_frequency(text: str) -> dict[str, int]:
    """Count frequency of each word (lowercased, stripped of punctuation).
    
    Example: word_frequency("Hello world hello")
    → {"hello": 2, "world": 1}
    
    Hint: str.split(), str.lower(), str.strip(".,!?")
    Use a dict comprehension or Counter.
    """
    # TODO
    ...


def pythagorean_triples(limit: int) -> list[tuple[int, int, int]]:
    """Return all Pythagorean triples (a, b, c) where a < b < c <= limit.
    
    Hint: nested list comprehension + condition a**2 + b**2 == c**2
    """
    # TODO — one-liner list comprehension
    ...


# ── 2. Generators ─────────────────────────────────────────────────────────
def running_average(numbers: list[float]) -> Generator[float, None, None]:
    """Yield the running average after each number.
    
    Example: list(running_average([1, 2, 3, 4]))
    → [1.0, 1.5, 2.0, 2.5]
    """
    # TODO: use yield
    ...


def chunked(iterable: list, size: int) -> Generator[list, None, None]:
    """Yield successive chunks of `size` from iterable.
    
    Example: list(chunked([1,2,3,4,5], 2))
    → [[1,2], [3,4], [5]]
    """
    # TODO
    ...


# ── 3. Decorators ─────────────────────────────────────────────────────────
import functools

def retry(times: int = 3):
    """Decorator factory: retry a function up to `times` on any exception.
    
    Usage:
        @retry(times=3)
        def unstable_function(): ...
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: implement retry logic
            # Raise the last exception if all retries exhausted
            ...
        return wrapper
    return decorator


# ─── Tests ────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print(word_frequency("Hello world hello world hello"))
    # → {"hello": 3, "world": 2}

    print(pythagorean_triples(20))
    # → [(3,4,5), (5,12,13), (6,8,10), (8,15,17), (9,12,15), (12,16,20)]

    print(list(running_average([1, 2, 3, 4])))
    # → [1.0, 1.5, 2.0, 2.5]

    print(list(chunked(list(range(7)), 3)))
    # → [[0,1,2],[3,4,5],[6]]

    attempt = 0
    @retry(times=3)
    def flaky():
        global attempt
        attempt += 1
        if attempt < 3:
            raise ValueError("not yet")
        return "success"

    print(flaky())  # → "success" after 3 attempts
