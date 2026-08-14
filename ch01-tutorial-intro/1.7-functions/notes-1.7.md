# Notes: 1.7 Functions

## What this section is about

This section introduces functions properly. A function packages up a
computation so you can use it without caring how it's implemented, you just
need to know what it does. The section walks through writing a `power`
function from scratch and uses it to explain the pieces of a function
definition, prototypes, and the difference between old-style and ANSI C
function declarations.

## Key ideas

**Why functions matter.** Once a function is written well, you can call it
without thinking about its internals. Knowing *what* it does is enough. C
makes defining and calling functions easy enough that you'll often see a tiny
function written and called exactly once, just because it makes the
surrounding code clearer.

**Example: `power(m, n)`.** C has no exponentiation operator (no `**` like
Fortran), so here's a simple version that raises `m` to the `n`th power for
non-negative `n`:

```c
#include <stdio.h>

int power(int m, int n);

/* test power function */
main()
{
    int i;
    for (i = 0; i < 10; ++i)
        printf("%d %d %d\n", i, power(2,i), power(-3,i));
    return 0;
}

/* power: raise base to n-th power; n >= 0 */
int power(int base, int n)
{
    int i, p;
    p = 1;
    for (i = 1; i <= n; ++i)
        p = p * base;
    return p;
}
```

**Function definition shape:**

```c
return-type function-name(parameter declarations, if any)
{
    declarations
    statements
}
```

Functions can be defined in any order and can live in one file or several,
though a single function can't be split across files.

**Local names.** Parameter names and local variables (like `base`, `n`, `i`,
`p` inside `power`) are local to that function. The `i` inside `power` has
nothing to do with the `i` inside `main`, so names can be reused freely
across functions without conflict. "Parameter" refers to the variable named
in a function's own definition; "argument" is sometimes used for the same
thing, along with "formal argument" and "actual argument."

**Returning values.** The `return` statement sends a value back to the
caller:

```c
return expression;
```

A function doesn't have to return a value. A bare `return;` (or just falling
off the end of the function by reaching the closing `}`) returns control
without a useful value. The caller is also free to ignore whatever value a
function returns.

**`main` returns a value too.** Since `main` is a function like any other, it
can return a status value to whatever ran the program. By convention, `0`
means normal termination and non-zero means something went wrong. Earlier
programs in the book skipped the `return` statement in `main` for simplicity,
but from here on they include it, as a reminder that programs should report
their status to the environment.

**Function prototypes.** A line like

```c
int power(int base, int n);
```

before `main` is a *function prototype*. It tells the compiler what
arguments `power` expects and what it returns, and the compiler checks that
the definition and every call agree with it. Parameter names in a prototype
are optional, so `int power(int, int);` would also work, but naming them is
better documentation.

**Old-style vs. ANSI style.** The biggest change ANSI C made to the language
was how functions are declared and defined. The old style looked like this:

```c
/* power: raise base to n-th power; n >= 0 */
/* (old-style version) */
power(base, n)
int base, n;
{
    int i, p;
    p = 1;
    for (i = 1; i <= n; ++i)
        p = p * base;
    return p;
}
```

Parameters were named between the parentheses, with their types declared
separately before the opening brace, and anything undeclared defaulted to
`int`. The matching old-style declaration, `int power();`, took no parameter
list at all, so the compiler couldn't check that calls used the right number
or types of arguments. In fact, since a function was assumed to return `int`
by default, this declaration was often skipped entirely. ANSI-style
prototypes fix this by letting the compiler catch mismatched argument counts
or types. The old style still works in ANSI C for backward compatibility,
but the book recommends always using prototypes when your compiler supports
them.

## Gotchas

- Local variable and parameter names only exist inside their own function.
  Reusing `i` in every function is fine and won't cause conflicts.
- A function can silently return no useful value if you forget the `return`
  statement or the caller ignores what's returned, watch for that when
  debugging.
- Old-style declarations like `int power();` give the compiler nothing to
  check calls against. Prefer full prototypes.

## Quick recap

A function groups behavior into a named, reusable, independently testable
unit, with parameters and locals scoped to itself. `return` sends a value
back (or nothing, if omitted). Function prototypes let the compiler catch
mismatched calls, which is the main thing ANSI C improved over the old K&R
function syntax.
