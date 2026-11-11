package ex011;

public class ex001 {
    public static void main(String[] args) {
        double valorCompra = 320.00;
        double valorDesconto;
        double valorFinal;
        double percentualDesconto;

        if (valorCompra < 100.00) {
            percentualDesconto = 0.0;
        } else if (valorCompra < 250.00) {
            percentualDesconto = 0.05;
        } else if (valorCompra < 500.00) {
            percentualDesconto = 0.10;
        } else {
            percentualDesconto = 0.15;
        }

        valorDesconto = valorCompra * percentualDesconto;
        valorFinal = valorCompra - valorDesconto;

        System.out.println("===== LOJA DO BAIRRO - CUPOM FISCAL =====");

        System.out.printf("Valor original da compra: R$ %.2f%n", valorCompra);
        System.out.printf("Percentual de desconto: %.0f%%%n", percentualDesconto * 100);
        System.out.printf("Valor do desconto: R$ %.2f%n", valorDesconto);
        System.out.printf("Valor FINAL a pagar: R$ %.2f%n", valorFinal);

        System.out.println("Faixa aplicada: " + (int)(percentualDesconto * 100) + "%");

    }
}
