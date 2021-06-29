                                             
                                              ** Twitter-Data-Analysis**__
                                               
                                               
                                               
**Dataset information**

The data is raw Twitter data dumb in JSON format on COVID19 related topics. It is collected using the following keywords:‘COVID19 Africa’, ‘COVID19 Vaccination
Africa’, ‘Sars-Cov2 Mutation Africa’.It has 6532 records(rows).The data is then extracted and converted to csv format.

**Pre Processing**

The preprocessing scripts modifies the tweets content in order to make possible the further analysis.
    • Duplicated rows are removed.
    • Unwanted columns are dropped.
    • Format of some columns has been changed to the appropriate format.
    • columns like polarity, subjectivity, retweet_count,favorite_count etc are converted to numbers.
The data is then visualised using different charts. The cleaned data was split for training and testing using sklearn, train test split module. Finally, SGD classifier was used to train the model using the training data. The accuracy of the model is then evaluated and it is 97% accurate.

**Dashboard**

    • A dashboard has been built using streamlit to provide the insights obtained.

    • The web app has two pages and selection of the data to be displayed. 
      
    • It has different plots that show different analyses of the data.

**CI Implementation with Travis CI**

    •  Travis CI has been set up to the repository such that when you git push new code (or merge a branch) to the main branch, the unit test in tests/*.py runs automatically.

**Information about other files**

    • processed_tweet_data.csv – contains our data set in csv format.
    • clean_processed_tweet_data.csv - contains the cleaned data set in CSV format.

