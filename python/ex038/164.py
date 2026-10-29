prod_preco = ('Maça', 2.0,
              'Banana', 2.0,
              'Laranja', 2.0)

linha = '=' * 40
print(f'{linha}')

for posicao in range(0, len(prod_preco)):
    if posicao % 2 == 0:
        print(f'{prod_preco[posicao]:.<30}', end=' ')
    else:
        print(f'R${prod_preco[posicao]:>7.2f}')

linha = '=' * 40
print(f'{linha}') 

