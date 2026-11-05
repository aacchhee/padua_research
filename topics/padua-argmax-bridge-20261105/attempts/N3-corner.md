# N3 practical corner-radius implementation — 2026-11-05

Developer: Codex, parent-assigned gpt-6.1-sol xhigh; runtime serving
metadata is not independently exposed. Rules/input SHA:
714f3cad18859c07cd13f31561f2a185f9591a7f. Branch:
codex/padua-argmax-bridge-20261105. Parent alone controls Git/shared records.

Authorized scope: quantitative implementation of IDEA-330/454/457;
actual per-degree W_n, no individual sign-preservation claim. Exact gate:
`../novelty-gate-N3-corner.md`, written before code/candidate development.
The analytic implication is separately recorded as PROVED in
`../theory/N3-corner-radius-reduction.md`; per-degree computer claims are
CONDITIONAL on independent replay in `../theory/N3-corner-bounds.md`.

## Completed work and dispositions

1. Read the assigned rules/handoff/plan/gates and relevant full predecessor
   entries/formulas. Recorded bounded scan honestly; relied on the inherited
   complete gate for registry coverage, without claiming truncated displays
   were a fresh full scan. No new mechanism or literature priority claim.
2. Reconstructed the elementary kappa implication with e<3. The physical
   radius H and scaled-phase sufficient box inequality are separate.
3. Implemented O(n^2) actual energy with 256-bit MPFR directed intervals,
   explicit removable 00 and the exact zero mask. Initial compile exposed
   two misleading-indentation warnings under -Werror; fixed before runs.
4. Executed n33/64/128 producer sums. Frozen repeat through the runner
   used 0.008147/0.036950/0.119526 CPU seconds (timings diagnostic).
   All three rational candidates have kappa>1/12500. Developer rational
   assembly/mask/phase checks passed. Independent replay is PENDING.
5. Direct corrected coefficient-kernel physical derivative diagnostic at
   n2–8 compared 145 nonzero cardinals; maximum relative midpoint error
   9.3973166522e-75. This is MEASURED numerical diagnostic, not an outward
   checker. No arbitrary fitted constant enters a bound.

No attempt was rejected/refuted. The implementation is retained pending
independent replay and testing in a complete phase cover. No degree/global
range upgrade and no B2 pass/kill are inferred from the corner computation.

## Frozen reproduction

Run from the repository root, with the official MPFR development header
available in the existing N3 runtime extraction:

```text
python topics/padua-argmax-bridge-20261105/code/n3_corner_run.py --output-dir local-output/argmax-bridge-20261105/N3-corner --mpfr-include local-output/argmax-bridge-20261105/N3/runtime/extracted/usr/include --receipt topics/padua-argmax-bridge-20261105/evidence/n3-corner-bounds.json
```

The runner freezes the compilation and every producer/diagnostic command
in the receipt. Compiler: Debian cc14.2.0; runtime MPFR4.2.2, GMP6.3.0;
Python3.12.14 and mpmath1.3.0. No randomness/seeds. The official mpfr.h
comes from the already downloaded Debian libmpfr-dev4.2.2-1 package;
its retrieval/provenance is in `N3.md` lines70 onward. No new network
download was performed by this worker. The cloud-environment runtime skill
was read and the environment status checked; no Docker/network work needed.

Short receipt: `../evidence/n3-corner-bounds.json`, SHA-256
fe843711ff66e4a89f7856fc952441537a69d2907a5c78a6a844d61fec3e9c46,
10114 bytes. Bulk native binary/raw JSON/diagnostics are under
`local-output/argmax-bridge-20261105/N3-corner/`; their identities and
commands are pinned in the receipt. The exact per-degree endpoint data
are embedded in the short receipt, so no large artifact is needed to
reconstruct the claimed finite bounds. Padua cold-storage transfer is
pending if these local diagnostic artifacts are retained.

## Runs needed

- Parent-assigned distinct checker: replay ell/E for n33/64/128 through a
  separately implemented exact/outward path, check the exact output bounds
  and common kappa>=1/12500, record code/input/output hashes. It must not
  reuse this producer's arithmetic kernel. No checker command is invented
  before that implementation exists.
- N3 main worker: after checker acceptance, integrate either the per-degree
  exact H bound or the common H<=1/(12500 n^2) into the corner predicate.
  A convenient conservative phase square is |alpha|,|beta|<=1/128.
- Run complete n33/64/128 phase covers and preserve the original B2 gates.
  A faster corner endpoint calculation itself proves no cover-growth law.
- Supplementary mathematical check and required Claude audit, coordinated
  by the parent; this developer cannot approve its own work.
