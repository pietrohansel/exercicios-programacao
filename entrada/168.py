lista = []
cont = 0

print(f"-=" * 40)

while True:
    valor = lista.append(int(input('Digite um número: ')))

    resposta = str(input('Quer continuar? [S/N]: ').upper().strip())
    if resposta in ("N"):
        break

    print(f"-=" * 40)

    lista.sort(reverse=True)
    cont += 1

    print(f'''{lista} | Contagem de números: {cont}''')

    if 5 in lista:
        print("O valor 5 está presente na lista")
    else:
        print("O valor 5 não está na lista")