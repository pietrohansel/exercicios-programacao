# 7. Algoritmo de Euclides para MDC

nA = int(input("Num1: "))
nB = int(input("Num1: "))

cont = 0 

while nB != 0:

    rA = nA % nB
    nA = nB
    nB = rA

print(f"MDC = {nA}")
