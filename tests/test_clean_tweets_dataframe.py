import unittest
import pandas as pd
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
from clean_tweets_dataframe import Clean_Tweets

df = pd.read_csv("../processed_tweet_data.csv")
class TestClean_Tweets(unittest.TestCase):

    def test_convert_to_datetime(self):
        self.assertEqual(df.dtypes['created_at'], "object")

    def test_convert_to_numbers(self):
        self.assertEqual(df.dtypes[ ['screen_count','followers_count','polarity','subjectivity','retweet_count','favorite_count','friends_count']], "float64","int64","float64","float64","float64","float64","int64")

    def test_drop_duplicate(self):
        self.assertEqual(df.duplicated().sum(),307)

    def test_drop_unwanted_column(self):
        self.assertEqual()
    
    def test_remove_non_english_tweets(self):
        self.assertEqual()

if __name__ == '__main__':
	unittest.main()