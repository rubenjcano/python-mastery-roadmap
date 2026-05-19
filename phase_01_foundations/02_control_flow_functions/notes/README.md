# Control Flow & Functions

## Comprehensions
```python
squares  = [x**2 for x in range(10) if x % 2 == 0]
lengths  = {word: len(word) for word in ["hello", "world"]}
unique   = {len(w) for w in ["hi", "hello", "hey"]}
lazy_sum = sum(x**2 for x in range(1_000_000))  # generator — no list in memory
```

## Generators
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

from itertools import islice
first_10 = list(islice(fibonacci(), 10))
```

## *args / **kwargs
```python
def flexible(*args: int, sep: str = ", ", **kwargs: str) -> str:
    nums   = sep.join(str(a) for a in args)
    extras = ", ".join(f"{k}={v}" for k, v in kwargs.items())
    return f"{nums} | {extras}"

flexible(1, 2, 3, sep=" + ", unit="kg")
```

## Decorators
```python
import functools, time

def timer(func):
    @functools.wraps(func)    # preserves __name__ and __doc__
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {time.perf_counter()-t0:.4f}s")
        return result
    return wrapper

@timer
def slow(n: int) -> int:
    return sum(range(n))
```

## functools must-knows
```python
from functools import lru_cache, partial, reduce

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    return n if n < 2 else fib(n-1) + fib(n-2)

double = partial(lambda x, y: x * y, 2)
print(double(5))   # 10
```

## itertools gems
```python
from itertools import chain, groupby, combinations, product

flat   = list(chain.from_iterable([[1,2],[3,4]]))  # [1,2,3,4]
pairs  = list(combinations([1,2,3], 2))            # [(1,2),(1,3),(2,3)]
grid   = list(product([0,1], repeat=3))            # all 3-bit combos
```
