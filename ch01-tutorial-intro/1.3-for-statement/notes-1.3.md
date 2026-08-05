# Notes: 1.3 The for statement

There's more than one way to write the same program. This section rewrites the temperature
converter using a `for` loop instead of a `while`, and shows how much it can compress.

## The rewritten program

```c
#include <stdio.h>

/* print Fahrenheit-Celsius table */
main()
{
    int fahr;

    for (fahr = 0; fahr <= 300; fahr = fahr + 20)
        printf("%3d %6.1f\n", fahr, (5.0/9.0)*(fahr-32));
}
```

Same output as before, but almost all the variables are gone. Only `fahr` is left, and it's an
`int`. The lower limit, upper limit, and step size now show up only as constants inside the
`for`. The Celsius calculation isn't even a separate assignment anymore, it's computed inline
as the third argument to `printf`.

## Expressions can go anywhere a value of that type is expected

This is the general rule behind folding the Celsius calculation straight into `printf`: anywhere
a value of some type is allowed, a more complicated expression of that type works just as well.
`printf`'s third argument needs to match `%6.1f`, a floating-point value, so any expression
that evaluates to a float can go there. No need for a separate `celsius` variable.

## How the for loop works

`for` is a loop, just like `while`, but with three parts inside the parentheses, separated by
semicolons:

```c
for (initialization; condition; increment)
    statement
```

- **Initialization** (`fahr = 0`) runs once, before the loop starts.
- **Condition** (`fahr <= 300`) is checked before each iteration. If true, the body runs.
- **Increment** (`fahr = fahr + 20`) runs after the body, then the condition is checked again.

The loop ends once the condition becomes false. Just like `while`, the body can be one
statement or a braced block. And the three parts inside the parentheses aren't limited to simple
assignments, they can be any expressions.

## while vs. for

There's no hard rule for picking one over the other, it comes down to whichever reads more
clearly. `for` tends to be the better choice when the initialization and increment are simple,
related, single statements, since it keeps all the loop control in one place instead of spreading
it across the top and bottom of the loop body.

## Quick recap

`for (init; condition; increment)` packs a loop's setup, test, and step into one line, which
works well when those three things are simple and related. Any expression of the right type can
be used wherever a value of that type is expected, so computations can be inlined directly into
calls like `printf` instead of needing their own variable.
