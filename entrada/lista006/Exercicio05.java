/* ================================================================
 *  EXERCICIO 05 - Lista 6 - SOLID na pratica: refatoracao
 *  META Escola Tecnica - Programacao Orientada a Objetos - 2026
 *  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
 *  ---------------------------------------------------------------
 *  ALARME RESIDENCIAL PRESO A UMA SIRENE
 *  AlarmeCasa cria a propria SireneBarulhenta. Para avisar no
 *  celular, seria preciso reescrever o alarme.
 *
 *  REGRAS OBRIGATORIAS:
 *  (a) Crie a interface Alerta com void disparar(String
 *      mensagem).
 *
 *  (b) Implementacoes: Sirene, NotificacaoCelular (recebe o
 *      numero no construtor) e LuzPiscante.
 *
 *  (c) AlarmeCasa recebe os alertas pelo construtor (Alerta[]
 *      alertas, guardado em atributo private final) e nao usa
 *      new para criar nenhum alerta.
 *
 *  (d) No main, monte o modo viagem (sirene + celular) e o modo
 *      noite (so a luz).
 *
 *  (e) Crie tambem AlertaDeTeste, que so conta os disparos, e
 *      prove que o alarme funciona sem fazer barulho: dois
 *      movimentos devem registrar 2 disparos.
 *
 *
 *  CRITERIOS (0,5 cada):
 *  [x] Interface Alerta com tres implementacoes reais.
 *  [x] Injecao pela construtora; nenhum new de alerta dentro do
 *      alarme.
 *  [x] Dois modos montados so no main, sem mudar AlarmeCasa.
 *  [x] AlertaDeTeste mostrando 2 disparos e justificativa
 *      citando o DIP.
 * ================================================================ */

interface Alerta {
    void disparar(String mensagem);
}

class Sirene implements Alerta {
    @Override
    public void disparar(String mensagem) {
        System.out.println("[SIRENE] UIUUU UIUUU! " + mensagem);
    }
}

class NotificacaoCelular implements Alerta {
    private final long numero;

    NotificacaoCelular(long numero) {
        this.numero = numero;
    }

    @Override
    public void disparar(String mensagem) {
        System.out.println("[CELULAR] Enviando SMS para " + numero + ": " + mensagem);
    }
}

class LuzPiscante implements Alerta {
    @Override
    public void disparar(String mensagem) {
        System.out.println("[LUZ] Pisca-pisca! " + mensagem);
    }
}

class AlertaDeTeste implements Alerta {
    private int disparos = 0;

    @Override
    public void disparar(String mensagem) {
        disparos++;
    }

    public int getDisparos() {
        return disparos;
    }
}

class AlarmeCasa {
    private final Alerta[] alertas;

    AlarmeCasa(Alerta[] alertas) {
        this.alertas = alertas;
    }

    public void detectarMovimento(String comodo) {
        String mensagem = "Movimento detectado na " + comodo;
        for (Alerta alerta : alertas) {
            alerta.disparar(mensagem);
        }
    }
}

public class Exercicio05 {
    public static void main(String[] args) {
        AlarmeCasa modoViagem = new AlarmeCasa(new Alerta[] {
            new Sirene(),
            new NotificacaoCelular(11987654321L) // no Java, int nao comporta esse valor; usar long? 
        });

        AlarmeCasa modoNoite = new AlarmeCasa(new Alerta[] {
            new LuzPiscante()
        });

        System.out.println("Modo viagem:");
        modoViagem.detectarMovimento("sala");

        System.out.println("\nModo noite:");
        modoNoite.detectarMovimento("garagem");

        AlertaDeTeste alertaTeste = new AlertaDeTeste();
        AlarmeCasa alarmeTeste = new AlarmeCasa(new Alerta[] { alertaTeste });

        alarmeTeste.detectarMovimento("quarto");
        alarmeTeste.detectarMovimento("cozinha");

        System.out.println("\nDisparos registrados pelo AlertaDeTeste: " + alertaTeste.getDisparos());
    }
}

/* JUSTIFICATIVA (3 a 5 linhas):
 *  Principio violado: DIP, porque o alarme dependia de uma classe concreta (SireneBarulhenta).
 *  O que eu mudei: criei a interface Alerta e as implementacoes no construtor de AlarmeCasa.
 *  Vantagem obtida: o alarme pode usar sirene, celular, luz ou teste sem alterar sua logica.
 *  Resultado: dois movimentos geram exatamente 2 disparos, sem barulho e sem acoplar a implementacao.
 */
