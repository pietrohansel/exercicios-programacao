#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[])
{

    int cont = 0;

     while (cont != 3)
    {
        printf("%d\n", cont);
        cont++;
    }
    
    cont = 0;

    do
    {
        printf("%d\n", cont);
        cont++;
    } while (cont != 3);
    

    return 0;

}
