#!/usr/bin/env python3
"""
update_tracker.py

Scans the repo, works out how far through K&R I am, and regenerates:
  - TRACKER.md            (overall %, per-chapter breakdown, progress chart)
  - progress/history.csv  (a dated datapoint appended every run)
  - progress/progress.png (a line chart of completion over time)

Progress is measured in three parts:
  - notes:      does each section have a real notes file (not just a scaffold)?
  - summaries:  does each finished chapter have a real summary file?
  - exercises:  how many .c solution files exist vs how many exercises are listed?

Run it from anywhere:
    python scripts/update_tracker.py
"""

import csv
import os
from datetime import date

import matplotlib
matplotlib.use("Agg")  # no display needed, just save a PNG
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# ---------------------------------------------------------------------------
# Repo layout
# ---------------------------------------------------------------------------
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROGRESS_DIR = os.path.join(REPO_ROOT, "progress")
HISTORY_CSV = os.path.join(PROGRESS_DIR, "history.csv")
CHART_PNG = os.path.join(PROGRESS_DIR, "progress.png")
TRACKER_MD = os.path.join(REPO_ROOT, "TRACKER.md")

# Markers that mean "this file is still just a scaffold, not real content".
NOTES_PLACEHOLDER = "<!-- placeholder:notes -->"
SUMMARY_PLACEHOLDER = "<!-- placeholder:summary -->"

# ---------------------------------------------------------------------------
# The full K&R structure. This is the single source of truth for folder names
# and for the total counts used in the percentages. Each entry is:
#   (chapter_number, chapter_folder, chapter_title, [(section_number, folder, official_exercise_count), ...])
# A section folder name is "<section_number>-<slug>", and the folder value below
# is exactly that folder name.
#
# official_exercise_count is the number of exercises the K&R book itself lists
# under that section (per the Pearson table of contents), with any numbered
# sub-subsections (like 1.5.1-1.5.4 or 7.8.1-7.8.7) folded into their parent
# section since this repo doesn't split those into their own folders. These
# counts are fixed and don't depend on what's actually in the repo yet, which
# is what makes the overall percentage meaningful even for chapters that
# haven't been started: an unstarted chapter still counts its real exercises
# against the total, instead of contributing 0 and quietly shrinking the pool.
# Chapter totals: 24, 10, 6, 14, 20, 6, 9, 8 = 97 exercises across the book.
# ---------------------------------------------------------------------------
KR = [
    (1, "ch01-tutorial-intro", "A Tutorial Introduction", [
        ("1.1", "Getting Started", "1.1-getting-started", 2),
        ("1.2", "Variables and Arithmetic Expressions", "1.2-variables-arithmetic", 2),
        ("1.3", "The for statement", "1.3-for-statement", 1),
        ("1.4", "Symbolic Constants", "1.4-symbolic-constants", 0),
        ("1.5", "Character Input and Output", "1.5-character-input-output", 7),
        ("1.6", "Arrays", "1.6-arrays", 2),
        ("1.7", "Functions", "1.7-functions", 1),
        ("1.8", "Arguments - Call by Value", "1.8-arguments-call-by-value", 0),
        ("1.9", "Character Arrays", "1.9-character-arrays", 4),
        ("1.10", "External Variables and Scope", "1.10-external-variables-scope", 5),
    ]),
    (2, "ch02-types-operators-expressions", "Types, Operators and Expressions", [
        ("2.1", "Variable Names", "2.1-variable-names", 0),
        ("2.2", "Data Types and Sizes", "2.2-data-types-sizes", 1),
        ("2.3", "Constants", "2.3-constants", 0),
        ("2.4", "Declarations", "2.4-declarations", 0),
        ("2.5", "Arithmetic Operators", "2.5-arithmetic-operators", 0),
        ("2.6", "Relational and Logical Operators", "2.6-relational-logical-operators", 1),
        ("2.7", "Type Conversions", "2.7-type-conversions", 1),
        ("2.8", "Increment and Decrement Operators", "2.8-increment-decrement-operators", 2),
        ("2.9", "Bitwise Operators", "2.9-bitwise-operators", 3),
        ("2.10", "Assignment Operators and Expressions", "2.10-assignment-operators-expressions", 1),
        ("2.11", "Conditional Expressions", "2.11-conditional-expressions", 1),
        ("2.12", "Precedence and Order of Evaluation", "2.12-precedence-order-evaluation", 0),
    ]),
    (3, "ch03-control-flow", "Control Flow", [
        ("3.1", "Statements and Blocks", "3.1-statements-blocks", 0),
        ("3.2", "If-Else", "3.2-if-else", 0),
        ("3.3", "Else-If", "3.3-else-if", 1),
        ("3.4", "Switch", "3.4-switch", 1),
        ("3.5", "Loops - While and For", "3.5-loops-while-for", 1),
        ("3.6", "Loops - Do-While", "3.6-loops-do-while", 3),
        ("3.7", "Break and Continue", "3.7-break-continue", 0),
        ("3.8", "Goto and labels", "3.8-goto-labels", 0),
    ]),
    (4, "ch04-functions-program-structure", "Functions and Program Structure", [
        ("4.1", "Basics of Functions", "4.1-basics-of-functions", 1),
        ("4.2", "Functions Returning Non-integers", "4.2-functions-returning-non-integers", 1),
        ("4.3", "External Variables", "4.3-external-variables", 8),
        ("4.4", "Scope Rules", "4.4-scope-rules", 0),
        ("4.5", "Header Files", "4.5-header-files", 0),
        ("4.6", "Static Variables", "4.6-static-variables", 1),
        ("4.7", "Register Variables", "4.7-register-variables", 0),
        ("4.8", "Block Structure", "4.8-block-structure", 0),
        ("4.9", "Initialization", "4.9-initialization", 0),
        ("4.10", "Recursion", "4.10-recursion", 2),
        ("4.11", "The C Preprocessor", "4.11-c-preprocessor", 1),
    ]),
    (5, "ch05-pointers-arrays", "Pointers and Arrays", [
        ("5.1", "Pointers and Addresses", "5.1-pointers-addresses", 0),
        ("5.2", "Pointers and Function Arguments", "5.2-pointers-function-arguments", 2),
        ("5.3", "Pointers and Arrays", "5.3-pointers-arrays", 0),
        ("5.4", "Address Arithmetic", "5.4-address-arithmetic", 0),
        ("5.5", "Character Pointers and Functions", "5.5-character-pointers-functions", 4),
        ("5.6", "Pointer Arrays; Pointers to Pointers", "5.6-pointer-arrays-pointers-to-pointers", 1),
        ("5.7", "Multi-dimensional Arrays", "5.7-multi-dimensional-arrays", 1),
        ("5.8", "Initialization of Pointer Arrays", "5.8-initialization-pointer-arrays", 0),
        ("5.9", "Pointers vs. Multi-dimensional Arrays", "5.9-pointers-vs-multi-dimensional-arrays", 1),
        ("5.10", "Command-line Arguments", "5.10-command-line-arguments", 4),
        ("5.11", "Pointers to Functions", "5.11-pointers-to-functions", 4),
        ("5.12", "Complicated Declarations", "5.12-complicated-declarations", 3),
    ]),
    (6, "ch06-structures", "Structures", [
        ("6.1", "Basics of Structures", "6.1-basics-of-structures", 1),
        ("6.2", "Structures and Functions", "6.2-structures-functions", 1),
        ("6.3", "Arrays of Structures", "6.3-arrays-of-structures", 1),
        ("6.4", "Pointers to Structures", "6.4-pointers-to-structures", 1),
        ("6.5", "Self-referential Structures", "6.5-self-referential-structures", 1),
        ("6.6", "Table Lookup", "6.6-table-lookup", 1),
        ("6.7", "Typedef", "6.7-typedef", 0),
        ("6.8", "Unions", "6.8-unions", 0),
        ("6.9", "Bit-fields", "6.9-bit-fields", 0),
    ]),
    (7, "ch07-input-output", "Input and Output", [
        ("7.1", "Standard Input and Output", "7.1-standard-input-output", 1),
        ("7.2", "Formatted Output - printf", "7.2-formatted-output-printf", 1),
        ("7.3", "Variable-length Argument Lists", "7.3-variable-length-argument-lists", 1),
        ("7.4", "Formatted Input - Scanf", "7.4-formatted-input-scanf", 1),
        ("7.5", "File Access", "7.5-file-access", 1),
        ("7.6", "Error Handling - Stderr and Exit", "7.6-error-handling-stderr-exit", 1),
        ("7.7", "Line Input and Output", "7.7-line-input-output", 1),
        ("7.8", "Miscellaneous Functions", "7.8-miscellaneous-functions", 2),
    ]),
    (8, "ch08-unix-system-interface", "The UNIX System Interface", [
        ("8.1", "File Descriptors", "8.1-file-descriptors", 0),
        ("8.2", "Low Level I/O - Read and Write", "8.2-low-level-io-read-write", 1),
        ("8.3", "Open, Creat, Close, Unlink", "8.3-open-creat-close-unlink", 1),
        ("8.4", "Random Access - Lseek", "8.4-random-access-lseek", 1),
        ("8.5", "Example - An implementation of Fopen and Getc", "8.5-example-implementation-fopen-getc", 2),
        ("8.6", "Example - Listing Directories", "8.6-example-listing-directories", 2),
        ("8.7", "Example - A Storage Allocator", "8.7-example-storage-allocator", 1),
    ]),
]

# ---------------------------------------------------------------------------
# Scanning helpers
# ---------------------------------------------------------------------------
def read_text(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except (OSError, UnicodeDecodeError):
        return ""


def notes_is_real(path):
    """A notes file counts as done if it exists, is not a scaffold, and has
    some actual content."""
    if not os.path.isfile(path):
        return False
    text = read_text(path)
    if NOTES_PLACEHOLDER in text:
        return False
    return len(text.strip()) > 0


def summary_is_real(path):
    if not os.path.isfile(path):
        return False
    text = read_text(path)
    if SUMMARY_PLACEHOLDER in text:
        return False
    return len(text.strip()) > 0


def count_solutions(exercises_dir):
    """Solved exercises = number of .c files in the exercises folder."""
    if not os.path.isdir(exercises_dir):
        return 0
    return sum(1 for name in os.listdir(exercises_dir) if name.endswith(".c"))


# ---------------------------------------------------------------------------
# Build the progress model
# ---------------------------------------------------------------------------
def scan():
    chapters = []
    for chnum, chfolder, chtitle, sections in KR:
        chdir = os.path.join(REPO_ROOT, chfolder)

        sec_rows = []
        for secnum, sectitle, secfolder, ex_official in sections:
            secdir = os.path.join(chdir, secfolder)
            notes_path = os.path.join(secdir, "notes-%s.md" % secnum)
            ex_dir = os.path.join(secdir, "exercises")

            sec_rows.append({
                "number": secnum,
                "title": sectitle,
                "exists": os.path.isdir(secdir),
                "notes_done": notes_is_real(notes_path),
                "ex_total": ex_official,
                "ex_solved_raw": count_solutions(ex_dir),
            })

        summary_path = os.path.join(chdir, "summary-%d.md" % chnum)
        ex_total_chapter = sum(s["ex_total"] for s in sec_rows)
        ex_solved_raw_chapter = sum(s["ex_solved_raw"] for s in sec_rows)
        chapters.append({
            "number": chnum,
            "folder": chfolder,
            "title": chtitle,
            "sections": sec_rows,
            "summary_done": summary_is_real(summary_path),
            "started": os.path.isdir(chdir),
            "ex_total": ex_total_chapter,
            # Solution files get sorted into a section folder by exercise
            # number, not by which section the exercise conceptually belongs
            # to in the book (see CLAUDE.md), so counting solved exercises
            # against the official per-section count doesn't line up.
            # Capping at the chapter level instead keeps the arithmetic
            # honest without requiring every solution file to live in its
            # "correct" section folder.
            "ex_solved": min(ex_solved_raw_chapter, ex_total_chapter),
        })
    return chapters


def totals(chapters):
    total_sections = sum(len(c["sections"]) for c in chapters)
    notes_done = sum(1 for c in chapters for s in c["sections"] if s["notes_done"])

    total_chapters = len(chapters)
    summaries_done = sum(1 for c in chapters if c["summary_done"])

    # Fixed, official K&R exercise counts (97 total), not derived from
    # whatever happens to exist in the repo yet. An unstarted chapter still
    # counts its real exercises against the total instead of contributing 0.
    ex_total = sum(c["ex_total"] for c in chapters)
    ex_solved = sum(c["ex_solved"] for c in chapters)

    # Single pool so the overall number is always well defined.
    possible = total_sections + total_chapters + ex_total
    done = notes_done + summaries_done + ex_solved
    overall = (100.0 * done / possible) if possible else 0.0

    return {
        "total_sections": total_sections,
        "notes_done": notes_done,
        "total_chapters": total_chapters,
        "summaries_done": summaries_done,
        "ex_total": ex_total,
        "ex_solved": ex_solved,
        "overall": overall,
    }


# ---------------------------------------------------------------------------
# History + chart
# ---------------------------------------------------------------------------
def append_history(overall):
    """Add (or update) today's datapoint. Re-running the tracker multiple
    times in one day replaces today's row instead of appending a new one, so
    the chart never gets more than one point per day."""
    os.makedirs(PROGRESS_DIR, exist_ok=True)
    rows = read_history()
    today = date.today().isoformat()
    rows = [(d, v) for d, v in rows if d != today]
    rows.append((today, overall))
    with open(HISTORY_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "overall_percent"])
        for d, v in rows:
            writer.writerow([d, "%.2f" % v])


def read_history():
    """One row per date (last value wins if the CSV has duplicates from
    before this was deduped on write), sorted chronologically."""
    if not os.path.isfile(HISTORY_CSV):
        return []
    by_date = {}
    with open(HISTORY_CSV, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            try:
                by_date[r["date"]] = float(r["overall_percent"])
            except (KeyError, ValueError):
                continue
    return sorted(by_date.items())


def make_chart(history):
    """Plot cumulative completion over time. If there is only one datapoint,
    matplotlib still draws a single marker, which is fine."""
    os.makedirs(PROGRESS_DIR, exist_ok=True)
    dates = [d for d, _ in history]
    values = [v for _, v in history]
    positions = range(len(values))

    plt.style.use("seaborn-v0_8-darkgrid") if "seaborn-v0_8-darkgrid" in plt.style.available else None

    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=140)
    # Both the line and the fill use the same integer x positions (one per
    # date, evenly spaced) so they can't drift apart from each other. Actual
    # dates are applied as tick labels afterwards.
    ax.plot(positions, values, marker="o", linewidth=2.4, markersize=6,
            color="#2f6fed", markerfacecolor="#ffffff",
            markeredgecolor="#2f6fed", markeredgewidth=1.8, zorder=3)
    ax.fill_between(positions, values, color="#2f6fed", alpha=0.12, zorder=1)

    ax.set_title("K&R progress over time", fontsize=14, fontweight="bold", pad=12)
    ax.set_ylabel("Completion (%)", fontsize=11)
    ax.set_ylim(0, 100)
    ax.margins(x=0.02)
    ax.grid(True, alpha=0.3)

    # Keep the x-axis readable even with many dates: pick at most 8 evenly
    # spaced positions and label those with their real dates.
    ax.set_xticks(list(positions))
    nbins = 8
    tick_positions = sorted(set(
        MaxNLocator(nbins=nbins, integer=True).tick_values(0, len(values) - 1)
    )) if len(values) > 1 else [0]
    tick_positions = [int(p) for p in tick_positions if 0 <= p < len(values)]
    ax.set_xticks(tick_positions)
    ax.set_xticklabels([dates[p] for p in tick_positions])
    for label in ax.get_xticklabels():
        label.set_rotation(30)
        label.set_ha("right")
        label.set_fontsize(9)

    if values:
        ax.annotate("%.1f%%" % values[-1],
                    xy=(len(values) - 1, values[-1]),
                    xytext=(0, 10), textcoords="offset points",
                    ha="center", fontsize=10, fontweight="bold",
                    color="#2f6fed")

    fig.tight_layout()
    fig.savefig(CHART_PNG)
    plt.close(fig)


# ---------------------------------------------------------------------------
# TRACKER.md
# ---------------------------------------------------------------------------
def progress_bar(pct, width=24):
    filled = int(round(pct / 100.0 * width))
    return "`[" + "#" * filled + "-" * (width - filled) + "]`"


def write_tracker(chapters, t):
    lines = []
    lines.append("# Progress Tracker")
    lines.append("")
    lines.append("Auto-generated by `scripts/update_tracker.py`. Do not edit by hand.")
    lines.append("")
    lines.append("_Last updated: %s_" % date.today().isoformat())
    lines.append("")
    lines.append("## Overall")
    lines.append("")
    lines.append("**%.1f%% complete** %s" % (t["overall"], progress_bar(t["overall"])))
    lines.append("")
    lines.append("| Metric | Done | Total |")
    lines.append("| --- | --- | --- |")
    lines.append("| Section notes | %d | %d |" % (t["notes_done"], t["total_sections"]))
    lines.append("| Chapter summaries | %d | %d |" % (t["summaries_done"], t["total_chapters"]))
    lines.append("| Exercises solved | %d | %d |" % (t["ex_solved"], t["ex_total"]))
    lines.append("")
    lines.append("## Progress over time")
    lines.append("")
    lines.append("![Progress over time](progress/progress.png)")
    lines.append("")

    # --- By chapter -------------------------------------------------------
    lines.append("## By chapter")
    lines.append("")
    lines.append("| Chapter | Notes | Summary | Exercises |")
    lines.append("| --- | :---: | :---: | :---: |")

    for c in chapters:
        notes_done = sum(1 for s in c["sections"] if s["notes_done"])
        notes_total = len(c["sections"])
        summary_cell = "yes" if c["summary_done"] else ("-" if notes_done < notes_total else "no")
        name = "%d. %s" % (c["number"], c["title"])
        lines.append("| %s | %d / %d | %s | %d / %d |" % (
            name, notes_done, notes_total, summary_cell, c["ex_solved"], c["ex_total"]))

    lines.append("")
    lines.append("**Legend (Summary column):** `yes` = summary written, "
                 "`no` = all sections in the chapter are done but the summary is "
                 "not written yet, `-` = chapter not finished yet so no summary is "
                 "expected.")
    lines.append("")

    # --- By subsection ----------------------------------------------------
    lines.append("## By subsection")
    lines.append("")
    for c in chapters:
        notes_done = sum(1 for s in c["sections"] if s["notes_done"])
        notes_total = len(c["sections"])
        summary_cell = "yes" if c["summary_done"] else ("-" if notes_done < notes_total else "no")
        lines.append("### Chapter %d - %s" % (c["number"], c["title"]))
        lines.append("")
        lines.append("| Section | Title | Notes | Summary | Exercises |")
        lines.append("| :---: | --- | :---: | :---: | :---: |")
        for s in c["sections"]:
            if not s["exists"]:
                notes_cell = "-"
            elif s["notes_done"]:
                notes_cell = "yes"
            else:
                notes_cell = "no"
            lines.append("| %s | %s | %s | %s | %d / %d |" % (
                s["number"], s["title"], notes_cell, summary_cell,
                s["ex_solved_raw"], s["ex_total"]))
        lines.append("")

    lines.append("**Legend (Notes column):** `yes` = notes written, "
                 "`no` = section folder exists but notes are still empty, "
                 "`-` = section folder not created yet. Exercise counts here are "
                 "official K&R per-section counts vs. `.c` files actually filed "
                 "in that section's folder; solution files get sorted by exercise "
                 "number (see CLAUDE.md), not by which section the exercise "
                 "conceptually belongs to, so a section can show more or fewer "
                 "solved than the book lists for it even though the chapter total "
                 "is accurate. The Summary column is "
                 "chapter-level, so it shows the same value for every section in a "
                 "chapter (`yes` written, `no` due but missing, `-` not expected yet).")
    lines.append("")

    with open(TRACKER_MD, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


# ---------------------------------------------------------------------------
def main():
    chapters = scan()
    t = totals(chapters)
    append_history(t["overall"])
    make_chart(read_history())
    write_tracker(chapters, t)
    print("Updated TRACKER.md")
    print("Overall: %.1f%%  (notes %d/%d, summaries %d/%d, exercises %d/%d)" % (
        t["overall"], t["notes_done"], t["total_sections"],
        t["summaries_done"], t["total_chapters"], t["ex_solved"], t["ex_total"]))


if __name__ == "__main__":
    main()
