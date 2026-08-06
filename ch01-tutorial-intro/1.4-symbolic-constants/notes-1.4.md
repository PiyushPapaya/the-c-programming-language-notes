# Notes: 1.4 Symbolic Constants

One last cleanup to the temperature converter before moving on: get rid of the "magic
numbers."

## The problem with magic numbers

Numbers like `300` and `20` sitting directly in the code don't tell a future reader what they
mean, and if you need to change one, you have to hunt down every place it's used and hope you
don't miss one or change the wrong occurrence. Giving them names fixes both problems.

## #define

A `#define` line defines a symbolic name for a piece of replacement text:

```c
#define name replacement list
```

After that, every place `name` appears in the code (as long as it's not inside quotes and not
part of a longer identifier) gets swapped out for the replacement text before compilation. The
name follows the same rules as a variable name: letters and digits, starting with a letter. The
replacement text isn't limited to numbers, it can be any sequence of characters.

```c
#include <stdio.h>

#define LOWER 0    /* lower limit of table */
#define UPPER 300  /* upper limit */
#define STEP  20   /* step size */

/* print Fahrenheit-Celsius table */
main()
{
    int fahr;

    for (fahr = LOWER; fahr <= UPPER; fahr = fahr + STEP)
        printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
}
```

## Not variables

`LOWER`, `UPPER`, and `STEP` are symbolic constants, not variables, so they don't get declared
anywhere. They're a text substitution done before the program is compiled, not something that
takes up storage at runtime.

## Conventions

Symbolic constants are conventionally written in all caps, so they're easy to tell apart from
lowercase variable names at a glance. Also note there's no semicolon at the end of a `#define`
line, it's not a C statement.

## Quick recap

`#define NAME value` swaps out magic numbers for readable names, and gives you exactly one
place to change a value instead of many. By convention the names are uppercase, and the line
itself has no trailing semicolon.
