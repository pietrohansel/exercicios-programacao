# 19. Ordenação especial com variável de controle

i = int(input("Digite o valor de i: "))

a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

# crescente

if i == 1:

    if a <= b:    # a = menor
        if b <= c:   # c = maior
            print(a, b, c)

        else:  # b = maior
            if a <= c:  # a = menor
                print(a, c, b)
            else:
                print(c, a, b)  # c = menor

    else:
        if a <= c:
            print(b, a, c)

        else:
            if b <= c:
                print(b, c, a)
            else:
                print(c, b, a)


# decrescente

elif i == 2:

    if a >= b:
        if b >= c:
            print(a, b, c)

        else:
            if a >= c:
                print(a, c, b)
            else:
                print(c, a, b)

    else:
        if a >= c:
            print(b, a, c)

        else:
            if b >= c:
                print(b, c, a)
            else:
                print(c, b, a)


# meio

elif i == 3:

    if a >= b and a >= c:

        if b <= c:
            print(b, a, c)
        else:
            print(c, a, b)

    elif b >= a and b >= c:

        if a <= c:
            print(a, b, c)
        else:
            print(c, b, a)

    else:

        if a <= b:
            print(a, c, b)
        else:
            print(b, c, a)

else:
    print("Valor de i inválido")
