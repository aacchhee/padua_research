# Handoff 02 — padua-3d-20261106 — substantive audit

- Status: done in 64292b52db63404853000e2cc4ac90727797075b
- Previous handoff: [01-work.md](01-work.md)
- Next agent / model / effort: **Claude, Opus 5.5, xhigh**.
- Role: independent substantive auditor of Codex development.
- Branch: `codex/padua-3d-20261106`.
- Input head SHA: `f1a5b0936d8fb2b033c69af59a6366550f170999`.
  This is the completed output commit; the following commit publishes this handoff.
- Main / base: `76ba4214b100c86a44941f5e9a662ce9ce48efb8`.
- Stage: AUDIT.
- Written by / date: Codex, assigned gpt-6-astra high · 2026-11-06.

## Task

Perform the **single substantive independent audit** of the entire completed
development batch. Read current rules and record their full SHA. Read the
complete `state/IDEAS.md`, including every obstruction/disposition table,
because this branch carries mechanism and negative-result content. Read
`literature/INDEX.md` before evaluating source/novelty claims. The original
AC instruction and BRIEF remain in handoff 01; do not treat expectations as
premises or use their historical 3-D exclusions to close this topic.

The [report](../report.md) is the scientific map, not a replacement for the
proofs, source coverage or actual reruns. Audit every claimed PROVED statement,
the finite/empirical distinctions, the failed/deferred candidates, the
original OPEN targets and the preregistered gate decisions. In particular:

1. **T1:** binary annihilator classification, all translated phases and
   canonical projection orders; single **whole-coset** coordinate-reflection
   hypothesis; no minimal Pi_n interpolation for every n>=2. Reconstruct
   node inequalities, d2 Padua escape and the degree-one exception. Arbitrary
   cosine images and unions are outside it; broad C_k is OPEN.
2. **T2/T3:** exact Fourier/folded-cosine matrix, zero-index multiplicities,
   algebraic versus generic-axis lifting, compatible-relation annihilators,
   three quadratic falsifiers, and the committed 171-case H39 cover.
   The normalized cubic obstruction and full unshifted M=39 extension were
   upgraded to PROVED **only after** actual distinct-agent execution and
   separate Fraction-convolution reconstruction. Audit these material status
   changes in this round. They do not upgrade rank distributions, quality
   observations, phases, other moduli or an infinite-degree target.
3. **T4:** all-n stack unisolvence and Newton recursion, exact height
   determinant, Lobatto discriminant/permutation comparison, singular
   Riemann-sum passage and the coefficient 3*zeta(3)/(2*pi^2). Check the
   general upper majorant and exact-greedy exp(O(n log n)) upper bound;
   floating greedy tie tolerance is not a theorem premise. Only monotone
   order has the proved exponential lower rate. M/A/L numerical screens
   stop at n7 after the specified n6/n7 losses.
4. **T5:** all real weight vectors on the fixed Gaussian grid, sharp
   positive21/signed15 support minima and the off-grid14 existence control;
   all-q section commutator formulas and the known necessary extension
   bound. No arbitrary-support minimal-cubature or compatibility conclusion
   follows. Completed-section minimization was not executed.
5. **T6:** real-space projection/cosine lift, translation multiplier and
   factor27 correction; facet-coordinate torus covering, sawtooth signs,
   harmonic subset for d>=3 and denominator648*pi^3. Verify the claimed
   primary Subbotin1983/DEKL2017 comparison to the actual reading coverage.
   Universal logarithmic order is explicitly known, not a novelty claim.

## Read first

- `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`.
- Topic `LOG.md`, `BRIEF.md`, `plan.md`, `report.md`, `rounds.md`, `gates.md`,
  both family preregistrations plus T5 preregistration.
- All `attempts/T1.md` through `T6.md`, all `novelty-gate-T*.md`, and all
  `theory/t*.md`; candidate details and deferred routes are retained there.
- `literature-3d.md`, `literature-T1.md` through `literature-T6.md`, and
  relevant linked inherited theory/source records.
- `independent-checks-math.md`, `independent-checks-computation.md`, their
  code/receipts, `evidence-manifest.json`, `COLD_STORAGE.md`, `cold-storage.json`.
- `results/padua-3d-20261106.md`; PR33 and its WORK/AUDIT/PR sections.

The canonical T2 gate-reading coverage caveat is in its attempt record.
Disposition it explicitly; later independent reading does not retroactively
change the timing. No historical novelty is asserted for the retained
mechanisms. Primary comparisons remain incomplete for potential structural
note claims; assess their actual scope without inventing acceptance.

## Reproducible checks

Use a fresh isolated checkout of the input SHA for producer reruns so that
original developer receipts stay intact. Record your own commands, source
hashes, versions and outputs; reading the Astra receipts is not your rerun.
Code is unchanged and the scripts are small. From that checkout's root,
with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1` where numeric libraries occur:

```sh
python topics/padua-3d-20261106/code/replay.py
python topics/padua-3d-20261106/code/t1_reflection_enum.py --output /tmp/padua-3d-claude-t1.json
python topics/padua-3d-20261106/code/t2_screen.py
python topics/padua-3d-20261106/code/t2_generators.py
python topics/padua-3d-20261106/code/t2_quality.py
python topics/padua-3d-20261106/code/t2_check_cover.py
python topics/padua-3d-20261106/code/t3_checks.py
python topics/padua-3d-20261106/code/t4_stacks.py --max-degree 12
python topics/padua-3d-20261106/code/t5_exact.py --output /tmp/padua-3d-claude-t5-exact.json
python topics/padua-3d-20261106/code/t5_support.py --output /tmp/padua-3d-claude-t5-support.json
python topics/padua-3d-20261106/code/t6_sanity.py
```

`t4_stacks.py` must stop at 7 under its existing gates; do not reopen a killed
screen to obtain n8..20. The original first T2 receipt's preregistration digest
differs from the later appended preregistration; the independent computation
record preserves this provenance NOTE. Compare scientific results separately
from timestamps, output paths and that historical digest. Never rewrite a
producer receipt to make a comparison pass.

Before reruns, `python topics/padua-3d-20261106/code/artifact_manifest.py --verify`
checks the frozen code/data set; rerun producer receipts will legitimately
have new metadata, so do this integrity check against the original checkout
before they are replaced. The D0 replay retrieves two historical fixtures
with read-only `git show` at a full pushed commit; a shallow clone may need
that commit fetched. Dependency versions are in the receipts. No AC desktop,
large cold-storage delivery, cluster allocation or new final IDs are needed.

## Scope limits

- Audit author files only under this topic and its own results file. Do not
  change the developer's proof to approve it silently. This is audit round1;
  return material findings for a development response, following WORKFLOW.
- Neither Astra supplementary check is the required Claude audit. Their
  accepted scope does not settle priority, the broad original targets or PR
  readiness. No BLOCKING/MAJOR supplementary finding remains; M1 wording
  was resolved and reviewed, and the provenance NOTE is retained.
- No final IDs are reserved: **no range**. Do not allocate IDs, apply shared
  registries or mark the draft ready in this audit. Readiness/reservation
  refresh belongs to later PR preparation after audit dispositions.
- Do not change other topics, main, tags, `.github/` or repository settings;
  do not merge. Only AC merges. Preserve earlier handoff bodies.
- Generated proof-essential code/data are committed and small. Optional raw
  catalogues are regeneration-only working outputs with actual identities;
  no archival delivery was performed. Do not manufacture an archive claim.

## Acceptance and outputs

Write `audit-01.md`, identifying this exact candidate SHA, your actual model
and effort, every reviewed claim/status/dependency, novelty/source coverage,
executed independent evidence, findings by severity and residual limits.
Keep any new evidence normally below16KiB per file, with code to regenerate
larger output. Update the topic log and results as appropriate, preserving
the original OPEN goals and all candidate dispositions.

If findings require material changes, set WORK and open handoff03 for the
Codex development response. If accepted, set PR and open handoff03 for
Codex preparation (fresh reservation procedure, direct reviewed registry
diff, and a readiness check later; only AC merges). Do not add unnecessary
whole-batch audit rounds: focused re-audit applies only to material changes.
Commit audit outputs first. In a following commit close this handoff as
`done in <output-sha>` and add exactly one new numbered handoff, then push
before replying. End with the corresponding short continuation prompt.
