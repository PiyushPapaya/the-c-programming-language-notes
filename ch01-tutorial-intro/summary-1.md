# Chapter 1 Summary: A Tutorial Introduction

## Big picture

Chapter 1 is a fast walk through the core of C, building up from "hello,
world" to functions, arrays, and scope, mostly by writing small text-handling
programs. The point isn't to cover the language exhaustively (that's the rest
of the book), it's to get enough of the basics in your hands that you can
write real, useful programs. By the end of the chapter you've touched most of
the pieces you need for everyday C: variables, loops, conditionals, arrays,
functions, and the idea of where a variable lives and who can see it.

## Main takeaways

- C programs are built out of small functions, each doing one clear job, tied
  together by a `main` that coordinates them. This shows up again and again:
  `power`, `getline`, `copy`, and others all follow the same shape.
- Character-based I/O (`getchar`/`putchar`) plus loops is the workhorse
  pattern for processing text one character at a time, whether you're
  counting lines, copying input, or building up a string.
- Arrays and character arrays (strings) are just indexed, zero-based storage.
  Strings specifically are `'\0'`-terminated character arrays, and every
  string function in the chapter (`getline`, `copy`) leans on that
  convention.
- Functions communicate either through arguments and return values, or
  through external variables. Argument passing keeps functions general and
  reusable; external variables are convenient but can make a program's data
  flow hard to follow. Prefer arguments unless there's a good reason not to.
- Automatic (local) variables are private to their function and don't
  survive between calls. External variables persist for the whole program
  and are visible to any function that declares them.

## Key tools and syntax introduced

- `for`, `while`, and the general shape of loops in C, including the
  comma operator and multiple initializations/increments in a `for`.
- `if` / `else if` / `else` chains for multi-way decisions.
- `#define` for symbolic constants.
- Arrays: declaration, zero-based indexing, and character arrays as strings.
- Functions: declarations (prototypes), definitions, parameters, `return`,
  and the `void` return type for functions that return nothing.
- Call by value: arguments are copied into a function, so a function can't
  change the caller's variable directly (this becomes important again once
  pointers show up in Chapter 5).
- `extern`, and the distinction between defining a variable (allocating
  storage) and declaring one (stating its type without allocating anything).
- Character arithmetic, like `c - '0'` to convert a digit character to its
  numeric value.

## How it connects to earlier chapters

This is the first chapter, so there's no earlier material, but it sets the
foundation for everything after it. Chapter 2 goes back and formalizes the
types and operators used loosely here. Chapter 3 expands on control flow
(`switch`, `do-while`, `break`/`continue`). Chapter 4 goes deeper into
functions, external variables, and scope, the exact topics section 1.10
opened the door on. Chapter 5 revisits call by value and shows how pointers
let a function actually modify a caller's variable, which section 1.8
explicitly said wasn't possible with plain arguments.

## Things to remember

- Split a program along its natural pieces: don't try to do everything in
  `main`.
- Strings are character arrays ending in `'\0'`, always.
- Prefer passing data through arguments over reaching for external
  variables. Externals are powerful, but that power comes at the cost of
  readability and safety.
- Local variables reset every call and start out as garbage if you don't set
  them yourself.
