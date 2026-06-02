while True:
    letra = input("Digite uma letra (ou 0 para sair): ") . lower()

    match letra:
        case "0":
            print("Programa finalizado...")
            break
        case "a" | "e" | "i" | "o" | "u":
            print("É uma vogal!")
        case 'b'|'c' |'d' |'e' |'f' |'g' |'h' |'j' |'k' |'l' |'m' |'n' |'p' |'q' |'r' |'s' |'t' |'v' |'w' |'x' |'y' |'z':
            print("É uma consoante!")
        case _:
            print("Entrada invalida. Tente novamente!")