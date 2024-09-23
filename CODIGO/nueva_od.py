from funciones import suma_filas
from cij import distancias
import numpy as np
import pandas as pd

np.set_printoptions(suppress=True, formatter={'float_kind':'{:0.0f}'.format})

def matriz_t (k, O, D):
    
    betha = 0.2696

    numero_viajes = sum(O)
    #pruebo calcular otro alpha
    suma = 0

    for i in range(len(O)):
        for j in range(len(O)):
            if distancias[i][j] == '∞':
                suma += 0
            else:
                suma += (O[i]*D[j])* ((distancias[i][j])**(-k)) * np.exp (-betha*distancias[i][j])
    alpha = numero_viajes/(suma)

    T_final = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(len(O)):
        for j in range(len(O)):
            if distancias[i][j] == '∞':
                T_final[i][j] = 0
            else:
                T_final[i][j] = alpha * O[i] * D[j] * ((distancias[i][j])**(-k)) * np.exp (-betha*distancias[i][j])
    
    T_final = np.rint(T_final)
    return T_final






