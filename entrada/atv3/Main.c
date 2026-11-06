#include <stdio.h>
#include <stdlib.h>

int main(){
    int count, a, *ponteiro; // ponteiro armazena endereço de memória da variável a

    count = 10; 

    ponteiro = &count; // ponteiro recebe o endereço de memória da variável count

    a = *ponteiro; // a recebe o valor armazenado no endereço de memória apontado pelo ponteiro 


    printf("Valor de count: %d\n", count);
    printf("Valor de a: %d\n", a);
    printf("Valor de ponteiro: %p\n", ponteiro);
    printf("Valor apontado por ponteiro: %d\n", *ponteiro);

    return 0;
}