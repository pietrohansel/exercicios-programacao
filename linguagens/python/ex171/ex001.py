menu = print("1 - Maçã / R$2,30\n2 - Laranja / R$3,60\n3 - Banana / R$1,85")

escolha = int(input("Escolha um número: "))
produto = preco = 0 

while escolha == 0:
    match escolha:
        case 1:
            produto = "Maçã"
            preco = 2.30
            break
        case 2: 
            produto = "Laranja"
            preco = 3.06
            break
        case 3:
            produto = "Banana"
            preco = 1.85
            break
        case _:
            print("Opção indisponível")
            continue

qtd = int(input("Qtd: "))

total = preco * qtd
print(total)