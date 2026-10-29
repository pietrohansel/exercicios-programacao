# 9. Média ponderada de um aluno

cod = input("Digite o seu código: ")
n1 = float(input("Digite sua primeira nota: "))  # 4
n2 = float(input("Digite sua segunda nota: "))  # 3
n3 = float(input("Digite sua terceira nota: "))  # 3

media = (n1*4 + n2*3 + n3*3) / 10

print(f"""
Código: {cod}         \n  
Primeira nota: {n1}   \n      
Segunda nota: {n2}    \n      
Terceira nota: {n3}   \n 
Média final: {media:.2f}  \n      """)

if media >= 5:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")
