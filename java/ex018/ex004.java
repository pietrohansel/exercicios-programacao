package ex018;

import java.util.Scanner;

public class ex004 {

    public static void main(String[] args) {

        Scanner teclado = new Scanner(System.in);
        int opcao;
        int totalConversoes = 0;

        do {
            System.out.println("====== CONVERSOR DE TEMPERATURA ======");
            System.out.println("1 - Celsius -> Fahrenheit");
            System.out.println("2 - Fahrenheit -> Celsius");
            System.out.println("3 - Celsius -> Kelvin");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opcao: ");
            
            opcao = teclado.nextInt();

            switch (opcao) {
                case 1:
                    System.out.print("Digite a temperatura em Celsius: ");
                    double c1 = teclado.nextDouble();
                    double f1 = c1 * 9.0 / 5 + 32;
                    System.out.printf("%.1f C = %.1f F\n", c1, f1);
                    totalConversoes++;
                    break;

                case 2:
                    System.out.print("Digite a temperatura em Fahrenheit: ");
                    double f2 = teclado.nextDouble();
                    double c2 = (f2 - 32) * 5.0 / 9;
                    System.out.printf("%.1f F = %.1f C\n", f2, c2);
                    totalConversoes++;
                    break;

                case 3:
                    System.out.print("Digite a temperatura em Celsius: ");
                    double c3 = teclado.nextDouble();
                    double k3 = c3 + 273.15;
                    System.out.printf("%.1f C = %.1f K\n", c3, k3);
                    totalConversoes++;
                    break;

                case 0:
                    System.out.println("Encerrando o conversor...");
                    break;

                default:
                    System.out.println("Opcao invalida! Escolha 0, 1, 2 ou 3.");
                    break;
            }
            System.out.println(); 
        } while (opcao != 0);

        System.out.println("Total de conversoes realizadas: " + totalConversoes);
        teclado.close();

    }
}

