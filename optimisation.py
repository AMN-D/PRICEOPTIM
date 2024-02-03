# import the pandas library
import pandas as pd
from sklearn.preprocessing import LabelEncoder

# load your dataset
df = pd.read_csv('amazon.csv')
le = LabelEncoder()
# remove non-usable columns
df['category'] = le.fit_transform(df['category'])

df.to_csv(r'amazon.csv', index=False)