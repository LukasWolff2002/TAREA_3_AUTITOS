def suma_columnas (t):
    D = [0 for i in range(10)]
    for elementos in t:
        for i in range (len(elementos)):
            D[i]+=elementos[i]

    return D

def suma_filas (t):
    O = [0 for i in range(10)]
    for i in range(len(t)):
        for elementos in t[i]:
            O[i]+=elementos

    return O
