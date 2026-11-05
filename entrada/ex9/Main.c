#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{

    int num = 0;

    printf("Digite um número:");
    scanf("%d", &num);
    

    if (num > 1 && num < 3) {
        printf("2");
    
    } else if (! num < 1 && num > 3) {
        printf("Tbm é 2");
    }
    
    
    return 0;
}
