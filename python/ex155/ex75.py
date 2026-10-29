# 36. Média de quatro notas com conceito

n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
n4 = float(input("Quarta nota: "))

media = (n1 + n2 + n3 + n4) / 4
conceito = 0 

if media < 3:
    conceito = "R"
else:
    if media >= 3 and media < 7:
        conceito = "E"
    else:
        if media >= 7:
            conceito = "A"

print(f"Média: {media:.2f}\nConceito: {conceito}")