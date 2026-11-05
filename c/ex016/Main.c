#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{

    int num = 0;
    
    printf("Digite um número:\n");
    scanf("%d", &num);

    if (num == 1)
    {
        printf("Acertou");

    } else {
        printf("Errou");
    }

    
    return 0;
}
