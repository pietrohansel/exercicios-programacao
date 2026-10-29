# 13. Verificação de número primo

n = int(input("Digite um número: "))

divores = 0 

for i in range(1, n+1):
    if n % i == 0:
        divores += 1 

if divores ==  2:
    print("Primo")

else:
    print("Não é primo")