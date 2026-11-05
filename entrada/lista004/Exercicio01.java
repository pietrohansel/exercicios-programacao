package lista004;

/* ================================================================
 *  EXERCICIO 01 - Lista 4 - Classes, objetos e encapsulamento
 *  META Escola Tecnica - Programacao Orientada a Objetos - 2026
 *  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
 *  ---------------------------------------------------------------
 *  FICHA DE LIVROS DA BIBLIOTECA
 *  Crie a classe Livro e use-a para cadastrar tres livros do
 *  acervo da escola.
 *
 *  REGRAS OBRIGATORIAS:
 *  (a) Classe Livro com os atributos private: String titulo,
 *      String autor, int anoPublicacao e int paginas.
 *  (b) Um construtor com os 4 parametros, usando this.atributo
 *      = parametro.
 *  (c) Metodo void exibirFicha() que imprime titulo, autor, ano
 *      e paginas com printf.
 *  (d) Metodo int idadeDoLivro(int anoAtual) que retorna
 *      anoAtual - anoPublicacao.
 *  (e) No main, crie 3 objetos: Dom Casmurro (Machado de Assis,
 *      1899, 256 p.), O Pequeno Principe (Antoine de
 *      Saint-Exupery, 1943, 96 p.) e Java: Como Programar (Paul
 *      e Harvey Deitel, 2017, 968 p.).
 *  (f) Para cada livro, chame exibirFicha() e mostre a idade em
 *      2026.
 *  (g) Cabecalho obrigatorio: "===== ACERVO DA BIBLIOTECA META
 *      =====".
 *  (h) Saida de referencia: idades 127, 83 e 9 anos.
 *
 *  CRITERIOS (0,5 cada):
 *  [ ] Classe Livro com 4 atributos private e construtor usando
 *      this.
 *  [ ] 3 objetos criados com new no main.
 *  [ ] idadeDoLivro retorna o valor (nao imprime dentro do
 *      metodo).
 *  [ ] Saida formatada com cabecalho e valores corretos.
 * ================================================================ */

// Escreva aqui as classes de apoio (SEM a palavra public antes de class).




class Livro {
    // Atributos privados
    private String titulo;
    private String autor;
    private int anoPublicacao;
    private int paginas;

    // Construtor com os quatro parâmetros
    public Livro(String titulo, String autor, int anoPublicacao, int paginas) {
        this.titulo = titulo;
        this.autor = autor;
        this.anoPublicacao = anoPublicacao;
        this.paginas = paginas;
    }

    // Método para exibir a ficha do livro
    public void exibirFicha() {
        System.out.printf("Título: %s%n", titulo);
        System.out.printf("Autor: %s%n", autor);
        System.out.printf("Ano de publicação: %d%n", anoPublicacao);
        System.out.printf("Número de páginas: %d%n", paginas);
    }

    // Método para calcular a idade do livro
    public int idadeDoLivro(int anoAtual) {
        return anoAtual - anoPublicacao;
    }
}

public class Exercicio01 {

    public static void main(String[] args) {

        // Criação dos três objetos
        Livro livro1 = new Livro("Dom Casmurro",
                "Machado de Assis", 1899, 256);

        Livro livro2 = new Livro("O Pequeno Principe",
                "Antoine de Saint-Exupery", 1943, 96);

        Livro livro3 = new Livro("Java: Como Programar",
                "Paul e Harvey Deitel", 2017, 968);

        // Cabeçalho obrigatório
        System.out.println("===== ACERVO DA BIBLIOTECA META =====");

        // Exibição do primeiro livro
        System.out.println("\n--- LIVRO 1 ---");
        livro1.exibirFicha();
        System.out.printf("Idade do livro em 2026: %d anos%n",
                livro1.idadeDoLivro(2026));

        // Exibição do segundo livro
        System.out.println("\n--- LIVRO 2 ---");
        livro2.exibirFicha();
        System.out.printf("Idade do livro em 2026: %d anos%n",
                livro2.idadeDoLivro(2026));

        // Exibição do terceiro livro
        System.out.println("\n--- LIVRO 3 ---");
        livro3.exibirFicha();
        System.out.printf("Idade do livro em 2026: %d anos%n",
                livro3.idadeDoLivro(2026));
    }
}
