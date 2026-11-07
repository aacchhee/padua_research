# Handoff 26 — Separate explanatory companion

- Status: done in 1036619b8df6041dac37793f20067f73d767ea50
- Previous handoff: 25-expanded-certificate-publication-preparation.md
- Next agent / model / effort: Codex coordinator; Sol high section developers; distinct Sol max mathematical/accessibility review per AC's preference
- Role: developer / orchestrator
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: `c6e195fa5211d4504fd2638f3c7686368e28daee`
- Main / base: `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`
- Stage: WORK
- Written by / date: Codex coordinator, serving metadata unexposed · 2026-11-07

AC requests a separate companion up to five times the current 48-page
paper, aimed at readers with university analysis. Keep exactly the same
five-section/subsection structure and theorem statements/numbers; retain
the formula numbers as well. Explain specialist language, notation,
motivations and intermediate arguments throughout. The original paper
directory and its existing PDF must remain intact.

Read rules, log, companion-paper/README.md, original mathematical source
and the accepted paper/consolidation-audit.md, affirmative-style-review.md
and section5-expansion-review.md as needed. The original is frozen at
the input SHA above. Work only in companion-paper/ for the new document.
Original paper/ is read-only. Preserve all original numbered statements
and numbered display blocks verbatim; additions are unnumbered. Define
terms before use, use examples and step-by-step derivations, retain direct
affirmative prose and the common proof organization. Keep actual theorem
assumptions, constants, degree guards, computational trust and retention
scope. This adds exposition, not new scientific claims or a native run.

Five Sol high developers own disjoint section groups; root owns main,
build/check utilities, docs and Git. A distinct Sol max reviewer owns
companion-paper/review.md. Build into the separate companion output tree.
Run check_correspondence.py with --artifacts after building to verify
preservation and actual label numbers; check the <=240-page ceiling,
diagnostics and rendered pages. Obtain one substantive focused review
of the expanded mathematics and reader accessibility, with exact freeze.
Resolve findings and document the actual artifact and review scope.

At completion commit outputs first; close 26 and open a numbered next
handoff in a separate handoff-only commit. Push the working branch before
replying and supply a fresh Europe/Oslo timestamped companion PDF. Carry
forward handoff 25's remaining publication context. Branch pushes are
authorized; the previously rejected PR metadata action remains pending.
Only AC merges. No main/force/tag/.github/settings changes.
