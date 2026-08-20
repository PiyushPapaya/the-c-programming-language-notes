# Notes: 3.1 Statements and Blocks

## What this section is about

This section covers the basic building blocks of control flow: statements and
blocks. It's short but it clears up two things that trip people up coming from
other languages: what the semicolon actually means in C, and what a block is.

## Key ideas

An expression like `x = 0`, `i++`, or `printf(...)` becomes a **statement**
once you put a semicolon after it:

```c
x = 0;
i++;
printf("hello\n");
```

In C, the semicolon **terminates** a statement. It's not a separator between
statements like it is in Pascal. That distinction matters because it means
every statement, including the last one in a block, needs its own trailing
semicolon.

Braces `{` and `}` group declarations and statements into a **compound
statement**, also called a **block**. A block is treated as a single
statement syntactically, so anywhere the grammar expects one statement (after
an `if`, `else`, `while`, or `for`), you can drop in a whole block instead.
The braces around a function body are the most obvious example of this.

Variables can be declared inside any block, not just at the top of a
function. That gets covered properly in Chapter 4.

## Gotchas

There is no semicolon after the closing brace `}` that ends a block. The
brace itself ends the block, so a semicolon there would just be an empty
statement.

## Quick recap

A semicolon ends a statement in C. Braces turn a group of statements into one
block, which can go anywhere a single statement is expected, and that block
doesn't get a semicolon after its closing brace.
