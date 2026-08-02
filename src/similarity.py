import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler

from src.validation import SIMILARITY_FEATURES


def get_per90_features() -> list[str]:
    """
    Return the per-90 columns used for similarity analysis.
    """
    return [
        f"{feature}_per90"
        for feature in SIMILARITY_FEATURES
    ]


def find_similar_players(
    df: pd.DataFrame,
    player_name: str,
    squad: str | None = None,
    top_n: int = 10,
) -> pd.DataFrame:
    """
    Find the most statistically similar players.

    Parameters
    ----------
    df : pd.DataFrame
        Prepared player dataset.
    player_name : str
        Name of the reference player.
    squad : str | None, optional
        Squad used to distinguish duplicate player records.
    top_n : int, optional
        Number of similar players to return.

    Returns
    -------
    pd.DataFrame
        Ranked table of similar players.
    """
    per90_features = get_per90_features()

    player_matches = df[
        df["Player"].str.casefold() == player_name.casefold()
    ]

    if player_matches.empty:
        raise ValueError(
            f"Player not found: {player_name}"
        )

    if squad is not None:
        player_matches = player_matches[
            player_matches["Squad"].str.casefold()
            == squad.casefold()
        ]

        if player_matches.empty:
            raise ValueError(
                f"Player not found: {player_name} - {squad}"
            )

    elif len(player_matches) > 1:
        available_squads = ", ".join(
            player_matches["Squad"].astype(str).tolist()
        )

        raise ValueError(
            f"Multiple records found for {player_name}. "
            f"Specify squad. Available squads: {available_squads}"
        )

    player_index = player_matches.index[0]

    scaler = StandardScaler()

    scaled_features = scaler.fit_transform(
        df[per90_features]
    )

    similarity_scores = cosine_similarity(
        scaled_features[player_index].reshape(1, -1),
        scaled_features,
    ).flatten()

    results = df[
        [
            "Player",
            "Squad",
            "Pos",
            "Age",
            "Min",
        ]
    ].copy()

    results["Similarity"] = similarity_scores

    results = results.drop(
        index=player_index
    )

    results = results.sort_values(
        by="Similarity",
        ascending=False,
    )

    return results.head(top_n).reset_index(drop=True)