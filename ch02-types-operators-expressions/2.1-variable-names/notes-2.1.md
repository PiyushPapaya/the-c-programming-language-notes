# Notes: 2.1 Variable Names

## What this section is about

The rules for naming variables and symbolic constants in C, and some
conventions for picking good names.

## Key ideas

Names are made of letters and digits, and the first character has to be a
letter. The underscore `_` counts as a letter, so it can start a name too, but
don't start your own variable names with one. Library routines often use
leading underscores for their own names, so you risk a clash.

Upper and lower case are different letters, so `x` and `X` are two separate
variables. The traditional style in C is:

- lower case for variable names
- all upper case for symbolic constants

At least the first 31 characters of a name are significant internally. For
function names and external variables, fewer characters may be guaranteed,
because those names sometimes have to survive being passed through an
assembler or linker. The standard only guarantees that external names are
unique in the first 6 characters, and in a single case (so `myVar` and `MYVAR`
might not be treated as different names for an external symbol).

Keywords like `if`, `else`, `int`, `float`, and so on are reserved. You can't
use them as variable names, and they're always lower case.

Pick names that describe what the variable is for, and that don't look too
similar to each other. Convention is to use short names (like `i`, `j`) for
local variables and loop indices, and longer, more descriptive names for
external variables.

## Gotchas

- Starting a name with `_` isn't illegal, but it's a bad idea because it can
  collide with names used internally by library code.
- Two names that only differ in case (`count` vs `Count`) are legal but easy
  to mix up by accident.

## Quick recap

Names start with a letter (or underscore, but don't), are case-sensitive, and
at least 31 characters are significant. Keep local names short, external names
descriptive, and don't fight the keywords.
