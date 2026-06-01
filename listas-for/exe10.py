import random

numero_secreto = random.randint(1,20)

palpite = int(input("Advinhe o número entre 1 a 20: "))

while palpite != numero_secreto:
    if palpite < numero_secreto:
        print("O número secreto é maior")

    else:
        print("O número secreto é menor!")

    palpite = int(input("Tente novamente: "))

print("Parabéns você acertou!")