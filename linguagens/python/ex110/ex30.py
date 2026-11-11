# 11) Reorganize as linhas dos códigos abaixo para que eles façam como pedido:

# A) Escrever os números de 1 a 4 e ao final escrever Fim. 

for i in range(5):
    print(i)

print("Fim")

# B) Se a idade for menor que 18 anos, escrever Maior, caso contrário escrever Menor. 

idade = 11

if idade >= 18:
    print("Maior")

else:
    print("Menor")

# C) Verificar se o número é positivo ou negativo 

numero = int(input(" "))

if numero >= 0:
    print("Positivo")

else:
    print("Negativo")

# D) Escrever todos os números pares de 1 a 10. 


for i in range(1,11):
    if i % 2 == 0:
        print(i)

print("Fim")

# E) Criar um menu que pede opções do usuário quando ele digitar 1 e sair quando ele digitar 0.

opcao = int(input(" "))

while opcao != 0:
    if opcao == 1:
        print("Cadastrar")

    else:
        print("Opção inválida")

    opcao = int(input(" "))

# F) Fazer uma contagem regressiva. 

contador = 5 

print("Lançamento")

while contador > 0:
    contador -= 1 
    print(contador)  