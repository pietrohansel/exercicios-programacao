import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        Cinema cinema = new Cinema();

        while (true) {
            System.out.print("Idade (-1 para encerrar): ");
            int idade = entrada.nextInt();
            if (idade == -1) {
                break;
            }
            entrada.nextLine();

            System.out.print("Dia da semana: ");
            String dia = entrada.nextLine().trim().toLowerCase();

            System.out.print("Hora da sessão (0 a 23): ");
            int hora = entrada.nextInt();

            if (cinema.validarDados(idade, dia, hora)) {
                cinema.gerarIngresso(idade, dia, hora);
            }
        }

        entrada.close();
    }
}
