# Metaprogramming

## Decorators as classes
```python
import functools

class cached_property:
    """Descriptor that caches the result of a method."""
    def __init__(self, func):
        self.func = func
        self.attrname = None
        functools.update_wrapper(self, func)

    def __set_name__(self, owner, name):
        self.attrname = name

    def __get__(self, obj, objtype=None):
        if obj is None: return self
        val = self.func(obj)
        obj.__dict__[self.attrname] = val   # cache in instance
        return val

class Circle:
    def __init__(self, radius: float): self.radius = radius

    @cached_property
    def area(self) -> float:
        import math; return math.pi * self.radius ** 2
```

## Metaclasses
```python
class SingletonMeta(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Config(metaclass=SingletonMeta):
    def __init__(self): self.debug = False

a = Config()
b = Config()
assert a is b   # True — same instance
```

## __init_subclass__ (cleaner than metaclasses for many cases)
```python
class Plugin:
    _registry: dict[str, type] = {}

    def __init_subclass__(cls, name: str, **kwargs):
        super().__init_subclass__(**kwargs)
        Plugin._registry[name] = cls

class CSVPlugin(Plugin, name="csv"): pass
class JSONPlugin(Plugin, name="json"): pass

print(Plugin._registry)  # {"csv": CSVPlugin, "json": JSONPlugin}
```

## inspect module
```python
import inspect

def get_function_info(func) -> dict:
    sig = inspect.signature(func)
    return {
        "params": list(sig.parameters.keys()),
        "source_lines": len(inspect.getsource(func).splitlines()),
        "is_coroutine": inspect.iscoroutinefunction(func),
    }
```
