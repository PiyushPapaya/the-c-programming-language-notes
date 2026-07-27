<!--
  BADGES AND LINKS use the repo path PiyushPapaya/the-c-programming-language-notes.
  If you fork or rename this repo, do a find-and-replace on that exact string and
  swap in your own USERNAME/REPO. It appears in the badge URLs just below.
-->

# The C Programming Language: Notes

[![License: MIT](https://img.shields.io/github/license/PiyushPapaya/the-c-programming-language-notes)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/PiyushPapaya/the-c-programming-language-notes)](https://github.com/PiyushPapaya/the-c-programming-language-notes/commits)
[![Repo size](https://img.shields.io/github/repo-size/PiyushPapaya/the-c-programming-language-notes)](https://github.com/PiyushPapaya/the-c-programming-language-notes)
[![Progress tracker](https://img.shields.io/badge/progress-tracked-2f6fed)](TRACKER.md)

Notes and solved exercises from working through **K&R**, *The C Programming Language*
by Kernighan and Ritchie, a chapter-by-chapter study log for learning C programming.

## What this is

This is my personal learning log for K&R. As I read each section, I write up clean
notes and summaries, list out the exercises, and solve them in C. An auto-updating
tracker keeps a running picture of how far through the book I am. It is a study
notebook, not a product, but it is public so other C learners can read along or use
it as a template for their own progress.

## Progress

![Progress over time](progress/progress.png)

See **[TRACKER.md](TRACKER.md)** for the full breakdown: overall percentage, a
per-chapter table, and a per-subsection table showing exactly what is done and what
is left.

## How this repo is organized

The layout follows the structure of the book.

- One folder per chapter, like `ch01-tutorial-intro/`.
- Inside each chapter, one folder per section, like `1.3-for-statement/`.
- Each section folder has:
  - `notes-1.3.md`, the notes for that section.
  - `exercises/`, holding `exercises-1.3.md` (the list of problems) and my solution
    files (`ex1-3a.c`, `ex1-3b.c`, and so on).
- Once every section in a chapter is done, the chapter gets a `summary-1.md`.

Chapter and section folders are created as I get to them, not all up front.
Reusable templates for notes, summaries, and exercise lists live in
[`TEMPLATES/`](TEMPLATES/), and the tracker script is in
[`scripts/`](scripts/update_tracker.py).

## How to use this

- If you are learning C, you are welcome to read the notes and summaries to learn
  from. They are written to be clear to someone other than me.
- If you want to track your own K&R progress, feel free to use this repo as a
  template: the folder structure, templates, and tracker script are reusable. The
  MIT license lets you read, reuse, and adapt any of it.

## Related files

- [TRACKER.md](TRACKER.md), the auto-generated progress report.
- [DAILY-LOG.md](DAILY-LOG.md), a short running log of what I worked on each day.

<!--
  GitHub topics cannot be set from a file. Add these manually in the repo:
  Settings > General, or the gear icon next to "About" on the repo home page.
  Topics to add:
  c, c-programming, kernighan-ritchie, k-and-r, learning-c,
  programming-exercises, study-notes, the-c-programming-language
-->
