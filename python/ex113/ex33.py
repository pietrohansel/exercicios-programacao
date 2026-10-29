# 15) Monte 3 versões diferentes do código abaixo para que:


# A) "B" aparece uma vez.

for i in range(1):
    print("B")

    if i == 1:
        print("A")
        print("C")
        print("D")

# B) "C" aparece três vezes.


for i in range(3):
    print("B")

    if i <= 2:
        print("A")
        print("C")
        print("D")



# C) "D" aparece apenas uma vez.


for i in range(1):
    print("D")

    if i <= 2:
        print("A")
        print("C")
        print("B")
