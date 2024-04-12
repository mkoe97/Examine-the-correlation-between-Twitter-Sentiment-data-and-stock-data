#Imports
import pandas as pd
from transformers import pipeline
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import os
import time

current_folder_path = os.getcwd()
file_name = 'smaller_Tweets_AMZN.csv'
full_path = os.path.join(current_folder_path, file_name)
df_tweets_2015 = pd.read_csv(full_path)

sentiment_analysis = pipeline("sentiment-analysis")
df_sentiment_2015 = pd.DataFrame(columns=['date', 'positives', 'neutral' , 'negatives', 'sentiment_score'])

i = 0
current_day_count = 0
positive_percentage = 0
negative_percentage = 0
neutral_percentage = 0
k = 0
bigger_than_512 = False

start_time = time.time()
#tokenizer = AutoTokenizer.from_pretrained("sentiment-analysis")
for row in df_tweets_2015.itertuples():
    current_date = row.date
    if i == 0:
        date_before = current_date
    tokens = sentiment_analysis.tokenizer(row.body)
    if len(tokens["input_ids"]) > 512:
        k = k + 1
        bigger_than_512 = True
    else:
        sentiment_value = sentiment_analysis(row.body)
    if current_date == date_before:
      if bigger_than_512 == True:
          bigger_than_512 = False
      else:
          current_day_count = current_day_count + 1
          if sentiment_value[0]["label"] == 'POSITIVE':
              positive_percentage = positive_percentage + 1
          elif sentiment_value[0]["label"] == 'NEUTRAL':
              neutral_percentage = neutral_percentage + 1
          else:
              negative_percentage = negative_percentage + 1
    else:
        positive_percentage = positive_percentage / current_day_count
        negative_percentage = negative_percentage / current_day_count
        neutral_percentage = neutral_percentage / current_day_count
        rows_to_add = pd.DataFrame({'date': [row.date], 'positives': [positive_percentage], 'neutral': [neutral_percentage], 'negatives': [negative_percentage]})
        df_sentiment_2015 = pd.concat([df_sentiment_2015, rows_to_add], ignore_index=True)
        positive_percentage = 0
        negative_percentage = 0
        neutral_percentage = 0
        current_day_count = 0

    if (i % 1000) == 0:
        print("i: ", i)
        print("k: ", k)
    i = i + 1
    date_before = current_date

end_time = time.time()
elapsed_time = end_time - start_time


print(df_sentiment_2015.head())
output_name = 'AMZN_normal_model.csv'
full_output_path = os.path.join(current_folder_path, output_name)
df_sentiment_2015.to_csv(full_output_path, index=False)
print(f"Elapsed Time: {elapsed_time} seconds")