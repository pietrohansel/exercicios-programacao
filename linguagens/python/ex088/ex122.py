print("\n===== Bem-vindo ao CineMovie =====")

carrinho = []
opcao = 0

while opcao != 4:

    print("\n===== MENU =====")
    print("1 - Ingressos")
    print("2 - Lanchonete")
    print("3 - Resumo")
    print("4 - Sair")

    opcao = int(input("\nEscolha uma opção: "))

    match opcao:

        case 1:
            print("\n----- Ingressos -----")

            idade = int(input("Qual é a sua idade? "))

            if idade < 12:
                print("Criança - Ingresso R$10,00")
                carrinho.append("Ingresso Criança - R$10,00")

            elif idade < 18:
                print("Adolescente - Ingresso R$20,00")
                carrinho.append("Ingresso Adolescente - R$20,00")

            else:
                print("Adulto - Ingresso R$30,00")
                carrinho.append("Ingresso Adulto - R$30,00")

        case 2:
            print("\n----- CineLanches -----")
            print("1 - Pipoca")
            print("2 - Refrigerante")
            print("3 - Chocolate")

            opcao_lanches = int(input("\nEscolha uma opção: "))

            match opcao_lanches:

                case 1:
                    tamanho = input(
                        "Tamanho: [P/M/G] "
                    ).lower().strip()

                    if tamanho == "p":
                        carrinho.append("Pipoca - Pequena")
                        print("Pipoca pequena adicionada!")

                    elif tamanho == "m":
                        carrinho.append("Pipoca - Média")
                        print("Pipoca média adicionada!")

                    elif tamanho == "g":
                        carrinho.append("Pipoca - Grande")
                        print("Pipoca grande adicionada!")

                    else:
                        print("Tamanho inválido!")

                case 2:
                    carrinho.append("Refrigerante")
                    print("Refrigerante adicionado!")

                case 3:
                    carrinho.append("Chocolate")
                    print("Chocolate adicionado!")

                case _:
                    print("Opção de lanche inválida!")

        case 3:
            print("\n----- Resumo -----")

            if len(carrinho) == 0:
                print("Seu carrinho está vazio.")

            else:
                for item in carrinho:
                    print("-", item)

            input("\nPressione ENTER para voltar ao menu...")

            continue

        case 4:
            print("\nObrigado por usar o CineMovie!")

        case _:
            print("\nOpção inválida!")

print("\nPrograma encerrado.")