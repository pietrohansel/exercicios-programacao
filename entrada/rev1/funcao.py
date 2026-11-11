def Printar(mensagem):
    print(mensagem)


def Somar(a,b):
    resultado = a + b
    print("O resultado da soma é:", resultado)


def CriarLista():
    lista = []

    for i in range(0,11,1):
        lista.append(i)

    for i in lista:
        print(i, end="-")

    return lista


def CriarLista2():
    lista = []
    cont = 0 

    while cont <= 10:
        lista.append(cont)
        print(cont, end="-")
        cont += 1

    return lista