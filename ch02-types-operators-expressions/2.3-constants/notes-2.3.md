# Notes: 2.3 Constants

## What this section is about

The different kinds of constants in C: integer, floating-point, character,
string, and enumeration, along with how to write each one and what type it
ends up being.

## Key ideas

**Integer constants.** A plain constant like `1234` is an `int`. Add a
trailing `l` or `L` to force `long`, like `123456789L`. A constant too big to
fit in an `int` becomes a `long` automatically. A trailing `u` or `U` makes it
`unsigned`, and `ul` or `UL` makes it `unsigned long`.

**Floating-point constants.** Anything with a decimal point (`123.4`) or an
exponent (`1e-2`), or both, is a floating constant. It's `double` by default.
A trailing `f` or `F` makes it `float`, and `l` or `L` makes it `long double`.

**Octal and hex.** A leading `0` on an integer constant means octal, a
leading `0x` or `0X` means hex. So decimal 31 is `037` in octal or `0x1f` in
hex. These can also take the `L` and `U` suffixes, so `0XFUL` is an
`unsigned long` with value 15.

**Character constants.** A single character in single quotes, like `'x'`, is
actually an integer: the numeric value of that character in the machine's
character set. Writing `'0'` instead of the number 48 keeps the code
independent of which character set is being used, and easier to read.
Because character constants are just integers, they can be used in ordinary
numeric expressions, though mostly you see them compared against other
characters.

Escape sequences represent characters that would otherwise be hard to type,
like `\n` for newline. There are also numeric escapes for an arbitrary byte
value: `'\ooo'` (one to three octal digits) or `'\xhh'` (one or more hex
digits). For example:

```c
#define VTAB '\013' /* ASCII vertical tab, octal */
#define BELL '\007' /* ASCII bell character, octal */
```

The full escape sequence list:

| Escape | Meaning | Escape | Meaning |
|---|---|---|---|
| `\a` | alert (bell) | `\\` | backslash |
| `\b` | backspace | `\?` | question mark |
| `\f` | formfeed | `\'` | single quote |
| `\n` | newline | `\"` | double quote |
| `\r` | carriage return | `\ooo` | octal number |
| `\t` | horizontal tab | `\xhh` | hexadecimal number |
| `\v` | vertical tab | | |

`'\0'` is the null character, value zero. It's often written instead of a
plain `0` to make it clear the code is dealing with a character, even though
the actual numeric value is the same.

**Constant expressions.** An expression made up only of constants, like
`31+28+1+31`, can be evaluated at compile time and used anywhere a constant
is allowed, including array sizes:

```c
#define MAXLINE 1000
char line[MAXLINE+1];
```

**String constants.** A sequence of characters in double quotes, like
`"I am a string"`. The quotes just delimit the string, they aren't part of
it. A string is really an array of characters, with a `'\0'` automatically
added at the end, so a string of n characters actually takes n+1 bytes of
storage. This is why there's no fixed limit on string length, but also why
programs have to scan a whole string to find out how long it is. The
standard `strlen(s)` function returns the length of a string, not counting
the terminating `'\0'`:

```c
/* strlen: return length of s */
int strlen(char s[])
{
    int i;

    while (s[i] != '\0')
        ++i;
    return i;
}
```

String constants can be concatenated at compile time just by placing them
next to each other, which is handy for splitting a long string across
several lines:

```c
"hello, " "world"
```

is the same as `"hello, world"`.

Watch the difference between `'x'` and `"x"`. `'x'` is an integer, the
numeric code for the letter x. `"x"` is an array of two characters: the
letter x and a trailing `'\0'`.

**Enumeration constants.** A named list of integer constants:

```c
enum boolean { NO, YES };
```

The first name gets value 0, the next gets 1, and so on, unless you assign
values explicitly. If only some values are given explicitly, the rest
continue counting up from the last one specified:

```c
enum escapes { BELL = '\a', BACKSPACE = '\b', TAB = '\t',
    NEWLINE = '\n', VTAB = '\v', RETURN = '\r' };

enum months { JAN = 1, FEB, MAR, APR, MAY, JUN,
    JUL, AUG, SEP, OCT, NOV, DEC }; /* FEB = 2, MAR = 3, etc. */
```

Names have to be distinct across different enumerations in the same scope,
but values don't have to be distinct within one enumeration.

Enums are a good alternative to `#define` for naming a set of related
constants, since the compiler can generate the values for you instead of you
picking them by hand. Compilers generally don't check that a value stored in
an enum variable is actually one of the valid names, but using an enum still
gives a debugger a chance to print the value by its symbolic name, which
`#define` can't do.

## Gotchas

- `'0'` and `0` are not the same value. `'0'` is the character code (48 in
  ASCII), not the number zero.
- `'x'` (character constant, an int) is not the same as `"x"` (string, a
  2-byte char array with a trailing `'\0'`).
- A leading `0` on a number literal means octal, not "just a number with a
  leading zero." Writing `010` gives you 8, not 10.

## Quick recap

Constants come in integer, floating, character, string, and enum flavors,
each with their own suffixes and rules. Strings are char arrays with an
implicit `'\0'` at the end. Character constants are really just integers.
Enums are a cleaner alternative to `#define` for related sets of constants.
