#include <stdio.h>

int main(void)
{
    int c, prevchar = ' ';
    while ((c = getchar()) != EOF)
    {
        if (prevchar != ' ' || c != ' ')
        {
            printf("%c", c);
        }

        prevchar = c;
    }
}