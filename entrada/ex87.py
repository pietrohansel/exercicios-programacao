from rich.panel import Panel
from rich import print

class Produto:

    def __init__(self, nome, preco = 0):
        self.nome = nome
        self.preco = preco

    def __str__(self) -> str:
        return f"{self.nome} custa R${self.preco:.2f}"

    def etiqueta(self):
        conteudo = f"{self.nome.center(30,' ')}"
        conteudo += f"{'-' * 30}"
        precof = f"R${self.preco:.2f}"
        conteudo += f"{precof.center(30,'.')}"
        etiqueta = Panel(conteudo, title="Produto", width=34)
        print(etiqueta)


p1 = Produto(nome = "Iphone", preco = 100)
p1.etiqueta()