
# Classes

# declaração de classe
class Gafanhoto:
    """
Essa clase cria um gafanhoto
    """

    # método construtor
    def __init__(self, nome="", idade=0):

        # atributos
        self.nome = nome
        self.idade = idade

        # métodos -> parenteses
    def aniversario(self):
        self.idade += 1
        # Dunder Method
    def __str__(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."


# declaração dos objetos
g1 = Gafanhoto('Pietro', 17)
print(g1)


g2 = Gafanhoto("Enzo", 13)
print(g1)
