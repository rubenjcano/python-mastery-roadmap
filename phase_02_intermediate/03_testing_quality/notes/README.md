# Testing & Code Quality

## pytest fundamentals
```python
# test_calculator.py
import pytest
from calculator import add, divide

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add_parametrized(a, b, expected):
    assert add(a, b) == expected
```

## Fixtures
```python
import pytest
from pathlib import Path

@pytest.fixture
def sample_data() -> list[dict]:
    return [{"name": "Alice", "score": 90}, {"name": "Bob", "score": 75}]

@pytest.fixture
def tmp_csv(tmp_path: Path) -> Path:
    csv = tmp_path / "test.csv"
    csv.write_text("name,score\nAlice,90\nBob,75")
    return csv

def test_process(sample_data, tmp_csv):
    # both fixtures injected automatically
    assert len(sample_data) == 2
    assert tmp_csv.exists()
```

## Mocking
```python
from unittest.mock import patch, MagicMock

def test_api_call():
    with patch("mymodule.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"status": "ok"}
        result = call_api("https://example.com")
        assert result == {"status": "ok"}
        mock_get.assert_called_once()
```

## ruff — fast linter (replaces flake8 + isort + many more)
```bash
ruff check .          # lint
ruff check . --fix    # auto-fix
ruff format .         # format (like black)
```

## mypy — static type checking
```bash
mypy src/ --strict
```

## Run everything
```bash
pytest --cov=src --cov-report=html   # tests + coverage
ruff check . && mypy src/            # quality gates
```
