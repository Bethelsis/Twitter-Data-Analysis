                         Twitter-Data-Analysis
Dataset Information

The data is raw Twitter data dumb in JSON format on COVID19 related topics. It is collected using the following keywords:‘COVID19 Africa’, ‘COVID19 Vaccination Africa’, ‘Sars-Cov2 Mutation Africa’.It has 6532 records(rows).

Methodology

First, I cleaned the tweets. I have dropped duplicated rows, dropped unwanted columns. I also changed the format of some columns to the appropriate format like from string to DateTime.Then I converted columns like polarity, subjectivity, retweet_count,favorite_count etc to numbers. Then I visualized the data using different charts. The cleaned data was split for training and testing using sklearn, train test split module. Finally, SGD classifier was used to train the model using the training data. I then checked the accuracy of the model.

Information about other files

• processed_tweet_data.csv -contains our data in CSV format

• clean_processed_tweet_data- contains the cleaned data set in CSV format.
