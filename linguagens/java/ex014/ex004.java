package ex014;

public class ex004 {
    public static void main(String[] args) {
        int numeroInicial = 10;
    
        System.out.println("====== CONTAGEM REGRESSIVA ======");

        if (numeroInicial <= 0) {
            System.out.println("ERRO: Numero invalido! Escolha um numero positivo.");
        }

        int contadorNumeros = 0;

        while (numeroInicial >= 0) {
            System.out.println(numeroInicial);
            contadorNumeros++;
            numeroInicial--;
        }

        System.out.println("BOOM! FELIZ ANO NOVO! FOGOS DE ARTIFICIO!");
        System.out.println("Total de numeros impressos na contagem: " + contadorNumeros);

    }
}
