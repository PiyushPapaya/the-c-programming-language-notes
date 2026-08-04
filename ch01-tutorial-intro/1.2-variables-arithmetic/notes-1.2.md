# Notes: 1.2 Variables and Arithmetic Expressions

This section builds a program that prints a Fahrenheit to Celsius conversion table, using the
formula `C = (5/9)(F-32)`. It's longer than "hello, world" but introduces a bunch of core
ideas at once: comments, declarations, variables, arithmetic, loops, and formatted output.

## The integer version

```c
#include <stdio.h>

/* print Fahrenheit-Celsius table
   for fahr = 0, 20, ..., 300 */
main()
{
    int fahr, celsius;
    int lower, upper, step;

    lower = 0;    /* lower limit of temperature scale */
    upper = 300;  /* upper limit */
    step = 20;    /* step size */

    fahr = lower;
    while (fahr <= upper) {
        celsius = 5 * (fahr-32) / 9;
        printf("%d\t%d\n", fahr, celsius);
        fahr = fahr + step;
    }
}
```

## Comments

`/* ... */` marks a comment. The compiler ignores everything between the markers. Comments
can go anywhere a blank, tab, or newline can go, and they're there to make the program easier
for a human to understand.

## Declarations

In C, every variable has to be declared before it's used, usually at the top of the function
before any executable statements. A declaration is a type followed by a list of variable names:

```c
int fahr, celsius;
int lower, upper, step;
```

`int` means integer. `float` means floating point (numbers with a fractional part). The exact
range of these types depends on the machine. A common case is a 16-bit int (-32768 to
32767), though 32-bit ints are common too. `float` is typically 32 bits, with at least six
significant digits.

Other basic types:
- `char`, a single byte character
- `short`, short integer
- `long`, long integer
- `double`, double-precision floating point

## Assignment and the while loop

```c
lower = 0;
upper = 300;
step = 20;
```

sets the starting values. Statements end with semicolons.

The table is built one line at a time with a `while` loop:

```c
while (fahr <= upper) {
    ...
}
```

The condition in parentheses is checked first. If it's true, the body runs. Then the condition
is checked again, and so on, until it's false, at which point the loop ends and execution moves
past it. The body can be multiple statements in braces, or a single statement with no braces:

```c
while (i < j)
    i = 2 * i;
```

Indent the body of the loop (one tab stop, shown as four spaces) so it's visually clear what's
inside the loop. The compiler doesn't care about this, but readers do. Braces style is a matter
of preference, K&R just picks one and sticks with it consistently.

## Why celsius = 5 * (fahr-32) / 9, not 5/9 * (fahr-32)

Integer division in C truncates, it throws away the fractional part. `5/9` as integers evaluates
to `0`, so multiplying by that would always give 0. Multiplying by `5` first and dividing by `9`
after avoids this.

## printf and format specifiers

`printf` is a general-purpose output function. Its first argument is a string with `%`
placeholders, and each one is matched in order with the arguments that follow. `%d` means
"print as a decimal integer."

```c
printf("%d\t%d\n", fahr, celsius);
```

prints the two integers separated by a tab. The number and type of `%` placeholders must
match the arguments, or you get wrong (or undefined) results.

`printf` is not part of the C language itself. C has no built-in input or output. `printf` is
just a function from the standard library, defined by the ANSI standard so it behaves
consistently across compilers. Its counterpart for reading input is `scanf` (covered in 7.4).

### Field widths

Adding a width number to `%d` right-justifies the output in a field of that many characters:

```c
printf("%3d %6d\n", fahr, celsius);
```

prints the first number in a field 3 characters wide and the second in a field 6 characters wide.

## The floating-point version

The integer version is inaccurate (0°F is really about -17.8°C, not -17), because integer
arithmetic can't represent the fraction. Switching to `float` fixes it:

```c
#include <stdio.h>

/* print Fahrenheit-Celsius table
   for fahr = 0, 20, ..., 300; floating-point version */
main()
{
    float fahr, celsius;
    float lower, upper, step;

    lower = 0;
    upper = 300;
    step = 20;

    fahr = lower;
    while (fahr <= upper) {
        celsius = (5.0/9.0) * (fahr-32.0);
        printf("%3.0f %6.1f\n", fahr, celsius);
        fahr = fahr + step;
    }
}
```

Now `5.0/9.0` is a ratio of floating-point values, so it isn't truncated to zero. A decimal point
in a constant is what marks it as floating point.

### Mixed int/float arithmetic

If an operator has two integer operands, you get integer arithmetic. If one operand is float and
the other int, the int gets converted to float first. So writing `(fahr-32)` instead of
`(fahr-32.0)` would still work correctly, since `32` gets promoted automatically. But writing
the explicit `.0` makes the floating-point intent clear to a human reader, even though the
compiler doesn't need it.

This same automatic conversion applies to assignments and comparisons too, like
`fahr = lower;` and `while (fahr <= upper)`, an int is converted to float as needed.

### Format specifiers for floats

`%3.0f` prints a float at least 3 characters wide, no decimal point, no fraction digits.
`%6.1f` prints at least 6 characters wide, with 1 digit after the decimal point.

| Specifier | Meaning |
|---|---|
| `%d` | decimal integer |
| `%6d` | decimal integer, at least 6 characters wide |
| `%f` | floating point |
| `%6f` | floating point, at least 6 characters wide |
| `%.2f` | floating point, 2 digits after the decimal point |
| `%6.2f` | floating point, at least 6 wide, 2 after the decimal point |

Width and precision can each be left off independently. `printf` also supports `%o` (octal),
`%x` (hex), `%c` (character), `%s` (string), and `%%` (a literal percent sign).

## Quick recap

Variables must be declared with a type before use. Integer division truncates, so watch out
for it when you want a fractional result, use floats and decimal points instead. `printf` format
strings pair `%` specifiers with arguments in order, and you can control width and precision to
control how numbers are printed.
