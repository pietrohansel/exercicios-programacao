# 4. Média aritmética de três notas

n1 = float(input("Nota1: "))
n2 = float(input("Nota2: "))
n3 = float(input("Nota3: "))

media = (n1+n2+n3)/3

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")