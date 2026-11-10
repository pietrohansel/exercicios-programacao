/* ================================================================
 *  EXERCICIO 01 - Lista 6 - SOLID na pratica: refatoracao
 *  META Escola Tecnica - Programacao Orientada a Objetos - 2026
 *  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
 *  ---------------------------------------------------------------
 *  O BOLETIM QUE FAZ TUDO
 *  A classe BoletimService calcula, formata, grava e envia
 *  e-mail. Sao quatro motivos para mudar em uma classe so.
 *
 *  REGRAS OBRIGATORIAS:
 *  (a) Rode o arquivo inicial e anote a saida.
 * 
 *  (b) Divida em quatro classes: CalculadoraMedia,
 *      FormatadorBoletim, RepositorioBoletim e
 *      NotificadorResponsavel, cada uma com um metodo.
 * 
 *  (c) O main passa a orquestrar as quatro (como a
 *      LojaSrpCorreta da Aula 20).
 * 
 *  (d) Referencia: Aluno: Ana | Media: 7,17 | APROVADO, seguido
 *      das linhas [ARQUIVO] e [EMAIL].
 *
 *  CRITERIOS (0,5 cada):
 *  [ ] Quatro classes com uma responsabilidade cada.
 *  [ ] BoletimService original removido ou reduzido a
 *      orquestrador.
 *  [ ] Saida igual a original.
 *  [ ] Justificativa citando o SRP.
 * ================================================================ */

// ====== CODIGO COM PROBLEMA: REFATORE A PARTIR DAQUI ======

/* ================================================================
-  EXERCICIO 01 - Lista 6 - SOLID na pratica: refatoracao
-  META Escola Tecnica - Programacao Orientada a Objetos - 2026
-  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
-  ---------------------------------------------------------------
-  O BOLETIM QUE FAZ TUDO
-  A classe BoletimService calcula, formata, grava e envia
-  e-mail. Sao quatro motivos para mudar em uma classe so.
 *
-  REGRAS OBRIGATORIAS:
-  (a) Rode o arquivo inicial e anote a saida.
- 
-  (b) Divida em quatro classes: CalculadoraMedia,
-      FormatadorBoletim, RepositorioBoletim e
-      NotificadorResponsavel, cada uma com um metodo.
- 
-  (c) O main passa a orquestrar as quatro (como a
-      LojaSrpCorreta da Aula 20).
- 
-  (d) Referencia: Aluno: Ana | Media: 7,17 | APROVADO, seguido
-      das linhas [ARQUIVO] e [EMAIL].
 *
-  CRITERIOS (0,5 cada):
-  [X] Quatro classes com uma responsabilidade cada.
-  [X] BoletimService original removido ou reduzido a
-      orquestrador.
-  [X] Saida igual a original.
-  [X] Justificativa citando o SRP.
- ================================================================ */

class CalculadoraMedia {
    public double calcular(double n1, double n2, double n3) {
        return (n1 + n2 + n3) / 3;
    }
}

class FormatadorBoletim {
    public String formatar(String aluno, double media) {
        return String.format("Aluno: %s | Media: %.2f | %s", aluno, media,
                media >= 7 ? "APROVADO" : "EM RECUPERACAO");
    }
}

class RepositorioBoletim {
    public void salvar(String aluno) {
        System.out.println("[ARQUIVO] gravando boletim_" + aluno + ".txt");
    }
}

class NotificadorResponsavel {
    public void enviar(String aluno) {
        System.out.println("[EMAIL] enviando boletim para o responsavel de " + aluno);
    }
}

public class Exercicio01 {

    public static void main(String[] args) {
        String aluno = "Ana";
        double n1 = 7.0;
        double n2 = 8.5;
        double n3 = 6.0;

        // Instanciando as classes com responsabilidades unicas
        CalculadoraMedia calculadora = new CalculadoraMedia();
        FormatadorBoletim formatador = new FormatadorBoletim();
        RepositorioBoletim repositorio = new RepositorioBoletim();
        NotificadorResponsavel notificador = new NotificadorResponsavel();

        // Orquestrando a execucao
        double media = calculadora.calcular(n1, n2, n3);
        String texto = formatador.formatar(aluno, media);
        
        System.out.println(texto);
        repositorio.salvar(aluno);
        notificador.enviar(aluno);
    }
}

/* JUSTIFICATIVA (3 a 5 linhas):
-  A classe original acumulava calculo, formatacao, persistencia e envio.
-  O que eu mudei: Dividi as responsabilidades em quatro classes especificas (CalculadoraMedia, FormatadorBoletim, RepositorioBoletim e NotificadorResponsavel) e ajustei o main para fazer a orquestracao.
-  Vantagem: facilidae de manutencao
 */
