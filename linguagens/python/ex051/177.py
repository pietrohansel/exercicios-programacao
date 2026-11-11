from random import randint
from time import sleep
from operator import itemgetter

dados = {"jogador1": randint(1, 6),
         "Jogador2": randint(1, 6),
         "Jogador3": randint(1, 6),
         "Jogador4": randint(1, 6)}

print(f"Valores sorteados: {dados}")

for k, v in dados.items():
    print(f"{k} tirou {v}")
    sleep(1)

rank = sorted(dados.items(), key=itemgetter(1), reverse=True)

print(rank)
