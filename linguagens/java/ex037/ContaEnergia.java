public class ContaEnergia {
    public boolean validarConsumo(float consumo_energia_kwh) {
        if (consumo_energia_kwh < 0) {
            System.out.println("Consumo inválido");
            return false;
        }
        return true;
    }

    public float calcularFaixaConsumo(float consumo_energia_kwh) {
        float valor_por_faixa;
        if (consumo_energia_kwh <= 100) {
            valor_por_faixa = 0.75f;
        } else if (consumo_energia_kwh <= 200) {
            valor_por_faixa = 0.90f;
        } else if (consumo_energia_kwh <= 300) {
            valor_por_faixa = 1.20f;
        } else {
            valor_por_faixa = 1.20f * 0.8f;
        }
        return consumo_energia_kwh * valor_por_faixa;
    }
}