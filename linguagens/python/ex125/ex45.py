# 6. Verificação de múltiplos

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

if n1 % n2 == 0 or n2 % n1 == 0:
    print("São múltiplos")
else:
    print("Não são multiplos")
