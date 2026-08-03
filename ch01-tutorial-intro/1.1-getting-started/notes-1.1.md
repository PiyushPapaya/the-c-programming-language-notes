# Notes: 1.1 Getting Started

The only way to learn a programming language is to write programs in it. The first program you should write is one that prints "hello, world" - this is the standard starting point in any language. Getting this working teaches you the mechanical parts: creating a file, compiling, loading, and running.

## The hello, world program

Here's the complete program:

```c
#include <stdio.h>
main()
{
  printf("hello, world\n");
}
```

To compile and run on UNIX: create a file named `hello.c`, then compile with `cc hello.c` and run with `a.out`. The exact process varies by system.

## Understanding the structure

Every C program consists of functions and variables. A function contains statements that specify what operations to do. Variables store values used during computation.

**`main`** is special - your program always starts executing at the beginning of `main`. Every program must have a `main` somewhere.

**`#include <stdio.h>`** tells the compiler to include information about the standard input/output library. This appears at the top of most C source files.

The **parentheses after main** surround the argument list. An empty list `()` means `main` expects no arguments.

**Braces `{ }`** enclose the statements of the function.

## Functions and calls

A function is called by naming it, followed by a parenthesized list of arguments. In our program, we call `printf("hello, world\n")`. This calls the library function `printf` with one argument: the string of characters between the quotes.

## Strings and escape sequences

A sequence of characters in double quotes, like `"hello, world\n"`, is called a character string or string constant. Right now, you'll mainly use strings as arguments to `printf` and other functions.

The `\n` in a string is C's notation for the newline character - it advances output to the left margin on the next line. `printf` does not automatically add a newline, so you must include `\n` if you want one.

Other escape sequences include:
- `\t` for tab
- `\b` for backspace
- `\"` for a double quote
- `\\` for the backslash itself

You can build output in stages by calling `printf` multiple times:

```c
printf("hello, ");
printf("world");
printf("\n");
```

produces the same output as one `printf("hello, world\n")`.

## Gotchas

- If you omit `\n` from a string, `printf` won't add a line advance - the next output will continue on the same line.
- You cannot split a string literal across lines in the source code. This will cause a compiler error:
  ```c
  printf("hello, world
  ");  // ERROR
  ```
- `\n` counts as a single character, not two.

## Quick recap

Start learning by writing and running actual programs. `main` is where execution begins. `printf` prints strings to the output. Use `\n` to get newlines and other escape sequences for special characters.
