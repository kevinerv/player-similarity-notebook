from pathlib import Path

import pandas as pd


def load_dataset(path: Path) -> pd.DataFrame:
    """
    Load a player dataset from a CSV file.

    Parameters
    ----------
    path : Path
        Path to the CSV dataset.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.

    Raises
    ------
    FileNotFoundError
        If the dataset file does not exist.
    """
    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path}"
        )

    df = pd.read_csv(path)

    return df