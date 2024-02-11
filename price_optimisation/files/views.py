import os
import random 
from pathlib import Path
import pandas as pd
from django.shortcuts import render, HttpResponse
from django.template import loader
import tensorflow as tf
from sklearn.model_selection import train_test_split

def perform_price_optimization():
    BASE_DIR = Path(__file__).resolve().parent.parent  # Get project root
    df = pd.read_csv(os.path.join(BASE_DIR, 'files', 'data', 'preprocessed_price_optimization_dataset.csv'))
    loaded_model = tf.keras.models.load_model(os.path.join(BASE_DIR, 'files', 'data', 'price_optimization_model.h5'))
    return df, loaded_model 

def homepage(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def actual_vs_predicted(request):
    df, loaded_model = perform_price_optimization()
    X = df[['product_id', 'category_id', 'brand_encoded', 'historical_price_scaled']] 
    y = df['historical_price'] 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    predictions = loaded_model.predict(X_test)
    evaluation = loaded_model.evaluate(X_test, y_test)
    actual_data = list(y_test) 
    predicted_data = list(predictions.flatten()) 
    zipped_data = list(zip(actual_data, predicted_data, df['product_id']))
    context = {
        'zipped_data': zipped_data,
        'evaluation': evaluation, 
        'actual_data': actual_data,
        'predicted_data': predicted_data,
    }
    return render(request, 'actual_vs_predicted.html', context)

def price_optimization(request):
    if request.method == 'POST':
        # Retrieve user input from the form
        product_id = request.POST.get('product_id')
        category_id = request.POST.get('category_id')
        brand = request.POST.get('brand')
        historical_price = float(request.POST.get('historical_price'))

        # Perform price optimization using the loaded model
        df, loaded_model = perform_price_optimization()
        # Assuming you have preprocessed the user input in a format compatible with your model
        input_data = preprocess_input(product_id, category_id, brand, historical_price)
        optimized_price = loaded_model.predict(input_data)

        # You can render a template with the optimized price or return a JSON response
        context = {
            'product_id': product_id,
            'optimized_price': optimized_price
        }
        return render(request, 'price_optimization_result.html', context)
    else:
        # Handle GET request (show the form)
        return render(request, 'price_optimization_form.html')

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

    
