# CLAUDE.md

## What this repo is

This is Piyush's notebook for working through *The C Programming Language* (2nd
edition) by Kernighan and Ritchie, usually just called K&R.

Here is the deal. He reads a section from the book as a PDF and pastes the text
into the chat. Your job is to take that pasted text and do the repetitive work:
write clean notes, pull out the exercises into a list, keep the folders
organized, update the progress tracker, and push to GitHub. That way he can spend
his time actually learning C and solving problems instead of formatting files.

You are the assistant that runs the repo. He is the one learning. When he pastes
text, you turn it into notes and an exercise list. He writes the solution `.c`
files himself.

Most of the time this repo runs on a smaller model, so follow the steps below
exactly and do not skip any. When in doubt, do the literal thing the steps say.

---

## Folder and file layout

Each chapter is a folder, for example `ch01-tutorial-intro/`. Inside a chapter:

- `summary-1.md` is the whole-chapter summary. The number matches the chapter
  (chapter 3 uses `summary-3.md`). It is written only after every section in the
  chapter has notes.
- One subfolder per section, for example `1.3-for-statement/`.

Each section subfolder contains:

- `notes-1.3.md`, the notes for that section. The number is the section number.
- `exercises/`, a folder that contains:
  - `exercises-1.3.md`, the list of exercise prompts pulled from the text.
  - The solution files Piyush adds himself, named `ex1-3a.c`, `ex1-3b.c`, and so
    on. That naming is `ex<chapter>-<section><letter>.c`.
  - `output/`, holding the compiled binary for each solution file, named to
    match it: `ex1-3a.c` builds to `output/ex1-3a.exe`. These `.exe` files ARE
    committed to git (see the `.gitignore` note below).

So `notes-x.y.md` and `exercises-x.y.md` are per section, and `summary-x.md` is
per chapter.

If a `.c` file or `.exe` ever turns up loose (chapter root, an old top-level
`output/` folder, or anywhere outside a section's `exercises/output/`), it is
clutter from before this convention was followed consistently. Sort it: the
exercise number tells you the section (`ex<chapter>-<section><letter>.c` means
section `<chapter>.<section>`), regardless of which part of the book text the
exercise conceptually belongs to. Move the `.c` file into that section's
`exercises/` folder with the correct name, move or rebuild its `.exe` into
`exercises/output/` with the matching name, and if `exercises-x.y.md` doesn't
already list that exercise, add it (checked off, since a solution exists)
using the real K&R exercise prompt text.

`.gitignore` ignores ordinary build junk (`*.o`, `*.out`, `a.out`, etc.) but
**not** `.exe`. Compiled `.exe` files under `exercises/output/` are tracked and
pushed like any other file, so `git add -A` picks them up with no special
handling.

Templates live in `TEMPLATES/`. Use them as the starting point:

- `TEMPLATES/notes-template.md` for section notes.
- `TEMPLATES/summary-template.md` for chapter summaries.
- `TEMPLATES/exercises-template.md` for exercise lists.

**Do not create chapter or section folders in advance.** Only create a folder
when Piyush asks for that specific section, or when the text he pastes covers it.

---

## The full K&R chapter and section list

Use these exact folder names. When Piyush says something like "set up 1.3", you
already know 1.3 is "The for statement" in Chapter 1, and the section folder is
`1.3-for-statement` inside `ch01-tutorial-intro`. Never ask him for the folder
name. Look it up here.

### Chapter 1 - A Tutorial Introduction  (folder: `ch01-tutorial-intro`)
- 1.1 Getting Started - `1.1-getting-started`
- 1.2 Variables and Arithmetic Expressions - `1.2-variables-arithmetic`
- 1.3 The for statement - `1.3-for-statement`
- 1.4 Symbolic Constants - `1.4-symbolic-constants`
- 1.5 Character Input and Output - `1.5-character-input-output`
  (subparts: File Copying, Character Counting, Line Counting, Word Counting)
- 1.6 Arrays - `1.6-arrays`
- 1.7 Functions - `1.7-functions`
- 1.8 Arguments - Call by Value - `1.8-arguments-call-by-value`
- 1.9 Character Arrays - `1.9-character-arrays`
- 1.10 External Variables and Scope - `1.10-external-variables-scope`

### Chapter 2 - Types, Operators and Expressions  (folder: `ch02-types-operators-expressions`)
- 2.1 Variable Names - `2.1-variable-names`
- 2.2 Data Types and Sizes - `2.2-data-types-sizes`
- 2.3 Constants - `2.3-constants`
- 2.4 Declarations - `2.4-declarations`
- 2.5 Arithmetic Operators - `2.5-arithmetic-operators`
- 2.6 Relational and Logical Operators - `2.6-relational-logical-operators`
- 2.7 Type Conversions - `2.7-type-conversions`
- 2.8 Increment and Decrement Operators - `2.8-increment-decrement-operators`
- 2.9 Bitwise Operators - `2.9-bitwise-operators`
- 2.10 Assignment Operators and Expressions - `2.10-assignment-operators-expressions`
- 2.11 Conditional Expressions - `2.11-conditional-expressions`
- 2.12 Precedence and Order of Evaluation - `2.12-precedence-order-evaluation`

### Chapter 3 - Control Flow  (folder: `ch03-control-flow`)
- 3.1 Statements and Blocks - `3.1-statements-blocks`
- 3.2 If-Else - `3.2-if-else`
- 3.3 Else-If - `3.3-else-if`
- 3.4 Switch - `3.4-switch`
- 3.5 Loops - While and For - `3.5-loops-while-for`
- 3.6 Loops - Do-While - `3.6-loops-do-while`
- 3.7 Break and Continue - `3.7-break-continue`
- 3.8 Goto and labels - `3.8-goto-labels`

### Chapter 4 - Functions and Program Structure  (folder: `ch04-functions-program-structure`)
- 4.1 Basics of Functions - `4.1-basics-of-functions`
- 4.2 Functions Returning Non-integers - `4.2-functions-returning-non-integers`
- 4.3 External Variables - `4.3-external-variables`
- 4.4 Scope Rules - `4.4-scope-rules`
- 4.5 Header Files - `4.5-header-files`
- 4.6 Static Variables - `4.6-static-variables`
- 4.7 Register Variables - `4.7-register-variables`
- 4.8 Block Structure - `4.8-block-structure`
- 4.9 Initialization - `4.9-initialization`
- 4.10 Recursion - `4.10-recursion`
- 4.11 The C Preprocessor - `4.11-c-preprocessor`
  (subparts: File Inclusion, Macro Substitution, Conditional Inclusion)

### Chapter 5 - Pointers and Arrays  (folder: `ch05-pointers-arrays`)
- 5.1 Pointers and Addresses - `5.1-pointers-addresses`
- 5.2 Pointers and Function Arguments - `5.2-pointers-function-arguments`
- 5.3 Pointers and Arrays - `5.3-pointers-arrays`
- 5.4 Address Arithmetic - `5.4-address-arithmetic`
- 5.5 Character Pointers and Functions - `5.5-character-pointers-functions`
- 5.6 Pointer Arrays; Pointers to Pointers - `5.6-pointer-arrays-pointers-to-pointers`
- 5.7 Multi-dimensional Arrays - `5.7-multi-dimensional-arrays`
- 5.8 Initialization of Pointer Arrays - `5.8-initialization-pointer-arrays`
- 5.9 Pointers vs. Multi-dimensional Arrays - `5.9-pointers-vs-multi-dimensional-arrays`
- 5.10 Command-line Arguments - `5.10-command-line-arguments`
- 5.11 Pointers to Functions - `5.11-pointers-to-functions`
- 5.12 Complicated Declarations - `5.12-complicated-declarations`

### Chapter 6 - Structures  (folder: `ch06-structures`)
- 6.1 Basics of Structures - `6.1-basics-of-structures`
- 6.2 Structures and Functions - `6.2-structures-functions`
- 6.3 Arrays of Structures - `6.3-arrays-of-structures`
- 6.4 Pointers to Structures - `6.4-pointers-to-structures`
- 6.5 Self-referential Structures - `6.5-self-referential-structures`
- 6.6 Table Lookup - `6.6-table-lookup`
- 6.7 Typedef - `6.7-typedef`
- 6.8 Unions - `6.8-unions`
- 6.9 Bit-fields - `6.9-bit-fields`

### Chapter 7 - Input and Output  (folder: `ch07-input-output`)
- 7.1 Standard Input and Output - `7.1-standard-input-output`
- 7.2 Formatted Output - printf - `7.2-formatted-output-printf`
- 7.3 Variable-length Argument Lists - `7.3-variable-length-argument-lists`
- 7.4 Formatted Input - Scanf - `7.4-formatted-input-scanf`
- 7.5 File Access - `7.5-file-access`
- 7.6 Error Handling - Stderr and Exit - `7.6-error-handling-stderr-exit`
- 7.7 Line Input and Output - `7.7-line-input-output`
- 7.8 Miscellaneous Functions - `7.8-miscellaneous-functions`

### Chapter 8 - The UNIX System Interface  (folder: `ch08-unix-system-interface`)
- 8.1 File Descriptors - `8.1-file-descriptors`
- 8.2 Low Level I/O - Read and Write - `8.2-low-level-io-read-write`
- 8.3 Open, Creat, Close, Unlink - `8.3-open-creat-close-unlink`
- 8.4 Random Access - Lseek - `8.4-random-access-lseek`
- 8.5 Example - An implementation of Fopen and Getc - `8.5-example-implementation-fopen-getc`
- 8.6 Example - Listing Directories - `8.6-example-listing-directories`
- 8.7 Example - A Storage Allocator - `8.7-example-storage-allocator`

---

## What to do when Piyush pastes book text

Follow these steps in order every time he pastes section or chapter text.

1. **Figure out what the text covers.** Read it and match it to the list above.
   It might be a single section (like 1.3) or a whole chapter at once.

2. **If it is a whole chapter, split it into its sections.** Handle each section
   one at a time using the steps below. Use the section boundaries in the book
   text (the "1.3", "1.4" headers) to decide where one section ends and the next
   begins.

3. **For each section, create the section folder** if it does not exist yet, using
   the exact folder name from the list above, inside the right chapter folder.
   Create the chapter folder too if it is missing.

4. **Write the notes file** `notes-x.y.md` in that section folder. Start from
   `TEMPLATES/notes-template.md`, then replace it with real notes based on the
   pasted text. Summarize the material clearly so another learner could read it
   and understand the section. Keep it accurate. Follow the tone rules below.

5. **Write the exercises.** Create the `exercises/` folder inside the section
   folder. Inside it, create `exercises-x.y.md` starting from
   `TEMPLATES/exercises-template.md`. Read every exercise out of the pasted text,
   count them, and list one checkbox line per exercise with its full prompt. Use
   the format `- [ ] **Exercise x-y (a).** prompt text`, with letters a, b, c in
   the order they appear. If the text has no exercises for this section, still
   create the file and write "Total exercises: 0" with no checkbox lines.

6. **Do not write solution `.c` files.** Piyush writes those himself.

7. **Update the tracker, then commit and push.** See the automation rules below.

---

## What to do when Piyush asks to "build the folder structure for x.y"

This is when he gives you a section number but no book text. In that case:

1. Create the chapter folder if missing, and the section folder from the list.
2. Create `notes-x.y.md` by copying `TEMPLATES/notes-template.md` as is. Leave it
   as the scaffold. Do not invent notes without the text.
3. Create the `exercises/` folder, and inside it create `exercises-x.y.md` by
   copying `TEMPLATES/exercises-template.md` as is. Leave it blank of real
   exercises until he pastes text.
4. Run the tracker, then commit and push (automation rules below).

The scaffolded files still contain the placeholder markers from the templates, so
the tracker correctly counts them as not done until you fill them in with real
content.

---

## When to write a chapter summary

Only write `summary-x.md` once every section in that chapter has real notes. Start
from `TEMPLATES/summary-template.md` and write the whole-chapter synthesis: the big
picture, the main takeaways, the key tools introduced, and how it connects to
earlier chapters. Do not write a summary for a chapter that is still in progress.

After writing a summary, run the tracker, commit, and push.

---

## Automation rules (do this after every change)

After ANY request that changes files in this repo, always finish with these steps,
in order:

1. Run the tracker:
   ```
   python scripts/update_tracker.py
   ```
2. Update `DAILY-LOG.md`. Add or update today's entry at the top (newest first,
   date format `YYYY-MM-DD`), following the existing format: which sections were
   touched, which exercises were solved, and a short "Notes:" line about anything
   worth remembering (tricky bugs, files that had to be sorted/renamed, decisions
   made). If an entry for today already exists, add to it instead of duplicating
   a second heading for the same date.
3. Stage everything:
   ```
   git add -A
   ```
4. Commit with a short, auto-generated message describing what changed, for
   example `Add notes and exercises for 1.3` or `Scaffold folder for 2.4` or
   `Add summary for chapter 1`. Keep the message short.
   ```
   git commit -m "Add notes and exercises for 1.3"
   ```
5. Push:
   ```
   git push
   ```

Every change ends with a push. Do not leave work uncommitted.

When a single request produces several separate commits (for example, one commit
per exercise), run the tracker once and write/update the `DAILY-LOG.md` entry
once at the end, covering everything done in that request, rather than repeating
steps 1-2 for every individual commit.

---

## Tone rules for the notes and summaries

Write like a clear-thinking person explaining something to a friend. Simple and
direct.

- No em dashes anywhere. Use periods, commas, or parentheses instead.
- Do not be dramatic or use inflated, flowery language. No hype words.
- Get the information across completely, but without padding or filler.
- "Casual voice" means the tone is relaxed, not that the writing is sloppy.
  Spelling, grammar, and formatting must be correct and clean. These notes are
  meant to be read and reused by other people, so they have to be readable.
- Explain things properly. Do not shorten so much that a concept becomes unclear.
- Small code snippets are good when they make an idea clearer.
