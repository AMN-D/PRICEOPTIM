import numpy as np 
import pandas as pd 
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('2020-Jan.csv')
null_counts = df.isnull().sum()

# Sum up the counts to find the total number of null values in the entire DataFrame
total_null_count = null_counts.sum()

print("Total number of null values in the DataFrame:", total_null_count)

"""df.drop(['category_code', 'user_session'], axis=1, inplace = True)

df['event_time'] = df['event_time'].str.replace(' UTC', '')
df['event_time'] = pd.to_datetime(df['event_time'])

df.dropna(axis=0, inplace=True)

l1 = LabelEncoder()
l1.fit(df['brand'])  # Fit the LabelEncoder to the 'brand' column
df['encoded_brand'] = l1.transform(df['brand'])  # Transform the 'brand' column and store the results in a new column 'encoded_brand'

df.to_csv('2020_Jan_Filtered.csv', index=False)"""
