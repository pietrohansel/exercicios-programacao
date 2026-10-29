# pessoas = {"nome": "Gustavo", "sexo": "M", "idade": 18}

# print(pessoas["nome"])
"""
for k, v in pessoas.items():
    print(f"{k} = {v}")

brasil = []
estado1 = {"UF": "Rio de Janeiro", "Sigla": "RJ"}
estado2 = {"UF": "Minas Gerais", "Sigla": "MG"}

brasil.append(estado1)
brasil.append(estado2)

print(brasil[0])
print(brasil[1])
print(brasil[1]["UF"])
"""

estado = dict()
brasil = list()

for c in range(0, 3):
    estado["UF"] = str(input("Unidade Federativa: "))
    estado["Sigla"] = str(input("Sigla do Estado: "))
    brasil.append(estado.copy()) # copy faz uma copia de um elemento
print(brasil)
