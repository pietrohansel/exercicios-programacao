# aula21.py

# help(print)

# print(input.__doc__)

# Dockstring

# def contador(i, f, p):
#     """
#     i = início
#     f = fim
#     p = passo
#     """
#     c = i
#     while c <= f:
#         print(c)


# help(contador)

# Parametros opcionais

# def somar (a=0,b=0,c=0):
#     s= a+b+c
#     print (s)

# somar(1,100,10)
# somar()

# # Escopo local

# def teste(valores):
#     aqui_dentro = 0 
#     valores = aqui_dentro
#     global a



# a = "A = global "

# Return

def somar (a,b,c):
    s = a+b+c
    return s

print(somar(1,2,3))

def fatorial (num=1):
    f = 1
    for c in range(num,0,-1):
        f *= c
    return f 

fatorial(4)