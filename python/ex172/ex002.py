import jogo as j 
import fileHandler as fH


def mostrarMenu():
    print("1 - Jogar\n2 - Score\n3 - Sair")




m1 = mostrarMenu()

opcao = int(input("Escolha uma opção: "))

match opcao:
    case 1:
        pass 
    case 2:
        pass
    case 3:
        pass 
    case _:
        print("Opção inválida") 