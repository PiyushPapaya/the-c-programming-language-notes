#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main(void)
{
    char s1[] = "hello world";
    char s2[] = "el";

    /*
    
    check for all the alphabets in s2, add them into a new array which has the banned words
    compare the s1 with the banned words
    if not banned words, add them into a new string
    */

    char banned[26];
    int bannedindex = 0;

    char news1[100];
    int news1index = 0;
    bool match = false;

    for (int i = 0; i < strlen(s2); i++)
    {
        if (strchr(banned, s2[i]) == NULL)
        {
            banned[bannedindex] = s2[i];
            bannedindex++;
        }
    }

    for (int j = 0; j < strlen(s1); j++)
    {
        match = false;

        for (int k = 0; k < bannedindex; k++)
        {
            if (s1[j] == banned[k])
            {
                match = true;
            }
        }

        if (!match)
        {
            news1[news1index] = s1[j];
            news1index++;
        }
    }

    news1[news1index] = '\0';

    printf("%s\n", news1);
}
