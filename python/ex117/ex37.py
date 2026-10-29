
quantidade_lotes = int(input("Quantidade de lotes: "))

codigos_lotes = []

for i in range(quantidade_lotes):
    codigo = int(input("Código do lote: "))
    codigos_lotes.append(codigo)

for i in range(quantidade_lotes - 1):

    for j in range(quantidade_lotes - 1 - i):

        if codigos_lotes[j] > codigos_lotes[j + 1]:

            aux = codigos_lotes[j]

            codigos_lotes[j] = codigos_lotes[j + 1]
            
            codigos_lotes[j + 1] = aux

print(codigos_lotes)