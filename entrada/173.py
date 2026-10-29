# 086.py

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

numeros = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input('Digite um número: '))

print(f"=-"*40)

for linha in range(0, 3):
    for coluna in range(0, 3):
                                    # Alinha         
        print(f"[{matriz[linha][coluna]:^5}]", end='')
    print()
