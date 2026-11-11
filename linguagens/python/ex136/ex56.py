# 17. Decomposição de notas

v = int(input("Digite um valor em reais: R$ "))

n100 = v // 100
resto = v % 100

n50 = resto // 50
resto = resto % 50

n10 = resto // 10
resto = resto % 10

n5 = resto // 5
resto = resto % 5

n1 = resto // 1

print(f"Notas de 100: {n100}")
print(f"Notas de 50: {n50}")
print(f"Notas de 10: {n10}")
print(f"Notas de 5: {n5}")
print(f"Notas de 1: {n1}")