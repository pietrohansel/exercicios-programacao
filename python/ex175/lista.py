class Tarefa:
    def __init__(self, titulo, concluida=False):
        self.titulo = titulo
        self.concluida = concluida

    def __str__(self):
        status = "x" if self.concluida else " "
        return f"[{status}] {self.titulo}"


class ListaDeTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar(self, titulo):
        if not titulo.strip():
            raise ValueError("O título da tarefa não pode estar vazio.")

        self.tarefas.append(Tarefa(titulo.strip()))

    def listar(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        for numero, tarefa in enumerate(self.tarefas, start=1):
            print(f"{numero}. {tarefa}")

    def concluir(self, indice):
        tarefa = self._obter_tarefa(indice)
        tarefa.concluida = True

    def remover(self, indice):
        tarefa = self._obter_tarefa(indice)
        self.tarefas.remove(tarefa)

    def _obter_tarefa(self, indice):
        if indice < 0 or indice >= len(self.tarefas):
            raise IndexError("Índice da tarefa inválido.")

        return self.tarefas[indice]


class Menu:
    def __init__(self):
        self.lista_de_tarefas = ListaDeTarefas()

    def exibir_menu(self):
        print("\n1 - Adicionar")
        print("2 - Listar")
        print("3 - Concluir")
        print("4 - Remover")
        print("5 - Sair")

    def executar(self):
        while True:
            self.exibir_menu()
            opcao = input("Escolha: ")

            if opcao == "1":
                titulo = input("Nova tarefa: ")
                try:
                    self.lista_de_tarefas.adicionar(titulo)
                except ValueError as erro:
                    print(erro)

            elif opcao == "2":
                self.lista_de_tarefas.listar()

            elif opcao == "3":
                try:
                    numero = int(input("Número da tarefa: ")) - 1
                    self.lista_de_tarefas.concluir(numero)
                except (ValueError, IndexError):
                    print("Número da tarefa inválido.")

            elif opcao == "4":
                try:
                    numero = int(input("Número da tarefa: ")) - 1
                    self.lista_de_tarefas.remover(numero)
                except (ValueError, IndexError):
                    print("Número da tarefa inválido.")

            elif opcao == "5":
                break

            else:
                print("Opção inválida.")


if __name__ == "__main__":
    Menu().executar()