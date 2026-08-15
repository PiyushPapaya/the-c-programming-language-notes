#include <stdio.h>
#include <stdbool.h>

int main(void)
{
    int c;

    bool textstate = false;
    bool commentstart = false;
    bool commentstate = false;
    bool commentend = false;

    while ((c = getchar()) != EOF)
    {
        if (textstate == true)
        {
            printf("%c", c);

            if (c == '"')
                textstate = false;

            continue;
        }

        if (commentstart == true)
        {
            if (c == '*')
            {
                commentstart = false;
                commentstate = true;
            }
            else
            {
                printf("/");
                printf("%c", c);
                commentstart = false;
            }

            continue;
        }

        if (commentstate == true)
        {
            if (c == '*')
                commentend = true;

            continue;
        }

        if (commentend == true)
        {
            if (c == '/')
            {
                commentend = false;
                commentstate = false;
            }
            else
            {
                commentend = false;

                if (c == '*')
                    commentend = true;
            }

            continue;
        }

        if (c == '"')
        {
            printf("%c", c);
            textstate = true;
        }
        else if (c == '/')
        {
            commentstart = true;
        }
        else
        {
            printf("%c", c);
        }
    }

    if (commentstart == true)
        printf("/");

    return 0;
}