from datetime import datetime

dados = {}

# coloca dentro do dicionario
dados["nome"] = str(input("Digite o seu nome: "))

nasc = int(input("Ano de Nascimento: "))

dados["idade"] = datetime.now().year - nasc  # coloca dentro do dicionario

# coloca dentro do dicionario
dados["CTPS"] = int(input("Carteira de Trabalho (0 não tem): "))

if dados["CTPS"] != 0:
    dados["contratação"] = int(input('Ano de Contrataação: '))
    dados["salario"] = float(input("Salário R$ "))
    dados["aposentadoria"] = dados["idade"] + (dados["contratação"] + 35) - datetime.now().year
print(dados)

for k, v in dados.items():       # mostra o dicionario formatado
    print(f"- {k} tem o valor {v}")
