#include <stdio.h>
#include <string.h>
#include <stdbool.h>

int main(void)
{
    char s1[] = "hello world";
    char s2[] = "e";

    bool match = false;
    int position = -1;

    for (int i = 0; i < strlen(s1); i++) {

        for (int j = 0; j < strlen(s2); j++) {

            if (s1[i] == s2[j]) {
                match = true;
                position = i;
                break;
            }
        }

        if (match) {
            break;
        }
    }

    printf("%d\n", position);
}
