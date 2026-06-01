senha = [123]

for i in range(3):
    s = input("Digite a senha:")

    if (senha == s):
        print("Acesso permitido")
        break
    else:
        print("Acesso negado")