import yaml
from src.preprocess import load_and_preprocess_data
from src.train import train_models, feature_importance
from src.optimization import optimize_hyperparameters
from src.optuna_optimization import optimize_with_optuna
import gdown

# Cargar parámetros desde params.yaml
with open("params.yaml", "r") as file:
    params = yaml.safe_load(file)

# Paso 1 y 2: Cargar y preprocesar los datos
X_train, X_test, y_train, y_test, transformed_feature_names = load_and_preprocess_data("data/data.csv", params)

# Paso 3: 
# Entrenar modelos y obtener el mejor modelo
trained_models, model_results = train_models(X_train, y_train, X_test, y_test, params)

# Paso 4:
# Optimizar hiperparámetros de los modelos entrenados
best_models = optimize_hyperparameters(X_train, y_train, trained_models, params)
print(f"\nMejores modelos optimizados:\n", best_models)

# Paso 5: Interpretación de resultados - Importancia de características
feature_importance(trained_models, transformed_feature_names)

# Extra: Optimización con Optuna
best_optuna_models = optimize_with_optuna(X_train, y_train, X_test, y_test, params)

output = "\nModelos optimizados con Optuna:\n"
for model, details in best_optuna_models.items():
    output += f"\nModelo: {model}\n"
    output += f"Mejor Puntaje: {details['score']:.4f}\n"
    output += "Parámetros Optimizados:\n"
    for param, value in details["params"].items():
        output += f"  - {param}: {value}\n"

print(output)


