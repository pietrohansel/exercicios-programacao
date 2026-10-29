
from pathlib import Path
import re
import shutil

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


def arquivos_de(exercicio):
    """Lista os arquivos de código de uma pasta ou de um arquivo solto."""
    if exercicio.is_file():
        return [exercicio]

    return [arquivo for arquivo in exercicio.rglob("*") if arquivo.is_file()]


def detectar_linguagem(exercicio):
    extensoes = {
        arquivo.suffix.lower()
        for arquivo in arquivos_de(exercicio)
        if arquivo.suffix.lower() in EXTENSOES
    }

    linguagens = {EXTENSOES[e] for e in extensoes}

    # HTML, CSS e JS podem compor um único exercício web.
    if extensoes & {".html", ".htm", ".css"}:
        linguagens.discard("javascript")
        linguagens.discard("typescript")
        linguagens.add("html-css-js")

    if len(linguagens) != 1:
        raise ValueError(
            f"{exercicio.name}: não foi possível identificar "
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


def exercicios_de_entrada():
    """Cada subpasta é um exercício; arquivos soltos de código também.

    Arquivos soltos sem extensão reconhecida (ex.: .gitkeep) são ignorados.
    """
    itens = []

    for item in ENTRADA.iterdir():
        if item.is_symlink() or item.name.startswith("."):
            continue

        if item.is_dir():
            itens.append(item)
        elif item.suffix.lower() in EXTENSOES:
            itens.append(item)

    return sorted(itens, key=lambda item: item.name)


def montar_planos(exercicios):
    """Valida todos os exercícios antes de mover qualquer um."""
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
            raise FileExistsError(f"destino já existe: {destino}")

        planos.append((exercicio, destino_pai, numero, destino))

    return planos


def main():
    if not ENTRADA.exists():
        # O Git não versiona pastas vazias: num clone limpo a pasta pode não
        # existir, mesmo existindo na máquina local. Isso não é um erro.
        print("A pasta entrada/ não existe. Nada para organizar.")
        return

    exercicios = exercicios_de_entrada()

    if not exercicios:
        print("Nenhum exercício novo encontrado.")
        return

    try:
        planos = montar_planos(exercicios)
    except (ValueError, FileExistsError) as erro:
        print(f"ERRO: {erro}")
        print(
            "Cada exercício deve ser uma pasta (ou um arquivo solto) com "
            "código de uma única linguagem. Nada foi movido."
        )
        raise SystemExit(1)

    for origem, destino_pai, numero, destino in planos:
        destino_pai.mkdir(parents=True, exist_ok=True)

        if origem.is_dir():
            shutil.move(str(origem), str(destino))
        else:
            # Arquivo solto: vira uma pasta exNNN com o arquivo dentro.
            destino.mkdir(parents=True, exist_ok=True)
            shutil.move(str(origem), str(destino / origem.name))

        print(f"{origem.name} -> {destino.relative_to(RAIZ)}")


if __name__ == "__main__":
    main()
