class Mae:
    def __init__(self, nome:str = "Mamãe"):
        self.nome = nome

    
    def fazer_pudim(self):
        print(f"{self.nome} frita coxinha no óleo de soja")

    def fazer_bolo(self):
        print(f"{self.nome} faz bolo de cenoura")

    
class Filho(Mae):
    def fazer_pudim(self):
        print(f"{self.nome} frita coxinha no azeite")