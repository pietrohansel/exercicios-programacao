/* ================================================================
 *  EXERCICIO 03 - Lista 5 - Heranca, polimorfismo, interfaces e static
 *  META Escola Tecnica - Programacao Orientada a Objetos - 2026
 *  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
 *  ---------------------------------------------------------------
 *  AVALIACOES DO BIMESTRE
 *  Prova, trabalho e seminario nao sao parentes, mas cumprem o
 *  mesmo contrato.
 *
 *  REGRAS OBRIGATORIAS:
 *  (a) interface Avaliavel com double calcularNota(), String
 *      descricao() e o metodo default String conceito(): nota
 *      >= 9 A, >= 7 B, >= 5 C, abaixo D.
 * 
 *  (b) Prova: acertos e totalQuestoes; nota = acertos * 10.0 /
 *      totalQuestoes.
 * 
 *  (c) Trabalho: notaConteudo (0 a 6) + notaApresentacao (0 a
 *      4).
 * 
 *  (d) Seminario: um double[] com as notas da banca; nota =
 *      media do array.
 * 
 *  (e) No main: Avaliavel[] com new Prova(19, 20), new
 *      Trabalho(4.0, 2.5) e new Seminario(new double[]{8.0,
 *      9.5, 7.0}). Imprima descricao, nota (1 casa) e conceito,
 *      e a media geral (2 casas).
 * 
 *  (f) Cabecalho: "===== AVALIACOES DO BIMESTRE =====".
 *      Referencia: 9,5 A - 6,5 C - 8,2 B - media geral 8,06.
 *
 *  CRITERIOS (0,5 cada):
 *  [ ] Interface com 2 metodos abstratos e 1 default.
 *  [ ] Tres classes com implements, sem heranca entre elas.
 *  [ ] conceito() nao foi reescrito nas classes (vem pronto da
 *      interface).
 *  [ ] Laco sobre Avaliavel[] e valores de referencia corretos.
 * ================================================================ */

// Escreva aqui as classes de apoio (SEM a palavra public antes de class).

import java.util.Locale;

interface Avaliavel {
    double calcularNota();
    String descricao();

    default String conceito() {
        double nota = calcularNota();
        if (nota >= 9) return "A";
        if (nota >= 7) return "B";
        if (nota >= 5) return "C";
        return "D";
    }
}

class Prova implements Avaliavel {
    private final int acertos;
    private final int totalQuestoes;

    public Prova(int acertos, int totalQuestoes) {
        this.acertos = acertos;
        this.totalQuestoes = totalQuestoes;
    }

    @Override
    public double calcularNota() {
        return acertos * 10.0 / totalQuestoes;
    }

    @Override
    public String descricao() {
        return "Prova (" + acertos + "/" + totalQuestoes + ")";
    }
}

class Trabalho implements Avaliavel {
    private final double notaConteudo;
    private final double notaApresentacao;

    public Trabalho(double notaConteudo, double notaApresentacao) {
        this.notaConteudo = notaConteudo;
        this.notaApresentacao = notaApresentacao;
    }

    @Override
    public double calcularNota() {
        return notaConteudo + notaApresentacao;
    }

    @Override
    public String descricao() {
        return "Trabalho (conteudo " + notaConteudo
                + " + apresentacao " + notaApresentacao + ")";
    }
}

class Seminario implements Avaliavel {
    private final double[] notasBanca;

    public Seminario(double[] notasBanca) {
        this.notasBanca = notasBanca;
    }

    @Override
    public double calcularNota() {
        double soma = 0;
        for (double n : notasBanca) {
            soma += n;
        }
        return soma / notasBanca.length;
    }

    @Override
    public String descricao() {
        return "Seminario (banca com " + notasBanca.length + " notas)";
    }
}

public class Exercicio03 {

    public static void main(String[] args) {
        System.out.println("===== AVALIACOES DO BIMESTRE =====");

        Avaliavel[] avaliacoes = {
            new Prova(19, 20),
            new Trabalho(4.0, 2.5),
            new Seminario(new double[]{8.0, 9.5, 7.0})
        };

        double soma = 0;

        for (Avaliavel a : avaliacoes) {
            double nota = a.calcularNota();
            soma += nota;
            System.out.printf(Locale.forLanguageTag("pt-BR"),
                    "%s - %.1f %s%n", a.descricao(), nota, a.conceito());
        }

        double mediaGeral = soma / avaliacoes.length;
        System.out.printf(Locale.forLanguageTag("pt-BR"),
                "Media geral: %.2f%n", mediaGeral);
    }
}