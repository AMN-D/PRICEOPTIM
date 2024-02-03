# import the pandas library
import pandas as pd

# load your dataset
df = pd.read_csv('amazon.csv')

# remove non-usable columns
df = df.drop(['img_link', 'product_link', 'user_id', 'user_name', 'review_id', 'review_title', 'review_content'], axis=1)

# if you want to remove rows with missing values instead, you can use this line
df = df.dropna()
df.to_csv(r'amazon.csv', index=False)
