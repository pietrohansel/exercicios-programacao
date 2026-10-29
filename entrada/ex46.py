# 7. Classificação de nadador por idade

idade = int(input("Digite sua idade: "))

if idade >= 5 and idade <= 7:
    print ("Infantil A")
else:
    if idade >= 8 and idade <= 10:
        print ("Infantil B")
    else:
        if idade >= 11 and idade <= 13:
            print ("Juvenil A")
        else:
            if idade >= 14 and idade <= 17:
                print ("Juvenil B")
            else:
                print ("Adulto")