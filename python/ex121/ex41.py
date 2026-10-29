# 2. Divisibilidade por 5 ou por 7

num = int(input("Digite um número: "))

if num % 5 == 0:
    print(f"O número {num} é divisível por 5.")
else:
    print(f"O número {num} não é divisível por 5.")

if num % 7 == 0:
    print(f"O número {num} é divisível por 7.")
else:
    print(f"O número {num} não é divisível por 7.")
