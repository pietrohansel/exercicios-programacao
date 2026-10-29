# 34. Data com mês por extenso

dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

if dia < 1 or dia > 31:
    print("Dia inválido")

else:
    if mes < 1 or mes > 12:
        print("Mês inválido")

    else:
        if mes == 2:
            if dia > 28:
                print("Fevereiro só tem 28 dias")

            else:
                mes = "Fevereiro"

        else:
            if mes == 1:
                mes = "Janeiro"

            else:
                if mes == 3:
                    mes = "Março"

                else:
                    if mes == 4:
                        mes = "Abril"

                    else:
                        if mes == 5:
                            mes = "Maio"

                        else:
                            if mes == 6:
                                mes = "Junho"

                            else:
                                if mes == 7:
                                    mes = "Julho"

                                else:
                                    if mes == 8:
                                        mes = "Agosto"

                                    else:
                                        if mes == 9:
                                            mes = "Setembro"

                                        else:
                                            if mes == 10:
                                                mes = "Outubro"

                                            else:
                                                if mes == 11:
                                                    mes = "Novembro"

                                                else:
                                                    mes = "Dezembro"

        print(f"{dia} de {mes} de {ano}")