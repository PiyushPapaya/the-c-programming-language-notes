# The C Programming Language: Notes

My notes, summaries, and exercise solutions as I work through *The C Programming
Language* (2nd edition) by Kernighan and Ritchie (K&R).

The idea is simple. I read a section from the book, paste the text into Claude,
and Claude writes up clean notes, lists out the exercises for that section, and
keeps the whole repo organized. That frees me up to focus on actually learning C
and solving the exercises.

## How it is organized

- One folder per chapter, like `ch01-tutorial-intro/`.
- Inside each chapter, one folder per section, like `1.3-for-statement/`.
- Each section folder has a `notes-1.3.md` and an `exercises/` folder.
- The `exercises/` folder holds `exercises-1.3.md` (the list of problems) and my
  solution files (`ex1-3a.c`, `ex1-3b.c`, and so on).
- Once every section in a chapter is done, the chapter gets a `summary-1.md`.

Chapter and section folders are created on demand, not all up front.

## Progress

See **[TRACKER.md](TRACKER.md)** for current progress, a per-chapter breakdown,
and a progress-over-time chart.

## Templates

Reusable templates for notes, summaries, and exercise lists live in
[`TEMPLATES/`](TEMPLATES/).

## Tracker script

`scripts/update_tracker.py` scans the repo and regenerates `TRACKER.md` plus the
progress chart. See [`scripts/requirements.txt`](scripts/requirements.txt) for
what it needs (just matplotlib).
