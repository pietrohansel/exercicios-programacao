/* ================================================================
 *  EXERCICIO 02 - Lista 5 - Heranca, polimorfismo, interfaces e static
 *  META Escola Tecnica - Programacao Orientada a Objetos - 2026
 *  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
 *  ---------------------------------------------------------------
 *  CENTRAL DE ENTREGAS: MOTO, CARRO E DRONE
 *  Uma classe abstrata define o molde; cada tipo de entrega
 *  calcula o proprio frete.
 *
 *  REGRAS OBRIGATORIAS:
 *  (a) abstract class Entrega com codigo e distanciaKm,
 *      construtor, os metodos abstratos double calcularFrete()
 *      e String tipo(), e o metodo concreto void resumo().
 * 
 *  (b) EntregaMoto: frete = 5,00 + 1,20 x km. 
 *      EntregaCarro: 8,00 + 1,80 x km. 
 *      EntregaDrone: 12,00 + 2,50 x km.
 * 
 *  (c) No main: Entrega[] com 
 *      Moto E01 (8 km), 
 *      Carro E02 (25km), 
 *      Drone E03 (4 km) e 
 *      Moto E04 (15 km).
 * 
 *  (d) Em um unico laco: chame resumo(), some os fretes e
 *      descubra a entrega mais cara.
 * 
 *  (e) Deixe comentada a linha // Entrega x = new
 *      Entrega("E99", 1); e explique em um comentario por que
 *      ela nao compila.
 * 
 *  (f) Cabecalho: "===== CENTRAL DE ENTREGAS =====".
 *      Referencia: 14,60 - 53,00 - 22,00 - 23,00 - total R$
 *      112,60 - mais cara E02.
 *
 *  CRITERIOS (0,5 cada):
 *  [ ] Classe abstract com 2 metodos abstratos e 1 concreto.
 *  [ ] Tres subclasses implementando os abstratos com
 *      @Override.
 *  [ ] Um unico laco polimorfico sobre Entrega[].
 *  [ ] Total, entrega mais cara e comentario sobre o new
 *      corretos.
 * ================================================================ */

// Escreva aqui as classes de apoio (SEM a palavra public antes de class).


abstract class Entrega {
    private String codigo;
    protected int distanciaKm;

    Entrega(String codigo, int distanciaKm) {
        this.codigo = codigo;
        this.distanciaKm = distanciaKm;
    }

    abstract double calcularFrete();

    abstract String tipo();

    String getCodigo() {
        return codigo;
    }

    void resumo() {
        System.out.printf("%s (%s) - %d km - Frete: R$ %.2f%n",
                codigo, tipo(), distanciaKm, calcularFrete());
    }
}

class EntregaMoto extends Entrega {

    EntregaMoto(String codigo, int distanciaKm) {
        super(codigo, distanciaKm);
    }

    @Override
    double calcularFrete() {
        return 5.00 + 1.20 * distanciaKm;
    }

    @Override
    String tipo() {
        return "Moto";
    }
}

class EntregaCarro extends Entrega {

    EntregaCarro(String codigo, int distanciaKm) {
        super(codigo, distanciaKm);
    }

    @Override
    double calcularFrete() {
        return 8.00 + 1.80 * distanciaKm;
    }

    @Override
    String tipo() {
        return "Carro";
    }
}

class EntregaDrone extends Entrega {

    EntregaDrone(String codigo, int distanciaKm) {
        super(codigo, distanciaKm);
    }

    @Override
    double calcularFrete() {
        return 12.00 + 2.50 * distanciaKm;
    }

    @Override
    String tipo() {
        return "Drone";
    }
}

public class Exercicio02 {

    public static void main(String[] args) {
        System.out.println("===== CENTRAL DE ENTREGAS =====");

        Entrega[] entregas = new Entrega[4];
        entregas[0] = new EntregaMoto("E01", 8);
        entregas[1] = new EntregaCarro("E02", 25);
        entregas[2] = new EntregaDrone("E03", 4);
        entregas[3] = new EntregaMoto("E04", 15);

        double total = 0;
        Entrega maisCara = null;

        for (Entrega e : entregas) {
            e.resumo();
            total += e.calcularFrete();

            if (maisCara == null || e.calcularFrete() > maisCara.calcularFrete()) {
                maisCara = e;
            }
        }

        System.out.printf("Total: R$ %.2f%n", total);
        System.out.println("Entrega mais cara: " + maisCara.getCodigo()
                + " (" + maisCara.tipo() + ")");
    }
}