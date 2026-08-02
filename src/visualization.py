

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from src.similarity import get_per90_features


def calculate_percentiles(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate percentile ranks for the per-90 similarity features.

    Parameters
    ----------
    df : pd.DataFrame
        Prepared player dataset.

    Returns
    -------
    pd.DataFrame
        Copy of the dataset with percentile columns from 0 to 100.
    """
    df_percentiles = df.copy()

    per90_features = get_per90_features()

    for feature in per90_features:
        percentile_column = f"{feature}_percentile"

        df_percentiles[percentile_column] = (
            df_percentiles[feature]
            .rank(pct=True)
            .mul(100)
        )

    return df_percentiles



def plot_player_radar(
    df: pd.DataFrame,
    player_name: str,
    comparison_name: str,
    player_squad: str | None = None,
    comparison_squad: str | None = None,
    output_path: Path | None = None,
) -> None:
    """
    Plot a percentile radar comparing two players.
    """
    df_percentiles = calculate_percentiles(df)

    def select_player(
        name: str,
        squad: str | None,
    ) -> pd.Series:
        matches = df_percentiles[
            df_percentiles["Player"].str.casefold()
            == name.casefold()
        ]

        if squad is not None:
            matches = matches[
                matches["Squad"].str.casefold()
                == squad.casefold()
            ]

        if matches.empty:
            raise ValueError(
                f"Player not found: {name}"
            )

        if len(matches) > 1:
            available_squads = ", ".join(
                matches["Squad"].astype(str).tolist()
            )

            raise ValueError(
                f"Multiple records found for {name}. "
                f"Specify squad. Available squads: {available_squads}"
            )

        return matches.iloc[0]

    player = select_player(
        player_name,
        player_squad,
    )

    comparison = select_player(
        comparison_name,
        comparison_squad,
    )

    feature_labels = [
        "Goals",
        "Assists",
        "Expected goals",
        "Expected assists",
        "Progressive carries",
        "Progressive passes",
        "Progressive receptions",
    ]

    percentile_columns = [
        f"{feature}_percentile"
        for feature in get_per90_features()
    ]

    player_values = (
        player[percentile_columns]
        .astype(float)
        .tolist()
    )

    comparison_values = (
        comparison[percentile_columns]
        .astype(float)
        .tolist()
    )

    player_values += player_values[:1]
    comparison_values += comparison_values[:1]

    angles = np.linspace(
        0,
        2 * np.pi,
        len(feature_labels),
        endpoint=False,
    ).tolist()

    angles += angles[:1]

    figure, axis = plt.subplots(
        figsize=(9, 9),
        subplot_kw={"polar": True},
    )

    axis.plot(
        angles,
        player_values,
        linewidth=2,
        label=f"{player_name} — {player['Squad']}",
    )
    axis.fill(
        angles,
        player_values,
        alpha=0.15,
    )

    axis.plot(
        angles,
        comparison_values,
        linewidth=2,
        label=f"{comparison_name} — {comparison['Squad']}",
    )
    axis.fill(
        angles,
        comparison_values,
        alpha=0.15,
    )

    axis.set_xticks(angles[:-1])
    axis.set_xticklabels(feature_labels)

    axis.set_ylim(0, 100)
    axis.set_yticks([20, 40, 60, 80, 100])
    axis.set_yticklabels(
        ["20", "40", "60", "80", "100"]
    )

    axis.set_title(
        "Player Statistical Profile Comparison\n"
        "Percentile rank within the eligible dataset",
        pad=25,
        fontsize=15,
    )

    axis.legend(
        loc="upper right",
        bbox_to_anchor=(1.30, 1.10),
    )

    figure.tight_layout()

    if output_path is not None:
        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        figure.savefig(
            output_path,
            dpi=300,
            bbox_inches="tight",
        )

    plt.show()