import unittest
import pandas as pd
import numpy as np
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))


df = pd.read_csv("clean_processed_tweet_data.csv")
class TestClean_Tweets(unittest.TestCase):

    def test_convert_to_datetime(self):
        self.assertEqual(df.dtypes['created_at'], "object")

    def test_convert_to_numbers(self):
        df1=df[['followers_count','polarity','subjectivity','retweet_count','favorite_count','friends_count']]
        self.assertEqual(df1.dtypes.tolist(), ["int64","float64","float64","float64","float64","int64"])

    def test_drop_duplicate(self):
        self.assertEqual(df.duplicated().sum(),0)

    #def test_drop_unwanted_column(self):
       # self.assertEqual()
    
    def test_remove_non_english_tweets(self):
        self.assertEqual(df['lang'].values.all(),np.array(["en" for _ in range(len(df['lang'].values))],dtype=object).all())

if __name__ == '__main__':
	unittest.main()
