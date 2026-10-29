package ex016;

import java.util.Scanner;

public class ex002 {
    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);

        int quantidadeItens = 0;
        double totalCompra = 0;
        double maiorPreco = 0;

        System.out.println("====== MERCADINHO DA ESQUINA - CAIXA ======");
        System.out.print("Preco do item (0 para encerrar): ");
        double preco = teclado.nextDouble();

        while (preco != 0) {
            if (preco < 0) {
                System.out.println("Preco invalido! Valor ignorado.");
            } else {
                quantidadeItens++;
                totalCompra += preco;

                if (preco > maiorPreco) {
                    maiorPreco = preco;
                }

                System.out.printf("  Item %d registrado: R$ %.2f%n", quantidadeItens, preco);
            }

            System.out.print("Preco do item (0 para encerrar): ");
            preco = teclado.nextDouble();
        }

        if (quantidadeItens == 0) {
            System.out.println("Nenhum item registrado. Caixa fechado.");
        } else {
            double precoMedio = totalCompra / quantidadeItens;

            System.out.println("====== RESUMO DA COMPRA ======");
            System.out.printf("Quantidade de itens: %d%n", quantidadeItens);
            System.out.printf("Total da compra: R$ %.2f%n", totalCompra);
            System.out.printf("Item mais caro: R$ %.2f%n", maiorPreco);
            System.out.printf("Preco medio por item: R$ %.2f%n", precoMedio);
        }

        teclado.close();
    }
}
