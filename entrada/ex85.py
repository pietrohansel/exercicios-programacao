from rich import print
from rich.panel import Panel
from rich.table import Table
from rich import inspect
from rich.traceback import install
install()

print("Olá, [red]Mundo!:earth_americas:")


caixa = Panel('Painel de exemplo', title="Mensagem", style="red")
print(caixa)


Table = Table(title="Tabela")
Table.add_column("Nome")
Table.add_column("Preço")
Table.add_row("Lápis", "R$1,50")
Table.add_row("Lápis", "R$5,00")
print(Table)


inspect(int, all=True)

