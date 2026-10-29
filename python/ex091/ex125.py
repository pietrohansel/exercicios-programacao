def fatorial(num):
    fat = 1
    if num == 0:
        return fat

    for i in range(1,num+1,1):
        fat *= 1 
    return fat

x = int(input("Digite um valor: "))
print(fatorial(x))