import java.util.Scanner;

public class Caixa {

    private double saldo;

    public Caixa(double saldoInicial) {
        this.saldo = saldoInicial;
    }

    void LerSaldo() {
        System.out.printf("Saldo: R$ %.2f%n", this.saldo);
    }

    void Saque(Scanner teclado) {
        System.out.print("Digite o valor de saque: ");
        double valor = teclado.nextDouble();

        if (valor <= 0 || valor > this.saldo || valor % 5 != 0) {
            System.out.printf("Valor de saque R$ %.2f inválido%n", valor);
            return;
        }

        this.saldo -= valor;
        System.out.printf("Saque de R$ %.2f efetuado%n", valor);

        CalculaCedulasSaque(valor);

        System.out.printf("Saldo: R$ %.2f%n", this.saldo);
    }

    private void CalculaCedulasSaque(double saque) {
        int c100 = 100, c50 = 50, c20 = 20, c10 = 10, c5 = 5;
        int restante = (int) saque;

        int q100 = restante / c100;
        restante %= c100;

        int q50 = restante / c50;
        restante %= c50;

        int q20 = restante / c20;
        restante %= c20;

        int q10 = restante / c10;
        restante %= c10;

        int q5 = restante / c5;
        restante %= c5;

        System.out.println("Cédulas entregues:");
        if (q100 > 0) System.out.printf("  %d x R$ 100%n", q100);
        if (q50 > 0) System.out.printf("  %d x R$ 50%n", q50);
        if (q20 > 0) System.out.printf("  %d x R$ 20%n", q20);
        if (q10 > 0) System.out.printf("  %d x R$ 10%n", q10);
        if (q5 > 0) System.out.printf("  %d x R$ 5%n", q5);
    }
}
