package ex012;

public class ex002 {
    public static void main (String[]args){
        int codigoPedido = 3;
        String nomeLanche = "Inválido";
        double precoLanche = 0;

        switch (codigoPedido) {
            case 1:
                nomeLanche = "Cachorro-Quente";
                precoLanche = 8.0;
                break;

            case 2:
                nomeLanche = "X-Salada";
                precoLanche = 14.50;
                break;

            case 3:
                nomeLanche = "X-Bacon";
                precoLanche = 17.0;
                break;
        
            case 4:
                nomeLanche = "Hamburguer Simples";
                precoLanche = 11.0;
                break;
        
            case 5:
                nomeLanche = "Refrigerante Lata";
                precoLanche = 5.0;
                break;

            default:
                System.out.println("ERRO: codigo de lanche invalido. Escolha de 1 a 5.");
                break;
        }

        System.out.println("====== LANCHONETE DO ZE ======");

        if (codigoPedido >= 1 && codigoPedido <= 5) {
            System.out.println("Código escolhido: " + codigoPedido);
            System.out.println("Lanche: " + nomeLanche);
            System.out.printf("Preço unitário: R$%.2f%n", precoLanche);
            System.out.println("Deseja batata frita junto? [S/N]");
        }
    }
    
}
