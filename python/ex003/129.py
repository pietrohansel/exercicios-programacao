# Aula 1

# Estrutura Aninhada --------------------------------------------------------------


'''
if

elif

elif

else
'''


# Prática  ------------------------------------------------------


'''
nome = str(input('Qual é o seu nome? '))

if (nome == 'Gustavo'):
    print('Que nome bonito')

elif (nome == 'Davi'):
    print('Que nome feio')

elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome')

else:
    print('Tenha um Bom dia!')
'''


# Exercícios -------------------------------------------------

'''
valor_casa = float(input('Qual é o valor da sua casa? R$ '))

salario_comprador = int(input('Qual é o seu salário? R$ '))

ano_de_pagamento = int(input('Em quantos anos vocẽ pretende pagar a casa? '))

limite = (salario_comprador*30/100)

prestacao_mensal = valor_casa / (ano_de_pagamento * 12)

if prestacao_mensal >= limite:
    print('O emnpréstimo será negado')
elif prestacao_mensal <= limite:
    print(f'O empreśtimo séra de: {valor_casa}')
'''

# --------------------------------------------------------------


'''cores = {'red': '\033[1;31m',
         'reset': '\033[m'}


numero_inteiro = int(
    input('Digite um número qualquer: '))

escolhe_binario = int(
    input('''

'''Digite:

 1 - binario,
 2 - octal,
 3 - hexadecimal,
 4 - Sair: '''


'''if escolhe_binario == 1:
    binario = bin(numero_inteiro)
    print(f'Essa é a conversão para binário: {binario[2:]} ')

elif escolhe_binario == 2:
    octal = oct(numero_inteiro)
    print(f'Esse é a conversão para octal: {octal[2:]}')

elif escolhe_binario == 3:
    hexadecimal = hex(numero_inteiro)
    print(f'Essa é a conversão para hexadecimal: {hexadecimal[2:]}')

else:
    print(f'Saindo')
'''

# -------------------------------------------------------------------------


'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))


if n1 > n2:
    print(f'O primeiro ({n1}) é maior')

elif n2 > n1:
    print(f'O segundo ({n2}) é maior')

else:
    print(f'Os valores são iguais')
'''


# ------------------------------------------------------------------------------------------

'''
from datetime import date
ano_nascim = int(input('Qual é o seu ano de nascimento? '))

ano_atual = date.today().year

idade = ano_atual-ano_nascim

if idade < 18:

    saldo = 18-idade
    ano = ano_atual+saldo
    print(
        f'Você tem {idade} anos e terá que se alistar daqui a {saldo} anos em {ano}')

elif idade > 18:
    saldo = idade - 18
    ano = ano_atual - saldo
    print(f'Vocẽ tem {idade} anos e deveria ter se alistado em {ano}')

else:
    print(f'Você tem {idade} e deve se alistar IMEDIATAMENTE')
200
'''

# ------------------------------------------------------------------------------------------

'''
# entrada

a = int(input('Digite o valor do primeiro segmento de reta: '))

b = int(input('Digite o valor do segundo segmento de reta: '))

c = int(input('Digite o valor do terceiro segmento de reta: '))

# processamento

if a + b > c and a + c > b and b + c > a:

    if a == b == c:
        print ('Triângulo equilátero')
    elif a!=b and a!=c and b!=c:
        print ('Triângulo escaleno')
    else:
        print ('Triângulo isósceles')
else:
    print ('Não é possível formar um triângulo')
'''


# ------------------------------------------------------------------------------------------

'''
peso = float(input('Digite seu peso: '))

altura = float(input('Digite sua altura: '))

imc = peso/(altura**2)

if peso

    if imc < 18.5:
        print('Abaixo do peso')
    elif  18.5 <= imc < 25:
        print('Peso ideal')
    elif 25 <= imc < 40:
        print('Sobrepeso')
    elif 30 <= imc < 40:
        print('Obesidade')
    elif imc > 40:
        print('Obesidade mórbida')
'''
# ------------------------------------------------------------------------------------------
'''
cores = {'red': '\033[1;31m',
         'green': '\033[1;32m',
         'reset': '\033[m'}

print(f"{cores['red']}Loja Pietro{cores['reset']}")
valor = float(input('O valor a ser pago é: '))
'''
'''
'''
#escolhe = int(input('''
#Método de pagamento

##2] - Cartão à vista
#[3] - 3x ou mais
#'##''))''''''
'''
if escolhe == 1:
    total = valor - (valor * 0.10)
    print(f'Total com desconto: R$ {total:.2f}')

elif escolhe == 2:
    total = valor - (valor * 0.05)
    print(f'Total com desconto: R$ {total:.2f}')

elif escolhe == 3:
    vezes = int(input('Em quantas vezes? '))

    if vezes >= 3:
        total = valor + (valor * 0.20)
        parcela = total / vezes

        print(f'{cores['green']}{vezes}x{cores["reset"]}')
        print(f'Total com juros: R$ {total:.2f}')
        print(f'{vezes}x de R$ {parcela:.2f}')
    else:
        print('Parcelamento mínimo é 3x')

else:
    print('Opção inválida')
'''
