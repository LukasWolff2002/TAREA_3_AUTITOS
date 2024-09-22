import pandas as pd
from funciones import suma_filas, suma_columnas
# Especifica el path al archivo xlsx
archivo = 'OD.xlsx'

# Usa read_excel para leer el rango específico
# Asegúrate de que la ruta del archivo sea correcta y accesible
df = pd.read_excel(archivo, usecols='B:K', skiprows=0, nrows=10)

# Convertir el DataFrame a una lista de listas
t = df.values.tolist()


#Con esto tengo los vecotres reales de la matriz OD
D = suma_columnas(t)
#Corresponde a la suma de las columnas

O = suma_filas(t)
#Corresponde a la suma de las filas

#Ahora obtengo los vectores reales:
archivo = 'VECTORES_2024.xlsx'

# Convertir los datos de la columna en una lista

df = pd.read_excel(archivo, usecols="B:K")
O_2024 = df.iloc[0].tolist()
D_2024 = df.iloc[1].tolist()




