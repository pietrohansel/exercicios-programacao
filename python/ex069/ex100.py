from rich import print

class Caneta:

    def __init__(self,cor="azul"):
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"

            case "vermelho" | "vermelha":
                escolha = "[red]"

            case "verde":
                escolha = "[green]"

            case _:
                escolha = "[white]"   

        self.cor = escolha
        self.tampada = True

    def escrever(self,msg):
        if self.tampada:
            print("Tampada")
        else:
            print(f"{self.cor}{msg}[/]")

    def quebrar_linha(self,qtd=1):
        print("\n" * qtd, end="")

    def tampar(self):
        self.tampada = True
        pass

    def destampar(self):
            self.tampada = False
            pass


c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")


c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Hello, Word")
c1.quebrar_linha(2)
c2.escrever("Hello, Word")
c3.escrever("Hello, Word")

