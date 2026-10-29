cod = input("Digite o código do produto: ")
quant = int(input("Digite a quantidade: "))

preco = 0 

if cod == "ABCD":
    preco = 12 * quant
else:
    if cod == "XYPK":
        preco = 25 * quant
    else:
        if cod == "KLMP":
            preco = 32 * quant
        else:
            if cod == "QRST":
                preco = 40 * quant
            else:
                print("Código Inválido")
                
if preco != 0:
    print(f"Valor total: R${preco:.2f}")
