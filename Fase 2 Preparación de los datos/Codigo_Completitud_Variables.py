
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import files

# Cargar el archivo Excel
df = pd.read_excel("vehiculos_electricos.xlsx")

# 1. Calcular los valores ausentes y presentes por columna
missing_data = df.isnull().sum()  # Número de valores nulos
total_data = df.shape[0]  # Número total de filas
missing_percentage = (missing_data / total_data) * 100  # Porcentaje de valores ausentes
present_percentage = 100 - missing_percentage  # Porcentaje de valores presentes

# Crear un DataFrame para facilitar la visualización
completion_df = pd.DataFrame({
    'Columna': df.columns,
    'Valores Ausentes (%)': missing_percentage,
    'Valores Presentes (%)': present_percentage
})

# Ordenar el DataFrame por los valores ausentes (opcional, para visualizar las columnas con más datos faltantes)
completion_df = completion_df.sort_values(by='Valores Ausentes (%)', ascending=False)

# 2. Graficar los porcentajes de completitud
plt.figure(figsize=(12, 8))
completion_df.set_index('Columna')[['Valores Ausentes (%)', 'Valores Presentes (%)']].plot(kind='barh', stacked=True, color=['red', 'green'])

# Títulos y etiquetas
plt.title('Completitud de las Variables', fontsize=16)
plt.xlabel('Porcentaje (%)')
plt.ylabel('Columnas')
plt.legend(title='Completitud', loc='lower right')
plt.tight_layout()

# Mostrar el gráfico
plt.show()
