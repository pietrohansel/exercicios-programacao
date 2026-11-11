def cadastrar(nomeArquivo, nomeItem):
    try:
        with open(nomeArquivo, 'at') as a:
            a.write(nomeItem + '\n')
    except:
        print('Erro ao abrir o arquivo')


def listar(nomeArquivo):
    try:
        with open(nomeArquivo, 'rt') as a:
            print(a.read())
    except:
        print("Erro ao ler o arquivo")


def existeArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'rt'):
            pass
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'wt+'):
            pass
    except:
        print('Erro na criação')
    else:
        print("Arquivo criado")


arquivo = 'itens.txt'

if existeArquivo(arquivo):
    print('Existe')
else:
    print('Não existe')


print('\n1 - Cadastrar item\n2 - Listar itens\n3 - Sair')

while True:

    opcao = int(input("\nSelecione uma opção: "))

    match opcao:

        case 1:
            nomeItem = input("Digite o nome do item: ")
            cadastrar(arquivo, nomeItem)

        case 2:
            listar(arquivo)

        case 3:
            print('Saindo')
            break