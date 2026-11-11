# 35. Cardápio de lanchonete

print('''\nTabela\nCódigo 100: Cachorro-quente — R$ 12,00\nCódigo 101: Bauru simples — R$ 15,00\nCódigo 102: Bauru com ovo — R$ 18,00\nCódigo 103: Hambúrguer — R$ 20,00\nCódigo 104: Cheeseburguer — R$ 22,00\nCódigo 105: Refrigerante — R$ 7,00\n''')


cod = int(input("Digite o seu código: "))

if cod < 100 or cod > 105:
    print("Código inválido")

else:
    quant = int(input("Digite a quantidade comprada: "))

    if cod == 100:
        total = quant * 12

    else:
        if cod == 101:
            total = quant * 15

        else:
            if cod == 102:
                total = quant * 18

            else:
                if cod == 103:
                    total = quant * 20

                else:
                    if cod == 104:
                        total = quant * 22

                    else:
                        total = quant * 7

    print(f"Valor total do pedido: R${total:.2f}")
