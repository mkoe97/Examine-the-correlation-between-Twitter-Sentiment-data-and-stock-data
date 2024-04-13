# Examine-the-correlation-between-Twitter-Sentiment-data-and-stock-data
DOI: 10.5281/zenodo.10966852

## Desription
  The project delves into the relationship between Twitter sentiment and the stock performance of the 4 big tech companies Apple, Amazon, Google and Microsoft. Specifically, it involves analyzing individual tweets containing the keyword "Apple", "Amazon", "Google" or "Microsoft" using two sentiment analysis models to determine their sentiment, which can be classified as positive or negative for the normal model and positive, neutral or negative social media model. By examining the daily percentages of these sentiment classifications, we assess how they correlate with fluctuations in stock data on subsequent days. Employing standard statistical methods such as the Pearson Coefficient, p-values, and Mean Squared Error, we meticulously analyze the predictive accuracy of this correlation. 

## External Datasets
  Stockdata dataset: (DOI: 10.34740/kaggle/dsv/1054465) https://www.kaggle.com/datasets/jacksoncrow/stock-market-dataset/data
  Twitter dataset  : (No DOI available) https://www.kaggle.com/datasets/omermetinn/tweets-about-the-top-companies-from-2015-to-2020/data
## Execution
  In order to execute the project, the datasets from the external Datasets part have to be downloaded and move to the correct directory. The stockdata dataset within the stockdata analysis directory and the twitter data in the data preperation directoy.

  After that the ipynb files in the data preparation directory can be executed, which will result in the smaller_Tweets_<Company>.csv files. On that ouput data the sentiment analysis can be executed to which will result in the <Company>_<model>.csv files, that can be found in the stock_data_analysis folder. 

  Lastly the Project_Text_Mining_Stock_Data_Analysis.ipynb can be executed, which needs the stock data of the individual company as well as the sentiment data of the model/company as an input. This combines the dataset to get do create the final output needed for the report.

## License
  CC0 1.0 Universal (CC0 1.0) Public Domain Dedication

The person who associated a work with this deed has dedicated the work to the public domain by waiving all of their rights to the work worldwide under copyright law, including all related and neighboring rights, to the extent allowed by law.

You can copy, modify, distribute and perform the work, even for commercial purposes, all without asking permission.

See the full legal text at: https://creativecommons.org/publicdomain/zero/1.0/legalcode

This repository including it's datasets is provided under the Creative Commons CC0 1.0 Universal Public Domain Dedication (CC0 1.0).


