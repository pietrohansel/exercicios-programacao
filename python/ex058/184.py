# F-Strings

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
