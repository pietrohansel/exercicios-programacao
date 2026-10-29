# 18. Duração de um jogo em horas inteiras

hora_inicio = int(input("Hora de início: "))

hora_termino = int(input("Hora de término: "))

if hora_termino > hora_inicio:
    c = hora_termino - hora_inicio   
    print (f"Duração do jogo: {c:.2f} horas")

else: 
    d = (24 - hora_inicio) + hora_termino
    print (f"Duração do jogo: {d:.2f} horas")
