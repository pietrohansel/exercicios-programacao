# 25. Índice de poluição

indice_poluicao = float(input("Indice de Poluição: "))

if indice_poluicao >= 0.5:
            print(" As indústrias dos grupos 1,2 e 3 devem paralisar suas atividades.")
else:
    if indice_poluicao >= 0.4:
        print(" Notifique as indústrias dos grupos 1 e 2")

    else:
        if indice_poluicao >= 0.3:
            print(" Notifique as indústrias do grupo 1")

        else:
            print("Nível dentro do aceitável")
    


