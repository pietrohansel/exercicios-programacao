import java.util.Scanner;

public class Estudante {

    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.print("Quantidade de estudantes: ");
        int qtdEstudantes = teclado.nextInt();

        int aprovados = 0;
        int recuperacao = 0;
        int reprovados = 0;

        for (int i = 1; i <= qtdEstudantes; i++) {
            System.out.println("\nEstudante " + i);

            double n1 = lerNota(teclado, "1ª nota: ");
            double n2 = lerNota(teclado, "2ª nota: ");
            double exame = lerNota(teclado, "Nota do exame final: ");

            double maior = Math.max(n1, n2);
            double menor = Math.min(n1, n2);

            double media = (maior + Math.max(menor, exame)) / 2.0;

            String situacao;
            if (media >= 7.0) {
                situacao = "Aprovado";
                aprovados++;
            } else if (media >= 5.0) {
                situacao = "Recuperação";
                recuperacao++;
            } else {
                situacao = "Reprovado";
                reprovados++;
            }

            System.out.printf("Média final: %.1f - %s%n", media, situacao);
        }

        System.out.println("\nAprovados: " + aprovados);
        System.out.println("Em recuperação: " + recuperacao);
        System.out.println("Reprovados: " + reprovados);

        teclado.close();
    }

    static double lerNota(Scanner teclado, String mensagem) {
        double nota;

        while (true) {
            System.out.print(mensagem);

            if (teclado.hasNextDouble()) {
                nota = teclado.nextDouble();

                if (nota >= 0 && nota <= 10) {
                    return nota;
                }

                System.out.println("Nota inválida! Digite um valor entre 0 e 10.");
            } else {
                System.out.println("Entrada inválida! Digite um número.");
                teclado.next();
            }
        }
    }
}