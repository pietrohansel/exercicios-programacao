from abc import ABC, abstractmethod

class animal(ABC):
    def __init__(self, nome:str=""):
        self.nome = nome


    def emitir_som(self):
        print(f"{self.nome} é um {self.__class__.__name__} e está emitindo um som")


class Cachorro(animal):
    def emitir_som(self):
        print(f"{self.nome} emitiu auaua")


class Pitbull(Cachorro):
    pass


class Gato(animal):
    def emitir_som(self):
        print(f"{self.nome} emitiu miau miau")


class Pato(animal):
    pass