# Examine-the-correlation-between-Twitter-Sentiment-data-and-stock-data


## External Datasets:
  Stockdata dataset: (DOI: 10.34740/kaggle/dsv/1054465) https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset/data
  Twitter dataset  : (No DOI available) https://www.kaggle.com/datasets/omermetinn/tweets-about-the-top-companies-from-2015-to-2020/data
## Execution
  In order to execute the project, the datasets from the external Datasets part have to be downloaded and move to the correct directory. The stockdata dataset within the stockdata analysis directory and the twitter data in the data preperation directoy.

  After that the ipynb files in the data preparation directory can be executed, which will result in the smaller_Tweets_<Company>.csv files. On that ouput data the sentiment analysis can be executed to which will result in the <Company>_<model>.csv files, that can be found in the stock_data_analysis folder. 

  Lastly the Project_Text_Mining_Stock_Data_Analysis.ipynb can be executed, which needs the stock data of the individual company as well as the sentiment data of the model/company as an input. This combines the dataset to get do create the final output needed for the report.

