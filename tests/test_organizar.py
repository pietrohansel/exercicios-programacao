import pytest

from scripts.organizar import organizar


@pytest.fixture
def raiz(tmp_path):
    (tmp_path / "entrada").mkdir()
    (tmp_path / "linguagens").mkdir()
    return tmp_path


def escrever(caminho, conteudo="print('oi')\n"):
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(conteudo, encoding="utf-8")


def test_arquivo_solto_vira_pasta_numerada(raiz):
    escrever(raiz / "entrada" / "calculadora.py")

    movidos = organizar(raiz / "entrada", raiz)

    destino = raiz / "linguagens" / "python" / "ex001" / "calculadora.py"
    assert destino.is_file()
    assert len(movidos) == 1


def test_pasta_preserva_nome_dos_arquivos(raiz):
    escrever(
        raiz / "entrada" / "cartao-visita" / "CartaoVisita.java",
        "class CartaoVisita {}\n",
    )

    organizar(raiz / "entrada", raiz)

    destino = raiz / "linguagens" / "java" / "ex001" / "CartaoVisita.java"
    assert destino.is_file()


def test_html_css_js_formam_um_unico_exercicio(raiz):
    exercicio = raiz / "entrada" / "site"
    escrever(exercicio / "index.html", "<h1>Oi</h1>\n")
    escrever(exercicio / "style.css", "h1 { color: red; }\n")
    escrever(exercicio / "app.js", "console.log('oi')\n")

    organizar(raiz / "entrada", raiz)

    destino = raiz / "linguagens" / "html-css-js" / "ex001"
    assert (destino / "index.html").is_file()
    assert (destino / "app.js").is_file()


def test_duas_linguagens_falham_sem_mover_nada(raiz):
    exercicio = raiz / "entrada" / "misto"
    escrever(exercicio / "main.py")
    escrever(exercicio / "Main.java", "class Main {}\n")

    with pytest.raises(ValueError, match="uma única linguagem"):
        organizar(raiz / "entrada", raiz)

    assert (exercicio / "main.py").is_file()
    assert not (raiz / "linguagens" / "python").exists()
    assert not (raiz / "linguagens" / "java").exists()


def test_dois_exercicios_da_mesma_linguagem_nao_colidem(raiz):
    escrever(raiz / "entrada" / "a" / "a.py")
    escrever(raiz / "entrada" / "b" / "b.py")

    organizar(raiz / "entrada", raiz)

    assert (raiz / "linguagens" / "python" / "ex001" / "a.py").is_file()
    assert (raiz / "linguagens" / "python" / "ex002" / "b.py").is_file()


def test_ignora_venv_na_deteccao_de_linguagem(raiz):
    exercicio = raiz / "entrada" / "projeto"
    escrever(exercicio / "main.py")
    escrever(exercicio / "venv" / "lib" / "dependencia.java", "class X {}\n")

    organizar(raiz / "entrada", raiz)

    destino = raiz / "linguagens" / "python" / "ex001"
    assert (destino / "main.py").is_file()


def test_pasta_sem_codigo_e_ignorada(raiz):
    pasta = raiz / "entrada" / "documentacao"
    pasta.mkdir()
    (pasta / "README.md").write_text("# Só documentação\n", encoding="utf-8")

    movidos = organizar(raiz / "entrada", raiz)

    assert movidos == []
    assert (pasta / "README.md").is_file()


def test_organizar_duas_vezes_nao_move_nada(raiz):
    escrever(raiz / "entrada" / "unico.py")
    organizar(raiz / "entrada", raiz)

    assert organizar(raiz / "entrada", raiz) == []
