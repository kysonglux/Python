import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Print an array's shapes and return the requested row slice."""
    if not isinstance(family, list) or not family:
        raise ValueError("family must be a non-empty 2D list")
    if not all(isinstance(row, list) for row in family):
        raise TypeError("family must be a 2D list")
    if not all(len(row) == len(family[0]) for row in family):
        raise ValueError("family must be rectangular")
    if not all(isinstance(value, (int, float)) and not isinstance(value, bool)
               for row in family for value in row):
        raise TypeError("family must contain only integers or floats")
    if not isinstance(start, int) or isinstance(start, bool):
        raise TypeError("start must be an integer")
    if not isinstance(end, int) or isinstance(end, bool):
        raise TypeError("end must be an integer")

    array = np.array(family)
    print(f"My shape is : {array.shape}")
    result = array[start:end].tolist()
    print(f"My new shape is : {np.array(result).shape}")
    return result
