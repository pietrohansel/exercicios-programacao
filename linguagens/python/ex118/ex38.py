# 37. Verificação de idade para votar

ano_atual = int(input("Digite o ano atual: "))

ano_nasc = int(input("Digite o seu ano de nascimento: "))

idade = ano_atual - ano_nasc

if idade < 16:
    print("Não possui idade suficiente votar")

else:
    print("Já possui idade suficiente para votar")