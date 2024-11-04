import optuna
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import optuna
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def optimize_with_optuna(X_train, y_train, X_test, y_test, params):
    best_models = {}
    
    # Configurar los estudios de optuna para cada modelo
    for model_name in params["models"].keys():
        param_grid = params["models"][model_name]
        
        def objective(trial):
            if model_name == "random_forest":
                n_estimators = trial.suggest_categorical("n_estimators", param_grid["n_estimators"])
                max_depth = trial.suggest_categorical("max_depth", param_grid["max_depth"])
                model = RandomForestRegressor(n_estimators=n_estimators, max_depth=max_depth, n_jobs=-1)
            
            elif model_name == "gradient_boosting":
                n_estimators = trial.suggest_categorical("n_estimators", param_grid["n_estimators"])
                max_depth = trial.suggest_categorical("max_depth", param_grid["max_depth"])
                learning_rate = trial.suggest_categorical("learning_rate", param_grid["learning_rate"])
                model = GradientBoostingRegressor(n_estimators=n_estimators, max_depth=max_depth, learning_rate=learning_rate)
            
            elif model_name == "linear_regression":
                fit_intercept = trial.suggest_categorical("fit_intercept", param_grid["fit_intercept"])
                model = LinearRegression(fit_intercept=fit_intercept)

            # Entrenar el modelo y evaluar
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            mse = mean_squared_error(y_test, y_pred)
            return mse

        # Optimizar y guardar el mejor modelo
        study = optuna.create_study(direction="minimize")
        study.optimize(objective, n_trials=50)
        best_models[model_name] = {"params": study.best_params, "score": study.best_value}
    
    return best_models





