/* ================================================================
 *  EXERCICIO 01 - Lista 5 - Heranca, polimorfismo, interfaces e static
 *  META Escola Tecnica - Programacao Orientada a Objetos - 2026
 *  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
 *  ---------------------------------------------------------------
 *  FOLHA DE PAGAMENTO DA ESCOLA
 *  Uma superclasse e duas subclasses que reaproveitam o calculo
 *  da mae e acrescentam o que e delas.
 *
 *  REGRAS OBRIGATORIAS:
 *  (a) Classe Funcionario com protected String nome e protected
 *      double salarioBase, construtor, double calcularSalario()
 *      (retorna o salario base), String getCargo() e void
 *      exibir().
 * 
 *  (b) Classe Professor extends Funcionario com horasAula (int)
 *      e valorHora. Salario = super.calcularSalario() +
 *      horasAula * valorHora.
 * 
 *  (c) Classe Coordenador extends Funcionario com gratificacao
 *      (percentual, ex.: 0.20). Salario =
 *      super.calcularSalario() * (1 + gratificacao).
 * 
 *  (d) Os construtores das filhas comecam com super(nome,
 *      salarioBase).
 * 
 *  (e) No main, monte um array Funcionario[] com: Rita Gomes
 *      (R$ 2.200), Joao Melo (Professor, base R$ 1.800, 80 h a
 *      R$ 35) e Sonia Ramos (Coordenadora, base R$ 4.500, 20%).
 * 
 *      Percorra chamando exibir() e somando a folha.
 *  (f) Cabecalho: "===== FOLHA DE PAGAMENTO - META =====".
 *      Referencia: 2.200,00 - 4.600,00 - 5.400,00 - total
 *      12.200,00.
 *
 *  CRITERIOS (0,5 cada):
 *  [ ] Duas subclasses com extends e super(...) no construtor.
 *  [ ] calcularSalario() sobrescrito com @Override e
 *      super.calcularSalario().
 *  [ ] getCargo() sobrescrito em cada filha.
 *  [ ] Array da superclasse percorrido e total correto.
 * ================================================================ */

// Escreva aqui as classes de apoio (SEM a palavra public antes de class).

/**
 * InnerExercicio01
 */




class Funcionario {
    protected String nome;
    protected double salarioBase;
    

    public Funcionario(String nome, double salarioBase){
        this.nome = nome;
        this.salarioBase = salarioBase;
    
    }

    double calcularSalario(){
        return salarioBase;
    }

    String getCargo(){
        return "Funcionário";
    }

    void exibir(){
        System.out.printf("===== FOLHA DE PAGAMENTO - META =====\nSalário base: %.2f\nSalário: %.2f ", salarioBase, calcularSalario());
    }
}


class Professor extends Funcionario{
    public int horasAula;
    public double valorHora;


    Professor(String nome, double salarioBase, int horasAula, double valorHora) {
        super(nome, salarioBase);
        this.horasAula = horasAula;
        this.valorHora = valorHora;
    
    }

        @Override 

        String getCargo(){
            return "Professor";
        }


        double calcularSalario(){
            return super.calcularSalario() + horasAula * valorHora;
        }
}


class Coordenador extends Funcionario{
    private double gratificacao;

    Coordenador(String nome, double salarioBase, double gratificacao){
        super(nome, salarioBase);
        this.gratificacao = gratificacao;
    }

        @Override

        String getCargo(){
            return "Coordenador";
        }

        double calcularSalario(){
            return super.calcularSalario() + (1 + gratificacao);
        }

}



public class Exercicio01 {

    public static void main(String[] args) {
        // ====== ESCREVA SUA SOLUCAO ABAIXO ======

        Funcionario[] funcionarios = new Funcionario[3];

        funcionarios[0] = new Funcionario("Rita Gomes", 2200);

        funcionarios[1] = new Professor("Joao Melo", 1800, 80, 35);

        funcionarios[2] = new Coordenador("Sonia Ramos", 4500, 0.20);


        for (int i = 0; i < funcionarios.length; i++){
            funcionarios[i].exibir();
        }

    }
}
