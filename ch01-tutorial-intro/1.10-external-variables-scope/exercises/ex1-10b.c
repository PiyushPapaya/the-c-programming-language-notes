#include <stdio.h>

#define TAB 4

int main(void)
{
    int c;
    int position = 0;

    while ((c = getchar()) != EOF)
    {
        if (c == '\t')
        {
            int spaces = TAB - (position % TAB);

            for (int i = 0; i < spaces; i++)
            {
                printf(" ");
            }

            position += spaces;
        }
        else if (c == '\n')
        {
            printf("\n");
            position = 0;
        }
        else
        {
            printf("%c", c);
            position++;
        }
    }

    return 0;
}