
#FILA -> FIFO
from collections import deque

fila = deque(["Maria", "João"])
fila.append("Carlos")
print(fila)

atentida = fila.popleft()
print(atentida)


# Counter
from collections import Counter

texto = "maçã banana banana pera"

contagem = Counter(texto.split())
print(contagem)


# Default Dict
from collections import defaultdict

tarefas = defaultdict(list)

tarefas["Casa"].append("Lavar louça")
tarefas["Trabalho"].append("Assinar jornais")

print(tarefas)


# OrderedDict

from collections import OrderedDict

tarefas_ordenadas = {}

tarefas_ordenadas["A"] = ["Estudar"]
tarefas_ordenadas["B"] = ["Exercícios"]
tarefas_ordenadas["C"] = ["Lazer"]

for prioridade, tarefa in tarefas_ordenadas:
    print(f"Prioridade {prioridade}: {tarefa}")

# Chain Map