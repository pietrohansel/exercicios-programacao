cores = {
    'red': '\033[1;31m',
    'reset': '\033[m'
}

lista = []

print('=' * 40)

for val in range(0, 5):
    lista.append(int(input('Digite um número: ')))

for cont, val in enumerate(lista):
    print(f'Posição = {cont} | Valor = {val}')

print('=' * 40)

print(
    f"MAIOR = {cores['red']}{max(lista)}{cores['reset']} MENOR = {min(lista)}")
