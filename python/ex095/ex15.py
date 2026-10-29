# 15. Potência sem usar operador de potência

base = int(input("Digite a base: "))

expoente = int(input("Digite o expoente: "))

potencia = 1 

for i in range(1, expoente+1):
    potencia = potencia * base

print(potencia)

