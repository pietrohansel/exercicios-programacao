# Conceito

print("3"+"3")  # junta os números

x = 2/2  # disão com casas decimais
print(x)

x = 2//2 # divisão sem a parte inteira
print(x)

x = 2%2 # calcula o resto da divisão

_n1 = 2 # variável pode iniciar com undescore

'ASCII' # norma de codificação

      #012345678910  -> índices 
print("Olá, Mundo")

# f-string antiga 1
nota = 8.5
s1 = "Você tirou %f na disciplina de Algoritmos" % nota
print (s1)

# f-string antiga 2
nota = 8.5
s1 = "Você tirou {} na disciplina de Algoritmos" .format(nota)
print (s1)

#f-strig 3 - Atual/Melhor
nota = 8.5
s1 = (f"Você tirou {nota} na disciplina de Algoritmos")
print (s1)