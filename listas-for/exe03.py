numeros = []

impares =[]
pares = []

for i in range (1,11):
    numeros = int(input(f"Digite o {i} número:"))

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numeros)
    else:
        impares.append(numeros)

print("Lista principal" , numeros)
print("Lista pares" , pares)
print("Lista impares" , impares)