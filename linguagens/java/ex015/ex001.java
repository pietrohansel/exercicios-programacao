package ex015;

import java.util.Scanner;

public class ex001 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        System.out.println("===== BOLETIM ESCOLAR - META =====");

        System.out.print("Digite o nome do aluno: ");
        String nome = teclado.nextLine();

        double somaNotas = 0;
        double maiorNota = 0;
        double menorNota = 10;

        for (int i = 1; i <= 4; i++) {
            System.out.print("Digite a nota do " + i + "o bimestre: ");
            double nota = teclado.nextDouble();
            somaNotas += nota;

            if (nota > maiorNota) maiorNota = nota;
            if (nota < menorNota) menorNota = nota;
        }

        double media = somaNotas / 4;

        String situacao;

        if (media >= 7.0) {
            situacao = "APROVADO";
        } else if (media >= 5.0) {
            situacao = "RECUPERACAO";
        } else {
            situacao = "REPROVADO";
        }

        System.out.printf("Aluno: %s%n", nome);
        System.out.printf("Soma das notas: %.1f%n", somaNotas);
        System.out.printf("Maior nota: %.1f%n", maiorNota);
        System.out.printf("Menor nota: %.1f%n", menorNota);
        System.out.printf("Media final: %.2f%n", media);
        System.out.printf("Situacao: %s%n", situacao);

        teclado.close();
    }
}