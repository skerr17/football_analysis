# This program downloads the latest version of the dataset
# "International Football Results from 1872 to 2017" from Kaggle
# https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017
# and saves it to a CSV file named "international-football-results-from-1872-to-2017.csv"
# Author: Stephen Kerr


# import the kagglehub library
# This library is used to download datasets from Kaggle
import kagglehub

# import the pandas library
import pandas as pd

# import the os library
import os


# Download latest version
path = kagglehub.dataset_download("martj42/international-football-results-from-1872-to-2017")

# save the dataframe to a csv file
csv_path = os.path.join(path, "results.csv")
football_results_df = pd.read_csv(csv_path)
football_results_df.to_csv("international-football-results-from-1872-to-2017.csv", index=False)
