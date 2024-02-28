from django.shortcuts import render, HttpResponse
from django.conf import settings
import json
from django.http import JsonResponse
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from django.views.decorators.csrf import csrf_exempt
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def homepage(request):

    df = pd.read_csv(os.path.join(settings.BASE_DIR, 'files', 'data', 'preprocessed_price_optimization_dataset.csv'))
    model_path = os.path.join(settings.BASE_DIR, 'files', 'data', 'price_optimization_model.h5')

    X = df[['product_id', 'category_id', 'brand_encoded', 'historical_price_scaled']] 
    y = df['historical_price'] 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    loaded_model = load_model(model_path)

    predictions = loaded_model.predict(X_test)
    evaluation = loaded_model.evaluate(X_test, y_test)

    actual_data = list(y_test) 
    predicted_data = list(predictions.flatten()) 

    context = {
        'actual_data': actual_data,
        'predicted_data': predicted_data,
    }

    return render(request, 'base.html', context)

@csrf_exempt
def custom(request):
    if request.method == 'GET':
        # Load the dataset
        df = pd.read_csv(os.path.join(settings.BASE_DIR, 'files', 'data', 'preprocessed_price_optimization_dataset.csv'))
        model_path = os.path.join(settings.BASE_DIR, 'files', 'data', 'price_optimization_model.h5')
        loaded_model = load_model(model_path)

        X = df[['product_id', 'category_id', 'brand_encoded', 'historical_price_scaled']]
        y = df['historical_price']
        y_pred = loaded_model.predict(X)

        mae = mean_absolute_error(y, y_pred)
        mse = mean_squared_error(y, y_pred)
        rmse = np.sqrt(mse)

        features = X.columns.tolist()
        outcome = y.name

        json_data = df.to_json(orient='records')

        context = {
            'features': features,
            'outcome': outcome,
            'json_data': json_data,
            'mae': mae,
            'mse': mse,
            'rmse': rmse,
        }

        return render(request, 'custom.html', context)

    elif request.method == 'POST':
        try:
            received_data = json.loads(request.body.decode('utf-8'))

            product_id = int(received_data.get('product_id'))
            category_id = int(received_data.get('category_id'))
            brand_encoded = float(received_data.get('brand_encoded'))
            historical_price_scaled = float(received_data.get('historical_price_scaled'))

            model_path = os.path.join(settings.BASE_DIR, 'files', 'data', 'price_optimization_model.h5')
            loaded_model = load_model(model_path)

            X = pd.DataFrame([[product_id, category_id, brand_encoded, historical_price_scaled]],
                             columns=['product_id', 'category_id', 'brand_encoded', 'historical_price_scaled'])
            optimized_price = loaded_model.predict(X)[0][0]

            y_pred = loaded_model.predict(X)
            mse = mean_squared_error(y, y_pred)
            rmse = np.sqrt(mse)

            response_data = {
                'optimized_price': optimized_price,
                'historical_price_scaled': historical_price_scaled,
                'mse': mse,
                'rmse': rmse
            }

            return render(request, 'custom.html', {'response_data': response_data})

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Failed to decode JSON data'}, status=400)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)