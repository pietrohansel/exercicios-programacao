# 11. Soma dos múltiplos de 3 em um intervalo

a = int(input("Digite um número: "))

b = int(input("Digite outro número: "))

soma = 0

for i in range(a,b+1):
    if i % 3 == 0:
        soma = soma + i
        
print(f"Soma: {soma}")
    