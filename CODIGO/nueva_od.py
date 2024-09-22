from obtencion_datos import O_2024, D_2024, O, D
from funciones import suma_filas, suma_columnas
import sys
from cij import distancias
import pandas as pd
import numpy as np
import pandas as pd

np.set_printoptions(suppress=True, formatter={'float_kind':'{:0.0f}'.format})

def matriz_t (k):
    
    betha = 0.2696

    #Debo calcular el valor de alpha

    T = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(len(O_2024)):
        #Le agrego a la matriz T una matriz de puros 0

        #recorro del 1 al 10
        #debo hacer 1 - 1, 1-2 
        #luego 2-1, 2-2
        for j in range(len(O_2024)):
            T[i][j] = O_2024[i] * D_2024[j]
            


    #Ahora debo calcula la suma de todo
    suma = sum(suma_filas(T))

    #Finalmente calculo alpha
    #Nesecito el total de viajes reales

    numero_viajes = sum(O_2024)
    alpha = numero_viajes / suma

    #pruebo calcular otro alpha
    suma = 0

    for i in range(len(O_2024)):
        for j in range(len(O_2024)):
            if distancias[i][j] == '∞':
                suma += 0
            else:
                suma += (O_2024[j]*D_2024[j])/(distancias[i][j]**2)
    alpha = numero_viajes/(suma)

    print(f'{alpha=}')

    T_final = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(len(O_2024)):
        for j in range(len(O_2024)):
            if distancias[i][j] == '∞':
                distancias[i][j] = 0
            T_final[i][j] = alpha * O[i] * D[j] * ((distancias[i][j])**k) * np.exp (-betha*distancias[i][j])
    
    T_final = np.rint(T_final)
    return T_final

T = matriz_t(0.5)




