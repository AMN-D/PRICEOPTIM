from django.shortcuts import render, HttpResponse
from django.conf import settings
import json
from django.http import JsonResponse
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import load_model
from django.views.decorators.csrf import csrf_exempt

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

    df = pd.read_csv(os.path.join(settings.BASE_DIR, 'files', 'data', 'preprocessed_price_optimization_dataset.csv'))
    json_data = df.to_json(orient='records')
    model_path = os.path.join(settings.BASE_DIR, 'files', 'data', 'price_optimization_model.h5')

    X = df[['product_id', 'category_id', 'brand_encoded', 'historical_price_scaled']] 
    y = df['historical_price'] 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    loaded_model = load_model(model_path)

    predictions = loaded_model.predict(X_test)
    evaluation = loaded_model.evaluate(X_test, y_test)

    actual_data = list(y_test) 
    predicted_data = list(predictions.flatten()) 
    
    features = X.columns.tolist()
    outcome = y.name

    if request.method == 'POST':
        try:
            received_dict = {}
            received_data = json.loads(request.body.decode('utf-8'))
            for key, value in received_data.items():
                received_dict[key] = value
            print("Received dictionary:", received_dict)

            for key, value in received_dict.items():
                if key in X.columns:
                    X[key] = pd.to_numeric(value)

            print(X)

            predictions = loaded_model.predict(X)
            evaluation = loaded_model.evaluate(X, y_test)
            predicted_data = predictions.flatten().tolist()

            print(predicted_data)

            return JsonResponse({'message': 'Received data successfully'}, status=200)
        except json.JSONDecodeError as e:
            return JsonResponse({'error': 'Failed to decode JSON data'}, status=400)

    context = {
        'features': features,
        'outcome': outcome,
        'json_data': json_data,
    }

    return render(request, 'custom.html', context)