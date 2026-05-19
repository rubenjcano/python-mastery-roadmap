"""
Solution 01 — Control Flow & Functions
"""
from typing import Generator
import functools
import string


def word_frequency(text: str) -> dict[str, int]:
    words = [w.strip(string.punctuation).lower() for w in text.split() if w.strip(string.punctuation)]
    return {w: words.count(w) for w in set(words)}


def pythagorean_triples(limit: int) -> list[tuple[int, int, int]]:
    return [
        (a, b, c)
        for a in range(1, limit+1)
        for b in range(a+1, limit+1)
        for c in range(b+1, limit+1)
        if a**2 + b**2 == c**2
    ]


def running_average(numbers: list[float]) -> Generator[float, None, None]:
    total = 0.0
    for i, n in enumerate(numbers, 1):
        total += n
        yield total / i


def chunked(iterable: list, size: int) -> Generator[list, None, None]:
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]


def retry(times: int = 3):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exc: Exception | None = None
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    print(f"Attempt {attempt}/{times} failed: {e}")
            raise last_exc  # type: ignore
        return wrapper
    return decorator
