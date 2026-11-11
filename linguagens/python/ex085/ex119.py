

# for i in range(1, 11, 1):
#     print(f'\nTabuada do {i}')

#     for j in range(1, 11, 1):
#         operacao = i * j
#         print(f'{i} x {j} = {operacao}')


# k = 1

# while k <= 10:
#     print(f'\nTabuada do {k}')
#     l = 1

#     while l <= 10:
#         print(f'{k} x {l} = {k * l}')
#         l += 1
#     k += 1



tabuada = 1 

while tabuada <= 10:
    print(f'\nTabuada do {tabuada}')
    num = 1

    for i in range(1,11,1):
        print(f'{tabuada} x {num} = {tabuada * num}')
        num +=1 

    tabuada += 1 
