#include <stdio.h>
#include <stdlib.h>


float media2(float a, float b) {
    float resultado;
    resultado = (a+b) / 2.0;
    return (resultado);
}


int main(int argc, char const *argv[]) {
    float x,y, media;
    x = 4.0;
    y = 6.0;

    media = media2(x,y);
    printf("Média: %f", media);

    return 0;
}

