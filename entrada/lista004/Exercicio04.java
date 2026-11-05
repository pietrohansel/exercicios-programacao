package lista004;
/* ================================================================

*  EXERCICIO 04 - Lista 4 - Classes, objetos e encapsulamento
 *  META Escola Tecnica - Programacao Orientada a Objetos - 2026
 *  Atividade para casa - Pontos: 2,0 (atividade total vale 10,0)
 *  ---------------------------------------------------------------
 *  PLAYLIST COM CAPACIDADE PARA 5 MUSICAS
 *  Uma classe que guarda outros objetos dentro de um array,
 *  controlando quantas posicoes estao ocupadas.
 *
 *  REGRAS OBRIGATORIAS:
 *  (a) Classe Musica com titulo, artista e duracaoSegundos
 *      (int), construtor e getters.
 * 
 *  (b) Metodo String duracaoFormatada() que devolve o tempo no
 *      formato "3:45". Dica: minutos = s / 60, segundos = s %
 *      60 e String.format("%d:%02d", ...).
 * 
 *  (c) Classe Playlist com private String nome, private
 *      Musica[] musicas = new Musica[5] e private int
 *      quantidade.
 * 
 *  (d) boolean adicionar(Musica m): guarda na posicao
 *      quantidade e incrementa. Se estiver cheia, imprime
 *      "Playlist cheia! Nao foi possivel adicionar: [titulo]" e
 *      retorna false.
 * 
 *  (e) int duracaoTotal(), Musica maisLonga() e void listar(),
 *      sempre percorrendo so ate quantidade.
 * 
 *  (f) No main: playlist Estudo Focado e 6 tentativas de adicao
 *      com as duracoes 225, 198, 254, 310, 187 e 240 segundos
 *      (a 6a deve ser recusada). Os titulos e artistas sao
 *      livres.
 * 
 *  (g) Cabecalho: "===== MINHA PLAYLIST =====". Referencia:
 *      duracao total 19:34 e mais longa com 5:10.
 *
 *  CRITERIOS (0,5 cada):
 *  [ ] Array de Musica com tamanho 5 e contador quantidade.
 *  [ ] adicionar recusa a 6a musica e retorna false.
 *  [ ] Lacos param em quantidade (nenhum NullPointerException).
 *  [ ] Duracao formatada em minutos:segundos e valores de
 *      referencia corretos.
 * ================================================================ */

// Escreva aqui as classes de apoio (SEM a palavra public antes de class).




class Musica {
    private String titulo;
    private String artista;
    private int duracaoSegundos;

    Musica(String titulo, String artista, int duracaoSegundos) {
        this.titulo = titulo;
        this.artista = artista;
        this.duracaoSegundos = duracaoSegundos;
    }

    String getTitulo() {
        return titulo;
    }

    String getArtista() {
        return artista;
    }

    int getDuracaoSegundos() {
        return duracaoSegundos;
    }

    String duracaoFormatada() {
        int minutos = duracaoSegundos / 60;
        int segundos = duracaoSegundos % 60;
        return String.format("%d:%02d", minutos, segundos);
    }
}

class Playlist {
    private String nome;
    private Musica[] musicas = new Musica[5];
    private int quantidade;

    Playlist(String nome) {
        this.nome = nome;
    }

    boolean adicionar(Musica m) {
        if (quantidade >= musicas.length) {
            System.out.println("Playlist cheia! Nao foi possivel adicionar: " + m.getTitulo());
            return false;
        }

        musicas[quantidade] = m;
        quantidade++;
        return true;
    }

    int duracaoTotal() {
        int total = 0;
        for (int i = 0; i < quantidade; i++) {
            total += musicas[i].getDuracaoSegundos();
        }
        return total;
    }

    Musica maisLonga() {
        if (quantidade == 0) {
            return null;
        }

        Musica longa = musicas[0];
        for (int i = 1; i < quantidade; i++) {
            if (musicas[i].getDuracaoSegundos() > longa.getDuracaoSegundos()) {
                longa = musicas[i];
            }
        }
        return longa;
    }

    void listar() {
        for (int i = 0; i < quantidade; i++) {
            Musica m = musicas[i];
            System.out.println((i + 1) + ". " + m.getTitulo()
                    + " - " + m.getArtista()
                    + " (" + m.duracaoFormatada() + ")");
        }
    }

    String getNome() {
        return nome;
    }
}

public class Exercicio04 {

    public static void main(String[] args) {
        System.out.println("===== MINHA PLAYLIST =====");

        Playlist playlist = new Playlist("Estudo Focado");

        playlist.adicionar(new Musica("Focus", "Artista A", 225));
        playlist.adicionar(new Musica("Study", "Artista B", 198));
        playlist.adicionar(new Musica("Concentracao", "Artista C", 254));
        playlist.adicionar(new Musica("Deep Work", "Artista D", 310));
        playlist.adicionar(new Musica("Revisao", "Artista E", 187));
        playlist.adicionar(new Musica("Extra", "Artista F", 240));

        System.out.println();
        playlist.listar();

        int total = playlist.duracaoTotal();
        int minutos = total / 60;
        int segundos = total % 60;
        System.out.println("Duracao total: " + String.format("%d:%02d", minutos, segundos));

        Musica longa = playlist.maisLonga();
        if (longa != null) {
            System.out.println("Musica mais longa: " + longa.getTitulo()
                    + " (" + longa.duracaoFormatada() + ")");
        }
    }
}