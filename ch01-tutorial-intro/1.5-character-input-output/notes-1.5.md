# Notes: 1.5 Character Input and Output

*Status: written from K&R section text.*

## What this section is about

This section covers the standard library's model for text input and output,
and builds a family of small programs (copy, character count, line count,
word count) using just `getchar` and `putchar`. These simple programs are the
basis for a lot of bigger programs you'll write later.

## The text stream model

Text input or output, no matter where it comes from or goes to, is treated as
a stream of characters. A text stream is a sequence of lines, and each line is
zero or more characters followed by a newline. The library handles making
every stream look like this, so you never have to worry about how lines are
actually represented on disk or by the OS.

## getchar and putchar

These are the simplest input/output functions in the standard library.

- `getchar()` reads the next character from the input stream and returns it.
- `putchar(c)` writes a character to the output.

```c
c = getchar();   // c now holds the next input character
putchar(c);       // prints that character
```

Calls to `putchar` and `printf` can be mixed freely. Output appears in the
order the calls happen.

## 1.5.1 File Copying

The simplest useful program you can write with just these two functions is
one that copies input to output, one character at a time.

```c
#include <stdio.h>

/* copy input to output; 1st version */
main()
{
    int c;
    c = getchar();
    while (c != EOF) {
        putchar(c);
        c = getchar();
    }
}
```

The key design question is: how do you tell "end of input" apart from a real
character? The answer is `EOF`, a special value `getchar` returns when there's
no more input, defined in `<stdio.h>`. Its actual numeric value doesn't
matter, you just use the symbolic constant.

This is exactly why `c` is declared `int` and not `char`. A `char` might not
be big enough to hold every possible character value plus `EOF` as a distinct
value, so you need a type wide enough to hold both. `int` is that type.

An assignment in C is itself an expression, with a value (the value assigned).
That means you can fold the read and the test together:

```c
#include <stdio.h>

/* copy input to output; 2nd version */
main()
{
    int c;
    while ((c = getchar()) != EOF)
        putchar(c);
}
```

This version has only one call to `getchar`, which is a nice simplification.
It's a common idiom in C, but be careful not to take this style so far that
the code becomes hard to read.

The parentheses around `c = getchar()` are required. `!=` has higher
precedence than `=`, so without parentheses:

```c
c = getchar() != EOF
```

would be parsed as:

```c
c = (getchar() != EOF)
```

which sets `c` to 0 or 1 (whether or not `EOF` was returned) instead of to the
actual character. Not what you want.

## 1.5.2 Character Counting

A program that counts characters looks a lot like the copy program, just
counting instead of printing.

```c
#include <stdio.h>

/* count characters in input; 1st version */
main()
{
    long nc;
    nc = 0;
    while (getchar() != EOF)
        ++nc;
    printf("%ld\n", nc);
}
```

`++nc` increments `nc` by one. It's shorthand for `nc = nc + 1`, and is
usually more efficient too. There's a matching `--` for decrementing. Both can
be prefix (`++nc`) or postfix (`nc++`); they differ when used inside larger
expressions (more in Chapter 2), but as standalone statements `++nc` and
`nc++` do the same thing.

`nc` is declared `long` instead of `int` because on some machines `int` is
only 16 bits (max value 32767), which overflows fast. `long` is guaranteed at
least 32 bits. The `%ld` conversion in `printf` matches a `long` argument.

You could go even bigger with a `double`, and use a `for` loop instead of
`while` to show another way to write the same logic:

```c
#include <stdio.h>

/* count characters in input; 2nd version */
main()
{
    double nc;
    for (nc = 0; getchar() != EOF; ++nc)
        ;
    printf("%.0f\n", nc);
}
```

`printf` uses `%f` for both `float` and `double`. `%.0f` suppresses the
decimal point and fractional digits.

The `for` loop body here is empty because all the work happens in the test and
increment parts. C still requires a statement for the body, so an isolated
semicolon (a null statement) is used, placed on its own line to make it
visible.

If the input has zero characters, the very first call to `getchar` fails the
test, and the loop body never runs, giving the correct answer of zero. `while`
and `for` test at the top of the loop before running the body, which is why
they naturally handle empty input correctly.

## 1.5.3 Line Counting

Since the library guarantees every line ends in a newline, counting lines is
just counting newline characters.

```c
#include <stdio.h>

/* count lines in input */
main()
{
    int c, nl;
    nl = 0;
    while ((c = getchar()) != EOF)
        if (c == '\n')
            ++nl;
    printf("%d\n", nl);
}
```

The `while` body is a single `if` statement, which controls `++nl`. An `if`
tests its parenthesized condition and, if true, runs the statement (or block)
that follows.

`==` is "is equal to", distinct from `=` which is assignment. Mixing these up
by accident (writing `=` when you mean `==`) is a classic C mistake, and the
compiler usually won't warn you, because `c = '\n'` is a perfectly legal
expression on its own.

A character in single quotes, like `'A'`, is a character constant: just
another way of writing a small integer equal to that character's value in the
machine's character set (65 for `'A'` in ASCII). Prefer `'A'` over the literal
65 since it's clearer and doesn't depend on a specific character set.

Escape sequences work in character constants too, so `'\n'` is the integer
value of the newline character (10 in ASCII). Note the distinction: `'\n'` is
a single character (an integer in expressions), while `"\n"` is a string
constant that happens to contain one character.

## 1.5.4 Word Counting

This program counts lines, words, and characters together, a stripped down
version of the Unix `wc` program. A "word" here is loosely defined as any
run of characters with no blank, tab, or newline in it.

```c
#include <stdio.h>

#define IN  1  /* inside a word */
#define OUT 0  /* outside a word */

/* count lines, words, and characters in input */
main()
{
    int c, nl, nw, nc, state;

    state = OUT;
    nl = nw = nc = 0;
    while ((c = getchar()) != EOF) {
        ++nc;
        if (c == '\n')
            ++nl;
        if (c == ' ' || c == '\n' || c == '\t')
            state = OUT;
        else if (state == OUT) {
            state = IN;
            ++nw;
        }
    }
    printf("%d %d %d\n", nl, nw, nc);
}
```

A new word is counted the moment the program hits the first character of it.
`state` tracks whether we're currently inside a word (`IN`) or not (`OUT`).
Using the symbolic constants `IN` and `OUT` instead of raw `1` and `0` makes
the program more readable, and makes it much easier to change things later,
since the "magic numbers" only live in one place.

`nl = nw = nc = 0;` sets all three to zero in one line. This works because
assignment is an expression, and assignments associate right to left, so it's
equivalent to:

```c
nl = (nw = (nc = 0));
```

`||` means logical OR. So `c == ' ' || c == '\n' || c == '\t'` reads as "c is
a blank, or c is a newline, or c is a tab". There's a matching `&&` for
logical AND, with slightly higher precedence than `||`. Both `&&` and `||`
evaluate left to right and stop as soon as the result is known (short
circuit evaluation): if `c` is a blank, the rest of the `||` chain is never
even checked. Not a big deal in this small example, but it matters more in
bigger programs.

The `else` in this program shows the general `if`-`else` form:

```c
if (expression)
    statement1
else
    statement2
```

Exactly one of `statement1` or `statement2` runs, depending on whether
`expression` is true or false. Either branch can be a single statement or a
block in braces.

## Gotchas

- `c` must be `int`, not `char`, so it can hold every character value plus the
  distinct `EOF` value.
- Forgetting the parentheses around `(c = getchar())` in a `while` condition
  changes the meaning completely, because `!=` binds tighter than `=`.
- Writing `=` instead of `==` in a condition is legal C and usually compiles
  without a warning, so it's a bug that's easy to miss.
- `while` and `for` test before the body runs, so they correctly do nothing on
  empty input. Don't reach for extra special-casing for that.

## Quick recap

`getchar` and `putchar` are the basic building blocks for character I/O, `c`
has to be `int` to safely hold `EOF`, and folding an assignment into a loop's
test condition (with parentheses) is a common, worthwhile C idiom once you're
used to reading it.
