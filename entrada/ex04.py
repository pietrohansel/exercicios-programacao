# 4. Soma dos dígitos de um número

num = int(input('Digite um numero: '))
soma = 0
ultimo = 0

while num > 0:
    ultimo = num % 10
    soma = soma + ultimo
    num = num // 10
print(soma)