# 12. Contagem de divisores

n = int(input("Digite um número: "))

divisor = 0 

for i in range(1, n+1):
    if n % i == 0:
        divisor += 1 

print(f"{divisor}")

