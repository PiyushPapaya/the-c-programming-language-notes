#include <stdio.h>
float coverter(int celcius);

int main(void)
{

    int c = getchar();
    printf("%c , %f\n", c, coverter(c));
}

float coverter(int celcius)
{

    float fahrenheit = celcius * 9 / 5.0 + 32;
    return fahrenheit;
}