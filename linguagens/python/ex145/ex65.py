# 26. Maior e menor entre dois números

num1 = float(input("Num1: "))
num2 = float(input("Num2: "))


if num1 == num2:
        print("Os dois números são iguais")
else:
    if num1 > num2:
        maior = num1
        menor = num2
    else:
        maior = num2
        menor = num1

    print(f"\nMaior: {maior}\nMenor: {menor}")





