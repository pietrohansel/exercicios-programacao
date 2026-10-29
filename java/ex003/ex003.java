package ex003;

public class ex003 {
    public static void main(String[] args) { 
            double celsius = 28.5; 
            double fahrenheit = (celsius * 9 / 5) + 32; 
            double kelvin = celsius + 273.15; 
            
            System.out.println("==== CONVERSOR DE TEMPERATURA ===="); 
            
            System.out.printf("Celsius: %.2f °C%n", celsius); 
            System.out.printf("Fahrenheit: %.2f °F%n", fahrenheit); 
            System.out.printf("Kelvin: %.2f K%n", kelvin);
    }
}
