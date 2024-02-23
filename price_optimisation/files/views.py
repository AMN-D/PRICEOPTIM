from django.shortcuts import render, HttpResponse
from django.template import loader

def homepage(request):
    selected_model = request.GET.get('model', '')
    print('value selected is', selected_model)
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

'''
import os
import random 
from pathlib import Path
import pandas as pd
from django.shortcuts import render, HttpResponse
from django.template import loader
import tensorflow as tf
from sklearn.model_selection import train_test_split
import json
from django.http import JsonResponse


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
        product_id = int(request.POST.get('product_id'))
        category_id = int(request.POST.get('category_id'))
        brand = int(request.POST.get('brand'))
        historical_price = float(request.POST.get('historical_price'))
        # Assuming you have the necessary feature encoding and scaling logic here
        df, loaded_model = perform_price_optimization()
        # Prepare the input features
        X = [[product_id, category_id, brand, historical_price]]
        # Make prediction
        optimized_price = loaded_model.predict(X)[0][0]
        # Pass the form data and prediction result to the template
        return render(request, 'price_optimization.html', {
            'show_result': True,
            'product_id': product_id,
            'category_id': category_id,
            'brand': brand,
            'historical_price': historical_price,
            'optimized_price': optimized_price,
        })
    else:
        return render(request, 'price_optimization.html', {'show_result': False})

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def perform_price_optimization():
    BASE_DIR = Path(__file__).resolve().parent.parent
    model_name = request.POST.get('model_name')
    if model_name == 'lowkey':
        model_path = os.path.join(BASE_DIR, 'files', 'data', 'price_optimization_model.h5')
    else:
        # Handle other model names or default behavior here
        model_path = 'default_model_path'  # Replace with appropriate default

    df = pd.read_csv(os.path.join(BASE_DIR, 'files', 'data', 'preprocessed_price_optimization_dataset.csv'))
    loaded_model = tf.keras.models.load_model(model_path)

    # Render the results (e.g., using a template)
    context = {'results': results}  # Replace 'results' with your actual results
    html_content = render_to_string('price_optimization_results.html', context)
    return JsonResponse({'html_content': html_content})
    
    
   # BASE_DIR = Path(__file__).resolve().parent.parent
   # df = pd.read_csv(os.path.join(BASE_DIR, 'files', 'data', 'preprocessed_price_optimization_dataset.csv'))
   # loaded_model = tf.keras.models.load_model(os.path.join(BASE_DIR, 'files', 'data', 'price_optimization_model.h5'))
   # return df, loaded_model 

'''



    
