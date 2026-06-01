ids_clientes = [101, 102, 103, 101, 104, 102, 105, 106, 10]

id_unico = []

for id in ids_clientes:
    if id not in id_unico:
        id_unico.append(id)

id_unico.sort()

print(id_unico)