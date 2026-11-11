valor1 = float(input("Valor 1: "))
valor2 = float(input("Valor 2: "))
valor3 = float(input("Valor 3: "))


if valor1 and valor2 and valor3 != 0:
    
    if valor1 == valor2 and valor1 == valor3:
        print('Equilátero')

    elif valor1 != valor2 and valor1 == valor3:
        print("Isósceles")

    else:
        print("Escaleno")

