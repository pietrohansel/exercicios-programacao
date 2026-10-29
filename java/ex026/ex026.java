package ex026;

public class ex026 {
    public static void main(String[] args) {

        // vetor 
        int n[] = {3,5,8,2}; 

        System.out.println("Total de casas de N" + n.length);

        for (int c = 0; c <= n.length-1; c++ ) {
            System.out.println("Na posiçaõ" + c + "temos o valor" + n[c]);
        }
    }
}
