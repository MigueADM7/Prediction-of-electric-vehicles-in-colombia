
# Cargar el dataset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar el dataset
file_path = 'Numero_de_Vehiculos_Electricos-Hibridos.xlsx'
df = pd.read_excel(file_path)

# Seleccionar solo columnas numericas
numeric_df = df.select_dtypes(include=[float, int])

# Graficar la matriz de correlación
correlation_matrix = numeric_df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')

# Guardar el grafico como imagen
plt.savefig('Correlación_variables.png')

plt.show()
