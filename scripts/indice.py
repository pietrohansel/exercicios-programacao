from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
LINGUAGENS = RAIZ / "linguagens"
ARQUIVO = LINGUAGENS / "README.md"


def contar_exercicios(pasta):
    return sum(
        1
        for item in pasta.iterdir()
        if item.is_dir() and item.name.startswith("ex")
    )


def gerar(linguagens=LINGUAGENS):
    """Monta o índice em Markdown com a contagem de exercícios por linguagem."""
    linhas = [
        "# Exercícios por linguagem",
        "",
        "Índice gerado automaticamente pelo workflow **Organizar exercicios**.",
        "",
        "| Linguagem | Exercícios |",
        "| --- | --- |",
    ]

    total = 0
    pastas = sorted(p for p in linguagens.iterdir() if p.is_dir())

    for pasta in pastas:
        quantidade = contar_exercicios(pasta)

        if quantidade == 0:
            continue

        total += quantidade
        linhas.append(f"| [{pasta.name}]({pasta.name}/) | {quantidade} |")

    linhas.extend(["", f"**Total:** {total} exercícios.", ""])

    return "\n".join(linhas)


def main():
    if not LINGUAGENS.exists():
        print("A pasta linguagens/ não existe. Nada para indexar.")
        return

    ARQUIVO.write_text(gerar(), encoding="utf-8")
    print(f"Índice atualizado: {ARQUIVO.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
