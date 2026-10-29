# 27. Pessoa mais pesada

nome1 = (input("Nome1: "))
nome2 = (input("Nome2: "))

peso1 = float(input("Peso1: "))
peso2 = float(input("Peso2: "))

if peso1 == peso2:
    print ("Ambas possuem o mesmo peso")

else:
    if peso1 > peso2:
        pessoa = nome1
        maior = peso1
    else:
        pessoa = nome2
        maior = peso2
    

    print (f"Pessoa: {pessoa}\nPeso: {maior}kg")