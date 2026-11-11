#include <stdio.h>
#include <stdlib.h>



int main(int argc, char *argv[]) {
    int A, B, soma, subtr, mult, divs;

    printf("Digite o primeiro valor:\n");
    scanf("%d", &A);

    printf("Digite o segundo valor:\n");
    scanf("%d", &B);

    soma = A + B;
    subtr = A - B;
    mult = A * B;
    divs = A / B;

    printf("Resultado:\n");
    printf("Soma: %d.\n", soma);
    printf("Subtração: %d.\n", subtr);
    printf("Multiplicação: %d. \n", mult);
    printf("Divisão: %d \n", divs);

    return 0;
}
