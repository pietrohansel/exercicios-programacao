public class Monitor {

    public static final double SENTINELA = 999.0;

    private static final double TEMPERATURA_MINIMA = 18.0;
    private static final double TEMPERATURA_MAXIMA = 30.0;
    private static final double LIMITE_INFERIOR_VALIDO = 0.0;
    private static final double LIMITE_SUPERIOR_VALIDO = 60.0;

    private int leiturasValidas;
    private int leiturasInvalidas;
    private int vezesAquecimento;
    private int vezesVentilacao;
    private int vezesEstavel;

    private double menorTemperatura = Double.POSITIVE_INFINITY;
    private double maiorTemperatura = Double.NEGATIVE_INFINITY;

    public void processarLeitura(double temperatura) {
        if (temperatura < LIMITE_INFERIOR_VALIDO || temperatura > LIMITE_SUPERIOR_VALIDO) {
            leiturasInvalidas++;
            System.out.println("Leitura inválida — ignorada.");
            return;
        }

        leiturasValidas++;

        if (temperatura < menorTemperatura) {
            menorTemperatura = temperatura;
        }
        if (temperatura > maiorTemperatura) {
            maiorTemperatura = temperatura;
        }

        if (temperatura < TEMPERATURA_MINIMA) {
            vezesAquecimento++;
            System.out.println("Ligar aquecimento.");
        } else if (temperatura > TEMPERATURA_MAXIMA) {
            vezesVentilacao++;
            System.out.println("Ligar ventilação.");
        } else {
            vezesEstavel++;
            System.out.println("Manter o sistema estável.");
        }
    }

    public void exibirResumo() {
        System.out.println("\n--- Resumo do monitoramento ---");
        System.out.println("Leituras válidas: " + leiturasValidas);

        if (leiturasValidas == 0) {
            System.out.println("Nenhuma leitura válida foi recebida.");
        } else {
            System.out.printf("Menor temperatura válida: %.1f °C%n", menorTemperatura);
            System.out.printf("Maior temperatura válida: %.1f °C%n", maiorTemperatura);
        }

        System.out.println("Aquecimento indicado: " + vezesAquecimento + " vez(es)");
        System.out.println("Ventilação indicada: " + vezesVentilacao + " vez(es)");
        System.out.println("Sistema estável: " + vezesEstavel + " vez(es)");
        System.out.println("Leituras inválidas: " + leiturasInvalidas);
    }
}
