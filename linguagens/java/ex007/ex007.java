package ex007;

public class ex007 {

    public static void main(String[] args) {

        int visualizacoes = 0;

        System.out.println("==== CONTADOR DE VISUALIZAÇÕES ====");

        System.out.println("Passo 1 → visualizações: " + visualizacoes);

        // Atualiza o contador para 3

        visualizacoes++;
        visualizacoes++;
        visualizacoes++;

        System.out.println("Passo 2 → visualizações: " + visualizacoes);

        visualizacoes += 12;

        System.out.println("Passo 3 → visualizações: " + visualizacoes);

        visualizacoes--;

        System.out.println("Passo 4 → visualizações: " + visualizacoes);

        visualizacoes *= 2;

        System.out.println("Passo 5 → visualizações: " + visualizacoes);

        // Saída

        int curtidas = 0;
        int comentarios = 0;
        int compartilhamentos = 0;

        curtidas += 25;

        comentarios++;
        comentarios++;
        comentarios++;

        compartilhamentos += 8;

        System.out.println();

        System.out.println("==== ENGAJAMENTO FINAL ====");

        System.out.printf("%-20s %d%n", "Visualizações:", visualizacoes);
        System.out.printf("%-20s %d%n", "Curtidas:", curtidas);
        System.out.printf("%-20s %d%n", "Comentários:", comentarios);
        System.out.printf("%-20s %d%n", "Compartilhamentos:", compartilhamentos);

    }
}