#include <stdio.h>

#define MAX 100

int getline(char s[], int lim);
void copy(char to[], char from[]);

int len;
int max = 0;
char current[MAX];
char highest[MAX];

int main(void)
{
    int c;

    while ((len = getline(current, MAX)) > 0) {
        if (len == MAX - 1) {
            while ((c = getchar()) != '\n' && c != EOF)
                ++len;

            if (c == '\n')
                ++len;
        }


        if (len > max) {
            max = len;
            copy(highest, current);
        }
    }

    if (max > 0) {
        printf("Length: %d\n%s", max, highest);
    }

    return 0;
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

    if (c == '\n') {
        s[i] = c;
        ++i;
    }

    s[i] = '\0';

    return i;
}

void copy(char to[], char from[])
{
    int i = 0;

    while ((to[i] = from[i]) != '\0')
        ++i;
}