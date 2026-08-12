#include <stdio.h>
#define OUT 0
#define IN 1

int main(void)
{

    int c;
    while ((c = getchar()) != EOF)
    {
        if (c != '\t' && c != '\n' && c != ' ')
        {
            printf("%c", c);
        }
        else
        {
            printf("\n");
        }
    }
}