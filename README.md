# Project Documentation

## Running the `main.py` Script

To run the `main.py` script, which generates the datasets (match, team, player, and statistics), ensure you have the `output.csv` file in the root directory of the project, as it is required for the script to generate the datasets.

### Running the Script

To execute the `main.py` script, use the following command in the terminal from the root directory of the project:

```bash
python main.py

```

This will generate the four datasets normalized.

# Unit Test

## Test Structure

- `create_match_dataset()`
- `create_team_dataset()`
- `create_player_dataset()`
- `create_statistics_dataset()`

Run the test with

```bash
python -m unittest discover -s tests

```

These tests ensure that:

- The correct columns are selected.
- The output CSV files are generated as expected.

---
