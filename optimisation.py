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

# Display the shapes of the training and testing sets
print("Shape of X_train:", X_train.shape)
print("Shape of y_train:", y_train.shape)
print("Shape of X_test:", X_test.shape)
print("Shape of y_test:", y_test.shape)


# Step 2: Building the Price Optimization Model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1)  # Output layer with one neuron (for predicting price)
])

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# Display the model summary
print("Model Summary:")
model.summary()

# Step 3: Training the Model
history = model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)

