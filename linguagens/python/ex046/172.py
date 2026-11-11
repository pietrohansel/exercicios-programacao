# 085.py
conjunto = [[], []]

numeros = 0

print("-="*40)

for valores in range(1, 8):
    numeros = int(input('Digite um número: '))

    if numeros % 2 == 0:
        conjunto[0].append(numeros)
    else:
        conjunto[1].append(numeros)

conjunto[0].sort()
conjunto[1].sort()

print(f"Conjunto = {conjunto}")
print(f"Pares {conjunto[0]}")
print(f"Ímpares = {conjunto[1]}")

print("-="*40)
