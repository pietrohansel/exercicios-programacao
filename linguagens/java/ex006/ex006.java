package ex006;

public class ex006 {
    public static void main(String[] args) {
        // Variáveis de Entrada
        byte idade = 21;
        short anoConclusaoEM = 2025;
        int numeroInscricao = 1234;
        long cpf = 12143534534L;
        float notaPrimeiraFase = 23.23F;
        double mediaFinalPonderada = 53.34;
        char turno = 'M';
        boolean necessidadeEspecial = false;
        String nomeCandidato = "Bruno";
        // Saída
        System.out.println("==== FICHA DE INSCRIÇÃO VESTIBULAR ====");
        System.out.printf("%-25s %s%n", "Nome:", nomeCandidato);
        System.out.printf("%-25s %d%n", "Idade:", idade);
        System.out.printf("%-25s %d%n", "Ano conclusão EM:", anoConclusaoEM);
        System.out.printf("%-25s %d%n", "Número inscrição:", numeroInscricao);
        System.out.printf("%-25s %d%n", "CPF:", cpf);
        System.out.printf("%-25s %.2f%n", "Nota primeira fase:", notaPrimeiraFase);
        System.out.printf("%-25s %.2f%n", "Média final ponderada:", mediaFinalPonderada);
        System.out.printf("%-25s %c%n", "Turno:", turno);
        System.out.printf("%-25s %b%n", "Necessidade especial:", necessidadeEspecial);

    }
    
}