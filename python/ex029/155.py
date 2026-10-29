# Conceito

'''
lanche = ["banana", "maça"]

lanche = [1] = 'uva'

lanche.append('pera') # Adiciona um elemento na lista

lanche.insert(0, 'chia')
'''
# Deleta o elemnto da lista e refaz a ordem

'''
del lanche[1]
lanche.pop(0)
lanche.remove("maça")

if 'banan' in lanche:
    lanche.remove('banana')
'''

'''
valores = list(range(4, 11))
print(valores)
'''

# Organiza a lista

'''
valores = [3, 5, 6, 3, 2, 7]

valores.sort(reverse=True)

print(valores)
'''
'''

num.append(7)  # Insere um elemento na lista
num.insert(5, 4)  # Insere um elemento na quinta posição

print(num)
'''

'''
num = []

for cont in range(0, 5):  # Adicione entradas a lista
    num.append(int(input('Digite um valor: ')))


for c, v in enumerate(num):  # Mostra a posição na lista
    print(f'Na posição {c} encontrei o valor {v}')
'''
'''
a = [1, 2, 3, 4]
b = a

b = a[:]  # altera a

b[3] = 5  # cria uma ligação com a

print(a)
print(b)()
'''