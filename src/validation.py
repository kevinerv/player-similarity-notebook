REQUIRED_COLUMNS = [
    "Player",
    "Nation",
    "Pos",
    "Squad",
    "Age",
    "MP",
    "Starts",
    "Min",
    "90s",
]

SIMILARITY_FEATURES = [
    "Gls",
    "Ast",
    "xG",
    "xAG",
    "PrgC",
    "PrgP",
    "PrgR",
]


import pandas as pd

def validate_dataset(df: pd.DataFrame) -> None:
    """
    Validate that the dataset contains the required columns
    for the player similarity analysis.

    Parameters
    ----------
    df : pd.DataFrame
        Dataset to validate.

    Raises
    ------
    ValueError
        If the dataset is empty or required columns are missing.
    """
    if df.empty:
        raise ValueError("Dataset is empty.")

    missing_columns = [
        column
        for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    print("✓ Dataset validation successful.")
    print(f"Players: {len(df)}")
    print("Required columns: OK")
    print(f"Similarity features: {len(SIMILARITY_FEATURES)}")
    print("Ready for similarity analysis.")