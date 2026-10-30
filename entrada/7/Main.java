import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        ContaEnergia c1 = new ContaEnergia();

        while (true) {
            System.out.print("Consumo de energia em kWh (-1 para sair): ");
            float consumo_energia_kwh = entrada.nextFloat();
            if (consumo_energia_kwh == -1) {
                break;
            }

            if (c1.validarConsumo(consumo_energia_kwh)) {
                float valor_conta = c1.calcularFaixaConsumo(consumo_energia_kwh);
                System.out.printf("Valor da conta: R$ %.2f%n", valor_conta);
            }
        }

        entrada.close();

    }
}
