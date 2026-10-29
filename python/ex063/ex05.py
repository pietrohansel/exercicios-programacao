# 5. Número invertido

num = int(input('Digite um numero: '))
invertido = 0

while num != 0:
    ult_dig = num % 10
    invertido = invertido * 10 + ult_dig
    num = num // 10
print(invertido)