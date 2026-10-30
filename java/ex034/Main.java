
public class Main {
    public static void main(String[] args) {
        Caneta c1 = new Caneta();
        c1.modelo = "Bic";
        c1.cor = "Azul";

        c1.ponta = 0.5;
        c1.carga = 100;

        c1.tampada = true;
        
        c1.status();
        c1.rabiscar();
        
        // Caneta c2 = new Caneta();
        // c2.modelo = "Bic";
        // c2.cor = "Vermelho";
        // c2.ponta = 2;
        // c2.carga = 100;
        // c2.tampada = false;
        // c2.status();
        // c2.rabiscar();
    }
}

