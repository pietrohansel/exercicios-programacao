# 28. Pessoa mais nova

ano_nasc1 = int(input("Ano de nascimento1: "))

ano_nasc2 = int(input("Ano de nascimento2: "))


if ano_nasc1 == ano_nasc2:
    print("Ambas possuem a mesma idade aproximadamente")

else:

    if ano_nasc1 > ano_nasc2:
        menor = ano_nasc1
        pessoa = 1

    else:
        menor = ano_nasc2
        pessoa = 2

    print(f"\nPessoa {pessoa} possui a menor idade")
    print(f"Ano: {menor}")