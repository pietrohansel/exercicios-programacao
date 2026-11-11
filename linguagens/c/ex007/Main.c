

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char const *argv[]) {
    // char cargo[] = {'c', 'h', 'e', 'f', 'e', '\0'};

    // char cargo[] = "Chefe"; // tamanho 6

    char nome[30]; 
    puts("\nInsira um nome:"); // pega até o primeiro espaço
    fgets(nome, sizeof(nome), stdin);

    printf("%s", nome);

    return 0;


}
