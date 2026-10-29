# 16. Sequência de Fibonacci

n = int(input("Digite um número: "))

anterior = 0
atual = 1 
proximo = 0 

print(anterior)

for i in range(1, n):
    print(atual)
    proximo = anterior + atual
    anterior = atual
    atual = proximo
