# 13. Preço total por código de produto


cod = int(input("Código: "))

total = quant = 0

prec1 = 10
prec2 = 20
prec3 = 30
prec4 = 40

if cod >= 1 and cod <= 4:
    quant = int(input("Quantidade: "))

if cod == 1:
    total = prec1 * quant

else:
    if cod == 2:
        total = prec2 * quant

    else:
        if cod == 3:
            total = prec3 * quant

        else:
            if cod == 4:
                total = prec4 * quant

            else:
                print(f"Código Inválido")

if total != 0:
    print(f"O valor total foi de R${total:.2f}")
