import numpy as np
from obtencion_datos import t , O_2024 , D_2024
from funciones import suma_filas, suma_columnas 

np.set_printoptions(suppress=True, formatter={'float_kind':'{:0.0f}'.format})
t = np.matrix(t)


def furness(t, O, D, tol=1e-6, maxit=10000):
    k = len(O)
    O = np.array(O)[:, np.newaxis].astype(float)
    D = np.array(D).astype(float)
    t = np.array(t)
    ai = np.ones((k, 1))
    bj = np.ones((1, k))
    iters = 0
    
    # Añadir un pequeño valor epsilon para evitar divisiones por cero
    epsilon = 1e-10

    while iters < maxit:
        # Calcular ai, evitando división por cero
        t_sum1 = t.sum(axis=1)[:, np.newaxis] + epsilon  # Suma de filas con epsilon
        ai = O / t_sum1
        
        # Actualizar t con ai
        t = t * np.dot(ai, np.ones((1, k)))
        
        # Calcular bj, evitando división por cero
        t_sum0 = t.sum(axis=0) + epsilon  # Suma de columnas con epsilon
        bj = D / t_sum0
        
        # Actualizar t con bj
        t = t * np.dot(np.ones((k, 1)), bj[np.newaxis, :])
        
        # Verificar convergencia
        if np.max(abs(t_sum1.flatten() / O.flatten() - 1)) < tol:
            break

        iters += 1
    t_rounded = np.rint(t)
    return t_rounded


