maior18 = 0
homens = 0
mulheres20 = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ").upper()

    if idade > 18:
        maior18 += 1

    if sexo == "M":
        homens += 1

    if sexo == "F" and idade < 20:
        mulheres20 += 1

    continuar = input("Quer continuar? (S/N): ").upper()

    if continuar == "N":
        break

print("Pessoas com mais de 18 anos:", maior18)
print("Homens cadastrados:", homens)
print("Mulheres com menos de 20 anos:", mulheres20)