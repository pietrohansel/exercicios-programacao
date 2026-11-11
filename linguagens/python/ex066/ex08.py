# 8. Sequência de Collatz

n = int(input("Num: "))

cont = 0 

print(n)

while n != 1:

    if n % 2 == 0:
        n = n // 2 
        print(n)

    else:
        n = n * 3 + 1 
        print(n)

    cont += 1 

print(f"Contagem = {cont}")