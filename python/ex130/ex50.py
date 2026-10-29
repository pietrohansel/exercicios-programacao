# 11. Menu de médias

print("-="*30)

n1 = float(input("Nota1: "))
n2 = float(input("Nota2: "))
n3 = float(input("Nota3: "))

print("-="*30)

print ("[1] Média Aritmética\n[2] Média Ponderada\n[3] Média Harmônica")

print("-="*30)

resp = int(input("Escolha qual tipo de média deseja calcular: "))

if resp == 1:
    media_arit = (n1+n2+n3) / 3
    print (f"Média Aritmética: {media_arit:.2f}")

else:
    if resp == 2:
        media_pond = (n1*3 + n2*3 + n3*4) / 10
        print(f"Média Ponderada: {media_pond:.2f}")

    else:
        if resp == 3:
            if n1 == 0 or n2 == 0 or n3 == 0:
                print("Não é possível calcular média harmônica com nota 0")
            else:
                media_harm = 3 / (1/n1 + 1/n2 + 1/n3)
                print (f"Média Harmônica: {media_harm:.2f}")
        else:
            print("Opção Inválida")

