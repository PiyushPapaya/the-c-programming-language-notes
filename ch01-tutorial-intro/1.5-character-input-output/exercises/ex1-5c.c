#include <stdio.h>

int main(void) {
    int blank = 0, tabs = 0, newline = 0, c;

    while ((c = getchar()) != EOF) {
        if (c == ' ') {
            blank++;
        }

        if (c == '\t') {
            tabs++;
        }

        if (c == '\n') {
            newline++;
        }
    }

    printf("Blank: %d, Tabs: %d, Newline: %d\n", blank, tabs, newline);

    return 0;
}
