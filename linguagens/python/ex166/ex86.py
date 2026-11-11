from rich import print
from rich import inspect


class Funcionario:
    """
    Cria uma apresentação do funcionário
    """

    empresa = "Curso em Vídeo"

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f":handshake: Prazer, me chamo [blue] {self.nome} trabalho no setor {self.setor} no cargo(a) de {self.cargo} da empresa {Funcionario.empresa}"


c1 = Funcionario("Pietro", "TI", "Analista")
print(c1.apresentacao())


# inspect(c1)