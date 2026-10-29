# 16. Verificação de triângulo e cálculo de área

v1 = float(input("Digite um valor: "))
v2 = float(input("Digite um valor: "))
v3 = float(input("Digite um valor: "))


if v1 + v2 > v3 and v1 + v3 > v2 and v2 + v3 > v1:
    x = print("É possivel formar um triângulo")

    p = (v1 + v2 + v3) / 2

    area = (p * (p-v1) * (p-v2) * (p-v3)) ** (1/2)

    print(f"Área: {area:.2f}")

else:
    x = print("Não é possivel formar um triângulo")
