import pandas as pd

# Especifica el path al archivo xlsx
archivo = 'OD.xlsx'

# Usa read_excel para leer el rango específico
# Asegúrate de que la ruta del archivo sea correcta y accesible
df = pd.read_excel(archivo, usecols='B:K', skiprows=0, nrows=11)

# Convertir el DataFrame a una lista de listas
t = df.values.tolist()



O = (list(df.columns))
D = O