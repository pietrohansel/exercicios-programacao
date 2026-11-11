if __package__:
    from . import funcao
else:
    import funcao


def main():
    funcao.Printar(mensagem = "Olá, mundo!")
    funcao.Somar(a=3, b=2)
    funcao.CriarLista()
    print(" ")
    funcao.CriarLista2()

if __name__ == "__main__":
    main()