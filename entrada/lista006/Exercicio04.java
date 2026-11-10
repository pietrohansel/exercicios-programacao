/* ================================================================
 *  EXERCICIO 04 - Lista 6 - SOLID na pratica: refatoracao
 *  META Escola Tecnica - Programacao Orientada a Objetos - 2026
 *  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
 *  ---------------------------------------------------------------
 *  A IMPRESSORA OBRIGADA A MANDAR FAX
 *  A interface Multifuncional e gorda: a impressora simples
 *  precisa fingir que digitaliza e envia fax.
 *
 *  REGRAS OBRIGATORIAS:
 *  (a) Separe em tres interfaces: Impressora, Digitalizador e
 *      Fax.
 *
 *  (b) ImpressoraSimples implementa so Impressora;
 *      MultifuncionalEscritorio implementa as tres.
 *
 *  (c) Crie no main os metodos static imprimirLote(Impressora
 *      i, String[] docs) e digitalizarContrato(Digitalizador
 *      d).
 *
 *  (d) Imprima boletim.pdf e cardapio.pdf nas duas impressoras,
 *      digitalize contrato.pdf e envie um fax na
 *      multifuncional.
 *
 *  (e) Deixe comentada a chamada //
 *      digitalizarContrato(simples); e explique por que o erro
 *      agora aparece na compilacao.
 *
 *  CRITERIOS (0,5 cada):
 *  [x ] Tres interfaces pequenas no lugar da gorda.
 *  [x ] Nenhum metodo vazio ou com excecao para "cumprir
 *      tabela".
 *  [ x] Metodos que recebem so a interface de que precisam.
 *  [x ] Justificativa citando o ISP.
 * ================================================================ */

interface Impressora {
    void imprimir(String documento);
}

interface Digitalizador {
    void digitalizar(String documento);
}

interface Fax {
    void enviarFax(String documento, String numero);
}

class ImpressoraSimples implements Impressora {

    @Override
    public void imprimir(String documento) {
        System.out.println("[IMPRESSORA SIMPLES] imprimindo " + documento);
    }
}

class MultifuncionalEscritorio implements Impressora, Digitalizador, Fax {

    @Override
    public void imprimir(String documento) {
        System.out.println("[MULTIFUNCIONAL] imprimindo " + documento);
    }

    @Override
    public void digitalizar(String documento) {
        System.out.println("[MULTIFUNCIONAL] digitalizando " + documento);
    }

    @Override
    public void enviarFax(String documento, String numero) {
        System.out.println("[MULTIFUNCIONAL] fax de " + documento + " para " + numero);
    }
}

public class Exercicio04 {

    public static void imprimirLote(Impressora i, String[] docs) {
        for (String documento : docs) {
            i.imprimir(documento);
        }
    }

    public static void digitalizarContrato(Digitalizador d) {
        d.digitalizar("contrato.pdf");
    }

    public static void main(String[] args) {
        ImpressoraSimples simples = new ImpressoraSimples();
        MultifuncionalEscritorio multi = new MultifuncionalEscritorio();

        String[] documentos = {"boletim.pdf", "cardapio.pdf"};

        imprimirLote(simples, documentos);
        imprimirLote(multi, documentos);

        digitalizarContrato(multi);
        multi.enviarFax("contrato.pdf", "11987654321");

        // digitalizarContrato(simples);
        // Erro de compilacao: o metodo exige um Digitalizador, mas 'simples'
        // e do tipo ImpressoraSimples, que implementa apenas Impressora.
        // Isso mostra a aplicacao do principio ISP: interfaces menores e
        // especificas evitam forcar classes a implementar comportamentos que
        // nao usam.
    }
}

//  JUSTIFICATIVA (3 a 5 linhas):
//  Principio violado: ISP (Interface Segregation Principle).
//  O que eu mudei: separei Impressora, Digitalizador e Fax em interfaces
//  pequenas e deixei cada classe implementar somente o que realmente usa.
//  Vantagem obtida: evita forcar classes a implementar metodos desnecessarios
//  e reduz erros de compilacao e acoplamento desnecessario.
