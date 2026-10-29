# 8. Menor entre três números inteiros

n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))

if n1 < n2:
    if n1 < n3:
        print (f"Menor: {n1}")
    else:
        print (f"Menor: {n3}")
else:
    if n2 < n3:
        print(f"Menor: {n2}")
    else:
        print (f"Menor: {n3}")
        
