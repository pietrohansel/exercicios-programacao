
class Gafanhoto:
    """
    Teste documentação de uma classe 
    """

    def __init__(self, n="", i=0):  # Método Construtor
        #Atributos de Instância
        self.nome = ""
        self.idade = 0

    #Métodos de Instância
    def aniversario(self):
        self.idade += 1 

    def __str__(self): # Dunder Method
        return "Print"

#Declaração de Objeto

c1 = Gafanhoto('Pedro',1)
print(c1)

print(c1.__doc__)
print(c1.__dict__)
