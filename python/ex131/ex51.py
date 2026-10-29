# 12. Crédito bancário

saldo = float(input("Digite seu saldo: "))


if saldo <= 0:
    print ("Saldo Inválido")

else:
    if saldo >= 0 and saldo <= 200:
        credito = 0

    else:
        if saldo >= 201 and saldo <= 400:
            credito = saldo * (20/100)

        else:
            if saldo >= 401 and saldo <= 600:
                credito = saldo * (30/100)

            else:
                credito = saldo * (40/100)

    print (f"Saldo Médio: R${saldo:.2f}")
    print (f"O valor do cŕedito será de R${credito:.2f}")
