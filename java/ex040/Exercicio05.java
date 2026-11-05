/* ================================================================
 *  EXERCICIO 05 - Lista 4 - Classes, objetos e encapsulamento
 *  META Escola Tecnica - Programacao Orientada a Objetos - 2026
 *  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
 *  ---------------------------------------------------------------
 *  CARTAO DA CANTINA ESCOLAR
 *  Junte tudo do Modulo 1 em um sistema pequeno, no mesmo
 *  espirito do NexBank da Aula 12, mas em outro dominio.
 *
 *  REGRAS OBRIGATORIAS:
 *  (a) Classe CartaoCantina com numero, titular, saldo e
 *      totalCompras, todos private. Nao crie setSaldo nem
 *      setNumero.
 * 
 *  (b) Construtor (numero, titular, saldoInicial): saldo
 *      inicial negativo nao e aceito.
 * 
 *  (c) void recarregar(double valor): aceita de R$ 0,01 a R$
 *      200,00 por recarga; fora disso recusa com mensagem.
 * 
 *  (d) boolean comprar(String item, double preco): aprova so se
 *      houver saldo; debita, soma 1 em totalCompras e imprime
 *      "Compra aprovada: Coxinha R$ 6,50 | Saldo: R$ 13,50". Se
 *      faltar saldo: "Saldo insuficiente para ..." e retorna
 *      false.
 * 
 *  (e) Classe Cantina com um array de 3 cartoes,
 *      cadastrar(CartaoCantina c) e relatorio() (numero,
 *      titular, compras, saldo e saldo total).
 * 
 *  (f) Sequencia no main: 
 * 
 *      Lucas (101, R$ 20) compra Coxinha
 *      6,50, Suco natural 7,00, tenta Pao de queijo 8,00 e
 *      recarrega 30. 
 * 
 *      Marina (102, R$ 50) tenta recarregar 250 e
 *      compra Prato feito 22,00. 
 * 
 *      Pedro (103, R$ 0) tenta Agua
 *      3,00, recarrega 15 e compra Agua 3,00.
 * 
 *  (g) Referencia do relatorio: Lucas 2 compras, R$ 36,50 -
 *      Marina 1 compra, R$ 28,00 - Pedro 1 compra, R$ 12,00 -
 *      total R$ 76,50.
 *
 *  CRITERIOS (0,5 cada):
 *  [ ] Saldo so muda por recarregar e comprar (sem setter).
 *  [ ] Regras de recarga e de saldo insuficiente funcionando.
 *  [ ] Cantina guarda os cartoes em array e gera o relatorio.
 *  [ ] Mensagens com printf e valores iguais a referencia.
 * ================================================================ */

// Escreva aqui as classes de apoio (SEM a palavra public antes de class).




package lista004;

class CartaoCantina {
    private int numero;
    private String titular;
    private double saldo;
    private int totalCompras;

    public CartaoCantina(int numero, String titular, double saldoInicial) {
        this.numero = numero;
        this.titular = titular;
        
        if (saldoInicial < 0) {
            System.out.println("Erro: Saldo inicial não pode ser negativo.");
            this.saldo = 0;
        } else {
            this.saldo = saldoInicial;
        }
        this.totalCompras = 0;
    }

    public void recarregar(double valor) {
        if (valor < 0.01 || valor > 200.00) {
            System.out.println("Recusa de recarga: Valor R$ " + valor + " fora do limite permitido (R$ 0,01 a R$ 200,00).");
        } else {
            saldo += valor;
            System.out.printf("Recarga de R$ %.2f aprovada para %s. Novo saldo: R$ %.2f\n", valor, titular, saldo);
        }
    }

    public boolean comprar(String item, double preco) {
        if (saldo < preco) {
            System.out.printf("Saldo insuficiente para %s (R$ %.2f). Saldo atual: R$ %.2f\n", item, preco, saldo);
            return false;
        } else {
            saldo -= preco;
            totalCompras++;
            System.out.printf("Compra aprovada: %s R$ %.2f | Saldo: R$ %.2f\n", item, preco, saldo);
            return true;
        }
    }

    public int getNumero() {
        return numero;
    }

    public String getTitular() {
        return titular;
    }

    public double getSaldo() {
        return saldo;
    }

    public int getTotalCompras() {
        return totalCompras;
    }
}

class Cantina {
    private CartaoCantina[] cartoes;
    private int contadorCartoes;

    public Cantina(int capacidade) {
        cartoes = new CartaoCantina[capacidade];
        contadorCartoes = 0;
    }

    public void cadastrar(CartaoCantina c) {
        if (contadorCartoes < cartoes.length) {
            cartoes[contadorCartoes] = c;
            contadorCartoes++;
        } else {
            System.out.println("Cantina cheia! Não é possível cadastrar mais cartões.");
        }
    }

    public void relatorio() {
        System.out.println("\n========== RELATÓRIO DA CANTINA ==========");
        double saldoTotalCantina = 0;
        
        for (int i = 0; i < contadorCartoes; i++) {
            CartaoCantina c = cartoes[i];
            System.out.printf("- %s (%d): %d compras, R$ %.2f em saldo\n", 
                c.getTitular(), c.getNumero(), c.getTotalCompras(), c.getSaldo());
            saldoTotalCantina += c.getSaldo();
        }
        
        System.out.printf("------------------------------------------\n");
        System.out.printf("Saldo total nos cartões: R$ %.2f\n", saldoTotalCantina);
        System.out.println("==========================================");
    }
}

public class Exercicio05 {
    public static void main(String[] args) {
        Cantina cantina = new Cantina(3);

        CartaoCantina c1 = new CartaoCantina(101, "Lucas", 20.00);
        cantina.cadastrar(c1);
        c1.comprar("Coxinha", 6.50);
        c1.comprar("Suco natural", 7.00);
        c1.comprar("Pão de queijo", 8.00);
        c1.recarregar(30.00);

        CartaoCantina c2 = new CartaoCantina(102, "Marina", 50.00);
        cantina.cadastrar(c2);
        c2.recarregar(250.00);
        c2.comprar("Prato feito", 22.00);

        CartaoCantina c3 = new CartaoCantina(103, "Pedro", 0.00);
        cantina.cadastrar(c3);
        c3.comprar("Água", 3.00);
        c3.recarregar(15.00);
        c3.comprar("Água", 3.00);

        cantina.relatorio();
    }
}
