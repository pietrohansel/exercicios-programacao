


# Classe
class Funcionario:
    # Atributos de Classe
    empresa = "Curso em Vídeo"

    # Atributos de Instância
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    # Métodos
    def apresentar(self) -> str:
        return f"[green]{self.nome}[/] é um novo funcionário(a) do setor [blue]{self.setor}[/] do cargo [red]{self.cargo}[/] da empresa [purple]{Funcionario.empresa}[/]"


f = Funcionario(nome="Pietro", setor="TI", cargo="Gerente")
print(f.apresentar())
# inspect(f, methods=True)

f = Funcionario(nome="Ana", setor="ADM", cargo="Supervisor")
print(f.apresentar())
