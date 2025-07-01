from banco import criar_banco, adicionar_contato, listar_contatos, atualizar_contato, deletar_contato

criar_banco()

while True:
    print("\nAgenda de Contatos")
    print("1 - Adicionar contato")
    print("2 - Listar contatos")
    print("3 - Atualizar contato")
    print("4 - Deletar contato")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        adicionar_contato(nome, telefone, email)
        print("Contato adicionado com sucesso.")

    elif opcao == "2":
        contatos = listar_contatos()
        for c in contatos:
            print(f"{c[0]} - {c[1]} | {c[2]} | {c[3]}")

    elif opcao == "3":
        id = int(input("ID do contato: "))
        nome = input("Novo nome: ")
        telefone = input("Novo telefone: ")
        email = input("Novo email: ")
        atualizar_contato(id, nome, telefone, email)
        print("Contato atualizado.")

    elif opcao == "4":
        id = int(input("ID do contato: "))
        deletar_contato(id)
        print("Contato deletado.")

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")
