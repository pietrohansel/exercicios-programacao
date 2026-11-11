package ex009;

public class ex009 {

    public static void main(String[] args) {

        String nomeAluno = "Rafaela Costa";
        String turma = "3º ano Técnico";

        double notaB1 = 7.5;
        int peso1 = 1;

        double notaB2 = 6.0;
        int peso2 = 2;

        double notaB3 = 8.2;
        int peso3 = 3;

        double notaB4 = 9.4;
        int peso4 = 4;

        int horasTotais = 80;
        int presencas = 68;

        double mediaPonderada =
                (notaB1 * peso1
                + notaB2 * peso2
                + notaB3 * peso3
                + notaB4 * peso4)
                / (peso1 + peso2 + peso3 + peso4);

        double frequencia = 100.0 * presencas / horasTotais;

        String situacao;

        if (mediaPonderada >= 7.0 && frequencia >= 75.0) {
            situacao = "APROVADO DIRETO";
        } else if ((mediaPonderada >= 4.0 && mediaPonderada < 7.0)
                || (frequencia >= 50.0 && frequencia < 75.0)) {
            situacao = "RECUPERAÇÃO";
        } else {
            situacao = "REPROVADO";
        }

        System.out.println("===== BOLETIM ESCOLAR =====");
        System.out.println("Aluno: " + nomeAluno);
        System.out.println("Turma: " + turma);

        System.out.printf("B1: %.1f (peso %d)%n", notaB1, peso1);
        System.out.printf("B2: %.1f (peso %d)%n", notaB2, peso2);
        System.out.printf("B3: %.1f (peso %d)%n", notaB3, peso3);
        System.out.printf("B4: %.1f (peso %d)%n", notaB4, peso4);

        System.out.printf("Média ponderada: %.2f%n", mediaPonderada);
        System.out.printf("Frequência: %.2f%%%n", frequencia);

        System.out.println("Situação: " + situacao);
    }
}