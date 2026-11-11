# 18) Uma pessoa esqueceu a senha de seu login. Faça um programa que pergunte uma senha até que o usuário digite: python123. 

# Quando acertar mostre: senha correta 

# Restrições: Usar obrigatoriamente a estrutura while 

senha = input("Digite a senha: ")

senha_correta = "python123"

while senha != senha_correta:
    senha = input("Digite a senha novamente: ")

print("Acesso liberado!", senha_correta)