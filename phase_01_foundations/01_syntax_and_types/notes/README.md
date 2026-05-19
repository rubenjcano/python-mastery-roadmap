# Syntax & Data Types

## Core Built-in Types

| Type | Example | Mutable |
|------|---------|---------|
| `int` | `42` | No |
| `float` | `3.14` | No |
| `str` | `"hello"` | No |
| `bool` | `True` | No |
| `list` | `[1, 2, 3]` | ✅ Yes |
| `tuple` | `(1, 2, 3)` | No |
| `dict` | `{"k": "v"}` | ✅ Yes |
| `set` | `{1, 2, 3}` | ✅ Yes |

## f-strings (always prefer)
```python
name = "Ruben"
score = 9.87654
print(f"Hello {name}, score: {score:.2f}")   # 2 decimal places
print(f"{2**10 = }")                           # debug: 2**10 = 1024
```

## Type hints (use everywhere)
```python
def greet(name: str, times: int = 1) -> str:
    return (f"Hello {name}! " * times).strip()
```

## Unpacking
```python
a, b, *rest = [1, 2, 3, 4, 5]    # a=1, b=2, rest=[3,4,5]
x, y = y, x                        # swap in one line
first, *_, last = range(10)        # first=0, last=9
```

## Dict tricks
```python
d1 = {"a": 1}; d2 = {"b": 2}
merged = {**d1, **d2}              # merge
value  = d1.get("missing", 0)     # safe access
```

## ⚠️ Common Pitfall: Mutable Default Arguments
```python
# BAD — the list is shared across ALL calls
def bad(items=[]):
    items.append(1)
    return items

# GOOD
def good(items=None):
    if items is None:
        items = []
    items.append(1)
    return items
```
