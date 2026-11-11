# 24. Média de aproveitamento e conceito

soma_notas = 0 
quant_notas = 0 

while True:
    nota = int(input("Nota: "))
    soma_notas += nota
    quant_notas += 1 

    resp = input("Quer continuar [S/N]: ").upper().strip()


    if resp == "N":

        media = soma_notas/quant_notas

        if media >= 9:
            conceito = "A"

        else:
            if media >= 7.5 and media < 9:
                conceito = "B"

            else:
                if media >= 6 and media < 7.5:
                    conceito = "C"

                else:
                    if media >= 4 and media < 6:
                        conceito = "D"

                    else:
                        conceito = "E"


        print (f"{conceito}")
        break

    