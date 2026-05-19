# Code Review Checklist

## Correctness
- [ ] Does the code do what it says it does?
- [ ] Are edge cases handled (empty input, None, 0, large values)?
- [ ] Are exceptions caught at the right level?
- [ ] Is error propagation appropriate?

## Pythonic Style
- [ ] Uses list/dict comprehensions where appropriate
- [ ] No unnecessary intermediate variables
- [ ] Type hints present and accurate
- [ ] Docstrings on public functions/classes

## Performance
- [ ] No N+1 query patterns
- [ ] Generator used instead of list where data could be large
- [ ] Caching used where appropriate (lru_cache, Redis)
- [ ] No blocking I/O in async context

## Testing
- [ ] New code has tests
- [ ] Tests cover happy path + edge cases
- [ ] Tests are fast and deterministic
- [ ] Mocks used correctly

## Security
- [ ] No hardcoded secrets
- [ ] Input validation on external data
- [ ] SQL queries use parameterised statements (no f-string SQL!)
- [ ] Dependencies are pinned

## Common things to flag
```python
# ❌ Mutable default arg
def f(items=[]):

# ❌ Bare except
try: ...
except: ...

# ❌ F-string SQL injection
cursor.execute(f"SELECT * FROM {table}")  # NEVER

# ❌ Catching and swallowing exceptions silently
try: do_thing()
except Exception: pass

# ✅ Explicit exception types
# ✅ Logging errors before re-raising
# ✅ Using `with` for resource management
```
