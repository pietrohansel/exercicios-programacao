#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{
    int vetores[10];

    printf("Digite 10 número:\n");
    for (int i = 0; i < 10; i++)
    {
        scanf("%d", &vetores[i]);
    }

    // acessa os vetores 
    printf("Valores do Array:\n");
    for (int i = 0; i < 10; i++)
    {
        printf("vetores[%d] = %d\n" , i , vetores[i]);
    }
    
    

    return 0;
}
