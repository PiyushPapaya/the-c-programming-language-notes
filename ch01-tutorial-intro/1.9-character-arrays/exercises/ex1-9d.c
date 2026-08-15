#include <stdio.h>

#define MAX 100

int getline(char s[], int lim);
char current[MAX];

int main(void)
{
    int len;
    int c;

    while ((len = getline(current, MAX)) > 0)
    {

        int end = len - 1;

        if (current[end] == '\n')
            --end;

        for (int i = end; i >= 0; --i)
            printf("%c", current[i]);

        printf("\n");

    }
}

int getline(char s[], int lim)
{
    int c, i;

    for (i = 0;
         i < lim - 1 && (c = getchar()) != EOF && c != '\n';
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