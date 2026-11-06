#include <stdio.h>
#include <stdlib.h>

void arit_avr(float a, float b){
    float calc;
    calc = (a + b) / 2;
    printf("Arithmetic Average: %.2f\n", calc);
}

int main(){
    arit_avr(10, 20);
    return 0;
}