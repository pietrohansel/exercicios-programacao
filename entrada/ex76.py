# 39. Menu de acesso a um cofre digital usando match case

print("\nCofre Digital")

print("\nEscolha uma forma de acesso:\n")

print('''1 - Acessar com biometria
2 - Acessar com login e senha
3 - Sair
''')

login_correto = "admin"
senha_correta = 1234

resp = int(input("Digite a opção desejada: "))

match resp:

    case 1:
        resp = input("Biometria reconhecida? [S/N]: ").lower().strip()

        if resp == "s":
            print("Acesso permitido. Cofre aberto.")

        else:
            print("Acesso negado. Biometria não reconhecida.")

    case 2:
        login = input("Login: ").lower().strip()

        if login == login_correto:

            senha = int(input("Senha: "))

            if senha == senha_correta:
                print("Acesso permitido. Cofre aberto.")

            else:
                print("Senha inválida.")

        else:
            print("Login inválido.")

    case 3:
        print("Sistema encerrado.")

    case _:
        print("Opção inválida.")