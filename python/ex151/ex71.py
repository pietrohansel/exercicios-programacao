# 32. Comissão progressiva por produto

quant_prod = int(input("Quantidade de produtos: "))

comissão = 0 

if quant_prod == 250:
    comissão = quant_prod
else:
    if quant_prod >= 250 and quant_prod <= 500:
        comissão = quant_prod * 1.50
    else:
        if quant_prod > 500:
            comissão = quant_prod * 2.00

print(f"Quantidade vendida: {quant_prod}\nComissão = R${comissão}")
