package lista004;
/* ================================================================
 *  EXERCICIO 02 - Lista 4 - Classes, objetos e encapsulamento
 *  META Escola Tecnica - Programacao Orientada a Objetos - 2026
 *  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
 *  ---------------------------------------------------------------
 *  PRODUTO DA PAPELARIA COM SETTERS QUE VALIDAM
 *  Encapsule um produto para que nenhum dado invalido consiga
 *  entrar no objeto.
 *
 *  REGRAS OBRIGATORIAS:
 *  (a) Classe Produto com private String nome, private double
 *      preco e private int estoque.
 *  (b) Getters para os tres atributos.
 *  (c) Setters com validacao. Se o valor for invalido, imprima
 *      "Nome invalido! Valor mantido." (ou Preco / Estoque) e
 *      nao altere o atributo:
 *  (d) setNome: rejeita null ou texto vazio (use
 *      nome.trim().isEmpty()). setPreco: aceita so valores
 *      maiores que zero. setEstoque: aceita zero ou mais.
 *  (e) O construtor chama os setters, assim a validacao vale
 *      desde a criacao.
 *  (f) Metodo boolean vender(int quantidade): so vende se a
 *      quantidade for positiva e houver estoque; retorna true
 *      ou false.
 *  (g) Metodo void repor(int quantidade): soma ao estoque
 *      apenas quantidades positivas.
 *  (h) No main: crie Produto("Caderno 10 materias", 24.90, 50),
 *      tente setPreco(-5) e setNome(" "), venda 12, tente
 *      vender 100 e reponha 20.
 *  (i) Cabecalho: "===== CONTROLE DE ESTOQUE - PAPELARIA
 *      =====". Referencia: preco continua R$ 24,90, vendas true
 *      e false, estoque final 58.
 *
 *  CRITERIOS (0,5 cada):
 *  [ ] Atributos private e getters corretos.
 *  [ ] Os tres setters validam e mantem o valor antigo quando o
 *      dado e invalido.
 *  [ ] vender retorna boolean e nao deixa o estoque ficar
 *      negativo.
 *  [ ] Construtor usa os setters e a saida bate com a
 *      referencia.
 * ================================================================ */

// Escreva aqui as classes de apoio (SEM a palavra public antes de class).

class Produto {
    private String nome;
    private double preco;
    private int estoque;

    Produto(String nome, double preco, int estoque) {
        setNome(nome);
        setPreco(preco);
        setEstoque(estoque);
    }

    public String getNome() {
        return nome;
    }

    public double getPreco() {
        return preco;
    }

    public int getEstoque() {
        return estoque;
    }

    public void setNome(String nome) {
        if (nome == null || nome.trim().isEmpty()) {
            System.out.println("Nome invalido! Valor mantido.");
            return;
        }
        this.nome = nome;
    }

    public void setPreco(double preco) {
        if (preco <= 0) {
            System.out.println("Preco invalido! Valor mantido.");
            return;
        }
        this.preco = preco;
    }

    public void setEstoque(int estoque) {
        if (estoque < 0) {
            System.out.println("Estoque invalido! Valor mantido.");
            return;
        }
        this.estoque = estoque;
    }

    public boolean vender(int quantidade) {
        if (quantidade > 0 && quantidade <= estoque) {
            estoque -= quantidade;
            return true;
        }
        return false;
    }

    public void repor(int quantidade) {
        if (quantidade > 0) {
            estoque += quantidade;
        }
    }
}

public class Exercicio02 {

    public static void main(String[] args) {
        // ====== ESCREVA SUA SOLUCAO ABAIXO ======

        System.out.println("===== CONTROLE DE ESTOQUE - PAPELARIA =====");

        Produto p = new Produto("Caderno 10 materias", 24.90, 50);

        p.setPreco(-5);
        p.setNome(" ");

        boolean venda12 = p.vender(12);
        boolean venda100 = p.vender(100);
        p.repor(20);

        System.out.printf("Produto: %s%n", p.getNome());
        System.out.printf("Preco: R$ %.2f%n", p.getPreco());
        System.out.printf("Venda de 12 unidades: %b%n", venda12);
        System.out.printf("Venda de 100 unidades: %b%n", venda100);
        System.out.printf("Estoque final: %d%n", p.getEstoque());

        // ====== FIM DA SUA SOLUCAO ======
    }
}
