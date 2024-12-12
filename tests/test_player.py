import unittest
import pandas as pd
import os
from main import create_player_dataset

class TestCreatePlayerDataset(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('output.csv')

    def test_create_player_dataset(self):
        create_player_dataset()

        player_df = pd.read_csv('player.csv')

        # Test that player IDs are unique
        self.assertEqual(player_df['player_id'].nunique(), len(player_df))

        # Test column names
        expected_columns = ['player_id','team_id','player_name']
        self.assertListEqual(list(player_df.columns), expected_columns)

    def tearDown(self):
        os.remove('player.csv')
