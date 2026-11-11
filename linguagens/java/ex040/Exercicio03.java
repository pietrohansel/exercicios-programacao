package lista004;
/* ================================================================
 *  EXERCICIO 03 - Lista 4 - Classes, objetos e encapsulamento
 *  META Escola Tecnica - Programacao Orientada a Objetos - 2026
 *  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
 *  ---------------------------------------------------------------
 *  SECRETARIA ESCOLAR: TRES FORMAS DE CADASTRAR UM ALUNO
 *  Pratique a sobrecarga de construtores e a cadeia this(...),
 *  deixando a validacao em um unico lugar.
 *
 *  REGRAS OBRIGATORIAS:
 *  (a) Classe Aluno com private String nome, private String
 *      curso e private double nota.
 * 
 *  (b) Construtor 1: Aluno(String nome) chama this(nome, "Nao
 *      informado").
 * 
 *  (c) Construtor 2: Aluno(String nome, String curso) chama
 *      this(nome, curso, 0.0).
 * 
 *  (d) Construtor 3 (completo): guarda os tres dados e so
 *      aceita nota entre 0 e 10. Fora disso, imprime "Nota
 *      invalida para [nome]. Registrada como 0,0." e grava 0.
 * 
 *  (e) Metodo String situacao(): nota >= 7 APROVADO, nota >= 5
 *      RECUPERACAO, abaixo disso REPROVADO.
 * 
 *  (f) Metodo void exibir() com nome, curso, nota (1 casa) e
 *      situacao em colunas (printf com %-12s).
 * 
 *  (g) No main: new Aluno("Ana Souza"), new Aluno("Bruno Lima",
 *      "Desenvolvimento de Sistemas"), new Aluno("Carla Dias",
 *      "Informatica", 8.5) e new Aluno("Diego Rocha",
 *      "Informatica", 12).
 * 
 *  (h) Cabecalho: "===== SECRETARIA ESCOLAR - CADASTRO =====".
 *
 *  CRITERIOS (0,5 cada):
 *  [ ] Tres construtores com assinaturas diferentes.
 *  [ ] Os construtores curtos usam this(...) na primeira linha.
 *  [ ] A validacao da nota existe apenas no construtor
 *      completo.
 *  [ ] situacao() retorna o texto correto e a tabela sai
 *      alinhada.
 * ================================================================ */

// Escreva aqui as classes de apoio (SEM a palavra public antes de class).

class Aluno {
    private String nome;
    private String curso;
    private double nota;

    Aluno(String nome) {
        this(nome, "Não informado");
    }
    
    Aluno(String nome, String curso) {
        this(nome, curso, 0.0);
    }

    Aluno(String nome, String curso, double nota) {
        this.nome = nome;
        this.curso = curso;
        if (nota >= 0.0 && nota <= 10.0) {
            this.nota = nota;
        } else {
            System.out.println("Nota invalida " + nome + ". Registrada com 0,0.");
            this.nota = 0.0;
        }
    }

    String situacao() {
        if (nota >= 7.0) {
            return "APROVADO";
        }
        if (nota >= 5.0) {
            return "RECUPERAÇÃO";
        }
        return "REPROVADO";
    }

    void exibir() {
        System.out.printf("%-12s %-30s %6.1f %-12s%n", nome, curso, nota, situacao());
    }

}

public class Exercicio03 {
    public static void main(String[] args) {
        // ====== ESCREVA SUA SOLUCAO ABAIXO ======
   System.out.println("===== SECRETARIA ESCOLAR - CADASTRO =====");

        new Aluno("Ana Souza").exibir();
        new Aluno("Bruno Lima", "Desenvolvimento de Sistemas").exibir();
        new Aluno("Carla Dias", "Informatica", 8.5).exibir();
        new Aluno("Diego Rocha", "Informatica", 12).exibir();


        // ====== FIM DA SUA SOLUCAO ======
    }
}
