matriz_quadrada = [
                   [5, 2, 9],
                   [1, 8, 3],
                   [4, 7, 6]
                             ]
soma = 0

for i in range(len(matriz_quadrada)):
    soma += matriz_quadrada[i][i]

print("Soma da diagonal principal:",soma)