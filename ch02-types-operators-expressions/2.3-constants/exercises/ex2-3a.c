#include <stdio.h>
#include <ctype.h>

#define MAX 100

int main(void)
{
    char hexa[MAX];
    int c;
    long int total = 0;
    int i = 0;

    while ((c = getchar()) != EOF && i < MAX - 1)
    {
        c = tolower(c);

        if (isdigit(c) || (c >= 'a' && c <= 'f') || c == 'x')
        {
            hexa[i] = c;
            ++i;
        }
    }

    hexa[i] = '\0';

    if (hexa[0] == '0' && hexa[1] == 'x')
    {
        int power = 1;

        for (int j = i - 1; j >= 2; --j)
        {
            int value;

            if (hexa[j] >= '0' && hexa[j] <= '9')
                value = hexa[j] - '0';
            else
                value = hexa[j] - 'a' + 10;

            total += value * power;
            power *= 16;
        }

        printf("%ld\n", total);
    }
    else
    {
        printf("Enter valid hex\n");
    }

    return 0;
}
