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

        # Load the model
        model_path = os.path.join(settings.BASE_DIR, 'files', 'data', 'price_optimization_model.h5')
        loaded_model = load_model(model_path)

        # Perform prediction
        X = df[['product_id', 'category_id', 'brand_encoded', 'historical_price_scaled']]
        y = df['historical_price']
        y_pred = loaded_model.predict(X)

        # Calculate metrics
        mae = mean_absolute_error(y, y_pred)
        mse = mean_squared_error(y, y_pred)
        rmse = np.sqrt(mse)

        # Print metrics for debugging
        print("Mean Absolute Error (MAE):", mae)
        print("Mean Squared Error (MSE):", mse)
        print("Root Mean Squared Error (RMSE):", rmse)

        # Prepare data for context
        features = X.columns.tolist()
        outcome = y.name

        # Convert DataFrame to JSON for passing to template
        json_data = df.to_json(orient='records')

        # Add calculated metrics to context
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

            # Check if all required keys are present in the received data
            if 'product_id' not in received_data or 'category_id' not in received_data \
                or 'brand_encoded' not in received_data or 'historical_price_scaled' not in received_data:
                return JsonResponse({'error': 'Missing required data'}, status=400)

            # Get the values for each key and convert them to numeric types
            product_id = int(received_data.get('product_id'))
            category_id = int(received_data.get('category_id'))
            brand_encoded = float(received_data.get('brand_encoded'))
            historical_price_scaled = float(received_data.get('historical_price_scaled'))

            # Load the model
            model_path = os.path.join(settings.BASE_DIR, 'files', 'data', 'price_optimization_model.h5')
            loaded_model = load_model(model_path)

            # Perform prediction
            X = pd.DataFrame([[product_id, category_id, brand_encoded, historical_price_scaled]],
                            columns=['product_id', 'category_id', 'brand_encoded', 'historical_price_scaled'])
            optimized_price = loaded_model.predict(X)[0][0]

            # Convert optimized_price to regular float
            optimized_price = float(optimized_price)

            response_data = {
                'optimized_price': optimized_price,
                'historical_price_scaled': historical_price_scaled
            }

            print(optimized_price)
            return JsonResponse(response_data)

        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Failed to decode JSON data'}, status=400)
        except ValueError as e:
            return JsonResponse({'error': 'Invalid data format'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)