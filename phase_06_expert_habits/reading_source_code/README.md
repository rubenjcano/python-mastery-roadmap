# Reading Source Code

The fastest way to level up is to read how the best libraries are built.

## Recommended reading list (in order)

| Library | Why | Link |
|---|---|---|
| `requests` | Simple, clean Python — great starting point | github.com/psf/requests |
| `FastAPI` | Modern Python patterns: Pydantic, dependency injection | github.com/fastapi/fastapi |
| `Pydantic v2` | Deep Python data model usage | github.com/pydantic/pydantic |
| `Click / Typer` | Decorator-based CLI design patterns | github.com/tiangolo/typer |
| `Rich` | Console rendering, advanced OOP | github.com/Textualize/rich |
| `httpx` | Async HTTP, clean API design | github.com/encode/httpx |
| `CPython` | The language itself | github.com/python/cpython |

## How to read source code

1. **Start with the entry point** — find `__init__.py`, look at what's exported
2. **Read the tests** — tests are documentation. Start with `test_*.py`
3. **Follow the main path** — trace one key function from API to implementation
4. **Look for patterns** — decorators, context managers, descriptors
5. **Check the changelog** — see what changed and why

## Exercise
Pick `requests` and answer:
- How does `Session` manage headers?
- What happens when you call `requests.get()`?
- How does redirect handling work?
