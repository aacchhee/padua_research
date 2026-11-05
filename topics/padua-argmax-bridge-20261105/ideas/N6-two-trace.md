# IDEA?argmax-bridge-codex-N6-01 — Fixed two-trace comparison for covering parallels

Aliases: diagonal-phase Lissajous parallels; unimodular phase family;
two-trace envelope; fixed-t endpoint comparison.

- Question / scope: for every n>=2 and real t,s, does comparison(C) in
  [the gate](../novelty-gate-N6.md) hold?
- Mechanism and hypotheses: Gamma_s(t)=(cos((n+1)t+s),cos(nt+s));
  retain corrected individual cardinals before their absolute values;
  compare only s=0 and s=pi at the same t.
- Closest registry entries read in full: IDEA-206/319/341/342 and T101/T364.
- Separation criterion: a specified pointwise inequality removes the
  second continuous parameter. The family substitution alone is equivalent
  to T364. Any exact strict reversal erases the inequality's proposed use.
- Literature baseline and limits: INDEX inspected; no external fulltext
  used and no source transfer or priority claim.
- Applicable obstructions: N086 kills only individual coarse-cell signs;
  this comparison assumes none. N079 forbids discarding cancellation
  before taking the four-copy absolute value.
- Novelty gate verdict: variant with difference of deferred319/341.
- Cheapest decisive test: construct n2 rational cardinals and evaluate
  t=pi/3, s=pi/3, with s=0/pi comparison points; all coordinates are rational.
- Kill criterion before testing: lambda(Gamma_(pi/3)(pi/3)) exceeds
  max(lambda(Gamma_0(pi/3)),lambda(Gamma_pi(pi/3))) exactly. If this point
  is inconclusive, try other rational-angle n2 values before any larger run.
- Test discriminability: a strict exact rational difference refutes this
  universal comparison, independently of the target corner inequality.
- Actual results: first point t=s=pi/3 was inconclusive (norm23/12
  versus endpoint maximum2). Then t=s=pi/4 gave the exact strict gap
  (5sqrt(2)-7)/6>0. The frozen standard-library checker PASS receipt is
  [n6-two-trace.json](../evidence/n6-two-trace.json); no float premise.
- Disposition: **REJECTED: refuted**, only for comparison(C). The
  covering-family identity remains valid and the broader319/341 route
  stays OPEN. This is not a corner-argmax counterexample.
- Canonical record: [PD-N?argmax-bridge-codex-N6-01](../theory/N6-two-trace-obstruction.md),
  PROVED analytic development result; independent review/audit pending.
- History: 2026-11-05, Codex N6, assigned Sol xhigh, rules/input98d6c00.
