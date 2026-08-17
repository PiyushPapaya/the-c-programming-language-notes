# Notes: 2.5 Arithmetic Operators

## What this section is about

The binary arithmetic operators C provides, and how integer division and the
modulus operator behave.

## Key ideas

The binary arithmetic operators are `+`, `-`, `*`, `/`, and the modulus
operator `%`.

**Integer division truncates.** Any fractional part of the result is
dropped, not rounded.

**Modulus.** `x % y` gives the remainder when `x` is divided by `y`. It's
zero exactly when `y` divides `x` evenly.

A classic use of `%` is a leap year check: a year is a leap year if it's
divisible by 4 but not by 100, except that years divisible by 400 are leap
years anyway:

```c
if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
    printf("%d is a leap year\n", year);
else
    printf("%d is not a leap year\n", year);
```

## Gotchas

- Integer division truncates toward zero (drops the remainder), it doesn't
  round to the nearest integer.
- `%` only makes sense on integer operands.

## Quick recap

`+ - * / %` are the binary arithmetic operators. `/` truncates on integers,
and `%` gives the remainder, both used together in things like the leap year
test above.
