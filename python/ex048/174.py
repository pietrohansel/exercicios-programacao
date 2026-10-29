# 087.py

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

soma_pares = soma_tercoluna = soma_seglinha = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(
            input(f"Digite o valor [{linha} , {coluna}]:"))

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f"[{matriz[linha][coluna]:^5}]", end='')

        if matriz[linha][coluna] % 2 == 0:
            soma_pares += matriz[linha][coluna]
    print()

for linha in range(0, 3):
    soma_tercoluna += matriz[linha][2]

for coluna in range(0, 3):
    soma_seglinha += matriz[coluna][1]


print(soma_pares)
print(soma_tercoluna)
print(soma_seglinha)
