buscador = [[10, 50, 40]
           [25, 67, 35]
           [78, 89, 34]]

busca = int(input("Digite o numero que deseja procurar: "))
achou = False

for i in range(len(buscador)):
    for j in range(len(buscador)):
        if buscador[i][j] == busca:
            print(f"O numero que voce procura esta na linha {i+1} e na coluna {j+1}.")
            achou = True
            break
    if achou:
        break

if not achou:
    print("O seu numero nao esta nessa lista")