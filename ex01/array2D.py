def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family, list):
        raise TypeError("family must be a list")
    if len(family) == 0:
        return []
    if not all(isinstance(item, list) for item in family):
        raise TypeError("All elements must be lists")
    first_size = len(family[0])
    if not all(len(item) == first_size for item in family):
        raise ValueError("All sublists must have the same size")

    rows = len(family)
    columns = len(family[0])
    print(f"My shape is : ({rows}, {columns})")

    sliced = family[start:end]
    new_rows = len(sliced)
    new_columns = len(sliced[0]) if new_rows > 0 else 0
    print(f"My new shape is : ({new_rows}, {new_columns})")

    return sliced
