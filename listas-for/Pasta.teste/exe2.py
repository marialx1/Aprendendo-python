from unittest import case

conceito = input("digite o conceito (A, B, C, D ou F): ")
match conceito:
    case "A":
        print("Exelente Trabalho!")
    case "B":
        print("Bom Desempenho.")
    case "C":
        print("Satisfatorio.")
    case "D":
        print("Abaixo da media (ATENÇAO).")
    case "F":
        print("Reprovado.")
    case _:
        print("Conceito desconhecido.")