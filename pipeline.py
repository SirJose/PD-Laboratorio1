import yaml
from src.preprocess import load_and_preprocess_data
from src.train import train_models
from src.optimization import optimize_hyperparameters

# Cargar parámetros desde params.yaml
with open("params.yaml", "r") as file:
    params = yaml.safe_load(file)

# Paso 1 y 2: 
# Cargar, explorar, visualizasr y preprocesar los datos
X_train, X_test, y_train, y_test = load_and_preprocess_data("data/data.csv", params)

# Paso 3: 
# Entrenar modelos y obtener el mejor modelo
trained_models, model_results = train_models(X_train, y_train, X_test, y_test, params)

# Paso 4:
# Optimizar hiperparámetros de los modelos entrenados
best_models = optimize_hyperparameters(X_train, y_train, trained_models, params)
print(f"\nMejores modelos optimizados:\n", best_models)
