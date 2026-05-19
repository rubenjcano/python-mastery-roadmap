def flatten_nested(nested: list[list[Any]]) -> list[Any]:
    """Flatten one level of nesting.
    
    Example: flatten_nested([[1, 2], [3, 4], [5]]) → [1, 2, 3, 4, 5]
    Hint: list comprehension with inner loop
    """
    flatten_nested = []
    for i in nested:
        for j in i:
            flatten_nested.append(j)
    return flatten_nested

nested = [[1, 2], [3, 4], [5]]
print(flatten_nested(nested))

    