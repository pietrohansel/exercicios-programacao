# Aula 4

# Estrutura

'''cont = 1
while cont <= 10:
    print(cont, ' ', end='')
    cont += 1
print('acabou')
'''
'''
numero = cont = soma = 0

# Sem contador

while numero != 9999:
    numero = int(input('Digite novamente'))

print('FIM')

# Com contador

while cont < 10:
    numero = int(input('Digite um numero: '))
    cont += 1
print('FIM')


#Infinita com Stop

while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
print(f'A soma vale: {soma}')
'''

# Exerícios

'''ler_numeros = contador = soma = 0

while True:

    ler_numeros = int(input('Digite um número: '))

    if ler_numeros == 999:
        break
    soma += ler_numeros

print(f'A soma vale: {soma}')'''

'''number = 0


while True:
    number = int(input('Digite um número: '))

    if number <= 0:
        break

    for tabuada in range(1, 11):
        print(f'{number} x {tabuada} = {number*tabuada}')

print('FIM')
'''

'''
from random import randint

numero_pc = 0
contador = 1

escolhe = str(input('Par ou Ímpar? [P/I]: ')).strip().lower()


while True:

    numero_jogador = int(input('Digite seu número: '))
    numero_pc = randint(1, 9)

    soma = numero_jogador + numero_pc

    print(f'Conputador = {numero_pc} , Você = {numero_jogador}')

    print(f'A soma dos valores foi {numero_jogador} + {numero_pc} = {soma}')

    if soma % 2 == 0:
        resultado = 'p'
    else:
        resultado = 'i'

    if resultado == escolhe:
        print (f'Você venceu - Vitórias = {contador}')
        contador += 1

    else:
        print('Voce perdeu')
        break
'''

contador_maiores_de_idade = contador_homens = contador_mulheres = 0


while True:

    nome = str(input('Digite o seu nome: '))
    idade = int(input('Digite sua idade: '))

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    print(f'Nome: {nome}, Idade: {idade} e Sexo: {sexo}')

    if idade >= 18:
        contador_maiores_de_idade += 1

    if sexo == 'M':
        contador_homens += 1

    elif sexo == 'F':
        contador_mulheres += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    print(f'''
           
           18+ = {contador_maiores_de_idade}
           Homens = {contador_homens} 
           Mulheres {contador_mulheres}
            
            ''')

    if continuar == 'N':
        print('FIM')
        break
