import re
import shutil
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
ENTRADA = RAIZ / "entrada"
LINGUAGENS = RAIZ / "linguagens"

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
    ".asm": "assembly",
    ".s": "assembly",
}

# Pastas que nunca contêm código do exercício
PASTAS_IGNORADAS = {
    "venv",
    ".venv",
    ".venv-dev",
    "node_modules",
    "__pycache__",
    ".git",
    "dist",
    "build",
    "target",
    "bin",
    "obj",
}


def _ignorado(arquivo, base):
    """Ignora arquivos dentro de pastas de ambiente/build e arquivos ocultos."""
    partes = arquivo.relative_to(base).parts
    return any(
        parte in PASTAS_IGNORADAS or parte.startswith(".")
        for parte in partes
    )


def arquivos_de(exercicio):
    """Lista os arquivos de código de uma pasta ou de um arquivo solto."""
    if exercicio.is_file():
        return [exercicio]

    return [
        arquivo
        for arquivo in exercicio.rglob("*")
        if arquivo.is_file() and not _ignorado(arquivo, exercicio)
    ]


def detectar_linguagem(exercicio):
    arquivos = arquivos_de(exercicio)
    extensoes = {
        arquivo.suffix.lower()
        for arquivo in arquivos
        if arquivo.suffix.lower() in EXTENSOES
    }

    linguagens = {EXTENSOES[e] for e in extensoes}

    # HTML, CSS e JS podem compor um único exercício web.
    if extensoes & {".html", ".htm", ".css"}:
        linguagens.discard("javascript")
        linguagens.discard("typescript")
        linguagens.add("html-css-js")

    if len(linguagens) != 1:
        nomes = sorted(
            arquivo.name
            for arquivo in arquivos
            if arquivo.suffix.lower() in extensoes
        )
        raise ValueError(
            f"{exercicio.name}: não foi possível identificar "
            f"uma única linguagem. Encontradas: {sorted(linguagens)}. "
            f"Arquivos: {', '.join(nomes) or 'nenhum'}"
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


def exercicios_de_entrada(entrada):
    """Cada subpasta é um exercício; arquivos soltos de código também.

    Pastas sem nenhum arquivo de extensão reconhecida (ex.: só README.md)
    são ignoradas em vez de quebrar a organização.
    """
    itens = []

    for item in entrada.iterdir():
        if item.is_symlink() or item.name.startswith("."):
            continue

        if item.is_dir():
            tem_codigo = any(
                arquivo.suffix.lower() in EXTENSOES
                for arquivo in arquivos_de(item)
            )

            if tem_codigo:
                itens.append(item)
        elif item.suffix.lower() in EXTENSOES:
            itens.append(item)

    return sorted(itens, key=lambda item: item.name)


def montar_planos(exercicios, linguagens):
    """Valida todos os exercícios antes de mover qualquer um."""
    planos = []

    for exercicio in exercicios:
        linguagem = detectar_linguagem(exercicio)
        destino_pai = linguagens / linguagem
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


def organizar(entrada=ENTRADA, raiz=RAIZ):
    """Move os exercícios de entrada/ para raiz/linguagens/<linguagem>/exNNN.

    Retorna a lista de (origem, destino) movidos.
    """
    if not entrada.exists():
        return []

    exercicios = exercicios_de_entrada(entrada)

    if not exercicios:
        return []

    planos = montar_planos(exercicios, raiz / "linguagens")
    movidos = []

    for origem, destino_pai, _numero, destino in planos:
        destino_pai.mkdir(parents=True, exist_ok=True)

        if origem.is_dir():
            shutil.move(str(origem), str(destino))
        else:
            # Arquivo solto: vira uma pasta exNNN com o arquivo dentro.
            destino.mkdir(parents=True, exist_ok=True)
            shutil.move(str(origem), str(destino / origem.name))

        movidos.append((origem, destino))
        print(f"{origem.name} -> {destino.relative_to(raiz)}")

    return movidos


def main():
    if not ENTRADA.exists():
        # O Git não versiona pastas vazias: num clone limpo a pasta pode não
        # existir, mesmo existindo na máquina local. Isso não é um erro.
        print("A pasta entrada/ não existe. Nada para organizar.")
        return

    try:
        movidos = organizar(ENTRADA, RAIZ)
    except (ValueError, FileExistsError) as erro:
        print(f"ERRO: {erro}")
        print(
            "Cada exercício deve ser uma pasta (ou um arquivo solto) com "
            "código de uma única linguagem. Nada foi movido."
        )
        raise SystemExit(1) from erro

    if not movidos:
        print("Nenhum exercício novo encontrado.")


if __name__ == "__main__":
    main()
