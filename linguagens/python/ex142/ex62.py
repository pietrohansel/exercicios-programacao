# 23. Cálculo com idades de homens e mulheres

homem1 = int(input("Idade homem 1: "))
homem2 = int(input("Idade homem 2: "))

mulher1 = int(input("Idade mulher 1: "))
mulher2 = int(input("Idade mulher 2: "))

if homem1 > homem2:
    homem_mais_velho = homem1
    homem_mais_novo = homem2

else:
    homem_mais_velho = homem2
    homem_mais_novo = homem1


if mulher1 < mulher2:
    mulher_mais_nova = mulher1
    mulher_mais_velha = mulher2


else:
    mulher_mais_nova = mulher2
    mulher_mais_velha = mulher1

soma_homem_velho_mulher_nova = homem_mais_velho + mulher_mais_nova

multiplica_homem_novo_mulher_velha = homem_mais_novo * mulher_mais_velha

print(f'''\nhomem velho + mulher nova: {soma_homem_velho_mulher_nova}\nhomem novo x mulher velha: {multiplica_homem_novo_mulher_velha}''')
