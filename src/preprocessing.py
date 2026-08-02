import numpy as np
import pandas as pd

from src.validation import SIMILARITY_FEATURES
from src.config import MIN_MINUTES


def filter_min_minutes(
    df: pd.DataFrame,
    min_minutes: int = MIN_MINUTES,
) -> pd.DataFrame:
    """
    Keep only players with enough minutes played.
    """
    return df[df["Min"] >= min_minutes].copy()


def calculate_per_90_stats(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create per-90 columns for all similarity features.
    """
    df = df.copy()

    for feature in SIMILARITY_FEATURES:
        df[f"{feature}_per90"] = df[feature] / df["90s"]

    return df


def prepare_similarity_data(
    df: pd.DataFrame,
    min_minutes: int = MIN_MINUTES,
) -> pd.DataFrame:
    """
    Prepare the dataset for player similarity analysis.

    The function:
    1. Filters players by minimum minutes.
    2. Calculates per-90 statistics.
    3. Replaces infinite values.
    4. Removes rows with missing similarity values.
    """
    df_prepared = filter_min_minutes(
        df=df,
        min_minutes=min_minutes,
    )

    df_prepared = calculate_per_90_stats(df_prepared)

    per90_features = [
        f"{feature}_per90"
        for feature in SIMILARITY_FEATURES
    ]

    df_prepared[per90_features] = (
        df_prepared[per90_features]
        .replace([np.inf, -np.inf], np.nan)
    )

    df_prepared = df_prepared.dropna(
        subset=per90_features
    )

    return df_prepared.reset_index(drop=True)