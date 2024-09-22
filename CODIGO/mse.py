import numpy as np
from obtencion_datos import t
from nueva_od import T
from obtencion_datos import O_2024 , D_2024
def mean_squared_error(matrix1, matrix2):
    print('hola')
    """
    Calcula el error cuadrático medio entre dos matrices.
    
    Args:
    - matrix1 (np.array): Primera matriz.
    - matrix2 (np.array): Segunda matriz.
    
    Returns:
    - float: Error cuadrático medio.
    """
    # Convertir las matrices a arrays de NumPy si no lo son
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    # Verificar que las matrices tengan la misma forma
    if matrix1.shape != matrix2.shape:
        raise ValueError("Las matrices deben tener la misma forma")
    
    # Calcular el MSE
    mse = np.mean((matrix1 - matrix2) ** 2)
    return mse



# Calcular el MSE

matriz1 = t
matriz2 = T

mse = mean_squared_error(matriz1, matriz2)
print(f"El MSE entre las dos matrices es: {mse}")


