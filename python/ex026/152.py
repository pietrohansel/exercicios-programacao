# Estrutura

# Tuplas

lanches = ('banana', 'uva', 'maça')

# print(lanches[1])

# print(lanches[0:2])

# print(lanches[0:]) #Vai até o final

# print(lanches[-1])

# print(len(lanches))

'''for c in lanches:
    print(c)
'''
'''
for comida in lanches:
    print(f'Comi uma {lanches}')

for cont in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[cont]}')

for pos, comida in enumerate(lanches):
    print(f'Eu vou comer uma {lanches} na posição {pos}')


print(sorted(lanches))  # ordem alfab

print(lanches.count('maça'))  # mostra a quantid de x

print(lanches.index("uva")) # mostra a posição de ocorrência
'''


# Exercícios

'''
contagem_extenso = ('zero', 'um', 'dois', 'trẽs', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'novo', 'dez',
                    'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

try:
    while True:
        number = int(input('Digite um número entre 0 a 20: '))

        if number < 0 or number > 20:
            print(f'{number} não é um valor válido!')
            break

        else:
            print(f'{contagem_extenso[number]}')

except ValueError:
    print('Digite um número válido')
'''

# Exercício 2

times = ('palmeiras', 'fluminense', 'bahia', 'são paulo', 'atletico paran')

print(
    f'1 - {times[0]}, 2 - {times[1]}, 3 - {times[2]}, 4 - {times[3]}, 5 - {times[4]}')

print(f'4 - {times[3]} 5 - {times[4]}')

print(f'{sorted(times)}')

print(f'{times.index('palmeiras')+1} ')
