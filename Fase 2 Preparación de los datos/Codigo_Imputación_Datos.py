
import pandas as pd
import numpy as np

# Cargar el dataset
file_path = 'Dataset_vehiculos_electricos_modificado.xlsx'
df = pd.read_excel(file_path)

# Excluir la columna FECHA_REGISTRO de las imputaciones
fecha_col = 'FECHA_REGISTRO'

# Reemplazar ceros por NaN en todas las columnas excepto FECHA_REGISTRO
df.loc[:, df.columns != fecha_col] = df.loc[:, df.columns != fecha_col].replace(0, np.nan)

# Reemplazar los ceros por NaN en todas las columnas
df.replace(0, np.nan, inplace=True)

# Explorar los valores faltantes
print("Valores faltantes por columna:")
print(df.isnull().sum())

# Imputación de datos
# Para columnas numéricas: Usaremos la media
num_cols = df.select_dtypes(include=['float64', 'int64']).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].mean())

# Para columnas categóricas: Usaremos la moda
cat_cols = df.select_dtypes(include=['object']).columns
for col in cat_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# Verificar si quedan valores faltantes
print("\nDespués de la imputación, valores faltantes por columna:")
print(df.isnull().sum())
