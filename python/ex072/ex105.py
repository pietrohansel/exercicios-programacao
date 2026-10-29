import itertools
from itertools import count, cycle, repeat, accumulate

# i = 0

# e = dir(i)  visualiza os metodos usados
# print(e)

# help(int.__add__)

# iteráveis possuem next, iter

# numeros = [1, 2, 3, 4, 5]

# z = [numero**2 for numero in numeros]

# print(z)


# quadrado = map(lambda x: x**2, numeros)
# print(quadrado)

# quadrado = list(map(lambda x: x**2, numeros))
# print(quadrado)

# x = [1, 2, 3, 4]

# for i in x:
#     print(i)

# # Count
# x = count(1, 2)
# print(x)

# # Cicle 
# x = cycle('abc')
# print(next(x))
# print(next(x))
# print(next(x))
# print("---------")
# print(next(x))
# print(next(x))
# print(next(x))

# # Repeat
# x = repeat(10,3)
# print(x)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


#Accumulate
x = list(accumulate([1,2,3,4,5]))
print(x)

