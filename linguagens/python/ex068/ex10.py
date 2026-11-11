# 10. Simulação de crescimento populacional

cidadeA = 80_000 

cidadeB = 200_000

anos = 0 

while cidadeA < cidadeB:
    cidadeA = cidadeA + cidadeB * 0.03
    cidadeB = cidadeB + cidadeA * 0.015
    anos += 1 


print(anos)