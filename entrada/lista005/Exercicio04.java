/* ================================================================
 *  EXERCICIO 04 - Lista 5 - Heranca, polimorfismo, interfaces e static
 *  META Escola Tecnica - Programacao Orientada a Objetos - 2026
 *  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
 *  ---------------------------------------------------------------
 *  BILHETERIA DO CINE META
 *  Um contador compartilhado por todos os objetos e uma classe
 *  utilitaria que nunca e instanciada.
 *
 *  REGRAS OBRIGATORIAS:
 *  (a) Classe Ingresso com private static int totalVendidos =
 *      0, public static final double PRECO_INTEIRA = 32.00 e os
 *      atributos de instancia numero e meia (boolean).
 * 
 *  (b) O construtor incrementa totalVendidos e usa o novo valor
 *      como numero do ingresso.
 * 
 *  (c) double valor(): meia-entrada paga metade de
 *      PRECO_INTEIRA. static int getTotalVendidos().
 * 
 *  (d) Classe final class UtilCinema com construtor private e
 *      os metodos static double aplicarDesconto(double valor,
 *      double percentual) e static String formatarSessao(int
 *      hora, int minuto) (ex.: "19h05").
 * 
 *  (e) No main: mostre a sessao, o total vendido antes de abrir
 *      (0), venda 5 ingressos (2 meias), liste cada um e mostre
 *      faturamento e valor com 10% de desconto de terca.
 * 
 *  (f) Em um comentario, explique por que totalVendidos e
 *      static e numero nao e.
 * 
 *  (g) Cabecalho: "===== BILHETERIA CINE META =====".
 *      Referencia: sessao 19h05 - 5 vendidos - faturamento R$
 *      128,00 - com desconto R$ 115,20.
 *
 *  CRITERIOS (0,5 cada):
 *  [ ] Contador static e constante static final corretos.
 *  [ ] Membros static acessados pelo nome da classe
 *      (Ingresso.getTotalVendidos()).
 *  [ ] UtilCinema com construtor private e so metodos static.
 *  [ ] Valores de referencia e comentario explicativo
 *      presentes.
 * ================================================================ */

// Escreva aqui as classes de apoio (SEM a palavra public antes de class).


/* ================================================================
 * EXERCICIO 04 - Lista 5
 * META Escola Tecnica - Programacao Orientada a Objetos - 2026
 * BILHETERIA DO CINE META
 * ================================================================ */


class Ingresso {

    private static int totalVendidos = 0;
    public static final double PRECO_INTEIRA = 32.00;

    private int numero;
    private boolean meia;

    // Construtor
    public Ingresso(boolean meia) {
        totalVendidos++;
        numero = totalVendidos;
        this.meia = meia;
    }

    // Calcula o valor do ingresso
    public double valor() {
        if (meia) {
            return PRECO_INTEIRA / 2;
        } else {
            return PRECO_INTEIRA;
        }
    }

    // Retorna o numero do ingresso
    public int getNumero() {
        return numero;
    }

    // Retorna se o ingresso e meia-entrada
    public boolean isMeia() {
        return meia;
    }

    // Retorna o total de ingressos vendidos
    public static int getTotalVendidos() {
        return totalVendidos;
    }
}


// Classe utilitaria
final class UtilCinema {

    private UtilCinema() {
    }

    // Aplica desconto percentual
    public static double aplicarDesconto(double valor, double percentual) {
        return valor - (valor * percentual / 100);
    }

    // Formata o horario da sessao
    public static String formatarSessao(int hora, int minuto) {
        return String.format("%02dh%02d", hora, minuto);
    }
}


public class Exercicio04 {

    public static void main(String[] args) {

        System.out.println("===== BILHETERIA CINE META =====");

        // Mostra a sessao
        System.out.println("Sessao: " +
            UtilCinema.formatarSessao(19, 5));

        // Mostra o total antes das vendas
        System.out.println("Total antes das vendas: " +
            Ingresso.getTotalVendidos());

        // Criacao dos 5 ingressos (3 inteiras e 2 meias)
        Ingresso[] ingressos = {
            new Ingresso(false),
            new Ingresso(true),
            new Ingresso(false),
            new Ingresso(true),
            new Ingresso(false)
        };

        double faturamento = 0;

        // Lista os ingressos vendidos
        System.out.println("\n--- INGRESSOS VENDIDOS ---");

        for (Ingresso ingresso : ingressos) {

            System.out.println(
                "Ingresso " + ingresso.getNumero() +
                " | " +
                (ingresso.isMeia() ? "Meia-entrada" : "Inteira") +
                " | R$ " + String.format("%.2f", ingresso.valor())
            );

            faturamento += ingresso.valor();
        }

        // Calcula o desconto de 10%
        double valorComDesconto =
            UtilCinema.aplicarDesconto(faturamento, 10);

        // Exibe os resultados finais
        System.out.println("\nTotal de ingressos vendidos: " +
            Ingresso.getTotalVendidos());

        System.out.printf("Faturamento: R$ %.2f%n", faturamento);

        System.out.printf("Com desconto de 10%%: R$ %.2f%n",
            valorComDesconto);

        /*
         * totalVendidos é static porque é compartilhado
         * por todos os objetos da classe Ingresso.
         *
         * numero não é static porque cada ingresso
         * possui seu proprio numero.
         */
    }
}

