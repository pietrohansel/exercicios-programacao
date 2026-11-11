# Estrutura


'''c = 1

while c < 10:
    print(c)
    c += 1
print('Fim')
'''

'''
n = 1
while n != 0:
    n = int(input('Digite um número: '))
print('Fim')
'''

# Exercícios


from random import randint
import random


def colorir():
    return {'reset': '\033[m',
            'red': '\033[1;31m',
            'green': '\033[1;32m'}


'''
cores = colorir()
sex = ""

while sex not in ['f', 'm']:

    sex = str(input('Digite seu sexo [M/F]: ')).lower().strip()

    if sex not in ('f', 'm'):
        print(f'{cores['red']}Inválido{cores['reset']}')

print(f'{cores['green']}Válido{cores['reset']}')
'''

''''
cont = 0
numero_aleatorio = 0

print('Pensei em um número!')
numero_aleatorio = random.randint(1, 10)

adivinha = int(input('Tente adivinhar o número: '))

while adivinha != numero_aleatorio:

    cont += 1
    print('Você errou!')
    adivinha = int(input('Tente novamente: '))

print('Voce acertou!')
print(f'Tentativas = {cont+1}')


n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

escolhe = 0

while escolhe != 5:

    #print('''
# [4] - Novos números
# [5] - Sair)
'''escolhe = int(input('Digite um número: '))

    if escolhe == 1:
        print(f'Soma = {n1 + n2}')

    elif escolhe == 2:
        print(f'Multiplicação = {n1 * n2}')

    elif escolhe == 3:
        if n1 > n2:
            print(f'Maior = {n1}')
        else:
            print(f'Maior = {n2}')

    elif escolhe == 4:
        print('Digite novos números:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif escolhe == 5:
        print('Saindo...')

    else:
        print('Opção inválida!')
'''
'''
n = int(input('Digite um número: '))
fatorial = 1

for i in range(1, n + 1):
    fatorial *= i

print(f'Fatorial de {n} é {fatorial}')
'''

'''
primero_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais

    while cont <= total:
        print(f'{primero_termo} -> ', end='')
        primero_termo += razao
        cont += 1

    print('Pausa')
    mais = int(input('Quantos a mais? '))

print('Finalizada')
'''

''''
n = (int(input("Quant de termos: ")))


t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end="")

cont = 3

while cont <= n:
    t3 = t1 + t2
    print(f' -> {t3}', end="")

    t1 = t2
    t2 = t3
    cont += 1


print(' -> FIM')
'''



