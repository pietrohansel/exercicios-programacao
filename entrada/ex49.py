# 10. Paridade e sinal de um número

n = int(input("Digite um número: "))

if n % 2 == 0:
    print("Par")
else:
    print("Ímpar")

if n < 0:
    print("Negativo")
else:
    if n == 0:
        print("Igual a zero")
    else:
        print("Positivo")

        