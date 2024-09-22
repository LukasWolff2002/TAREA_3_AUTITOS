#Primero obtengo las distancias en cada trayecto
import pandas as pd
from obtencion_datos import t

# Especifica el path al archivo xlsx
archivo = 'DISTANCIAS.xlsx'

# Usa read_excel para leer el rango específico
# Asegúrate de que la ruta del archivo sea correcta y accesible
df = pd.read_excel(archivo, usecols='B:K', skiprows=0, nrows=10)

distancias = df.values.tolist()

