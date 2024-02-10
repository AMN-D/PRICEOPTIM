from sklearn.model_selection import train_test_split
from django.shortcuts import render, HttpResponse
import tensorflow as tf
import pandas as pd
from pathlib import Path
import os

def homepage(request):
    return HttpResponse('HomePage')

def actual_vs_predicted(request):
    BASE_DIR = Path(__file__).resolve().parent.parent  # Get project root
    df = pd.read_csv(os.path.join(BASE_DIR, 'files', 'data', 'preprocessed_price_optimization_dataset.csv'))

    X = df[['product_id', 'category_id', 'brand_encoded', 'historical_price_scaled']]  # Features
    y = df['historical_price']  # Target variable (prices)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    loaded_model = tf.keras.models.load_model(os.path.join(BASE_DIR, 'files', 'data', 'price_optimization_model.h5'))
    predictions = loaded_model.predict(X_test)
    evaluation = loaded_model.evaluate(X_test, y_test)

    # Prepare data to pass to the template
    actual_data = list(y_test)  # Actual historical prices
    predicted_data = list(predictions.flatten())  # Predicted prices

    # Pass data to the template
    context = {
        'actual_data': actual_data,
        'predicted_data': predicted_data,
        'evaluation': evaluation  # Optional: pass evaluation results to template
    }

    # Render the template with the provided context
    return render(request, 'actual_vs_predicted.html', context)



    
