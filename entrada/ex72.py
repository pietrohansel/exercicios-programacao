# 33. Menu de fast food


print("\nLanchonete\n\n1. X-Burger + Refrigerante: R$ 18,00\n2​. X-Salada + Suco: R$ 22,00\n3. Hot Dog + Refrigerante: R$ 15,00\n4. Combo Família: R$ 50,00\n")

pedido = int(input("Escolha seu pedido: "))

nome_pedido = ""
total = 0

if pedido > 4 or pedido <1:
    print ("Opção inválida")

else:
    quant = int(input("Quantidade: "))
    
    if pedido == 1:
        nome_pedido = "X-Burger + Refrigerante: R$ 18,00"
        total = 18.00 * quant

    else:
        if pedido == 2:
            nome_pedido = "X-Salada + Suco: R$ 22,00"
            total = 22.00 * quant

        else:
            if pedido == 3:
                nome_pedido = "Hot Dog + Refrigerante: R$ 15,00"

                total = 15.00 * quant
            
            else:
                if pedido == 4:
                    nome_pedido = "Combo Família: R$ 50,00"
                    total = 50.00 * quant

    print (f"\nPedido: {nome_pedido}\n\nQuantidade: {quant}\n\nPreço final: R${total:.2f}")



