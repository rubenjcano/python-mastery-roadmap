# Memory & Performance

## Profile before optimising — always
```bash
# CPU profiling
python -m cProfile -s cumulative my_script.py

# Line-level profiling (pip install line_profiler)
kernprof -l -v my_script.py

# Memory profiling (pip install memray)
memray run my_script.py
memray flamegraph memray-my_script.bin

# Scalene — combined CPU + memory (recommended)
pip install scalene
scalene my_script.py
```

## __slots__ — eliminate per-instance __dict__
```python
# Normal class: each instance stores a __dict__ (~200 bytes overhead)
class Point:
    def __init__(self, x, y): self.x, self.y = x, y

# With __slots__: ~60 bytes overhead, also faster attribute access
class PointSlots:
    __slots__ = ("x", "y")
    def __init__(self, x, y): self.x, self.y = x, y

import sys
p1 = Point(1, 2)
p2 = PointSlots(1, 2)
print(sys.getsizeof(p1))   # ~48 + dict overhead
print(sys.getsizeof(p2))   # ~56 (no dict)
```

## Numba JIT — speed up numerical code
```python
from numba import jit
import numpy as np

@jit(nopython=True)
def monte_carlo_pi(n: int) -> float:
    inside = 0
    for _ in range(n):
        x, y = np.random.random(), np.random.random()
        if x*x + y*y <= 1.0:
            inside += 1
    return 4 * inside / n

# First call compiles; subsequent calls are near-C speed
result = monte_carlo_pi(10_000_000)
```

## Generator vs list — memory
```python
import sys

lst = [x**2 for x in range(100_000)]    # allocates all at once
gen = (x**2 for x in range(100_000))    # lazy

print(sys.getsizeof(lst))   # ~800 KB
print(sys.getsizeof(gen))   # ~128 bytes
```

## tracemalloc — find memory leaks
```python
import tracemalloc

tracemalloc.start()
# ... run your code ...
snapshot = tracemalloc.take_snapshot()
top = snapshot.statistics("lineno")
for stat in top[:3]:
    print(stat)
```
