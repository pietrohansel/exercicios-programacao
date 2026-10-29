lista = []

print('=' * 40)

while True:

    n = int(input('Digite um número: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado')

    else:
        print('Valor duplicado')

    r = str(input('Quer continuar? [S/N] ')).strip().upper()

    if r in 'Nn':
        break

print('=' * 40)

lista.sort
print(f'{lista}')

print('=' * 40)
