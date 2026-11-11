# 6. Conversão de decimal para binário

num = int(input('Digite um número: '))
num_bin = 0
posicao = 0

while num != 1 :
    dig_bin = num % 2
    num_bin += (dig_bin * 10) ** posicao
    posicao += 1
    num = num // 2
print(num_bin)