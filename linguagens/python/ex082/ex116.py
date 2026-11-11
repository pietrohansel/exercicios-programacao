valor1 = int(input("Valor 1: "))
valor2 = int(input("Valor 2: "))

print("\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisao\n")

opcao = int(input("Escolha uma opção: "))


match opcao:
    case 1:
        print(valor1 + valor2)

    case 2:
        print(valor1 - valor2)

    case 3:
        print(valor1 * valor2)

    case 4:
        print(valor1 / valor2)
