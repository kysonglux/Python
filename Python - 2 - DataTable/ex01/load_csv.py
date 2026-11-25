from pathlib import Path

import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Load a CSV dataset, print its dimensions, and return it."""
    try:
        dataset = pd.read_csv(Path(path))
    except (OSError, TypeError, ValueError, pd.errors.ParserError):
        return None
    print(f"Loading dataset of dimensions {dataset.shape}")
    return dataset
