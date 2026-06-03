from unittest import case

numero = int(input("digite um numero de 1 a 7:"))

match numero:
      case 1:
          print("Domingo")
      case 2:
          print("Segunda-Feira")
      case 3:
          print("Terceira-Feira")
      case 4:
          print("Quarta-Feira")
      case 5:
          print("Quinta-Feira")
      case 6:
          print("Sexta-Feira")
      case 7:
          print("Sabado")
      case _:
          print("Dia invalido")