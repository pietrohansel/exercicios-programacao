# 3. Contagem de dígitos de um número

cont = 0
num = int(input('Digite um numero: '))

while num != 0:
    num = num // 10
    cont += 1
    
print(cont)
    