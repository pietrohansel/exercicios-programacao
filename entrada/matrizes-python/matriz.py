import numpy as np

A = np.array([[2, 3]])
B = np.array([[4], [5]])

resultado = A @ B

print(resultado)

a = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]


b = [
    [20,50,50],
    [40,10,80],
    [70,20,30],
]

# coluna indice 0


def matrizString(matriz):
    string_matriz = ""

    for linha in matriz:
        string_linha = "|"

        for elemento in linha:
            string_linha += str(elemento) + "|"

        string_matriz += string_linha + "\n"

    return string_matriz 



def visualizar_matriz(matriz):
    print(matrizString(matriz))


def somaMatriz(matriz1, matriz2):
    matriz_soma = []
    for i in range(len(matriz1)):
        nova_linha = []
        for j in range(len(matriz1[0])):
            elemento1 = matriz1[i][j]
            elemento2 = matriz2[i][j]
            nova_linha.append(elemento1 + elemento2)

        matriz_soma.append(nova_linha)

    return matriz_soma




soma = somaMatriz(a,b)
visualizar_matriz(soma)