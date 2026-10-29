package ex022;

import java.util.Scanner;

public class ex022 {
    public static void main(String[] args) {

        String fruta = "Opção Inválida";
        Scanner valor = new Scanner(System.in);

        System.out.println("Escolha uma fruta: 1 - pera\n2 - maçã");
        int escolha = valor.nextInt();


        switch (escolha) {
            case 1:
                fruta = "pera";
                break;

            case 2:
                fruta = "maçã";
                break;
        
            default:
                break;
        }

        System.out.println(fruta);
        valor.close();
    }
}


