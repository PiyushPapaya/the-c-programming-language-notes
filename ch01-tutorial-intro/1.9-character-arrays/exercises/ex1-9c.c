#include <stdio.h>

#define MAX 100

int getline(char s[], int lim);
int removespaces(char s[]);

char current[MAX];
int len;

int main(void)
{
    while ((len = getline(current, MAX)) > 0)
    {
        int newlen = removespaces(current);

        if (newlen > 0)
        {
            for (int i = 0; i < newlen; i++)
            {
                printf("%c", current[i]);
            }

            printf("\n");
        }
    }

    return 0;
}

int getline(char s[], int lim)
{
    int c, i;

    for (i = 0;
         i < lim - 1 &&
         (c = getchar()) != EOF &&
         c != '\n';
         ++i)
    {
        s[i] = c;
    }

    if (c == '\n')
    {
        s[i] = c;
        ++i;
    }

    s[i] = '\0';

    return i;
}

int removespaces(char s[])
{
    int i = 0;

    while (s[i] != '\0')
        ++i;

    --i;

    if (i >= 0 && s[i] == '\n')
        --i;

    while (i >= 0 && (s[i] == ' ' || s[i] == '\t'))
        --i;

    s[i + 1] = '\n';
    s[i + 2] = '\0';

    return i + 2;
}