# 21. Preço das maçãs

maca = int(input("Quantidade de Maçãs: "))

if maca < 12:
    maca = 1.30 * maca
    print (f"Preço: R${maca:.2f}")
else:
    maca = 1 * maca
    print (f"Preço: R${maca:.2f}")
