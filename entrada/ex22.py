# 3) O programa abaixo identifica com um x todos os números ímpares de 0 a 4. 

for i in range(5):
    if i % 2 == 0:
        print(i)
    else:
        print("x")

print("fim")

""" 
-----------------------------------

A) Quantos blocos diferentes o programa tem? 

3 blocos 

-----------------------------------

B) Onde cada bloco começa? 

for, if e else 

-----------------------------------

C) Onde cada bloco termina? 

Linha 5, linha 3 e linha 5 

----------------------------------

D) Quais são os blocos do programa? 

-- 1° Bloco 

for i in range(5):
    if i % 2 == 0:
        print(i)
    else:
        print("x")

print("fim")

-- 2° Bloco 

if i % 2 == 0:
        print(i)

-- 3° Bloco 

else:
    print("x")

"""