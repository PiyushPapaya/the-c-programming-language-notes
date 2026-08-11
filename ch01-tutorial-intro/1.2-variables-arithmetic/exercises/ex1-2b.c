#include <stdio.h>

int main(void){
    /*Fahrenheit = c * 9/5 + 32*/
    int lower = 0;
    int upper = 1000;
    int step = 20;
    printf("Celcius to Fahrenheit Converter\n");
    while(lower<= upper){
        float fahrenheit = lower * 9/5.0 + 32;
        printf("%3d\t%7.2f\n", lower, fahrenheit);
        lower = lower + step;
    }
}