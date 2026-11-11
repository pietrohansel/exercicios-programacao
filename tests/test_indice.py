from scripts.indice import gerar


def test_indice_conta_exercicios_por_linguagem(tmp_path):
    linguagens = tmp_path / "linguagens"

    for pasta in ("python/ex001", "python/ex002", "java/ex001"):
        (linguagens / pasta).mkdir(parents=True)

    (linguagens / "sql").mkdir()

    indice = gerar(linguagens)

    assert "[python](python/) | 2" in indice
    assert "[java](java/) | 1" in indice
    assert "sql" not in indice
    assert "**Total:** 3 exercícios." in indice
