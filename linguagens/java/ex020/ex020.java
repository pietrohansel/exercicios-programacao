package ex020;
import java.util.Scanner;

public class ex020 {

    public static void main(String[] args) {
        int idade = 30;

        // Entrada e saída

        Scanner teclado = new Scanner(System.in);

        System.out.println("Digite o nome do aluno: ");
        String nome = teclado.nextLine();

        System.out.println("Digite sua nota: ");
        float nota = teclado.nextFloat();

        System.out.printf("A nota de %s é %d", nome, nota);


        // Converte para outros formatos 

        String valor = Integer.toString(idade); 
        System.out.println(valor);

        // float valor = Float.parseFloat(valor);
        // System.out.println(valor);


    }
}

