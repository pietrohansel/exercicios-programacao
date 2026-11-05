import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.println("Digite o saldo inicial: ");
        double saldoInicial = teclado.nextDouble();

        Caixa caixa = new Caixa(saldoInicial);
        char opcao;

        do {
            caixa.LerSaldo();
            caixa.Saque(teclado);


            System.out.print("\nDeseja realizar outra operação? (s/n): ");
            opcao = teclado.next().charAt(0);

        } while (opcao == 's' || opcao == 'S');

        teclado.close();
    }
}
