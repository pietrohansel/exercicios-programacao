package ex013;

public class ex003 {
    public static void main(String[] args) {
        int numeroTabuada = 7;
        int somaAcumulada = 0;

        System.out.println("===== TABUADA DO " + numeroTabuada + " =====");

        for (int i = 1; i <= 10; i++) {
            int resultado = numeroTabuada * i;
            System.out.printf("%d + %2d = %3d%n", numeroTabuada,i,resultado);

            somaAcumulada += resultado;

        }

        double mediaAritmetica = somaAcumulada / 10;

        System.out.println("Soma de todos os resultados: " + somaAcumulada);

        System.out.printf("Média Aritmética: %.1f%n", mediaAritmetica);

    }
}
