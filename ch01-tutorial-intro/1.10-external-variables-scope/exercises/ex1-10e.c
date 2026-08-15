#include <stdio.h>
#include <stdbool.h>

#define MAX 100

int main(void)
{
    int c;

    bool textstate = false;
    bool charstate = false;
    bool commentstart = false;
    bool commentstate = false;
    bool commentend = false;
    bool escape = false;

    char stack[MAX];
    int top = 0;

    while ((c = getchar()) != EOF)
    {
        if (textstate == true)
        {
            if (escape == true)
            {
                escape = false;
                continue;
            }

            if (c == '\\')
            {
                escape = true;
                continue;
            }

            if (c == '"')
                textstate = false;

            continue;
        }

        if (charstate == true)
        {
            if (escape == true)
            {
                escape = false;
                continue;
            }

            if (c == '\\')
            {
                escape = true;
                continue;
            }

            if (c == '\'')
                charstate = false;

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
                commentstart = false;

                if (c == '(' || c == '[' || c == '{')
                {
                    if (top < MAX)
                        stack[top++] = c;
                }
                else if (c == ')' || c == ']' || c == '}')
                {
                    if (top == 0)
                    {
                        printf("Error: unmatched %c\n", c);
                        return 1;
                    }

                    if ((c == ')' && stack[top - 1] != '(') ||
                        (c == ']' && stack[top - 1] != '[') ||
                        (c == '}' && stack[top - 1] != '{'))
                    {
                        printf("Error: mismatched %c\n", c);
                        return 1;
                    }

                    --top;
                }
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
            textstate = true;
        }
        else if (c == '\'')
        {
            charstate = true;
        }
        else if (c == '/')
        {
            commentstart = true;
        }
        else if (c == '(' || c == '[' || c == '{')
        {
            if (top < MAX)
                stack[top++] = c;
            else
            {
                printf("Error: too many nested symbols\n");
                return 1;
            }
        }
        else if (c == ')' || c == ']' || c == '}')
        {
            if (top == 0)
            {
                printf("Error: unmatched %c\n", c);
                return 1;
            }

            if ((c == ')' && stack[top - 1] != '(') ||
                (c == ']' && stack[top - 1] != '[') ||
                (c == '}' && stack[top - 1] != '{'))
            {
                printf("Error: mismatched %c\n", c);
                return 1;
            }

            --top;
        }
    }

    if (textstate == true)
    {
        printf("Error: unmatched double quote\n");
        return 1;
    }

    if (charstate == true)
    {
        printf("Error: unmatched single quote\n");
        return 1;
    }

    if (commentstate == true || commentend == true)
    {
        printf("Error: unmatched comment\n");
        return 1;
    }

    if (commentstart == true)
    {
        if (top < MAX)
            stack[top++] = '/';
    }

    if (top != 0)
    {
        printf("Error: unmatched %c\n", stack[top - 1]);
        return 1;
    }

    printf("No obvious syntax errors found.\n");

    return 0;
}