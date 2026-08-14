#include <stdio.h>
int c;
int alphabets[26] = {0};
int main(void)
{
    while ((c = getchar()) != EOF)
    {
        if (c >= 'a' && c <= 'z')
        {
            alphabets[c - 'a']++;
        }
    }

    for (int i = 0; i < 26; i++)
    {
        printf("%c: ", i + 'a');
        for (int j = 0; j < alphabets[i]; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}