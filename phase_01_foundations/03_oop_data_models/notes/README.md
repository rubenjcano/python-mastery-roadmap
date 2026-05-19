# OOP & Data Models

## dataclasses — the modern way
```python
from dataclasses import dataclass, field

@dataclass(order=True, frozen=True)
class Point:
    x: float
    y: float
    label: str = field(default="", compare=False)

    def distance_to(self, other: "Point") -> float:
        return ((self.x-other.x)**2 + (self.y-other.y)**2) ** 0.5
```

## Pydantic — validated data (industry standard)
```python
from pydantic import BaseModel, field_validator

class User(BaseModel):
    name: str
    age: int
    email: str

    @field_validator("age")
    @classmethod
    def must_be_positive(cls, v: int) -> int:
        if v < 0:
            raise ValueError("Age must be positive")
        return v

user = User(name="Ruben", age=28, email="ruben@example.com")
user_dict = user.model_dump()
user_json = user.model_dump_json()
```

## Dunder methods (Python data model)
```python
class Vector:
    def __init__(self, x: float, y: float) -> None:
        self.x, self.y = x, y

    def __repr__(self) -> str:          # for developers
        return f"Vector({self.x}, {self.y})"
    def __str__(self) -> str:           # for end users
        return f"({self.x}, {self.y})"
    def __add__(self, other: "Vector") -> "Vector":
        return Vector(self.x+other.x, self.y+other.y)
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector): return NotImplemented
        return self.x == other.x and self.y == other.y
    def __hash__(self) -> int:
        return hash((self.x, self.y))
```

## Abstract Base Classes
```python
from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def read(self) -> list[dict]: ...
    @abstractmethod
    def write(self, data: list[dict]) -> None: ...

class CSVSource(DataSource):
    def __init__(self, path: str) -> None: self.path = path
    def read(self) -> list[dict]: return []       # implement
    def write(self, data: list[dict]) -> None: pass
```

## Properties
```python
class Temperature:
    def __init__(self, celsius: float) -> None:
        self._celsius = celsius

    @property
    def celsius(self) -> float: return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        if value < -273.15: raise ValueError("Below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32
```
