from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from joblib import Parallel, delayed, dump
import pandas as pd

def train_models(X_train, y_train, X_test, y_test, params):
    models = {
        "Linear Regression": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_jobs=-1),  # Entrenamiento paralelo
        "Gradient Boosting": GradientBoostingRegressor(n_iter_no_change=5, validation_fraction=0.1)  # Early stopping
    }

    model_results = []
    trained_models = {}

    for model_name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        mse = mean_squared_error(y_test, y_pred)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        model_results.append({
            "Model": model_name,
            "MSE": mse,
            "MAE": mae,
            "R2": r2
        })
        trained_models[model_name] = model

        print(f"\n{model_name} - MSE: {mse}, MAE: {mae}, R2: {r2}")
        dump(model, f'models/{model_name}.joblib')

    # Exportar resultados de métricas a CSV
    results_df = pd.DataFrame(model_results)
    results_df.to_csv("results/model_performance.csv", index=False)
    
    return trained_models, results_df

def feature_importance(trained_models, feature_names):
    for model_name, model in trained_models.items():
        if hasattr(model, "feature_importances_"):
            importances = model.feature_importances_
            importance_df = pd.DataFrame({
                "Feature": feature_names,
                "Importance": importances
            }).sort_values(by="Importance", ascending=False)
            
            # Guardar importancia de características en CSV
            importance_df.to_csv(f"results/{model_name}_feature_importance.csv", index=False)
            print(f"Importancia de características exportada para {model_name}")

