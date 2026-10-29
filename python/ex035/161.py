while True:
    sexo = input("Digite seu sexo: [M/F] ").strip().upper()

    if sexo != "M" and sexo != "F":
        print("Digite novamente:")
    else:
        print("Dados válidos")
        break