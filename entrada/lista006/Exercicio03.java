/* ================================================================
 *  EXERCICIO 03 - Lista 6 - SOLID na pratica: refatoracao
 *  META Escola Tecnica - Programacao Orientada a Objetos - 2026
 *  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
 *  ---------------------------------------------------------------
 *  O PINGUIM QUE QUEBRA O PROGRAMA
 *  Pinguim herda voar() e responde com uma excecao. Quem usa
 *  Ave e pego de surpresa.
 *
 *  REGRAS OBRIGATORIAS:
 *  (a) Rode o original e veja a UnsupportedOperationException.
 *
 *  (b) Tire voar() de Ave e crie a interface Voador.
 *
 *  (c) Pardal extends Ave implements Voador; Pinguim extends
 *      Ave e ganha nadar().
 *
 *  (d) No main: todas as aves comem (laco em Ave[]) e so as
 *      voadoras voam (laco em Voador[]), sem usar instanceof.
 *
 *  (e) Deixe comentada a linha // Voador x = new Pinguim(); e
 *      explique por que agora ela nem compila.
 *
 *  CRITERIOS (0,5 cada):
 *  [ x] voar() saiu da superclasse.
 *  [ x] Interface Voador implementada so pelo pardal.
 *  [ x] Programa roda ate o fim sem excecao e sem instanceof.
 *  [ x] Justificativa citando o LSP.
 * ================================================================ */

/**
 **/

interface Voador {
    public String voar();
}

class Ave {
    protected String nome;

    public Ave(String nome) {
        this.nome = nome;
    }

    public void comer() {
        System.out.println(nome + " esta comendo.");
    }
}

class Pardal extends Ave implements Voador {
    public Pardal() {
        super("Pardal");
    }

    @Override
    public String voar() {
        System.out.println(nome + " esta voando.");
        return nome + " voou.";
    }
}

class Pinguim extends Ave {
    public Pinguim() {
        super("Pinguim");
    }

    public String nadar() {
        System.out.println(nome + " esta nadando.");
        return nome + " nadou.";
    }
}

public class Exercicio03 {

    public static void main(String[] args) {
        Ave[] aves = { new Pardal(), new Pinguim() };

        for (Ave a : aves) {
            a.comer();
        }

        Voador[] voadores = { new Pardal() };
        for (Voador v : voadores) {
            v.voar();
        }

        // Voador x = new Pinguim();
        // Nao compila porque Pinguim nao implementa Voador. Se houvesse essa
        // atribuicao, estaríamos violando o Princípio da Substituicao de Liskov
        // (LSP): um objeto que nao sabe voar nao pode ser tratado como um voador.
    }
}

/* JUSTIFICATIVA (3 a 5 linhas):
 *  Principio violado: LSP (princípio da substituição de Liskov).
 *  O que eu mudei: movi voar() para a interface Voador e implementei apenas em Pardal.
 *  Vantagem obtida: cada classe expõe apenas comportamentos que fazem sentido para ela.
 *  Agora o codigo usa somente Ave[] para comer e Voador[] para voar.
 */

