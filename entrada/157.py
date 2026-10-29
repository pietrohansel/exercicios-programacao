# Aula19.py

# Estrutura

dados = dict()
dados = {"nome": "Pedro", "idade": 34}

dados["sexo"] = "M"  # Adiciona um elemento

print(dados.values())  # Mostra apenas os valores -> Pedro, 34, M
print(dados.keys())  # Mostra apenas as chaves -> Nome, Idade , Sexo
print(dados.items())  # Mostra ambos

for k, v in dados.items():  # percorre todos os valores
    print(f"O {k} é {v}")
