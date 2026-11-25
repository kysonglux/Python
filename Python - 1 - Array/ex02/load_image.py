from pathlib import Path

import numpy as np
from PIL import Image, UnidentifiedImageError


def ft_load(path: str) -> np.ndarray:
    """Load a JPG or JPEG image as an RGB NumPy array."""
    image_path = Path(path)
    if image_path.suffix.lower() not in {".jpg", ".jpeg"}:
        raise ValueError("unsupported image format; expected JPG or JPEG")

    try:
        with Image.open(image_path) as image:
            array = np.array(image.convert("RGB"))
    except FileNotFoundError as error:
        raise FileNotFoundError(f"image not found: {path}") from error
    except (UnidentifiedImageError, OSError) as error:
        raise ValueError(f"could not load image: {path}") from error

    print(f"The shape of image is: {array.shape}")
    print(array)
    return array
