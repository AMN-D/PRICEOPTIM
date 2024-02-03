# import the pandas library
import pandas as pd

# load your dataset
df = pd.read_csv('amazon.csv')

# remove non-usable columns
df = df.drop(['about_product', 'product_id'], axis=1)

# if you want to remove rows with missing values instead, you can use this line
df = df.dropna()

df.to_csv(r'amazon.csv', index=False)