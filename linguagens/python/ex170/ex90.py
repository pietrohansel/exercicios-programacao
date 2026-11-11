from rich.panel import Panel
from rich import print


class Gamer:

    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()

    def add_favoritos(self, games):
        self.favoritos.append(games)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f"Nome real: [black on white] {self.nome} [/]"
        conteudo += f"\nJogos favoritos: "

        for num, game in enumerate(self.favoritos):
            conteudo += f"\n:video_game: {game}"

        painel = Panel(conteudo, title=(f"Jogador{self.nick}"))
        print(painel)


j1 = Gamer(nome="Pietro", nick="Gamer01")
j1.add_favoritos("Sniper Elite")
j1.add_favoritos("Castelvania")
j1.ficha()
