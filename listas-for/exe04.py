maiores = 0
menores = 0

ANO_ATUAL = 2026

for i in range(1,8):
    ano_nascimento = int(input(f"Digite o ano de nascimento da {i} pessoa: "))

    idade = ANO_ATUAL - ano_nascimento

    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f"Quantidade de pessoas maiores de idade: {maiores}")
print(f"Quantidade de pessoas menores de idade: {menores}")
