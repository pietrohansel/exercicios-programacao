from rich.panel import Panel
from rich import print

class Churrasco:

    consumo_padrao: float = 400
    preco_kg: float = 83.40

    def __init__(self, qtd):
        self.qtd = qtd

    def calcular_qtd_carne(self):
        return (Churrasco.consumo_padrao * self.qtd) / 1000

    def calcular_custo_total(self):
        return self.calcular_qtd_carne() * Churrasco.preco_kg

    def calcular_custo_individual(self):
        return self.calcular_custo_total() / self.qtd

    def analisar(self):
        conteudo = f"Qtd de carne = {self.calcular_qtd_carne():.2f} kg\n"
        conteudo += f"Custo total = {self.calcular_custo_total():.2f}\n"
        conteudo += f"Custo individual = {self.calcular_custo_individual():.2f}\n"
        painel = Panel(conteudo, title="Mensagem")
        print(painel)

c1 = Churrasco(qtd=10)
c1.analisar()
