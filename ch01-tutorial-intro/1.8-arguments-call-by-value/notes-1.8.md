# Notes: 1.8 Arguments - Call by Value

## What this section is about

This section covers how C passes arguments to functions: by value. That's a
different model than languages like Fortran (call by reference) or Pascal's
`var` parameters, where the called function can reach back and modify the
caller's original variable. C copies values in instead, and this section
explains what that means in practice and why it's actually a good thing.

## Key ideas

**Call by value.** When you call a function, C gives it copies of the
argument values in temporary variables, not access to the originals.
Whatever the function does to those temporaries has no effect on the
caller's variables. This is different from "call by reference" languages,
where the called function can reach the original variable directly.

**Why this is a feature, not a limitation.** Because parameters behave like
already-initialized local variables, you can use them as working storage
inside the function without needing extra variables. Here's `power` rewritten
to take advantage of that:

```c
/* power: raise base to n-th power; n >= 0; version 2 */
int power(int base, int n)
{
    int p;
    for (p = 1; n > 0; --n)
        p = p * base;
    return p;
}
```

Here `n` itself is counted down to zero (a for loop running backwards), so
there's no need for the separate loop variable `i` from the earlier version.
Whatever happens to `n` inside `power` is invisible to whatever variable was
passed in by the caller, it's just a local copy.

**When you do need to modify the caller's variable.** Sometimes a function
needs to actually change something in the calling routine. To do that, the
caller passes the address of the variable (a pointer to it), and the
function declares its parameter as a pointer and modifies the variable
indirectly through that pointer. This is the subject of Chapter 5.

**Arrays are the exception.** When you pass an array's name as an argument,
what actually gets passed is the address of the array's first element, not
copies of every element. That means the function can reach into the original
array and change its contents through that address. This behavior is picked
up in the next section.

## Gotchas

- Passing a plain variable to a function and modifying the parameter inside
  the function never changes the caller's variable. If you expect a function
  to "return" a value this way and it doesn't, this is why.
- Arrays behave differently from ordinary variables when passed to
  functions, because what's passed is an address, not a copy of the data.
  Don't assume all arguments behave the same way.

## Quick recap

C always passes arguments by value: the function gets a copy, not the
original. This makes parameters convenient, pre-initialized local variables
rather than a source of hidden side effects. To let a function modify a
caller's variable, you pass a pointer to it explicitly (Chapter 5). Arrays
are a special case: passing an array passes the address of its first
element, so functions can modify the original array's contents directly.
