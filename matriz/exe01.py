notasAlunos = [ ["Joao", 8.7, 9.0], ["Maria", 7.3, 9.0], ["Jose", 8.3, 5.2] ]
mediaAlunos = []
for i in notasAlunos:
    media = (i[1]+i[2])/2
    lista = [i[0],media]
    mediaAlunos.append(lista)

print(f"Lista de notas de alunos: {notasAlunos}")
print(f"Lista de notas: {mediaAlunos}")
