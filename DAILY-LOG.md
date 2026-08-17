# Daily Log

A running log of what I worked on each day while going through K&R. Newest entries
go at the top. Each entry is short: the date, which sections or exercises I touched,
and anything worth remembering.

<!-- Format for a new entry:

## YYYY-MM-DD
- Sections: 1.1, 1.2
- Exercises solved: 1-1, 1-2
- Notes: anything that tripped me up or clicked today.

-->

## 2026-08-17
- Sections: 2.4, 2.5 (real notes from pasted text); 2.6, 2.7, 2.8, 2.9, 2.10 (scaffolded, no book text pasted yet)
- Exercises solved: 2-2, 2-3, 2-4, 2-5, 2-6, 2-7, 2-8, 2-9, 2-10
- Notes: nine solution files (`2-2.c` through `2-10.c`) showed up loose in the chapter root instead of the `ex<chapter>-<section><letter>.c` convention. Sorted each into its section folder using the exercise-number-as-section-number rule (`2-6.c` -> section 2.6, etc.), which means some land in a different section than where the exercise conceptually appears in the book (e.g. the bit-manipulation exercises 2-6 through 2-9 are spread across 2.6-2.9 by number, not grouped under Bitwise Operators). Exercises 2-6 through 2-10 are function-only (no `main`), so no `.exe` was built for those, only for 2-3, 2-4, and 2-5. Added a CLAUDE.md rule to update this log automatically after every change going forward.
- Fixed the tracker: `scripts/update_tracker.py` was computing "total exercises" by scanning whatever `exercises-x.y.md` files already existed in the repo, so unstarted chapters (3 through 8) contributed 0 to the denominator instead of their real exercise counts. That's why the overall percent jumped to ~42% after only 1.something chapters. Added the official K&R per-section exercise counts (97 total across the book, from the Pearson table of contents) as a fixed field in the `KR` structure, and changed the math to cap solved-exercise counts at the chapter level (not per-section) since solution files get sorted by exercise number, not by which section they conceptually belong to in the book, so per-section capping was undercounting. Overall dropped from a bogus 41.7% to an honest 27.5%. Also fixed the progress chart: `progress/history.csv` had accumulated multiple duplicate rows per day from re-running the tracker, and the chart plotted the line against date labels but filled the area against plain integer indices, so duplicate rows made the line and the fill visually diverge. `append_history` now overwrites today's row instead of appending a new one each run, and the chart uses the same integer x-positions for both the line and the fill. Rebuilt `history.csv` from scratch by replaying it against every day's last commit with the corrected formula, so the chart's past points are accurate instead of just being wiped.

## 2026-08-16
- Sections: 2.1, 2.2, 2.3
- Exercises solved: none yet (notes and exercise lists written; 2.2 has exercise 2-1 open, 2.1 and 2.3 have none in the section text)
- Notes: started Chapter 2, set up the chapter folder and the first three sections. No chapter 2 summary yet since only 3 of 12 sections are done.

## 2026-08-15
- Sections: 1.9, 1.10
- Exercises solved: 1-16, 1-17, 1-18, 1-19, 1-20, 1-21, 1-22, 1-23, 1-24
- Notes: finished Chapter 1, so wrote the chapter summary too. Solution files kept showing up loose or misnamed (e.g. `1-16.c` in the chapter root, `1-20.c` in the exercises folder) instead of the `ex<chapter>-<section><letter>.c` convention, renamed them into place each time.

## 2026-08-14
- Sections: 1.6, 1.7, 1.8
- Exercises solved: 1-13, 1-14, 1-15
- Notes: 1.8 (Arguments - Call by Value) has no exercises in the section text, so its exercises file was created with a total of 0.

## 2026-08-12
- Sections: 1.3 (exercise cleanup), 1.5
- Exercises solved: 1-5, 1-6, 1-7, 1-8, 1-9, 1-10, 1-11, 1-12
- Notes: renamed and marked the 1.3 exercise 5 solution complete, then scaffolded and filled in 1.5 (Character Input and Output) the same day, notes and all seven exercises.

## 2026-08-11
- Sections: 1.1, 1.2
- Exercises solved: 1-1, 1-2, 1-3, 1-4
- Notes: renamed solution files to match the `ex<chapter>-<section><letter>.c` convention (they were named things like `hello.c` and `excercise-1-3.c`). Found and fixed a real bug in exercise 1-4: the Celsius to Fahrenheit formula used `+` instead of `*` (`lower + 9/5.0 + 32`), which threw every output value off by a constant +1.8°F.

## 2026-08-06
- Sections: 1.4
- Exercises solved: none (1.4, Symbolic Constants, has no exercises in the section text)

## 2026-08-05
- Sections: 1.3
- Exercises solved: none yet (notes and exercise list written, solution came later on 2026-08-12)

## 2026-08-04
- Sections: 1.2
- Exercises solved: none yet (notes and exercise list written, solutions came later on 2026-08-11)

## 2026-08-03
- Sections: 1.1
- Exercises solved: none yet (notes and exercise list written, solutions came later on 2026-08-11)

## 2026-07-27
- Set up the repo: tooling, templates, CLAUDE.md, and the progress tracker.
- No K&R sections read yet. Ready to start Chapter 1.
