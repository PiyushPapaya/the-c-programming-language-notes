# Notes: 3.3 Else-If

## What this section is about

This section covers the `else if` chain, the standard way to write a
multi-way decision in C, and walks through binary search as a worked example
of it.

## Key ideas

The pattern is:

```c
if (expression)
    statement
else if (expression)
    statement
else if (expression)
    statement
else
    statement
```

The expressions are checked in order. As soon as one is true, its statement
runs and the whole chain stops there, skipping everything after it. Each
`statement` can be a single statement or a braced block, same as always.

The final `else` handles the "none of the above" case, the default that
applies when nothing else matched. If there's nothing to do in that case, the
trailing `else` can just be left off. Alternatively, it's a good spot to put
error-checking code that catches a condition that should be "impossible" if
the rest of the logic is correct.

### Worked example: binary search

The book uses binary search to show a natural three-way decision. Given a
sorted array `v` of `n` elements, `binsearch` looks for `x` and returns its
index, or `-1` if it isn't there:

```c
/* binsearch: find x in v[0] <= v[1] <= ... <= v[n-1] */
int binsearch(int x, int v[], int n)
{
    int low, high, mid;

    low = 0;
    high = n - 1;
    while (low <= high) {
        mid = (low+high)/2;
        if (x < v[mid])
            high = mid + 1;
        else if (x > v[mid])
            low = mid + 1;
        else /* found match */
            return mid;
    }
    return -1; /* no match */
}
```

At each step, the value at the midpoint is compared to `x`, and there are
exactly three possible outcomes: `x` is smaller, `x` is bigger, or `x`
matches. That's exactly what `else if` is built for. If `x` is smaller than
`v[mid]`, the search narrows to the lower half; if bigger, it narrows to the
upper half; if equal, it's found. The loop keeps halving the search range
until it either finds a match or the range becomes empty (`low > high`).

## Gotchas

None specific to this section beyond what carries over from 3.2: keep an eye
on how each `else` binds, and use braces if a chain gets complicated enough
that the grouping isn't obvious at a glance.

## Quick recap

`else if` chains are the natural way to express "check these conditions in
order, do the first thing that matches." The trailing `else` is your default
case, and binary search is a clean example of a three-way `else if` decision
falling straight out of the problem (less than, greater than, or equal).
