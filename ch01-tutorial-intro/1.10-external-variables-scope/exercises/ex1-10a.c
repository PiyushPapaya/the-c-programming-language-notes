#include <stdio.h>

int coloum = 4;
int position = 0;
int main(void)
{
    int c;
    while ((c = getchar()) != EOF)
    {
        if (c == '\t')
        {
            int extra = coloum - (position % coloum);
            for (int i = 0; i < extra; i++)
            {
                printf(" ");
            }
        }
        else if (c == '\n')
        {
            printf("\n");
            position = 0;
        }

        else
        {
            printf("%c", c);
        }

        position++;
    }
}
