# Notes: 1.9 Character Arrays

## What this section is about

This section builds a program that reads a bunch of text lines and prints the
longest one. It's the first real example of arrays of characters (strings) and
it introduces the pattern of splitting a program into small functions that each
do one clear job.

## Key ideas

The problem breaks down naturally into three pieces:

- get the next line of input
- if it's longer than anything seen so far, save it
- print the longest line at the end

That maps to two helper functions plus a `main` that ties them together.

**`getline`** reads one line of input into a character array and returns its
length. Returning 0 is used to signal end of file, since a real line always has
length at least 1 (even a blank line is just `'\n'`, which is one character).

```c
int getline(char s[], int lim)
{
    int c, i;

    for (i = 0; i < lim - 1 && (c = getchar()) != EOF && c != '\n'; ++i)
        s[i] = c;
    if (c == '\n') {
        s[i] = c;
        ++i;
    }
    s[i] = '\0';
    return i;
}
```

**`copy`** copies one character array into another, relying on the fact that
the source is `'\0'`-terminated. It stops as soon as it copies the null
character, and that same null character gets carried into the destination.

```c
void copy(char to[], char from[])
{
    int i;
    i = 0;
    while ((to[i] = from[i]) != '\0')
        ++i;
}
```

**`main`** just drives the two: keep calling `getline`, and whenever the line
is longer than the current max, call `copy` to save it.

The `'\0'` character (the null character, value zero) is what marks the end of
a string in C. Any string constant like `"hello\n"` is stored as its characters
plus a trailing `'\0'`. `printf`'s `%s` format expects this, and so does `copy`.

Function declarations at the top of the file (like `int getline(char line[], int maxline);`) tell the compiler what to expect before the functions are defined further down. Since `int` is the default return type, `getline`'s return type could technically be left off, but it's written explicitly here.

`copy` is declared `void` because it doesn't return anything, it's used purely
for its side effect of filling in `to`.

## Gotchas

- Array size in a function parameter (like `char s[]`) doesn't actually need to
  match the caller's array size in the declaration; it just sets aside storage
  inside the function, and the real limit (`lim`) is passed in separately.
- `getline` has no way to know in advance how long a line will be, so it
  protects itself against overflow by checking against `lim`. `copy`, on the
  other hand, is only ever called with a destination the caller already knows
  is big enough, so it skips that check. Not every function needs the same
  level of defensiveness, it depends on what the caller can already guarantee.
- If a line is longer than the array can hold, `getline` just stops collecting
  characters early, without reading a newline. It's on `main` to notice this
  (by checking length and the last character read) and decide what to do about
  it. The book's own example doesn't bother handling this case.

## Quick recap

Split a program along its natural pieces: one function to read input, one to
save it, and a small `main` to coordinate. Strings in C are just character
arrays terminated by `'\0'`, and every string-handling function in this section
leans on that convention.
