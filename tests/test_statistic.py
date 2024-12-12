import unittest
import pandas as pd
import os
from main import create_statistics_dataset

class TestCreateStatisticsDataset(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('output.csv')

    def test_create_statistics_dataset(self):
        create_statistics_dataset()

        stat_df = pd.read_csv('statistics.csv')

        # Test columns in the final statistics dataset
        expected_columns = ['Stat_Id','player_id', 'match_id', 'goals_scored', 'minutes_played',
                            'fraction_of_total_minutes_played', 'fraction_of_total_goals_scored']
        self.assertListEqual(list(stat_df.columns), expected_columns)

    def tearDown(self):
        os.remove('statistics.csv')
