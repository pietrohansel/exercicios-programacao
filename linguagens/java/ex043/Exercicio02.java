/* ================================================================
-  EXERCICIO 02 - Lista 6 - SOLID na pratica: refatoracao
-  META Escola Tecnica - Programacao Orientada a Objetos - 2026
-  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
-  ---------------------------------------------------------------
-  FRETE DOS CORREIOS CHEIO DE IF-ELSE
-  Toda modalidade nova obriga a abrir o metodo calcular e
-  acrescentar mais um else if.
 *
-  REGRAS OBRIGATORIAS:
-  (a) Crie a interface ModalidadeFrete com double
-      calcular(double pesoKg) e String nome().
- 
-  (b) Uma classe por modalidade: Pac (18,00 + 2,50 x kg),
-      Sedex (28,00 + 4,00 x kg) e RetiradaLoja (0,00).
- 
-  (c) CalculadoraFrete passa a receber a modalidade:
-      calcular(ModalidadeFrete m, double pesoKg).
- 
-  (d) Prova do OCP: sem alterar CalculadoraFrete, acrescente
-      Motoboy: R$ 12,00 ate 5 kg; acima disso, 12,00 + 3,00
-      por kg excedente.
- 
-  (e) Mostre a tabela para 3 kg e 8 kg. Referencia (3 kg):
-      25,50 - 40,00 - 0,00 - 12,00. Motoboy com 8 kg: 21,00.
 *
-  CRITERIOS (0,5 cada):
-  [X] Interface com uma classe por modalidade.
-  [X] Nenhum if por tipo dentro de CalculadoraFrete.
-  [X] Motoboy adicionado sem editar o nucleo.
-  [X] Valores de referencia e justificativa citando o OCP.
- ================================================================ */


interface ModalidadeFrete {
    double calcular(double pesoKg);
    String nome();
}


class Pac implements ModalidadeFrete {
    public double calcular(double pesoKg) {
        return 18.00 + 2.50 * pesoKg;
    }
    public String nome() {
        return "PAC";
    }
}

class Sedex implements ModalidadeFrete {
    public double calcular(double pesoKg) {
        return 28.00 + 4.00 * pesoKg;
    }
    public String nome() {
        return "SEDEX";
    }
}

class RetiradaLoja implements ModalidadeFrete {
    public double calcular(double pesoKg) {
        return 0.00;
    }
    public String nome() {
        return "RETIRADA";
    }
}

class Motoboy implements ModalidadeFrete {
    public double calcular(double pesoKg) {
        if (pesoKg <= 5) {
            return 12.00;
        } else {
            return 12.00 + 3.00 * (pesoKg - 5);
        }
    }
    public String nome() {
        return "MOTOBOY";
    }
}


class CalculadoraFrete {
    public double calcular(ModalidadeFrete m, double pesoKg) {
        return m.calcular(pesoKg); // Polimorfismo em acao!
    }
}

public class Exercicio02 {
    public static void main(String[] args) {
        CalculadoraFrete calc = new CalculadoraFrete();
        
        ModalidadeFrete pac = new Pac();
        ModalidadeFrete sedex = new Sedex();
        ModalidadeFrete retirada = new RetiradaLoja();
        ModalidadeFrete motoboy = new Motoboy();

        // (e) Mostrando a tabela para 3 kg e 8 kg
        System.out.println("=== TABELA DE FRETES PARA 3 KG ===");
        System.out.printf("%s: R$ %.2f%n", pac.nome(), calc.calcular(pac, 3));
        System.out.printf("%s: R$ %.2f%n", sedex.nome(), calc.calcular(sedex, 3));
        System.out.printf("%s: R$ %.2f%n", retirada.nome(), calc.calcular(retirada, 3));
        System.out.printf("%s: R$ %.2f%n", motoboy.nome(), calc.calcular(motoboy, 3));

        System.out.println("\n=== TESTE MOTOBOY COM 8 KG ===");
        System.out.printf("%s (8 kg): R$ %.2f%n", motoboy.nome(), calc.calcular(motoboy, 8));
    }
}

/* JUSTIFICATIVA (3 a 5 linhas):
-  Principio violado: Open-Closed Principle (OCP) - originalmente, adicionar novas modalidades exigia modificar o codigo existente com blocos if-else.
-  O que eu mudei: Extraí o comportamento de calculo para uma interface (ModalidadeFrete) e criamos classes isoladas para cada frete, inclusive a nova classe Motoboy.
-  Vantagem obtida: O sistema agora esta fechado para modificacoes e aberto para extensoes; podemos criar novos tipos de frete criando novas classes sem alterar o nucleo da calculadora.
 */