'''
pessoas = ['João', 'Pietro', 'Eduardo', 'Zé']
dados = [1, 2, 3, 4]

pessoas.append(dados[:])

# lista dentro de outra lista

# 0             #1            #2               #3
pessoas = [['João', 1], [' Pietro', 2], ['Eduardo', 3], ['Zé', 4]]

print(pessoas)

print(pessoas[0][0])

print(pessoas[1])

galera = list()
dado = list()

for dado in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade')))
    galera.append(dado[:])
    dado.clear()

print(galera)
'''