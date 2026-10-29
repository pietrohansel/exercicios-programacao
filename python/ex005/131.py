# Estrutura

'''for x in range(inicio, fim, passo):
    print('Hello')
print('Fim')
'''

# Aplicações

'''for y in range (6,0,-1):
    print (y)
print ('cabo')

for y in range(6, 0, -3):
    print(y)
print('cabo')
'''

# Exercícios

'''
for fogos in range(10, 0, -1):
    print(fogos)
print('fim')
'''

'''
for pares in range (0,51,2):
    print(pares)
'''

'''
soma = 0
cont = 0

for x in range(1, 501, 2):
    if x % 3 == 0:
        soma += +x
        cont += 1
print(soma, cont)
'''

'''
x = (int(input('Digite um número: ')))

for n in range(0, 11,):
    print(f'{x} x {n} = {x*n}')
'''

'''
soma = 0
cont = 0

for number in range(1, 11):

    number = int(input(f'Digite o {number}° valor: '))

    cont += 1

    print(f'Contador = {cont}')

    if number % 2 == 0:
        soma += number
        print(f'Soma = {soma}')
    else:
        print('Somente pares')
'''

'''
primary = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = primary + (11-1) * razao

for n in range(primary, decimo, razao):
    razao = primary + n
    print(razao)
'''
cores = {'red': '\033[1;31m',
         'green': '\033[1;32m',
         'yellow': '\033[1;33m',
         'reset': '\033[m'}

'''
for x in range(1, 11):
    num = int(input('Digite um número qualquer: '))

    if num < 2: #nao deixa negativos
        print(f'{cores["red"]}{num}{cores["reset"]} NÃO é um número primo!')
    else:
        primo = True
        for i in range(2, num):
            if num % i == 0:
                primo = False
                break

        if primo:
            print(f'{cores["green"]}{num}{cores["reset"]} é um número primo!')
        else:
            print(f'{cores["red"]}{num}{cores["reset"]} NÃO é um número primo!')
'''

'''
frase = str(input('Escreva uma frase: ')).strip().lower

palavras = ''.split(frase)

junto = ''.join(frase)

inverso = ''

for x in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
'''
'''
ano_atual = 2026

maiores = 0
menores = 0

for pessoas in range(1, 8):
    ano = int(input(f'Digite o {pessoas}° ano de nascimento: '))

    idade = ano_atual-ano

    if idade < 18:
        print('Menor de idade')
        menores += 1

    elif idade >= 18:
        print('Maior de idade')
        maiores += 1

print(f'{cores['green']} Maiores de idade: {maiores} {cores['reset']},{cores['red']} Menores de idade: {menores}{cores['reset']}')
'''

'''
maior = 0
menor = 0

for pessoas in range(1, 4):
    pesos = float(input(f'Digite o {pessoas}° peso: '))

    if pessoas == 1:
        maior = pesos
        menor = pesos
    else:
        if pesos > maior:
            maior = pesos
        if pesos < menor:
            menor = pesos

print(f'O maior peso é: {cores["green"]}{maior}kg {cores["reset"]}')
print(f'O menor peso é: {cores["yellow"]}{menor}kg {cores["reset"]}')
'''

'''
somaidade = 0

for pessoas in range(1, 5):

    print(f'--------------PESSOA {pessoas}-------------')
    nome = str(input(f'Digite o seu nome: ')).strip()
    idade = int(input(f'Digite a sua idade: '))
    sexo = str(input(f'Sexo [M/F]: ')).strip()

    somaidade += idade
    mediaidade = somaidade/pessoas

print(f'{somaidade}{mediaidade}')
'''


