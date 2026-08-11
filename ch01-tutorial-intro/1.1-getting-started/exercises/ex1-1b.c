#include <stdio.h>

int main(void){
    printf("Hello Piyush\c");
}

/*error: expected ';' before '}' token
    4 |     printf("Hello Piyush")
      |                           ^
      |                           ;
    5 | }
      | ~ 
*/

/*warning: unknown escape sequence: '\c'
    4 |     printf("Hello Piyush\c");
      |                            ^
*/