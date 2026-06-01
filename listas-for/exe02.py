notas = []

for i in range(4):
    nota = float(input(f"Digite a nota:"))
    notas.append(nota)

media = sum(notas) / len(notas)

print("Notas:", notas)
print("Média:", media)

if media >= 7.0:
    print("Aprovado")
else:
    print("Recuperação")
    