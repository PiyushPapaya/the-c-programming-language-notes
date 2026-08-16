# Notes: 2.2 Data Types and Sizes

## What this section is about

The basic data types C provides, the qualifiers you can attach to them, and
why their exact sizes are left up to the compiler and hardware rather than
fixed by the language.

## Key ideas

C has a small set of basic types:

- `char`: a single byte, holds one character in the local character set.
- `int`: an integer, normally the natural word size of the machine.
- `float`: single-precision floating point.
- `double`: double-precision floating point.

On top of these, qualifiers change how a type behaves:

`short` and `long` apply to integers, and give you a different size than
plain `int`:

```c
short int sh;
long int counter;
```

The word `int` can be left out here, and usually is, so `short sh;` and
`long counter;` are the normal way to write it.

The language guarantees an ordering, not exact sizes: `short` is at least 16
bits, `long` is at least 32 bits, and `short` is never longer than `int`,
which is never longer than `long`. A compiler is free to pick whatever sizes
make sense for its own hardware within those rules. In practice `short` is
often 16 bits and `int` is 16 or 32 bits, but this is implementation
dependent, not something to hardcode assumptions about.

`signed` and `unsigned` apply to `char` or any integer type. `unsigned`
values are always zero or positive, and wrap around using arithmetic modulo
2^n, where n is the number of bits in the type. So an 8-bit `unsigned char`
holds 0 to 255, while a `signed char` holds -128 to 127 (on a two's
complement machine). Whether a plain `char` is signed or unsigned by default
is machine dependent, but printable characters are always positive, so this
rarely bites you unless you're doing arithmetic on `char` values directly.

`long double` gives extended precision floating point. Like the integer
types, the exact sizes of `float`, `double`, and `long double` are
implementation defined, and could end up as one, two, or three genuinely
different sizes depending on the compiler.

The standard headers `<limits.h>` and `<float.h>` hold symbolic constants
for the actual ranges and sizes on whatever machine you're compiling for,
instead of you having to guess or hardcode them.

## Gotchas

- Don't assume `int` is always 16 or always 32 bits. The language only
  promises minimums and an ordering between `short`, `int`, and `long`.
- Whether plain `char` is signed or unsigned isn't fixed by the language,
  it depends on the compiler and platform.
- Use `<limits.h>` and `<float.h>` instead of hardcoding size assumptions if
  you actually need to know the exact range of a type.

## Quick recap

C gives you `char`, `int`, `float`, `double`, plus `short`/`long` and
`signed`/`unsigned` qualifiers. Exact sizes are implementation defined, the
language only guarantees minimum sizes and an ordering. Check `<limits.h>`
and `<float.h>` if you need real numbers.
