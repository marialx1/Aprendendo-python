matriz = [[15, 42, 7],
       [23, 91, 12],
       [34, 8, 55]]
matriz_v = [sum(n) for n in matriz]
matriz_s = [n for conjunto in matriz for n in conjunto]
matriz_s = [15,42,7,23,91,12,34,8,55]
maior = max(matriz_s)
matriz_s.index(maior)
