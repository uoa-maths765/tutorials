# Contributing

This file defines how work is submitted and reviewed. The whole point is to practise a
real collaborative workflow, so we follow it even though the tasks are small.

## Language policy

**Use whatever language you're most comfortable in.** Python, MATLAB, Julia, R — all fine,
and you may switch week to week. What is *not* optional is that someone else can run your
code and get your figure. Reproducibility is the skill; the language is not.

## Submitting work (pull requests)

1. **Sync** with the latest `main`:
   ```
   git checkout main
   git pull
   ```
2. **Branch**, named `week<NN>-<username>`:
   ```
   git checkout -b week01-jpatinoe
   ```
3. **Work** inside `week<NN>/<username>/`. Include:
   - `report.md` — half-page model report (model, reduction, justification, breakdown).
   - the figure file, meeting the week's spec.
   - your code.
   - a short `README.md` with the exact command(s) to regenerate the figure.
4. **Commit** in small, sensible steps with clear messages
   (`git commit -m "week01: nondimensionalise cooling model"`).
5. **Push and open a pull request.** In the PR description, paste the one line a reviewer
   should run to regenerate your figure.

## Reviewing (you will be assigned one PR per week)

Reviewing is graded participation and is the most professionally useful part. For the PR
you're assigned:

**Reviewer checklist**
- [ ] I followed the README and **regenerated the figure** (or hit a specific, reported blocker).
- [ ] The `report.md` clearly states the reduction/assumption and *why* it holds, plus any other conclusion.
- [ ] Code is readable: sensible names, brief comments where the logic isn't obvious.
- [ ] No stray files, no absolute paths that only work on the author's machine.

Leave at least one substantive comment. "Approve" only once you could actually rerun it.
Requesting changes is normal and helpful — it's not criticism of the person.

## The reproducibility standard (non-negotiable)

A folder passes if a classmate can, from a clean checkout:

1. read your `README.md`,
2. run the stated command(s),
3. obtain your figure,

**without contacting you.** If that fails, the contribution isn't finished — regardless of
whether the maths is correct.

## Commit hygiene

- Commit code and reports, **not** large data dumps or environment folders.
- One logical change per commit where you can.
- If you use a notebook, also commit a runnable script or clear run instructions.
