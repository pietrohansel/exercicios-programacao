
from pathlib import Path
import re
import shutil
import sys

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "entrada"

# Extensões que identificam cada linguagem
EXTENSOES = {
    ".py": "python",
    ".java": "java",
    ".js": "javascript",
    ".mjs": "javascript",
    ".cjs": "javascript",
    ".html": "html-css-js",
    ".htm": "html-css-js",
    ".css": "html-css-js",
    ".java": "java",
    ".c": "c",
    ".h": "c",
    ".cpp": "cpp",
    ".hpp": "cpp",
    ".cc": "cpp",
    ".php": "php",
    ".ts": "typescript",
    ".tsx": "typescript",
    ".cs": "csharp",
    ".go": "go",
    ".rs": "rust",
    ".rb": "ruby",
    ".kt": "kotlin",
    ".swift": "swift",
    ".sql": "sql",
}


def detectar_linguagem(pasta):
    extensoes = {
        arquivo.suffix.lower()
        for arquivo in pasta.rglob("*")
        if arquivo.is_file()
        and arquivo.suffix.lower() in EXTENSOES
    }

    linguagens = {EXTENSOES[e] for e in extensoes}

    # HTML, CSS e JS podem compor um único exercício web.
    if extensoes & {".html", ".htm", ".css"}:
        linguagens.discard("javascript")
        linguagens.discard("typescript")
        linguagens.add("html-css-js")

    if len(linguagens) != 1:
        raise ValueError(
            f"{pasta.name}: não foi possível identificar "
            f"uma única linguagem. Encontradas: {sorted(linguagens)}"
        )

    return linguagens.pop()


def proximo_numero(pasta):
    numeros = []

    if pasta.exists():
        for item in pasta.iterdir():
            if item.is_dir():
                match = re.fullmatch(r"ex(\d+)", item.name)
                if match:
                    numeros.append(int(match.group(1)))

    return max(numeros, default=0) + 1


def main():
    if not ENTRADA.exists():
        print("A pasta entrada/ não existe.")
        sys.exit(1)

    exercicios = sorted(
        item for item in ENTRADA.iterdir()
        if item.is_dir() and not item.is_symlink()
    )

    if not exercicios:
        print("Nenhum exercício novo encontrado.")
        return

    # Validar todos antes de mover qualquer pasta.
    planos = []
    for exercicio in exercicios:
        linguagem = detectar_linguagem(exercicio)
        destino_pai = RAIZ / linguagem
        numero = proximo_numero(destino_pai)

        # Reservar números também entre exercícios deste lote.
        while any(
            plano[1] == destino_pai
            and plano[2] == numero
            for plano in planos
        ):
            numero += 1

        destino = destino_pai / f"ex{numero:03d}"

        if destino.exists():
            raise FileExistsError(f"Destino já existe: {destino}")

        planos.append((exercicio, destino_pai, numero, destino))

    for origem, destino_pai, numero, destino in planos:
        destino_pai.mkdir(parents=True, exist_ok=True)
        shutil.move(str(origem), str(destino))
        print(f"{origem.name} -> {destino.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
