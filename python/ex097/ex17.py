# 17. Média de N alunos

quant_alunos = int(input("Quantidade de alunos: "))

soma = aprovados = 0

menor = maior = media = 0 


for i in range(1,quant_alunos+1):
    nota = float(input("Nota: "))

    soma += nota

    if i == 1:
        maior = nota 
        menor = nota

    else:
        if nota < menor:
            menor = nota 

        else:
            maior = nota

    if nota >= 6:
        aprovados += 1 

media = soma /quant_alunos

print(f"Media = {media}")
print(f"Maior = {maior}")
print(f"Menor = {menor}")
print(f"Aprovados = {aprovados}")