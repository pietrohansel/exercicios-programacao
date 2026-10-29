preco = float(input("Digite o preco: "))

desconto = float(input("Desconto: [0/100%]"))

desconto_aplicado = (desconto * preco) / 100

print(f'Valor com desconto: {desconto_aplicado}')

