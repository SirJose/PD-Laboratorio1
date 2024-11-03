from sklearn.model_selection import GridSearchCV
import pandas as pd

def optimize_hyperparameters(X_train, y_train, models, params):
    best_models = {}

    # Optimización para Random Forest
    rf_param_grid = params['models']['random_forest']
    rf_grid = GridSearchCV(models["Random Forest"]["model"], param_grid=rf_param_grid, cv=5)
    rf_grid.fit(X_train, y_train)

    best_models["Random Forest"] = {"model": rf_grid.best_estimator_, "best_score": rf_grid.best_score_}
    print(f"Random Forest - Mejor configuración: {rf_grid.best_params_}, Mejor puntaje: {rf_grid.best_score_}")

    return best_models
