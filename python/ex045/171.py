lista = []
maior = menor = 0

while True:
    nome = str(input('Digite o seu nome: '))
    peso = float(input('Digite o seu peso: '))

    lista.append([nome, peso])

    if len(lista) == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

    resp = str(input('Você quer continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break

print(f'\nForam cadastradas {len(lista)} pessoas')

print(f'O maior peso foi: {maior}')
for p in lista:
    if p[1] == maior:
        print(f'Pessoa mais pesada: {p[0]}')

print(f'O menor peso foi: {menor}')
for p in lista:
    if p[1] == menor:
        print(f'Pessoa mais leve: {p[0]}')
