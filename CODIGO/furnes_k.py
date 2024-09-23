from furnes import furness
from obtencion_datos import O_2024 , D_2024
from mse import T
from funciones import suma_columnas, suma_filas

t = (furness(T , O_2024 , D_2024))

print(t)

print(suma_columnas(t))
print(suma_filas(t))

