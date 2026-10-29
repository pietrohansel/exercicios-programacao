# 1. Soma dos positivos até zero

soma_positivo = 0
qtd_positivo = 0
num_negativo = 0
media = 0

num = 1
while num != 0:
    num = int(input('Digite um numero: '))
    if num > 0:
        soma_positivo = soma_positivo + num
        qtd_positivo = qtd_positivo +1
    else:
        if num < 0:
            num_negativo = num_negativo + 1
media = soma_positivo / qtd_positivo

print(f'A soma dos numeros positivos: {soma_positivo}')
print(f'Quantidade de numeros negativos: {num_negativo}')
print(f'A media dos numeros positivos é: {media:.2f}')
