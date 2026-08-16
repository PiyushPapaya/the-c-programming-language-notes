#include <stdio.h>
#include <limits.h>


int main (void){
        printf("CHAR_BIT   = %d\n", CHAR_BIT);
    printf("CHAR_MIN   = %d\n", CHAR_MIN);
    printf("CHAR_MAX   = %d\n", CHAR_MAX);

    printf("SCHAR_MIN  = %d\n", SCHAR_MIN);
    printf("SCHAR_MAX  = %d\n", SCHAR_MAX);

    printf("UCHAR_MAX  = %u\n", UCHAR_MAX);

    printf("SHRT_MIN   = %d\n", SHRT_MIN);
    printf("SHRT_MAX   = %d\n", SHRT_MAX);

    printf("USHRT_MAX  = %u\n", USHRT_MAX);

    printf("INT_MIN    = %d\n", INT_MIN);
    printf("INT_MAX    = %d\n", INT_MAX);

    printf("UINT_MAX   = %u\n", UINT_MAX);

    printf("LONG_MIN   = %ld\n", LONG_MIN);
    printf("LONG_MAX   = %ld\n", LONG_MAX);

    printf("ULONG_MAX  = %lu\n", ULONG_MAX);
}