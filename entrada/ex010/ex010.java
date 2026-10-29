public class ex010 {
    public static void main(String[] args) {

        double a = 23.0;
        double b = 7.0;

        System.out.println("==== CALCULADORA ARITMÉTICA ====");

        // 5 operações
        System.out.println("Adição: " + (a + b));
        System.out.println("Subtração: " + (a - b));
        System.out.println("Multiplicação: " + (a * b));
        System.out.printf("Divisão: %.4f%n", (a / b));
        System.out.println("Resto: " + (a % b));

        System.out.println("Valor de a: " + a);
        System.out.println("++a: " + (++a));
        System.out.println("Valor de a depois: " + a);

        System.out.println("Valor de b: " + b);
        System.out.println("b--: " + (b--));
        System.out.println("Valor de b depois: " + b);

        System.out.println("++a aumenta antes de usar; b-- usa o valor antes de diminuir.");

        double quadradoA = a * a;
        double cuboA = a * a * a;
        double mediaAritmetica = (a + b) / 2;

        System.out.println("Quadrado de A: " + quadradoA);
        System.out.println("Cubo de A: " + cuboA);
        System.out.println("Média: " + mediaAritmetica);
    }
}
