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
import re
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
#   (chapter_number, chapter_folder, chapter_title, [(section_number, folder), ...])
# A section folder name is "<section_number>-<slug>", and the folder value below
# is exactly that folder name.
# ---------------------------------------------------------------------------
KR = [
    (1, "ch01-tutorial-intro", "A Tutorial Introduction", [
        ("1.1", "1.1-getting-started"),
        ("1.2", "1.2-variables-arithmetic"),
        ("1.3", "1.3-for-statement"),
        ("1.4", "1.4-symbolic-constants"),
        ("1.5", "1.5-character-input-output"),
        ("1.6", "1.6-arrays"),
        ("1.7", "1.7-functions"),
        ("1.8", "1.8-arguments-call-by-value"),
        ("1.9", "1.9-character-arrays"),
        ("1.10", "1.10-external-variables-scope"),
    ]),
    (2, "ch02-types-operators-expressions", "Types, Operators and Expressions", [
        ("2.1", "2.1-variable-names"),
        ("2.2", "2.2-data-types-sizes"),
        ("2.3", "2.3-constants"),
        ("2.4", "2.4-declarations"),
        ("2.5", "2.5-arithmetic-operators"),
        ("2.6", "2.6-relational-logical-operators"),
        ("2.7", "2.7-type-conversions"),
        ("2.8", "2.8-increment-decrement-operators"),
        ("2.9", "2.9-bitwise-operators"),
        ("2.10", "2.10-assignment-operators-expressions"),
        ("2.11", "2.11-conditional-expressions"),
        ("2.12", "2.12-precedence-order-evaluation"),
    ]),
    (3, "ch03-control-flow", "Control Flow", [
        ("3.1", "3.1-statements-blocks"),
        ("3.2", "3.2-if-else"),
        ("3.3", "3.3-else-if"),
        ("3.4", "3.4-switch"),
        ("3.5", "3.5-loops-while-for"),
        ("3.6", "3.6-loops-do-while"),
        ("3.7", "3.7-break-continue"),
        ("3.8", "3.8-goto-labels"),
    ]),
    (4, "ch04-functions-program-structure", "Functions and Program Structure", [
        ("4.1", "4.1-basics-of-functions"),
        ("4.2", "4.2-functions-returning-non-integers"),
        ("4.3", "4.3-external-variables"),
        ("4.4", "4.4-scope-rules"),
        ("4.5", "4.5-header-files"),
        ("4.6", "4.6-static-variables"),
        ("4.7", "4.7-register-variables"),
        ("4.8", "4.8-block-structure"),
        ("4.9", "4.9-initialization"),
        ("4.10", "4.10-recursion"),
        ("4.11", "4.11-c-preprocessor"),
    ]),
    (5, "ch05-pointers-arrays", "Pointers and Arrays", [
        ("5.1", "5.1-pointers-addresses"),
        ("5.2", "5.2-pointers-function-arguments"),
        ("5.3", "5.3-pointers-arrays"),
        ("5.4", "5.4-address-arithmetic"),
        ("5.5", "5.5-character-pointers-functions"),
        ("5.6", "5.6-pointer-arrays-pointers-to-pointers"),
        ("5.7", "5.7-multi-dimensional-arrays"),
        ("5.8", "5.8-initialization-pointer-arrays"),
        ("5.9", "5.9-pointers-vs-multi-dimensional-arrays"),
        ("5.10", "5.10-command-line-arguments"),
        ("5.11", "5.11-pointers-to-functions"),
        ("5.12", "5.12-complicated-declarations"),
    ]),
    (6, "ch06-structures", "Structures", [
        ("6.1", "6.1-basics-of-structures"),
        ("6.2", "6.2-structures-functions"),
        ("6.3", "6.3-arrays-of-structures"),
        ("6.4", "6.4-pointers-to-structures"),
        ("6.5", "6.5-self-referential-structures"),
        ("6.6", "6.6-table-lookup"),
        ("6.7", "6.7-typedef"),
        ("6.8", "6.8-unions"),
        ("6.9", "6.9-bit-fields"),
    ]),
    (7, "ch07-input-output", "Input and Output", [
        ("7.1", "7.1-standard-input-output"),
        ("7.2", "7.2-formatted-output-printf"),
        ("7.3", "7.3-variable-length-argument-lists"),
        ("7.4", "7.4-formatted-input-scanf"),
        ("7.5", "7.5-file-access"),
        ("7.6", "7.6-error-handling-stderr-exit"),
        ("7.7", "7.7-line-input-output"),
        ("7.8", "7.8-miscellaneous-functions"),
    ]),
    (8, "ch08-unix-system-interface", "The UNIX System Interface", [
        ("8.1", "8.1-file-descriptors"),
        ("8.2", "8.2-low-level-io-read-write"),
        ("8.3", "8.3-open-creat-close-unlink"),
        ("8.4", "8.4-random-access-lseek"),
        ("8.5", "8.5-example-implementation-fopen-getc"),
        ("8.6", "8.6-example-listing-directories"),
        ("8.7", "8.7-example-storage-allocator"),
    ]),
]

CHECKBOX_RE = re.compile(r"^\s*-\s*\[[ xX]\]", re.MULTILINE)


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


def count_exercises(exercises_md_path):
    """Total exercises listed = number of checkbox lines in the file."""
    if not os.path.isfile(exercises_md_path):
        return 0
    return len(CHECKBOX_RE.findall(read_text(exercises_md_path)))


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
        for secnum, secfolder in sections:
            secdir = os.path.join(chdir, secfolder)
            notes_path = os.path.join(secdir, "notes-%s.md" % secnum)
            ex_dir = os.path.join(secdir, "exercises")
            ex_md = os.path.join(ex_dir, "exercises-%s.md" % secnum)

            sec_rows.append({
                "number": secnum,
                "exists": os.path.isdir(secdir),
                "notes_done": notes_is_real(notes_path),
                "ex_total": count_exercises(ex_md),
                "ex_solved": count_solutions(ex_dir),
            })

        summary_path = os.path.join(chdir, "summary-%d.md" % chnum)
        chapters.append({
            "number": chnum,
            "folder": chfolder,
            "title": chtitle,
            "sections": sec_rows,
            "summary_done": summary_is_real(summary_path),
            "started": os.path.isdir(chdir),
        })
    return chapters


def totals(chapters):
    total_sections = sum(len(c["sections"]) for c in chapters)
    notes_done = sum(1 for c in chapters for s in c["sections"] if s["notes_done"])

    total_chapters = len(chapters)
    summaries_done = sum(1 for c in chapters if c["summary_done"])

    ex_total = sum(s["ex_total"] for c in chapters for s in c["sections"])
    ex_solved = sum(min(s["ex_solved"], s["ex_total"]) if s["ex_total"] else 0
                    for c in chapters for s in c["sections"])

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
    os.makedirs(PROGRESS_DIR, exist_ok=True)
    new_file = not os.path.isfile(HISTORY_CSV)
    with open(HISTORY_CSV, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["date", "overall_percent"])
        writer.writerow([date.today().isoformat(), "%.2f" % overall])


def read_history():
    rows = []
    if not os.path.isfile(HISTORY_CSV):
        return rows
    with open(HISTORY_CSV, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for r in reader:
            try:
                rows.append((r["date"], float(r["overall_percent"])))
            except (KeyError, ValueError):
                continue
    return rows


def make_chart(history):
    """Plot cumulative completion over time. If there is only one datapoint,
    matplotlib still draws a single marker, which is fine."""
    os.makedirs(PROGRESS_DIR, exist_ok=True)
    dates = [d for d, _ in history]
    values = [v for _, v in history]

    plt.style.use("seaborn-v0_8-darkgrid") if "seaborn-v0_8-darkgrid" in plt.style.available else None

    fig, ax = plt.subplots(figsize=(9, 4.5), dpi=140)
    ax.plot(dates, values, marker="o", linewidth=2.4, markersize=6,
            color="#2f6fed", markerfacecolor="#ffffff",
            markeredgecolor="#2f6fed", markeredgewidth=1.8, zorder=3)
    ax.fill_between(range(len(values)), values, color="#2f6fed", alpha=0.12, zorder=1)

    ax.set_title("K&R progress over time", fontsize=14, fontweight="bold", pad=12)
    ax.set_ylabel("Completion (%)", fontsize=11)
    ax.set_ylim(0, 100)
    ax.margins(x=0.02)
    ax.grid(True, alpha=0.3)

    # Keep the x-axis readable even with many dates.
    ax.xaxis.set_major_locator(MaxNLocator(nbins=8, integer=False))
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
    lines.append("![Progress over time](progress/progress.png)")
    lines.append("")
    lines.append("## By chapter")
    lines.append("")
    lines.append("| Chapter | Notes | Summary | Exercises |")
    lines.append("| --- | --- | --- | --- |")

    for c in chapters:
        notes_done = sum(1 for s in c["sections"] if s["notes_done"])
        notes_total = len(c["sections"])
        ex_total = sum(s["ex_total"] for s in c["sections"])
        ex_solved = sum(min(s["ex_solved"], s["ex_total"]) if s["ex_total"] else 0
                        for s in c["sections"])
        summary_cell = "yes" if c["summary_done"] else ("-" if notes_done < notes_total else "no")
        name = "%d. %s" % (c["number"], c["title"])
        lines.append("| %s | %d / %d | %s | %d / %d |" % (
            name, notes_done, notes_total, summary_cell, ex_solved, ex_total))

    lines.append("")
    lines.append("Legend: Summary shows `yes` when written, `no` when the chapter's "
                 "sections are all done but the summary is still missing, and `-` "
                 "while the chapter is not finished yet.")
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
