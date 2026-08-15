#include <stdio.h>

#define MAX 100

int getline(char s[], int lim);
char current[];

int main(void)
{
    int len;
    int c;

    while ((len = getline(current, MAX)) > 0)
    {

        if (len == MAX - 1)
        {
            while ((c = getchar()) != '\n' && c != EOF)
                ++len;

            if (c == '\n')
                ++len;
        }

        if (len >= 80)
        {
            printf("Length: %d\n", len);
            printf("%s", current);
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