# 082
lista = []

pares = []

impares = []

print("-=" * 40)

while True:
    valores = (int(input("Digite um número: ")))
    
    reposta = str(input("Quer continuar? [S/N]: ")).strip().upper()
    if reposta in "N":
        break

    lista.append(valores)

    if valores % 2 == 0:
        pares.append(valores)
    else:
        impares.append(valores)
        
    print(f"Geral: {lista} | Pares = {pares} | Ímpares = {impares})")
    print("-=" * 40)
