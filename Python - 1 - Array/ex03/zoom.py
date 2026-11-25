from pathlib import Path

import numpy as np

from load_image import ft_load


def zoom_image(array: np.ndarray, size: int = 400) -> np.ndarray:
    """Return a centered square crop of the image."""
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("expected an RGB image array")
    if size <= 0 or size > min(array.shape[:2]):
        raise ValueError("zoom size must fit within the image")

    start_y = (array.shape[0] - size) // 2
    start_x = (array.shape[1] - size) // 2
    return array[start_y:start_y + size, start_x:start_x + size, 0:1]


def display_image(array: np.ndarray) -> None:
    """Display an image with axes, using the first available image viewer."""
    try:
        import matplotlib.pyplot as plt
    except ImportError:
        from PIL import Image

        Image.fromarray(array.squeeze()).show()
        return

    plt.imshow(array.squeeze(), cmap="gray" if array.shape[2] == 1 else None)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


def main() -> None:
    image_path = Path("animal.jpeg")
    try:
        image = ft_load(str(image_path))
        zoomed = zoom_image(image)
        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)
        display_image(zoomed)
    except (FileNotFoundError, ValueError, OSError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
