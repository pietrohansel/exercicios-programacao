# 2. Validação de senha com tentativas limitadas

senha_correta = 'python123'
tentativas = 1
acesso_permitido = False

senha = input('Digite a senha: ')

while tentativas <= 3 and acesso_permitido == False:

    if senha == senha_correta:
        acesso_permitido = True

    else:
        senha = input('Digite a senha: ')
        
if acesso_permitido == True:
    print('Acesso permitido')
else:
    print('Acesso negado')