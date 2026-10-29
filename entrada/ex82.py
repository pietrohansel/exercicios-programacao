
class Gafanhoto:

    def __init__(self):  # Método Construtor
        #Atributos de Instância
        self.nome = ""
        self.idade = 0

    #Métodos de Instância
    def aniversario(self):
        self.idade += 1 

    def mensagem(self):
        return f"{self.nome}"

#Declaração de Objeto

c1 = Gafanhoto()
print(c1)