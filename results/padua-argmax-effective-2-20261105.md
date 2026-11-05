## padua-argmax-effective-2-20261105 — explicit local scale and phase-boundary profile

Branch `codex/padua-argmax-effective-2-20261105`; [draft PR25](https://github.com/aacchhee/padua_research/pull/25).
Mathematical development complete at the scoped checkpoint below. Claude
[audit-01](../topics/padua-argmax-effective-2-20261105/audit-01.md) accepts
the mathematics at every stated scope with no status change; record findings
(attribution of T06/T07, scope wording, dispositions) are addressed in
[response-01](../topics/padua-argmax-effective-2-20261105/response-01.md);
the required Claude response check is pending.
All IDs provisional; no canonical registry changes.

- **PROVED analytic T05/T06/T07:** W_n<=10^10 n^4 Lambda_c,
  Lambda_n<=27500 Lambda_c, and for every n>=2 strict descent at both nonnode
  corners whenever0<H<=10^-11/n², with loss>=n² Lambda_c H/16.
  [Radius](../topics/padua-argmax-effective-2-20261105/theory/corner-n2-local-radius.md).
  This closes H3's physical n^-2 scale while leaving useful constants/practical
  coverage unresolved; individual cardinal sign changes are allowed. T07
  instantiates PD-T227 §Scope(8) and provides an all-degree counterpart
  to PD-T228's eventual n^-2 radius, with the smaller explicit constant10^-11. Relative to PD-T251 the new radius is larger only
  for n>=473; strict descent is available on
  max(1/(2[n(n+1)]³),10^-11/n²). T06 re-derives a known global O(log² n)
  bound with explicit auxiliary constants, without claiming first constants.
- **PROVED analytic T03:** exact cotangent profile on all four closed diamond
  edges with absolute error<=7/(12[n(n+1)]²), midpoint S_n=L_{n(n+1)}.
  [Boundary](../topics/padua-argmax-effective-2-20261105/theory/profile-boundary-cotangent.md).
  **PROVED scoped N01:** the leading-factor-only trial a(alpha,beta)*b_n
  misses a divergent midpoint logarithm; full-diamond H2 is not refuted.
- **PROVED analytic T04:** full noncorner reflection defect>=1/8192 for
  n>=48 and rho<=1/10, uniform in admissible odd center.
  [Defect](../topics/padua-argmax-effective-2-20261105/theory/defect-radius-extension.md).
  T01 verifies exact endpoint-weighted phase structure; T02 is a CONDITIONAL
  arithmetic diagnosis with hypothetical C, not an effective threshold.
- **MEASURED / verification:** fresh frozen n17/n24 producer/checker replays
  accept all regenerated/committed certificates. Compiled full-lambda samples
  and all-admissible-center projection samples do not certify continua.
  The bounded box pilot's actual incomplete frontiers/costs are in the report.
- A distinct Astra high [supplement](../topics/padua-argmax-effective-2-20261105/independent-math-checks.md)
  reconstructs all mathematical candidates with no unresolved finding and runs
  a separate70-digit checker. Claude audit-01 independently reconstructed every
  claim and accepted the disclosed novelty-gate timing qualifications.

**PD-T099 remains OPEN.** The certified global range stays exactly2–32; no new
n>32, explicit full-diamond N1 or completed bridge33<=n<N_* is supplied.
[Report](../topics/padua-argmax-effective-2-20261105/report.md) and
[gate verdicts](../topics/padua-argmax-effective-2-20261105/gates.md).
Next: Claude response check of response-01, then audited PR preparation;
practical H1/full-diamond H2 remain OPEN research. All40 original bulk files
were reverified byte-identical in the Codex sandbox; physical archival is
pending and no delivery or durable retention is claimed.
