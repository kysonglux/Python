import numpy as np


def _validate_image(array: np.ndarray) -> None:
    if not isinstance(array, np.ndarray):
        raise TypeError("array must be a NumPy array")
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("array must be an RGB image")


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    _validate_image(array)
    return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keep the red channel and remove the other channels."""
    _validate_image(array)
    result = np.zeros_like(array)
    result[:, :, 0] = array[:, :, 0]
    return result


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keep the green channel and remove the other channels."""
    _validate_image(array)
    result = np.zeros_like(array)
    result[:, :, 1] = array[:, :, 1]
    return result


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keep the blue channel and remove the other channels."""
    _validate_image(array)
    result = np.zeros_like(array)
    result[:, :, 2] = array[:, :, 2]
    return result


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Convert the image to grayscale while preserving its shape."""
    _validate_image(array)
    grey = np.mean(array, axis=2, keepdims=True).astype(array.dtype)
    return np.repeat(grey, 3, axis=2)
