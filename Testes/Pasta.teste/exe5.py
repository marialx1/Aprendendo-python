perfil = input("Qual o seu perfil?")

match perfil:
    case "ADMIN":
        print("Acesso total: Criar, Ler, Atualizar e Deletar.")
    case "GERENTE":
        print("Acesso gerencial: Criar, Ler, Atualizar.")
    case "EDITOR":
        print("Acesso de conteudo: Ler, Atualizar.")
    case "VISITANTE":
        print("Acesso restrito: Apenas leitura.")
    case _:
        print("Perfil nao reconhecido. Acesso bloqueado")