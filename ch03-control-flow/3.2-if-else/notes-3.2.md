# Notes: 3.2 If-Else

## What this section is about

This section formalizes the `if-else` statement, which you've already been
using, and spends most of its time on one specific trap: the "dangling else"
ambiguity in nested ifs.

## Key ideas

The formal shape is:

```c
if (expression)
    statement1
else
    statement2
```

The `else` part is optional. `expression` is evaluated: if it's true (nonzero),
`statement1` runs. If it's false (zero) and there's an `else`, `statement2`
runs instead.

Since `if` just tests whether a value is nonzero, you can write

```c
if (expression)
```

instead of the more explicit

```c
if (expression != 0)
```

This is sometimes clean and natural, sometimes cryptic, depending on context.

### The dangling else

Because the `else` is optional, nested `if`s without braces create an
ambiguity: which `if` does a given `else` belong to? C resolves this by
attaching the `else` to the **nearest previous `else`-less `if`**. For
example:

```c
if (n > 0)
    if (a > b)
        z = a;
    else
        z = b;
```

Here the `else` binds to the inner `if (a > b)`, exactly as the indentation
suggests. If you actually wanted the `else` to go with the outer `if`, you
need braces to force it:

```c
if (n > 0) {
    if (a > b)
        z = a;
}
else
    z = b;
```

This ambiguity gets genuinely dangerous in code like:

```c
if (n > 0)
    for (i = 0; i < n; i++)
        if (s[i] > 0) {
            printf("...");
            return i;
        }
else /* WRONG */
    printf("error -- n is negative\n");
```

The indentation implies the `else` pairs with `if (n > 0)`, but the compiler
doesn't care about indentation. It attaches the `else` to the nearest
`else`-less `if`, which is `if (s[i] > 0)`. The code compiles fine and does
something completely different from what it looks like it does. Bugs like
this are hard to spot by eye, which is why it's worth using braces on nested
`if`s even when they aren't strictly required.

## Gotchas

Notice the semicolon after `z = a;` in the examples above. Grammatically,
whatever follows `if` or `else` is a statement, and an expression statement
like `z = a;` always needs its own terminating semicolon, same as any other
statement.

## Quick recap

`else` always binds to the closest `if` that doesn't already have one. When
you nest `if`s, use braces to make the grouping explicit rather than relying
on indentation, since indentation is just for humans and the compiler ignores
it.
