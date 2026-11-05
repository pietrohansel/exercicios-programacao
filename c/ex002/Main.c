#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{

    double A, B;

    printf("Valor de A: ");
    scanf("%lf", &A);

    printf("Valor de B: ");
    scanf("%lf", &B);

    double area = A * B;
    double perimetro = (2 * A) + (2 * B);

    printf("Área: %.2lf\nPerimetro: %.2lf", area, perimetro);

    return 0;
}
