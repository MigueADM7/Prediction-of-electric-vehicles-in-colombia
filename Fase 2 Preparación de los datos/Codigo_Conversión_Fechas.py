
import pandas as pd

# Cargar el dataset
file_path = 'Dataset_vehiculos_electricos_imputado.xlsx'
df = pd.read_excel(file_path)

print(df['FECHA_REGISTRO'].head(10))

# Intentar convertir a datetime sin especificar un formato 
df['FECHA_REGISTRO'] = pd.to_datetime(df['FECHA_REGISTRO'], errors='coerce', dayfirst=False)

# Verificar si alguna fecha sigue siendo NaT
print(f"Valores nulos en FECHA_REGISTRO: {df['FECHA_REGISTRO'].isnull().sum()}")
df['FECHA_REGISTRO'] = pd.to_datetime(df['FECHA_REGISTRO'], errors='coerce', format='%m-%d-%Y')

# Verificar el tipo de datos después de la conversión
print(f"Tipo de datos de FECHA_REGISTRO: {df['FECHA_REGISTRO'].dtype}")

# Verificar los primeros registros después de la conversión
print(df['FECHA_REGISTRO'].head(10))

# Extraer el año de la columna FECHA_REGISTRO
df['AÑO_REGISTRO'] = df['FECHA_REGISTRO'].dt.year

# Verifica los primeros registros de las columnas
print(df[['FECHA_REGISTRO', 'AÑO_REGISTRO']].head())
