package ex005;

public class ex005 {

    public static void main(String[] args) {

        // Variáveis de entrada

        String nome = "Gavi";
        String cargo = "ADS";

        int horasMes = 123;
        double valorHora = 30.23;
        double valeRefeicao = 450;

        // Descontos

        double salarioBruto = horasMes * valorHora;
        double inss = 0.08 * salarioBruto;
        double irrf = 0.12 * salarioBruto;
        double salarioLiquido = salarioBruto - inss - irrf;

        // Saída

        System.out.println("=== Holerite ===");

        System.out.println("Funcionário: " + nome);
        System.out.println("Cargo: " + cargo);
        System.out.println("Horas/mês: " + horasMes);

        System.out.println("------");

        System.out.printf("Salário bruto: %.2f%n", salarioBruto);
        System.out.printf("INSS: %.2f%n", inss);
        System.out.printf("IRRF: %.2f%n", irrf);
        System.out.printf("Refeição: %.2f%n", valeRefeicao);
        System.out.printf("Salário líquido: %.2f%n", salarioLiquido);
    }
}