package ex004;

public class ex004 {
    public static void main(String[] args) {
        String nomePaciente = "Joseph";
        int idade = 29;
        double peso = 72.5;
        double altura = 1.74;
        double imc = peso / (altura*altura); 
        String imcFormatado = "IMC: %.2f".formatted(imc);

        System.out.println("=====Ficha IMC=====");
        System.out.println("Nome: " + nomePaciente);
        System.out.println("Idade: " + idade);
        System.out.println("Altura: " + altura);
        System.out.println("Peso: " + peso + "kg");


        if (imc >= 40) {
            System.out.println("Estado: Obesidade grau III");

        } else if (imc > 35) {
            System.out.println("Estado: Obesidade grau II");

        } else if (imc > 30) {
            System.out.println("Estado: Obesidade grau I");

        } else if (imc > 25) {
            System.out.println("Estado: Sobrepeso");

        } else if (imc > 18) {
            System.out.println("Estado: Peso normal");

        } else {
            System.out.println("Estado: Abaixo do peso");
        }

        System.out.println(imcFormatado);

        System.out.println("Diferença: o int elimina as casas decimais, enquanto o double mantém o valor decimal.");

    }
    
}
