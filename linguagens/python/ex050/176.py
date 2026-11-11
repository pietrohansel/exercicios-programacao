# 089.py

lista = []

while True:
    nome = str(input("Digite o seu nome: "))
    nota1 = float(input("Digite a sua primeira nota: "))
    nota2 = float(input("Digite a sua segunda nota: "))
    media = (nota1 + nota2)/2

    lista.append([nome, [nota1, nota2], media])

    pergunta = str(input("Quer continuar? [S/N]")).strip().upper()

    if pergunta in ("N"):
        break

print("=-" * 40)

print(f"{"NOTA":<4}   {"NOME":<5} {"MÉDIA":>8}")

print("=-" * 40)

for i, a in enumerate(lista):
    print(f"{i:<4}{a[0]:<5}{a[2]:>8.2f}")
