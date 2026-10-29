# 38. Conversão de nota numérica em grau

nota = int(input("Digite sua nota: "))

conversao = ""

if nota <= 0 or nota > 100:
    print("Nota inválida")

else:
    if nota >= 50 and nota <= 59:
        conversao = "Grau E"

    else:
        if nota >= 60 and nota <= 69:
            conversao = "Grau D"

        else:
            if nota >= 70 and nota <= 79:
                conversao = "Grau C"

            else:
                if nota >= 80 and nota <= 89:
                    conversao = "Grau B"

                else:
                    if nota >= 90 and nota <= 100:
                        conversao = "Grau A"

    print(f"Nota em graus: {conversao}")
