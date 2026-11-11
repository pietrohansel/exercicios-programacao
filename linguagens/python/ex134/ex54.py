# 15. Aumento de salário por cargo

cod = int(input("Código do cargo: "))

salario = float(input("Salário atual: "))

if cod == 101:
    novo_salario = salario + (salario * (10/100))

else:
    if cod == 102:
        novo_salario = salario + (salario * (20/100))

    else:
        if cod == 103:
            novo_salario = salario + (salario * (30/100))

        else:
            novo_salario = salario + (salario * (40/100))

diferenca = novo_salario - salario

print(f"""
Salário Antigo: R${salario:.2f}
Novo Salário: R${novo_salario:.2f}
Diferença: R${diferenca:.2f}
""")
