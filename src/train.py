from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from joblib import dump


def train_models(X_train, y_train, X_test, y_test, params):
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(),
        "Gradient Boosting": GradientBoostingRegressor()
    }

    # Entrenamiento y evaluación
    model_results = {}
    for model_name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        model_results[model_name] = mse

        # Imprimir resultados
        print(f"{model_name} - MSE: {mse}")

        # Guardar modelo
        dump(model, f'models/{model_name}.joblib')


    return model_results
