package ex008;  

public class ex008 {
    public static void main(String[] args) {
        
        double valorCompra = 78.50;
        double valorPago = 100.00;
        double troco = valorPago - valorCompra ;
        int trocoInteiro = (int) Math.round(troco);

        int notas200 = trocoInteiro / 200;
        trocoInteiro = trocoInteiro % 200;

        int notas100 = trocoInteiro / 100;
        trocoInteiro = trocoInteiro % 100;

        int notas50 = trocoInteiro / 50;
        trocoInteiro = trocoInteiro % 50;

        int notas20 = trocoInteiro / 20;
        trocoInteiro = trocoInteiro % 20;

        int notas10 = trocoInteiro / 10;
        trocoInteiro = trocoInteiro % 10;

        int notas5 = trocoInteiro / 5;
        trocoInteiro = trocoInteiro % 5;

        int notas2 = trocoInteiro / 2;
        trocoInteiro = trocoInteiro % 2;

        int totalNotas = notas200 + notas100 + notas50 + notas20 + notas10 + notas5 + notas2;

        System.out.println("===== CAIXA - TROCO EM NOTAS =====");

        System.out.printf("Compra   : R$ %.2f%n", valorCompra);
        System.out.printf("Pago     : R$ %.2f%n", valorPago);
        System.out.printf("Troco    : R$ %.2f%n", troco);

        System.out.println("-----------------------------");

        System.out.println("Qtde notas de R$ 200 = " + notas200);
        System.out.println("Qtde notas de R$ 100 = " + notas100);
        System.out.println("Qtde notas de R$  50 = " + notas50);
        System.out.println("Qtde notas de R$  20 = " + notas20);
        System.out.println("Qtde notas de R$  10 = " + notas10);
        System.out.println("Qtde notas de R$   5 = " + notas5);
        System.out.println("Qtde notas de R$   2 = " + notas2);

        System.out.println("-----------------------------");

        System.out.println("Total de notas entregues: " + totalNotas);

        if (trocoInteiro > 0) {
            System.out.println("Valor restante sem nota disponível: R$ " + trocoInteiro);

    }

}
    
}

