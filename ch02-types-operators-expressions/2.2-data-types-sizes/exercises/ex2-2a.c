#include <stdio.h>

int getline(char s[], int lim)

{
    int c;
    for (int i = 0; i < lim - 1; i++)
    {
        if ((c = getchar()) != EOF)
        {
            if (c != '\n')
            {
                s[i] = c;
            }
            else
            {
                break;
            }
        }
        else
        {
            break;
        }
    }
}
