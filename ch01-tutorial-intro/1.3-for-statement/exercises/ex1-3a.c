#include <stdio.h>

int main(void){
    /*Fahrenheit = c * 9/5 + 32*/
    for ( int i = 300; i >= 0; i = i - 10){
    float fahrenheit = i * 9/5.0 + 32;
    printf("%3d\t%7.2f\n", i, fahrenheit);
    }
}