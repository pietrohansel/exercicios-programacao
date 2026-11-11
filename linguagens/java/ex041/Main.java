import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);
        Monitor monitor = new Monitor();

        System.out.println("Monitoramento de temperatura");
        System.out.println("Digite 999 para encerrar.");

        while (true) {
            System.out.print("Temperatura (°C): ");

            if (!teclado.hasNextDouble()) {
                System.out.println("Entrada inválida — digite um número.");
                teclado.next();
                continue;
            }

            double temperatura = teclado.nextDouble();

            if (temperatura == Monitor.SENTINELA) {
                break;
            }

            monitor.processarLeitura(temperatura);
        }

        monitor.exibirResumo();
        teclado.close();
    }
}
