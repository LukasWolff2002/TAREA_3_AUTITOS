import numpy as np
from obtencion_datos import t
from nueva_od import matriz_t
from obtencion_datos import O_2024 , D_2024, O, D
def mean_squared_error(matrix1, matrix2):
    # Convertir las matrices a arrays de NumPy si no lo son
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    # Verificar que las matrices tengan la misma forma
    if matrix1.shape != matrix2.shape:
        raise ValueError("Las matrices deben tener la misma forma")
    
    # Calcular el MSE
    mse = (np.mean((matrix1 - matrix2) ** 2))/100
    return mse



# Calcular el MSE

k_0 = 1
matriz1 = t
error_0 = mean_squared_error(matriz1, matriz_t(1, O, D))

print(f"Error cuadrático medio con k = 1: {error_0}")

k_1 = k_0 - 0.001
error_1 = mean_squared_error(t, matriz_t(k_1, O, D))

while error_1 < error_0:
    k_0 = k_1
    error_0 = error_1
    k_1 -= 0.001
    error_1 = mean_squared_error(t, matriz_t(k_1, O, D))

print(f"El valor de k que minimiza el error cuadrático medio es: {k_0}")
print(f"Error cuadrático medio: {error_0}")

#Donde la matriz final es
T = (matriz_t(k_0, O, D))

#Luego le aplico furnes a esta matriz









