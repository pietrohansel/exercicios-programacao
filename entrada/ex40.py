# 1. Divisibilidade por 2 e por 3

num = int(input("Digite um número: "))

if num % 2 == 0 and num % 3 == 0:
    print(f"Número {num} é divisível por 2 e 3 ao mesmo tempo.")
else:
    print(f"Número {num} não é divisível por 2 e 3 ao mesmo tempo")