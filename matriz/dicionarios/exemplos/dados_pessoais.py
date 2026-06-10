from email.policy import default

dados_pessoais = {

      "nome": "Joao",
      "idade": 21,
      "nascimento": "20-05-2005",
      "sexo": "M",
      "altura": 1.70,
      "temCNH": True
}

continuar = "s"
while continuar == "s":


    dados = input("digite o que voce quer encontrar: ")

    print(dados_pessoais.get(dados, "valor nao encontrado!"))

    continuar = input("quer continuar? [s/n]:") [0].lower()

