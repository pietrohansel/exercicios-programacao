/* ================================================================
 *  EXERCICIO 05 - Lista 5 - Heranca, polimorfismo, interfaces e static
 *  META Escola Tecnica - Programacao Orientada a Objetos - 2026
 *  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
 *  ---------------------------------------------------------------
 *  CLINICA VETERINARIA PATA AMIGA
 *  Use todo o Modulo 2 no mesmo programa: abstrata, interface,
 *  polimorfismo, instanceof e static.
 *
 *  REGRAS OBRIGATORIAS:
 *  (a) abstract class Animal com nome, idadeAnos, os abstratos
 *      String emitirSom() e double precoConsulta(), e o
 *      concreto void apresentar().
 * 
 *  (b) interface Vacinavel com void vacinar(String vacina) e
 *      int totalVacinas().
 * 
 *  (c) Cachorro (consulta R$ 120, "Au au!") e Gato (R$ 100,
 *      "Miau!") estendem Animal e implementam Vacinavel. Peixe
 *      (R$ 60) so estende Animal.
 * 
 *  (d) Classe Clinica com private static int atendimentosDoDia,
 *      faturamento e contador de vacinas. O metodo
 *      atender(Animal a, String vacina) apresenta o animal,
 *      soma a consulta e, se a instanceof Vacinavel v, aplica a
 *      vacina; senao imprime que nao precisa.
 * 
 *  (e) No main: fila Animal[] com Thor (cachorro, 3), Mimi
 *      (gato, 2), Nemo (peixe, 1) e Luna (cachorro, 5); atenda
 *      todos com a vacina "Antirrabica" e feche o caixa.
 * 
 *  (f) Cabecalho: "===== CLINICA VETERINARIA PATA AMIGA =====".
 *      Referencia: 4 atendimentos - 3 vacinas - faturamento R$
 *      400,00.
 *
 *  CRITERIOS (0,5 cada):
 *  [ ] Hierarquia com classe abstrata e tres subclasses.
 *  [ ] Interface implementada so por quem faz sentido (o peixe
 *      nao).
 *  [ ] instanceof com padrao (a instanceof Vacinavel v) e
 *      contador static.
 *  [ ] Fila polimorfica e fechamento de caixa com os valores de
 *      referencia.
 * ================================================================ */

// Escreva aqui as classes de apoio (SEM a palavra public antes de class).





// Classe Mãe
abstract class Animal {

    // Atributos
    public String nome;
    public int idadeAnos;        


    //Construtor
    public Animal(String nome, int idadeAnos){
        this.nome = nome;
        this.idadeAnos = idadeAnos;
    }

    // Métodos abstratos
    public abstract String emitirSom();

    public abstract double precoConsulta();

    // Método concreto
    public void apresentar() {
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idadeAnos + " anos");
        System.out.println("Som: " + emitirSom());
    }

}



// Clase "Pai"
interface Vacinavel {

    // Métodos 
    void vacinar(String vacina);

    int totalVacinas();

}



// Classe filho
class Cachorro extends Animal implements Vacinavel {

    private int vacinasAplicadas = 0;

    public Cachorro(String nome, int idadeAnos) {
        super(nome, idadeAnos);
    }

    @Override
    public String emitirSom() {
        return "Au au";
    }


    @Override
    public double precoConsulta() {
        return 120.00;
    }

    @Override
    public void vacinar(String vacina) {
        vacinasAplicadas++;
        System.out.println("Vacina aplicada: " + vacina);
        }

    @Override
    public int totalVacinas() {
        return vacinasAplicadas;
    }

}


// Classe filho
class Peixe extends Animal{

    public Peixe(String nome, int idadeAnos) {
        super(nome, idadeAnos);
    }

    @Override
    public String emitirSom() {
        return "Glub, glub";
    }


    @Override
    public double precoConsulta() {
        return 60.00;
    }

}


// Classe filho
class Gato extends Animal implements Vacinavel {

    private int vacinasAplicadas = 0;

    public Gato(String nome, int idadeAnos) {
        super(nome, idadeAnos);
    }

    @Override
    public String emitirSom() {
        return "Miau miau";
    }


    @Override
    public double precoConsulta() {
        return 100.00;
    }

    @Override
    public void vacinar(String vacina) {
        vacinasAplicadas++;
        System.out.println("Vacina aplicada: " + vacina);
        }

    @Override
    public int totalVacinas() {
        return vacinasAplicadas;
    }

}

class Clinica {

    private static int atendimentosDoDia = 0;
    
    private double faturamento = 0.0;

    private int contadorVacinas = 0;


    public void atender(Animal a, String vacina) {

        atendimentosDoDia++;

        a.apresentar();

        faturamento += a.precoConsulta();

        if (a instanceof Vacinavel v) {
            v.vacinar(vacina);

            contadorVacinas++;

        } else {
            System.out.println("Não precisa tomar a vacina");
        }
    }


    public void fecharCaixa() {
        
        System.out.println("\n====== FECHAMENTO DO CAIXA ======");
        
        System.out.println("Atendimentos: " + atendimentosDoDia);

        System.out.println("Vacinas aplicadas: " + contadorVacinas);

        System.out.printf("Faturamento: R$ %.2f%n",faturamento);
    }

}


public class Exercicio05 {

    public static void main(String[] args) {
        // ====== ESCREVA SUA SOLUCAO ABAIXO ======

        System.out.println("===== CLINICA VETERINARIA PATA AMIGA =====");

        Animal[] fila = {
            new Cachorro("Thor",  3),
            new Gato("Mimi", 2),
            new Peixe("Nemo", 1),
            new Cachorro("Luna", 5)

        };

        Clinica clinica = new  Clinica();

        for (Animal a : fila) {
            clinica.atender(a,"Antirrabica");
        }

        clinica.fecharCaixa();

        // ====== FIM DA SUA SOLUCAO ======
    }
}
