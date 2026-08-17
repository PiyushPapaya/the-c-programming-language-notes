# Notes: 2.4 Declarations

## What this section is about

How to declare variables in C: the basic syntax, initializing them at
declaration time, and the `const` qualifier.

## Key ideas

All variables have to be declared before use (though some declarations can
happen implicitly by context). A declaration gives a type and a list of one
or more variable names of that type:

```c
int lower, upper, step;
char c, line[1000];
```

You can also spread them across separate declarations instead:

```c
int lower;
int upper;
int step;
char c;
char line[1000];
```

This takes more space but makes it easier to attach a comment to each
variable individually, which helps later when you're editing.

**Initializing at declaration.** Follow the name with `=` and an expression:

```c
char esc = '\\';
int i = 0;
int limit = MAXLINE + 1;
float eps = 1.0e-5;
```

The rules differ depending on the kind of variable:

- **Non-automatic** variables (external or static) are initialized once,
  conceptually before the program starts running, and the initializer has to
  be a constant expression.
- **Automatic** variables are initialized every time the function or block
  they're declared in is entered, and the initializer can be any expression,
  not just a constant.
- External and static variables default to zero if you don't initialize them.
- Automatic variables with no explicit initializer hold garbage (undefined
  values), so don't assume they start at zero.

**`const`.** Applying `const` to a declaration says the value won't change.
For an array, it means the elements won't be altered:

```c
const double e = 2.71828182845905;
const char msg[] = "warning: ";
```

`const` also shows up on array function arguments, to promise the function
won't modify the array:

```c
int strlen(const char[]);
```

What actually happens if you try to change a `const` anyway is
implementation-defined, so don't rely on it doing anything predictable.

## Gotchas

- Automatic variables without an initializer are garbage, not zero. Only
  external/static variables default to zero.
- An automatic variable's initializer re-runs every time its scope is
  entered, so it's not a one-time setup the way it is for external/static
  variables.
- `const` is a promise, not a hard guarantee enforced everywhere. Violating
  it is implementation-defined behavior, not something you can count on.

## Quick recap

Declare a type and a list of names, optionally initializing each with `=`.
External/static variables zero-init automatically and initialize once;
automatic variables don't zero-init and re-initialize on every entry. Use
`const` to mark a variable (or array argument) as read-only.
