#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {

    char str_origem[10];
    char str_destino[10];

    printf("Entre o nome:");
    fgets(str_origem, sizeof(str_origem), stdin);

    strcpy(str_destino, str_origem);

    printf("\n%s\n", str_destino);


    return 0;
}

