# Classes

# declaração de classe
class Gafanhoto:

    # método construtor
    def __init__(self):

        # atributos
        self.nome = ''
        self.idade = '0'

        # métodos  -> parenteses
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é gafanhoto(a) e tem {self.idade} anos de idade."


# declaração dos objetos
g1 = Gafanhoto()
g1.nome = 'Pietro'
g1.idade = 18
print(g1.mensagem())


g2 = Gafanhoto()
g2.nome = 'Enzo'
g2.idade = 13
print(g2.mensagem())
