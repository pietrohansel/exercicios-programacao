# 30. Soma dos dois maiores valores

v1 = float(input("Valor 1: "))
v2 = float(input("Valor 2: "))
v3 = float(input("Valor 3: "))

if v1 <= v2 and v1 <= v3:
    menor = v1

else:
    if v2 <= v1 and v2 <= v3:
        menor = v2

    else:
        menor = v3

soma = v1 + v2 + v3 - menor

print(f"\nSoma dos dois maiores valores: {soma}")
