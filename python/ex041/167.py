numeros = []

print('=-' * 40)


for valores in range(0, 5):

    v = (int(input('Digite um número: ')))

    if valores == 0 or valores > numeros[-1]:
        numeros.append(v)

    else:
        pos = 0
        while pos < len(numeros):
            if v <= numeros[pos]:
                numeros.insert(pos, v)
                break
            pos += 1

print('=-' * 40)

print(numeros)
