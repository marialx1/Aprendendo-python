carrinho = []

produto = ""

while produto != "sair":
    produto = input("Digite um produto: ")

    if produto != "sair":
        carrinho.append(produto)

carrinho.sort()

print("Os produtos foram adicionados ao carrinho!")
print(carrinho)