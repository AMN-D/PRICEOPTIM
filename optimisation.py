# import the pandas library
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# load your dataset
df = pd.read_csv('amazon.csv')
df['actual_price'] = df['actual_price'].str.replace('₹', '').str.replace(',', '').astype(float)
df['discounted_price'] = df['discounted_price'].str.replace('₹', '').str.replace(',', '').astype(float)

# Remove '%' symbol from 'discount_percentage'
df['discount_percentage'] = df['discount_percentage'].str.replace('%', '').astype(float)

# Remove ',' from 'rating_count'
df['rating_count'] = df['rating_count'].str.replace(',', '').astype(int)


df.to_csv(r'amazon.csv', index=False)