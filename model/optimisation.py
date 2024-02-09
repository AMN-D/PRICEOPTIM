import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf
# Load the preprocessed dataset
df = pd.read_csv('preprocessed_price_optimization_dataset.csv')

# Step 1: Splitting the dataset into features and target variable
X = df[['product_id', 'category_id', 'brand_encoded', 'historical_price_scaled']]  # Features
y = df['historical_price']  # Target variable (prices)

# Step 2: Further split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Load the saved model from disk
loaded_model = tf.keras.models.load_model('price_optimization_model.h5')

# Use the loaded model for predictions
predictions = loaded_model.predict(X_test)

# Evaluate the loaded model
loaded_model.evaluate(X_test, y_test)
# Use the trained model for predictions

# Display the first few predictions
for i in range(5):
    print("Predicted price:", predictions[i][0])
    print("Actual price:", y_test.iloc[i])
    print()  # Empty line for clarity
