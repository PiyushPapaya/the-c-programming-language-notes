#include <stdio.h>

int c, wordcount = 0;
int array[10];
int main(void)
{

    while ((c = getchar()) != EOF)
    {
        if (c != ' ' && c != '\t')
        {
            /* array[wordcount] = array[wordcount] +1;*/
            wordcount = wordcount + 1;
        }
        else
        {
            array[wordcount] = array[wordcount]  +1 ;
            wordcount = 0;
        }
    }
    for (int i = 0; i <= 9; i++)
    {
        printf("%d: ", i);
        for(int j = 0; j <array[i]; j++){
            printf("#");
        }
        printf("\n");
    }
}