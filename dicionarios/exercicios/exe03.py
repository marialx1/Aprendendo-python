
dicionario_de_quadrados = {}

for i in range (1, 6):
    dicionario_de_quadrados.setdefault(i, i**2)


for k, v in dicionario_de_quadrados.items():
    print(f" {k} -> {v}")



lista = ["macarrao", "feijao", "arroz", "feijao", "carne", "arroz", "miojo", "arroz"]

print("Quantos arrozez", lista.count("feijao"))


