# MATHS 765 Mathematical Modelling — Tutorial Repository

Shared repository for the weekly tutorial work in the Mathematical Modelling course
(Weeks 1–6). This is where you practise building small models, producing figures, and
working the way real teams work: version control, pull requests, and code review.

## The one rule that matters: reproducibility

**Any classmate must be able to regenerate your figure from your folder without asking you a question.**
Everything else here serves that goal. Your code can be in any language you like —
Python, MATLAB, Julia, whatever you're fastest in. We standardise the *deliverable and
the interface*, not the language.

## Repository layout

```
/week01/
  /<your-username>/
    report.md      <- half-page model report (what you reduced and why, conclusions, etc.)
    figure.png     <- the figure, meeting the week's spec
    <your code>    <- the script(s)/notebook that produced figure.png
    README.md      <- exact commands to regenerate figure.png
...
PARTICIPANTS.md    <- add yourself here in Week 1
CONTRIBUTING.md    <- how to contribute and review (read this first)
```

Each week you add **one folder** under that week, named with your username.

## Each contribution contains

1. **`report.md`** — half a page. State the model, the reduction/assumption you made,
   *why* it's justified, and where it would break or any other conclusions you think it's relevant.
2. **A figure** — meeting the spec given in that week's tutorial.
3. **The code** that produced the figure, in your language of choice.
4. **A short `README.md`** — the exact command(s) to regenerate the figure
   (e.g. `python solve.py`, or `run main.m`), plus anything needed to run it.

## Workflow (every week)

1. Pull the latest `main`.
2. Branch: `git checkout -b week01-<username>`.
3. Do the work in your folder.
4. Commit and push; open a **pull request**.
5. You'll be **assigned to review** a classmate's PR — check that you can rerun their
   figure. Approve or request changes.

See **[CONTRIBUTING.md](CONTRIBUTING.md)** for the details and the review checklist.

## Getting help

Open an issue with the `question` label, or ask in the tutorial. Struggling with Git is
expected in Week 1 — that's what the first tutorial is for.
