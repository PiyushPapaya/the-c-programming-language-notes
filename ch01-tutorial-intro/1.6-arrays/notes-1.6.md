# Notes: 1.6 Arrays

## What this section is about

This section introduces arrays through a program that counts how many times
each digit appears in the input, along with counts of white space and
everything else. It's a good excuse to show off arrays, the `else if` chain,
and a neat trick where a character digit like `'7'` can be turned directly
into the number 7.

## Key ideas

**Declaring and using an array.** Instead of ten separate variables for the
ten digits, you can declare one array:

```c
int ndigit[10];
```

Array indexing in C always starts at zero, so the valid elements are
`ndigit[0]` through `ndigit[9]`. Any integer expression can be used as a
subscript, whether that's a loop variable like `i` or a plain constant.

**The full program:**

```c
#include <stdio.h>

/* count digits, white space, others */
main()
{
    int c, i, nwhite, nother;
    int ndigit[10];

    nwhite = nother = 0;
    for (i = 0; i < 10; ++i)
        ndigit[i] = 0;

    while ((c = getchar()) != EOF)
        if (c >= '0' && c <= '9')
            ++ndigit[c-'0'];
        else if (c == ' ' || c == '\n' || c == '\t')
            ++nwhite;
        else
            ++nother;

    printf("digits =");
    for (i = 0; i < 10; ++i)
        printf(" %d", ndigit[i]);
    printf(", white space = %d, other = %d\n", nwhite, nother);
}
```

**Turning a digit character into a number.** The trick is `c - '0'`. Since
chars are just small integers in C, and the character set guarantees that
`'0'` through `'9'` are consecutive increasing values, subtracting `'0'` from
any digit character gives you its numeric value (0 through 9). That's exactly
a valid subscript for `ndigit`.

**Multi-way decisions with `if / else if / else`.** This pattern shows up
constantly:

```c
if (condition1)
    statement1
else if (condition2)
    statement2
...
else
    statementn
```

The conditions are checked top to bottom. As soon as one is true, its
statement runs and the whole chain is done. If none match, the final `else`
runs (if there is one). If there's no final `else`, nothing happens when no
condition matches. Style-wise, keep every `if`/`else if` at the same
indentation level rather than nesting each one further right, or the code
marches off the edge of the page.

The book also mentions that Chapter 4's `switch` statement is another way to
write a multi-way branch, and works particularly well when you're comparing
one integer or character value against a set of constants.

## Gotchas

- Array indices start at 0, not 1. `ndigit[10]` gives you elements
  `ndigit[0]` to `ndigit[9]`, there is no `ndigit[10]`.
- `c - '0'` only works because `'0'` to `'9'` are guaranteed consecutive in
  the character set. Don't assume the same trick works for letters in every
  context without checking.

## Quick recap

Arrays give you indexed storage instead of a pile of separate variables.
Indexing starts at 0. `char` arithmetic works like `int` arithmetic, which is
what makes `c - '0'` a clean way to convert a digit character to its value.
`if / else if / else` chains are the standard way to write multi-way
decisions, keep them flat, not nested.
