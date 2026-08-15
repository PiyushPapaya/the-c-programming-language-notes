#include <stdio.h>

#define WIDTH 20

int main(void)
{
    int c;
    int position = 0;
    int possiblebreak = -1;
    char array[WIDTH + 1];

    while ((c = getchar()) != EOF)
    {
        if (c == '\n')
        {
            for (int i = 0; i < position; i++)
                printf("%c", array[i]);

            printf("\n");

            position = 0;
            possiblebreak = -1;
            continue;
        }

        array[position] = c;

        if (c == ' ' || c == '\t')
            possiblebreak = position;

        position++;

        if (position == WIDTH)
        {
            if (possiblebreak >= 0)
            {
                for (int i = 0; i < possiblebreak; i++)
                    printf("%c", array[i]);

                printf("\n");

                int newposition = 0;

                for (int i = possiblebreak + 1; i < position; i++)
                {
                    array[newposition] = array[i];
                    newposition++;
                }

                position = newposition;
                possiblebreak = -1;

                for (int i = 0; i < position; i++)
                {
                    if (array[i] == ' ' || array[i] == '\t')
                        possiblebreak = i;
                }
            }
            else
            {
                for (int i = 0; i < position; i++)
                    printf("%c", array[i]);

                printf("\n");

                position = 0;
                possiblebreak = -1;
            }
        }
    }

    if (position > 0)
    {
        for (int i = 0; i < position; i++)
            printf("%c", array[i]);

        printf("\n");
    }

    return 0;
}