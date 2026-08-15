# Notes: 1.10 External Variables and Scope

## What this section is about

This section draws the line between local (automatic) variables and external
(global) variables, and rewrites the longest-line program to use external
variables instead of passing everything through arguments. It's less about new
syntax and more about a design tradeoff: convenience now versus tangled code
later.

## Key ideas

**Automatic variables** are the ordinary local variables you've been using,
like `line` and `longest` inside `main`. They belong only to the function they
are declared in, no other function can see them (even if another function
happens to use the same name, like `i` in both `getline` and `copy`, those are
two unrelated variables). They come into existence when the function is
called, and disappear when it returns. Since they don't persist between calls,
they must be set explicitly every time, otherwise they hold garbage.

**External variables** are the opposite: defined outside of any function, so
any function can reach them by name. They exist for the whole run of the
program, not just while some function is active, so they keep their values
even after the function that set them has returned. Because of that, they can
be used to pass data between functions instead of using argument lists.

Rewriting the longest-line program with `line`, `longest`, and `max` as
externals means `getline` and `copy` no longer need parameters at all, they
just reach out and touch the shared variables directly:

```c
#include <stdio.h>
#define MAXLINE 1000

int max;
char line[MAXLINE];
char longest[MAXLINE];

int getline(void);
void copy(void);

main()
{
    int len;

    max = 0;
    while ((len = getline()) > 0)
        if (len > max) {
            max = len;
            copy();
        }
    if (max > 0)
        printf("%s", longest);
    return 0;
}

int getline(void)
{
    int c, i;

    for (i = 0; i < MAXLINE - 1 && (c = getchar()) != EOF && c != '\n'; ++i)
        line[i] = c;
    if (c == '\n') {
        line[i] = c;
        ++i;
    }
    line[i] = '\0';
    return i;
}

void copy(void)
{
    int i;

    i = 0;
    while ((longest[i] = line[i]) != '\0')
        ++i;
}
```

**Definition vs. declaration.** An external variable must be *defined* exactly
once, outside any function; that's what actually sets aside storage for it
(the lines near the top of the file above). Any function that wants to use it
then needs a *declaration*, which just states its type without allocating
anything new. That declaration uses the `extern` keyword, for example
`extern int max;` inside a function body.

In practice, that `extern` declaration is often unnecessary. If the definition
already appears earlier in the same file, before the function that uses it,
the function can just use the variable directly, no `extern` needed. This is
why common style is to put all external variable definitions at the top of
the file and skip `extern` everywhere else, which is what the rewritten
program above does.

If a program spans multiple files, and a variable is defined in one file but
used in another, then that other file does need an `extern` declaration to
connect to it. The usual way to manage this is to collect all those
declarations into a header file (a `.h` file) and `#include` it wherever
needed, the same way `<stdio.h>` declares the standard library functions.
Chapter 4 covers this in more depth.

**Empty parameter lists.** Since `getline` and `copy` no longer take
arguments, it'd seem natural to declare them as `getline()` and `copy()`. But
for compatibility with older C, an empty `()` in a declaration is treated as
an old-style declaration that turns off argument checking entirely. To
actually declare "this function takes no arguments," you have to write
`void` explicitly, as in `int getline(void);`.

## Gotchas

- It's tempting to make everything external because it shortens argument
  lists and variables are always reachable. But external variables are always
  there whether you want them or not. Leaning on them too much means data can
  get changed in unexpected places, and the program becomes harder to trace
  and modify.
- The externally-wired version of `getline` and `copy` above is actually
  worse than the original argument-passing version. It works, but it
  hardcodes the names `line` and `longest` into functions that used to be
  general purpose, so they can no longer be reused for anything else.

## Quick recap

Local variables are private to their function and vanish between calls.
External variables are shared and persist for the whole program, defined once
outside any function and declared with `extern` elsewhere if needed. They're
powerful for passing data around without argument lists, but that power comes
at the cost of clarity, so use them deliberately, not by default.
