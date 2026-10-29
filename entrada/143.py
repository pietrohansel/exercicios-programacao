
# Aula 7


cores = {'red': '\033[1,31m',
         'green': '\033[1,32m',
         'reset': '\033[m'}


# Exercício 1 ------------------------------------------------------

numeroaleatorio = int(input(f'Digite um número: '))

dobro = (numeroaleatorio*2)
triplo = (numeroaleatorio*3)
raiz = (numeroaleatorio**(1/2))

print(
    f'Dobro: {cores["green"]}{dobro}, Triplo: {triplo} e Raiz {raiz} {cores["reset"]}')


# Exercício 2 ------------------------------------------------------


nota1 = int(input('Digite sua nota: '))
nota2 = int(input('Digite sua outra nota: '))
media = (nota1+nota2/2)

print(f'Essa é sua média {cores["green"]}{media}')


# Exercício 3 ------------------------------------------------------


valor_em_metros = int(input('Escreva sua medida em metro: '))
conversao_para_cm = (valor_em_metros*100)
conversao_para_mm = (valor_em_metros*1000)

print(
    f'Esse é seu valor convertido em cm: {conversao_para_cm}cm, esse é em mm: {conversao_para_mm}')


# Exercício 4 ------------------------------------------------------


numero_aleatorio = int(input('Digite um número: '))

x0 = numero_aleatorio*0
x1 = numero_aleatorio*1
x2 = numero_aleatorio*2
x3 = numero_aleatorio*3
x4 = numero_aleatorio*4
x5 = numero_aleatorio*5
x6 = numero_aleatorio*6
x7 = numero_aleatorio*7
x8 = numero_aleatorio*8
x9 = numero_aleatorio*9
x10 = numero_aleatorio*10

print(f'{numero_aleatorio} x 0 = {x0}')
print(f'{numero_aleatorio} x 1 = {x1}')
print(f'{numero_aleatorio} x 2 = {x2}')
print(f'{numero_aleatorio} x 3 = {x3}')
print(f'{numero_aleatorio} x 4 = {x4}')
print(f'{numero_aleatorio} x 5 = {x5}')
print(f'{numero_aleatorio} x 6 = {x6}')
print(f'{numero_aleatorio} x 7 = {x7}')
print(f'{numero_aleatorio} x 8 = {x8}')
print(f'{numero_aleatorio} x 9 = {x9}')
print(f'{numero_aleatorio} x 10 = {x10}')
