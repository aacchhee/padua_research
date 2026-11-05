# Response 01 — Claude audit-01, F1–F4 and N1/N2

Developer response, 2026-11-05. Audited candidate:
ae7e6187e8731b6f83aa444d4d702a0ef779c564. Audit output:
48f7479700cfe3966c4e3fe4bf72122a30ddb6e6; response input/rules:
44c4d5a1aeb31307613e892a5b67c7cb968e4ee9. Main advanced to
5db1e01dcd2258f45de2adcaef43859e59734618 and was merged at
9ec2a54c5b6af56514feaf11c9fc329f19a88820. Rules are unchanged.
Audit-01 is retained without edits. Role/model disclosure is in LOG.md.

All findings are accepted and addressed below. Material F1 changes and the
new measured baseline return to Claude Opus 5.5 xhigh for re-audit. No audit
acceptance or merge readiness is inferred from this response.

## F1 — accepted: reconstruction never uses terminal divisors

The primary text confirms the auditor's layer-degree claim, not the earlier
C4 obstruction interpretation. [Source recheck](source-recheck-01.md):

- FHV2015 arXiv1406.0364v2 §3.1 Thm3.1 and (3.3)–(3.10), pp16–18;
  §3.3 Thm3.3 and (3.11)–(3.15), pp20–21, full induction. In faithful
  paraphrase: assuming coefficients through layer k, lower coefficients at
  k+1 divide by a diagonal difference from k−1; the remaining diagonal
  coefficients divide by a difference from k. Axes use marginal data.
- Van Assche2011 arXiv1104.3778v1 Thm3.1, equations (3.1)–(3.5),
  pp9–10 and proof, gives the r=2 compatibility pattern.

For target layer t<=N−1, lower-coefficient denominators have degree t−2
and diagonal denominators degree t−1. Thus their maximum degree is N−2.
Normality of the relevant opposite corner makes each such divisor nonzero.
The terminal d=0 cannot enter any coefficient in the requested triangle.

The local proof independently reconstructs (A), (B1), (B2), rather than
inheriting the audit's sketch, and justifies polynomial-family independence,
axis conditions, induction coverage and N=1. Substantive records are split:

- **PD-T?nn-mop-iep-codex-03, PROVED**:
  [interior divisor nonvanishing](theory/interior-divisor-nonvanishing.md).
- **PD-T?nn-mop-iep-codex-04, PROVED**:
  [marginal reconstruction on the normal triangle](theory/marginal-reconstruction.md),
  including terminal equality as a necessary final boundary condition.

The previous **PD-N?nn-mop-iep-codex-01 failure classification is withdrawn**.
Its algebra was true, but the alleged failed step would propagate to degree-N
coefficients, outside the normal NN coefficient domain. It is not a step of
C4. Under WORKFLOW L5 this is not a useful evidenced failed mechanism to
register. No final negative ID is assigned. The
[historical file](theory/terminal-division-obstruction.md) retains the full
original wording and [SPLITS.md](SPLITS.md) records the mapping. The old
equalities are not disproved or weakened; their positive roles are preserved.

gate.md, report.md, candidates.md, exact-runs.md and the topic results now
state that C4 is complete on the finite coefficient triangle under full
normality through degree N, without a terminal modification. Two fixed
shifted lines still do not suffice to fill the lattice; that separate source
correction remains. Kozhan–Vaktnäs Def2.8/Thm3.6 comparison is refined without
importing rectangular perfectness for common-support triangular data.

The orchestrator also actually reran the auditor's checker:

```sh
python topics/nn-mop-iep-20261103/audit-01/claude_layer_recursion_check.py > /tmp/nn-mop-response-layer.json
```

Exit 0, Python3.12.14, code SHA-256
13d59af82304a712d792c6e2f96c76f42ec732575dcfa3452a92295071c011b3.
Output: 6,367 bytes, SHA-256
9e3c53ec8668303428b57204498bdef468cac21af1832fbc645d78bb225ae551.
24 cases, 467 sites, 256 marginal identities, 809 nonzero divisions,
128 terminal zero-d sites; maximum divisor degree N−2. This is a developer
replay of existing auditor code, finite MEASURED support, not the new proof
or another independent implementation. Input identities are emitted by the
unchanged checker; raw output remains local and regenerable.

## F2 — accepted: spectral mismatch, not a shifted/fixed-site dichotomy

Updated report.md, C2 and theory/fixed-site-dictionary-failure.md. PD-T057's
blockwise interior commuting identities also couple adjacent levels. The
112 same-site counterexamples refute only the named literal identification;
their MEASURED status/counts and C2's narrow disposition are unchanged.

The decisive distinction is that both NN difference operators have eigenvalue
x on a consistent MOP vector, whereas the bivariate pair represents two
coordinate functions and joint node values (x_l,y_l). Two index directions
alone supply no second independent spectral coordinate. No universal
impossibility of a lifted/covariant operator representation is asserted.
No additional full-lattice count was promoted into this result.

## F3 — accepted and executed: C4-only floating-point baseline

A C4-only baseline is meaningful without any specified C3. The earlier LOG
sentence suggesting that no numerical run was pending is corrected. The
new [executable](code/c4_float_baseline.py),
[receipt](c4-baseline-01.md) and
[PD-T?nn-mop-iep-codex-05, MEASURED](theory/c4-baseline-measurements.md)
implement and execute the comparator requested by audit F3.

Both source Kravchuk/Hahn weight definitions and parameters were checked on
arXiv2608.25758v1 §5.1 Examples5.1–5.2 p20. The local coordinate is
z=2k/(N−1)−1 and coefficients are monic in z. Stieltjes marginals followed
by A/B layers are computed in binary64, compared with 140/220-digit runs;
N4 also has an exact Fraction mixed-moment comparison.

```sh
python3 topics/nn-mop-iep-20261103/code/c4_float_baseline.py --family krawtchouk --sizes 4 8 12 16 24 32 --dps 140 220 > /tmp/nn-mop-c4-krawtchouk-final.json
python3 topics/nn-mop-iep-20261103/code/c4_float_baseline.py --family hahn --sizes 4 8 12 16 24 32 --dps 140 220 > /tmp/nn-mop-c4-hahn-final.json
```

Both final commands exited 0; every reference comparison passed the 1e−60
precision-convergence threshold. That convergence is not an independent
reference algorithm for all N. All coefficients remained finite without zero
division, while fieldwise normwise relative error exceeds one for Kravchuk
N24/32 and Hahn N16/24/32. The receipt gives every error, digits-lost value,
input/code hash, environment and output identity, and discloses intermediate
failed reference convergence before precision was raised.

This demonstrates finite accuracy loss for this implementation, not general
instability, the error source, C3/C4 superiority, or reproduction of the
papers' different algorithms/residual metrics. Required next execution is
the Claude re-audit replay of these exact commands; no larger run is needed
for the bounded statement. Wider size studies and error decomposition remain
outside this response, with no claimed execution.

## F4 — accepted: version-dependent raw output identities

Added provenance notes to exact-runs.md and independent-check.md. The original
checkers embed Python version and the small checker also SymPy version. Raw
hashes are environment-dependent. Cross-environment mathematical identity
requires normalising only those metadata fields, while keeping source/input
hashes and result values. Audit-01's verified normalised reproduction is
credited to Claude, not presented as a new developer execution. The new
baseline also records elapsed time, argv and platform; its receipt explicitly
separates raw identity from reproducible case values.

## N1 — source coverage note addressed within the required scope

literature.md records this round's primary locator rechecks under the existing
source IDs; source-recheck-01.md gives full coverage and omissions. FHV,
Van Assche and KV finite-domain locators were accessible to the developer's
web PDF service. Earlier ADY/ADV/Toda and KV inverse-theorem reports were
not all reread. This does not retroactively give audit-01 primary-source
coverage; the re-auditor must state its own access and coverage honestly.

## N2 — accepted: IDEA-197 added to shortlist

gate.md now includes IDEA-197, with PD-T095/PD-N042/PD-T102: its structure
and commutant claims concern two commuting bivariate sections. One MOP
spectral variable and two measures do not meet that setting; a banded
Hessenberg step-line matrix alone supplies no second spectral coordinate.

## Remaining process obligations

Supplementary Astra checking completed and is recorded in
[response-independent-01.md](response-independent-01.md): both full written
proofs reconstructed and all twelve baseline cases independently rerun with
identical case payloads. Its inspected code/proof hashes are unchanged;
subsequent baseline prose edits only credit that completed replay. It cannot
replace Claude re-audit.
No final IDs assigned and no topic scientific-registry integration performed.
Existing reservations are unchanged. Main integration preserves inherited
registries without renumbering. Required next step is Claude Opus5.5 xhigh
re-audit of F1–F4, the split/withdrawal, primary-source coverage and new finite
baseline, followed by fresh-scan PR preparation if accepted. Only AC merges.
