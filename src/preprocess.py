import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

def load_and_preprocess_data(filepath, params):
    # Cargar datos
    data = pd.read_csv(filepath)
    print("Columnas del dataset:", data.columns)

    # Dividir datos en características y variable objetivo
    X = data.drop('price', axis=1)
    y = data['price']

    # Dividir en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=params['split']['test_size'], random_state=params['split']['random_state'])

    print("Tamaño de los conjuntos de entrenamiento y prueba:", X_train.shape, X_test.shape, y_train.shape, y_test.shape)

    # Identificar variables numéricas y categóricas (excluyendo 'price')
    num_features = X.select_dtypes(include=['float64', 'int']).columns
    cat_features = X.select_dtypes(include=['object']).columns

    print("Características numéricas:", num_features)
    print("Características categóricas:", cat_features)

    # Configurar preprocesamiento
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), num_features),
            ('cat', OneHotEncoder(), cat_features)
        ]
    )

    # Aplicar preprocesamiento
    X_train = preprocessor.fit_transform(X_train)
    X_test = preprocessor.transform(X_test)
    
    return X_train, X_test, y_train, y_test
