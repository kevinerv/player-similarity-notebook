# ⚽ Player Similarity Notebook

A professional Jupyter Notebook that identifies football players with similar statistical profiles using per-90 metrics, standardized features and cosine similarity.

## What the product does

The notebook allows the user to:

- Load and validate a football player dataset.
- Filter players with insufficient playing time.
- Calculate performance metrics per 90 minutes.
- Select a reference player and squad.
- Find the most statistically similar players.
- Review a ranked similarity table.
- Compare the selected player with the closest match using a percentile radar.
- Export the results to CSV and save the radar image.

## Who it is for

This product is designed for:

- Football analysts.
- Scouting students.
- Independent scouts.
- Sports journalists.
- Data-driven content creators.
- Python users interested in football analytics.

## Main features

- Reusable preprocessing pipeline.
- Minimum-minutes filter.
- Seven attacking and progression metrics.
- StandardScaler normalization.
- Cosine similarity ranking.
- Duplicate player handling by squad.
- Clear validation errors.
- Percentile radar comparison.
- CSV and PNG exports.
- Modular and scalable project structure.

## Metrics used

The current version compares players using:

- Goals.
- Assists.
- Expected goals.
- Expected assists.
- Progressive carries.
- Progressive passes.
- Progressive receptions.

All metrics are converted to per-90 values before the similarity analysis.

## Project structure

```text
player-similarity-notebook/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── 01_Player_Similarity_product_clean.ipynb
│
├── outputs/
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── similarity.py
│   ├── validation.py
│   └── visualization.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Requirements
Python 3.10 or newer.
Jupyter Notebook or JupyterLab.
A compatible football player CSV dataset.

The required Python packages are listed in requirements.txt.

## Installation

Clone or download the project and open a terminal in the project root.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Start Jupyter:

```bash
jupyter notebook
```

Open:

```text
notebooks/01_Player_Similarity_product_clean.ipynb
```
## How to use it

Place the dataset inside:

```text
data/raw/
```

Confirm the filename in the notebook:

```python
DATASET_FILENAME = "players_data_light-2024_2025.csv"
```

Edit the player selection section:

```python
PLAYER_NAME = "Leandro Trossard"
SQUAD = None
TOP_N = 10
```

For a player with multiple squad records:

```python
PLAYER_NAME = "Omar Marmoush"
SQUAD = "Manchester City"
TOP_N = 10
```

Run all notebook cells in order.

The notebook will:

Validate the dataset.
Prepare the player statistics.
Return the most similar players.
Generate a percentile radar.
Export the results.
## Generated files

The notebook creates:

```text
outputs/similar_players_<player_name>.csv
outputs/player_comparison_radar.png
```

Generated outputs are ignored by Git.

## How similarity is calculated

The current pipeline is:

```text
Raw statistics
      ↓
Minimum-minutes filter
      ↓
Per-90 conversion
      ↓
StandardScaler
      ↓
Cosine similarity
      ↓
Top-N ranking
```

A higher similarity score means the players have more similar statistical profiles across the selected metrics.

Similarity does not mean that the players have the same overall quality, market value, tactical role or league difficulty.

## Current limitations
The current metrics focus mainly on attacking and progression performance.
The same feature set is used for all outfield positions.
Goalkeepers are not supported.
League strength is not adjusted.
Tactical context and team style are not modeled.
Transferred players may have separate records for each squad.
## Planned versions
### v0.2 — Position profiles
Position-specific metrics.
Position-compatible comparisons.
Age and league filters.
### v0.3 — Custom scouting
User-selected metrics.
Custom metric weights.
Configurable minimum minutes.
Advanced result filters.
### v0.4 — Player reports
Extended visual reports.
Strengths and weaknesses.
Multiple player comparison.
PDF export.
### v1.0 — Web application
Streamlit interface.
CSV upload.
Interactive filters.
No-code user experience.
## Disclaimer

This product is an analytical tool. Results depend on the quality, coverage and context of the source dataset and should not replace professional scouting judgment.