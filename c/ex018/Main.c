#include <stdio.h>
#include <stdlib.h>

// função 
float arit_avr(float a, float b){
    float calc;
    calc = (a + b) / 2;
    return calc;
}

int main(int argc, char const *argv[])
{
    float result = arit_avr(10, 20);
    printf("Arithmetic Average: %.2f\n", result);
    return 0;
}
