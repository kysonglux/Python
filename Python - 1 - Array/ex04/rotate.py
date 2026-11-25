import numpy as np

from load_image import ft_load


def crop_square(array: np.ndarray, size: int = 400) -> np.ndarray:
    """Return a centered single-channel square crop."""
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("expected an RGB image array")
    if size <= 0 or size > min(array.shape[:2]):
        raise ValueError("crop size must fit within the image")

    start_y = (array.shape[0] - size) // 2
    start_x = (array.shape[1] - size) // 2
    return array[start_y:start_y + size, start_x:start_x + size, 0:1]


def manual_transpose(array: np.ndarray) -> np.ndarray:
    """Transpose a 2D array without using a library transpose operation."""
    if array.ndim == 3 and array.shape[2] == 1:
        array = array[:, :, 0]
    if array.ndim != 2:
        raise ValueError("expected a 2D array")

    result = np.empty((array.shape[1], array.shape[0]), dtype=array.dtype)
    for row in range(array.shape[0]):
        for column in range(array.shape[1]):
            result[column, row] = array[row, column]
    return result


def display_image(array: np.ndarray) -> None:
    """Display an image using the first available image viewer."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        from PIL import Image

        Image.fromarray(array).show()
        return

    plt.imshow(array, cmap="gray")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def main() -> None:
    try:
        image = ft_load("animal.jpeg")
        cropped = crop_square(image)
        print(f"New shape after slicing: {cropped.shape}")
        print(cropped)
        transposed = manual_transpose(cropped)
        print(f"New shape after Transpose: {transposed.shape}")
        print(transposed)
        display_image(transposed)
    except (FileNotFoundError, ValueError, OSError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
