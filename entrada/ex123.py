
# def letras (p1):
#     tam = len(p1)

#     if tam:
#         print('+',"-" * tam,'+')
#         print('|', p1,'|')
#         print('+',"-" * tam,'+')


# letras('Pietro')


# def validar(string, min, max):

#     x = input(string)
#     tam = len(x)

#     while tam< min or tam > max:
#         x = input(string)
#         tam= len(x) 
#     return x
    
# s1 = validar('Pietro', 10,30)

# while True:
#     try:
#         x = int(input("Numero: "))
#         break
#     except ValueError:
#         print("Numero invalido")

calc = lambda x,y: (x+5) * y   
 
print(calc(5,2))        


