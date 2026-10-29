# from abc import ABC, abstractmethod
# import math


# class FiguraGeometrica(ABC):

#     @abstractmethod
#     def perimetro(self):
#         pass

#     @abstractmethod
#     def area(self):
#         pass


# class Quadrado(FiguraGeometrica):

#     def __init__(self, lado=1):
#         self.lado = lado

#     def perimetro(self):
#         return self.lado * 4

#     def area(self):
#         return self.lado ** 2


# class Circulo(FiguraGeometrica):

#     def __init__(self, raio=1):
#         self.raio = raio

#     def perimetro(self):
#         return 2 * math.pi * self.raio

#     def area(self):
#         return math.pi * self.raio ** 2