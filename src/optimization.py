from sklearn.model_selection import GridSearchCV
import pandas as pd

def optimize_hyperparameters(X_train, y_train, models, params):
    best_models = {}

    # Optimización para Random Forest
    rf_param_grid = params['models']['random_forest']
    rf_grid = GridSearchCV(models["Random Forest"], param_grid=rf_param_grid, cv=5)
    rf_grid.fit(X_train, y_train)
    best_models["Random Forest"] = {"model": rf_grid.best_estimator_, "best_score": rf_grid.best_score_}
    print(f"\nRandom Forest - Mejor configuración: {rf_grid.best_params_}, Mejor puntaje: {rf_grid.best_score_}")

    # Optimización para Gradient Boosting
    gb_param_grid = params['models']['gradient_boosting']
    gb_grid = GridSearchCV(models["Gradient Boosting"], param_grid=gb_param_grid, cv=5)
    gb_grid.fit(X_train, y_train)
    best_models["Gradient Boosting"] = {"model": gb_grid.best_estimator_, "best_score": gb_grid.best_score_}
    print(f"\nGradient Boosting - Mejor configuración: {gb_grid.best_params_}, Mejor puntaje: {gb_grid.best_score_}")

    # Optimización para Linear Regression
    lr_grid = GridSearchCV(models["Linear Regression"], param_grid={}, cv=5)
    lr_grid.fit(X_train, y_train)
    best_models["Linear Regression"] = {"model": lr_grid.best_estimator_, "best_score": lr_grid.best_score_}
    print(f"\nLinear Regression - Mejor puntaje: {lr_grid.best_score_}")

    return best_models