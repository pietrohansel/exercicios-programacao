# def nome_funcao():
#     faca alguma coisa
#     faça outra coisa
#     return valor_final


def cadastrar_produto():
    produto = input('Digite o nome do produto: ')
    produto = produto.casefold()
    return produto

produto = cadastrar_produto()
print(f'{produto} cadastrado com sucesso')


def cadastrar_cliente():
    cliente = input("Digite seu nome: ")
    return cliente

cliente = cadastrar_cliente()
print(f'Cliente {cliente} cadastrado com sucesso')
