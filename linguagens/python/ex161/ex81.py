
def tributar():
    preco = float(input('Preço: '))
    custo = float(input('Custo: '))
    carga_tributaria = (preco - custo) / preco * 100
    return carga_tributaria

result = tributar()
print(f'Porcentagem do tributo: {result:.2f}%')
