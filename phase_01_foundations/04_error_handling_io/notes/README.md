# Error Handling & I/O

## Exception Hierarchy
```
BaseException
 ├── SystemExit
 ├── KeyboardInterrupt
 └── Exception
      ├── ValueError, TypeError, AttributeError
      ├── OSError (IOError, FileNotFoundError)
      ├── RuntimeError
      └── ... (create your own by subclassing Exception)
```

## Custom Exceptions
```python
class DataValidationError(ValueError):
    def __init__(self, field: str, message: str) -> None:
        self.field = field
        super().__init__(f"Validation error on '{field}': {message}")

try:
    raise DataValidationError("age", "must be positive")
except DataValidationError as e:
    print(f"Field: {e.field}")   # Field: age
```

## Context Managers
```python
# Using contextlib
from contextlib import contextmanager

@contextmanager
def timer(label: str):
    import time
    t0 = time.perf_counter()
    try:
        yield
    finally:
        print(f"{label}: {time.perf_counter()-t0:.4f}s")

with timer("my operation"):
    sum(range(1_000_000))
```

## pathlib — always use over os.path
```python
from pathlib import Path

base = Path("data")
csv_file = base / "sales" / "2024.csv"

csv_file.parent.mkdir(parents=True, exist_ok=True)

# Read / write
text = csv_file.read_text(encoding="utf-8")
csv_file.write_text("col1,col2\n1,2", encoding="utf-8")

# Iteration
for f in base.rglob("*.csv"):
    print(f.stem, f.suffix)
```

## Logging (never use print in production)
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
)
logger = logging.getLogger(__name__)

logger.debug("debug info (not shown at INFO level)")
logger.info("pipeline started")
logger.warning("missing column, using default")
logger.error("failed to connect", exc_info=True)
```
