import unittest
import pandas as pd
import os
from main import create_match_dataset


class TestCreateMatchDataset(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('output.csv')

    def test_create_match_dataset(self):

        create_match_dataset()


        match_df = pd.read_csv('match.csv')

        # Test column names
        expected_columns = ['match_id','match_name', 'home_team_id', 'away_team_id', 'home_goals', 'away_goals']
        self.assertListEqual(list(match_df.columns), expected_columns)

    # Cleanup
    def tearDown(self):
        os.remove('match.csv')

