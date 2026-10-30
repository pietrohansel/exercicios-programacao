
public class Cinema {
    public boolean validarDados(int idade, String dia, int hora) {
        boolean dadosValidos = true;
        if (idade < 0){
            System.out.println("Idade inválida");
            dadosValidos = false;
        }

        if (!dia.equals("segunda") && !dia.equals("terça") && !dia.equals("quarta")
                && !dia.equals("quinta") && !dia.equals("sexta") && !dia.equals("sábado")
                && !dia.equals("domingo")) {
            System.out.println("Dia inválido");
            dadosValidos = false;
        }

        if (hora < 0 || hora > 23) {
            System.out.println("Horário inválido");
            dadosValidos = false;
        }

        return dadosValidos;
    } 

    public void gerarIngresso(int idade, String dia, int hora) {
        double preco;
        if (idade >= 60) {
            preco = 16;
        } else if (idade >= 13) {
            preco = 24;
        } else {
            preco = 12;
        }

        double desconto = 0;
        if (dia.equals("quarta")) {
            desconto += preco * 0.20;
        }
        if (hora < 16) {
            desconto += 3;
        }
        preco -= desconto;

        System.out.printf("Ingresso\nPreço: R$ %.2f\nDia: %s\nHora: %d\nDesconto: R$ %.2f%n",
                preco, dia, hora, desconto);
    }
}
