
import pandas as pd

# Cargar el dataset
file_path = 'Dataset_vehiculos_electricos_imputado.xlsx'
df = pd.read_excel(file_path)

# Ver las primeras filas de la columna FECHA_REGISTRO para inspeccionar los valores
print(df['FECHA_REGISTRO'].head(10))

# Intentar convertir a datetime sin especificar un formato (permitir que pandas infiera)
df['FECHA_REGISTRO'] = pd.to_datetime(df['FECHA_REGISTRO'], errors='coerce', dayfirst=False)

# Verificar si alguna fecha sigue siendo NaT
print(f"Valores nulos en FECHA_REGISTRO: {df['FECHA_REGISTRO'].isnull().sum()}")

# Si hay valores NaT, forzar una conversión manual para los formatos MM-DD-YYYY
# Esto solo será necesario si el paso anterior no resuelve todos los casos
df['FECHA_REGISTRO'] = pd.to_datetime(df['FECHA_REGISTRO'], errors='coerce', format='%m-%d-%Y')

# Verificar el tipo de datos de la columna FECHA_REGISTRO después de la conversión
print(f"Tipo de datos de FECHA_REGISTRO: {df['FECHA_REGISTRO'].dtype}")

# Verificar los primeros registros después de la conversión
print(df['FECHA_REGISTRO'].head(10))

# Extraer el año de la columna FECHA_REGISTRO
df['AÑO_REGISTRO'] = df['FECHA_REGISTRO'].dt.year

# Verifica los primeros registros de las columnas
print(df[['FECHA_REGISTRO', 'AÑO_REGISTRO']].head())
