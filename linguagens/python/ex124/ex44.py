# 5. Maior entre três valores

v1 = float(input("Valor 1: "))
v2 = float(input("Valor 2: "))
v3 = float(input("Valor 3: "))

if v1 > v2:
    if v1 > v3:
        print(f"{v1} é o maior.")
    else:
        print(f"{v3} é o maior.")
else:
    if v2 > v3:
            print(f"{v2} é o maior.")
    else:
         print(f"{v3} é o maior.")
