from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(
    1, 10), randint(1, 10), randint(1, 10), )

print(f'\n {numeros}')

numeros = sorted(numeros)

print(f'\n MENOR = {min(numeros)} MAIOR = {max(numeros)}')
