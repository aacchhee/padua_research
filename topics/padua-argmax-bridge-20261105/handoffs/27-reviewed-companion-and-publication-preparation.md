# Handoff 27 — Reviewed explanatory companion and publication preparation

- Status: open
- Previous handoff: 26-expanded-explanatory-companion.md
- Next agent / model / effort: Codex coordinator, gpt-6.1-sol medium for routine publication preparation; Sol high for mathematical exposition; distinct Sol max for necessary focused mathematical/accessibility review per AC's preference
- Role: orchestrator / publication preparation
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: `1036619b8df6041dac37793f20067f73d767ea50`
- Main / base: `f70a260e5b5f9a01209dc8a05faabdcf8db1feeb`
- Stage: WORK (remaining publication preparation; companion request complete)
- Written by / date: Codex coordinator, serving metadata unexposed · 2026-11-07

## Read first and completed work

Read rules, the current log, companion-paper/README.md, BUILD.md and
review.md. Handoff 25 retains the earlier publication context. AC asked
for a separate companion up to five times the 48-page article, preserving
its exact structure and theorem/formula numbers, for readers with
university analysis. The screenshot was an example: the explanatory
standard applies throughout. This work is complete and reviewed.

The original paper directory and original PDF remain intact at baseline
`c6e195fa5211d4504fd2638f3c7686368e28daee`. All companion work is in
companion-paper/ and its separate local-output tree. The new document
has 162 pages with the same five sections/subsections, 13 formal
statements, 90 numbered display environments, all 211 original displays
and all 113 compiled label numbers preserved. Definitions and calculations
are explained throughout, including the finite-row coefficient ledgers.
The distinct Sol max review ACCEPTS the complete companion at source
freeze `ac945041ce73b74c2c4ec29c42ebeb8773e7a9b8`; no finding remains.

Current companion download:
`local-output/padua-argmax-bridge-20261105/companion-paper/padua-companion-20261107-222747-Oslo.pdf`,
1153227 bytes, SHA-256
`2ec6b0723ccea6eef1368dfa0c974c4ec679a3279ef84d6ccb696c4a42c7d2f7`.
The unchanged original 48-page PDF remains under paper/ in local-output,
640116 bytes, SHA-256
`07db86350e74f66a46269965ace65300750f5405ddcd9d30f8daeb59411ca0f0`.
Use fresh Europe/Oslo timestamped filenames for revised downloads.

## Remaining task and boundaries

Respond to further reader/editorial feedback and continue proportionate
publication preparation. Preserve the original article when revising the
companion. Keep the same statement/formula numbers and the direct,
affirmative style. Use the separate companion build; run
check_correspondence.py and, when the preserved local baseline PDF/aux
exist, its --artifacts mode. Review a material new derivation by focused
diff; completed broad proof reviews remain the baseline.

Retain handoff 25's separate historical batch/readiness, qualified
prior-art, final human review, durable public code/evidence release and
eventual single-TeX submission tasks. Intermediate IDs remain authorized
until reviewed PR preparation. Author/disclosures, template provenance,
actual native-verification scope and selective retention are unchanged.
Native campaigns and new research require a substantive task reason.

Evidence index remains 396 entries / 32414 bytes; the conservative
generated-size bound remains 9774001 bytes against AC's 10000000 cap.
All PDFs, dependencies, logs and images stay outside Git. Branch pushes
remain authorized; the previously rejected PR metadata action remains
pending in the canonical log. Root alone controls Git; only AC merges.
No main/force/tag/.github/settings changes belong to this task.

Record actual changes/checks, commit outputs first, then close this
handoff and open the next numbered handoff in a separate handoff-only
commit at the next session boundary. Push before replying and provide
the fresh timestamped PDF for a revised draft.
