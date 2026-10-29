# 22. Resultado de uma partida de futebol

time1 = input("Nome do time: ")
gols1 = int(input("Gols: "))

time2 = input("Nome do time: ")
gols2 = int(input("Gols: "))


if gols1 > gols2:
    print (f"Vencedor: {time1}")
    
else:
    print (f"Vencedor: {time2}")
    
    if gols1 == gols2:
        print ("Empate")
