#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int num;

    printf("Digite um número: ");
    scanf("%d", &num);

    switch (num) {
        case (1):
            printf("Vc digitou o número 1");
            break;
            
        case (2):
            printf("Vc digitou o número 2");
            break;


        default:
            printf("Você não digitou 1 e nem 2");
            break;
        }

    return 0;
}
