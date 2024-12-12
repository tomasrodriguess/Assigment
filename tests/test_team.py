import unittest
import pandas as pd
import os
from main import create_team_dataset

class TestCreateTeamDataset(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('output.csv')

    def test_create_team_dataset(self):
        create_team_dataset()

        team_df = pd.read_csv('team.csv')

        # Test if the dataframe contains the correct number of unique teams
        unique_teams = team_df['team_id'].nunique()
        self.assertEqual(unique_teams, len(team_df))


        # Test column names
        expected_columns = ['team_id','match_name']
        self.assertListEqual(list(team_df.columns), expected_columns)

    def tearDown(self):
        os.remove('team.csv')
