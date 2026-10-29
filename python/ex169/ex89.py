class Livro:

    def __init__(self, p_total):
        self.atual = 1
        self.total = p_total

    def passarPagina(self,qtd):
        cont = 0
        for pg in range(0,qtd,1):
            if not self.fim_do_livro():
                self.atual += 1 
                print(f"{self.atual}")
                cont += 1 

    def fim_do_livro(self) -> bool:
        return True if self.atual == self.total else False


c1 = Livro(p_total=20)
c1.passarPagina(10)
