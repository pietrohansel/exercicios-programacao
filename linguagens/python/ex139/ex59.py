# 20. Duração de jogo em horas e minutos

hora_inicial = int(input("Hora inicial: "))
minuto_inicial = int(input("Minuto inicial: "))
hora_final = int(input("Hora final: "))
minuto_final = int(input("Minuto final: "))

inicio = hora_inicial * 60  + minuto_inicial
fim = hora_final * 60 + minuto_final

if fim < inicio:
    fim += 24 * 60

duracao = fim - inicio

h = duracao // 60
m = duracao % 60

print(f"{h} horas e {m} minutos")
