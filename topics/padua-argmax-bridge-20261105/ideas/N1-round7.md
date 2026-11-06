# IDEA?argmax-bridge-codex-N1-07 — Compare the existing model's logarithmic coefficients

Aliases: near-model leading-log test; compact log-degree endpoint; exact
linear-log coefficient; corner-normalized coefficient comparison.

2026-11-06. Rules/input `8dc1521cf68f7780bd10e02495f6f71a639c03c6`.
Codex mathematical worker; inherited model/effort, serving metadata unexposed.
Only this round's newly assigned files are writable; the coordinator owns Git.

## Prospective gate and fixed scope

Before this record, read the complete 1031-line `state/IDEAS.md`, including
every obstruction/disposition table, headings, identifiers, aliases and
summaries. Full closest entries read: IDEA-327/333 in alln
`gated/CANDIDATES.md`, IDEA-336/337 in effective `ideas/r1-r2-r5.md`,
IDEA-455/456/459 in phase2 `ideas/H2-H3.md`, and IDEA-358's complete
T269/270/271 theory chain. The applicable full obstruction proofs are
PD-N079 and PD-N132; PD-T220's exact finite-degree cusp was also read.
The immediate N1-01/02/04/05/06/09–15 proofs, round5/6 idea records,
round5/6 independent reviews, N5-04 and C1 with its review were read.
PD-T159's exact positive corner sum and same-mesh identity were read.

Searches used `rg -n -i` and `rg -l -i` over the full registry,
argmax/Lebesgue topics, track negative-result indexes and literature INDEX:
`leading.*(log|coefficient)|log.*coefficient|compactification|compact.*t=|near.model|primitive.*cusp|coefficient.*(quadratic|phase)`,
and the endpoint, shifted-harmonic, cotangent, digamma and phase-profile
synonyms appearing in the earlier gate. The literature INDEX warning,
headings and matching Padua/cotangent entries, in particular LIT-312/379/388
and their dated coverage corrections, were inspected before attribution.
No PDF, external theorem, exhaustive external search or priority claim is
used. This is a quantitative continuation of IDEA-337/459.

- Question / scope: does the already fixed M_near have a leading or
  next-log coefficient obstruction to C1 on alpha,beta>=0, alpha+beta<=1/2?
- Mechanism: extract its L^2 and L coefficients without changing any model
  term. Retain the exact fixed-count finite part as an unresolved remainder.
- Separation: an explicit uniformly valid coefficient identity and sign
  inequality, rather than the existing error bound or a fixed-phase fit.
  Any surviving O(rho)L coefficient at the origin, or a coefficient larger
  than the corner's, kills the proposed favorable coefficient conclusion.
- Obstructions escaped: PD-N132 forbids dropping the phase-dependent L
  term; it is retained explicitly. PD-N079/PD-T220 forbid an exact
  finite-n purely quadratic primitive bound; no such bound is proposed.
  Its cusp coefficient O(log n/n) belongs to the finite-h remainder.
- Verdict: variant with difference, no new model or correction family.
- Cheapest test: algebraic extraction of both coefficients and exact
  integration of the max-formula coefficient A before any integrator.

## Claim fixed before computation

Let L=log n, a=(cos alpha+cos beta)/2, r2=alpha^2+beta^2, and use C,U0
from the frozen N1-04/05 definitions. The proposed coefficient identities are

    B0=4a/pi^2,
    b_M=2U0/pi+[8a log2+4a loga
                          +2(alpha sin alpha+beta sin beta)]/pi^2.

The intended analytic test is the uniform pair

    B0<=4/pi^2-47r2/(48pi^2),
    b_M<=b_c-r2/(24pi^2),
    b_c=(8/pi^2)[gamma+log(8/pi)].

It must be proved from the reciprocal-pair series and elementary
inequalities, including all zero-phase limits. The model coefficients
are to be separated from the still OPEN full inequality
M_near<=Lambda_c+1/4096. No O(1) term may be discarded in that comparison.
If a uniform O(1) remainder is proved, it is supporting compactification
only, with no small numerical remainder or onset inferred.

## Bounded implementation plan, preregistered

At most one pilot, <=300 process CPU seconds, Python/mpmath at 60 digits:
evaluate the primitive S_n(0,0) from its corrected periodic divided-
Chebyshev definition and compare it with PD-T159's separately weighted
positive corner sum at exactly n=17,24,32. Include the actual endpoint
polynomial collision value. This checks normalization only: M_near's
approximation theorem is not asserted at these degrees. Report floating
results as MEASURED, not interval proofs. No fits, finite-energy
extrapolation, model maximum grid, expensive integral or second pilot.
Exact Fraction checks of elementary rational proof inequalities may share
that short script; they are explanatory controls, not universal proof
premises. The analytic proof must stand without these measurements.

## Retained alternatives and limits

1. Leading-coefficient-only comparison: insufficient near the origin;
   consolidate into the two-coefficient test rather than treating it as
   a full C1 argument.
2. Sample/fitted coefficient inference: abandoned without execution;
   exact endpoint cancellation determines the coefficients.
3. Validated whole-domain integrator: deferred until this analytic gate
   is assessed and an actual finite-part error budget is specified.
4. A second correction/model: excluded by the already used round5 allowance.

Full comparison, any actual onset, far phases, other center classes and
all-n energy remain OPEN. Certified global range 2–40 is unchanged.

## Round7 outcome — 2026-11-06

The exact two-coefficient test survives analytically in
[N1-16](../theory/N1-round7-coefficients.md). It proves the displayed
B_M and b_M identities, both uniform negative quadratic coefficient
gaps, and a phase-uniform O(1) remainder for the unchanged M_near.
The log-degree endpoint therefore has no coefficient obstruction;
the second coefficient is smooth/even and has no O(rho) cusp.
The finite-n primitive cusp is retained in the bounded part, not refuted.

Disposition: **retained successful quantitative variant** for these
supporting coefficient statements. The full C1 inequality remains
**OPEN** in [N1-17](../theory/N1-round7-comparison.md), with the exact
remaining function F_n and eta=107/3584000 stated there. The leading-
coefficient-only alternative is insufficient, consolidated into this
two-coefficient result; no separate failure theorem is created.

The sole preregistered normalization pilot ran once at 60 decimal
digits, exactly n17/24/32, process CPU0.31307493s, exit0. Corrected
periodic primitive and separately weighted PD-T159 corner sum agree
within1.62e-59, with the actual polynomial endpoint collision included.
This is **MEASURED**, not M_near evaluation, rigorous roundoff enclosure
or proof input. Receipt/code are linked in the attempt. No fit,
numerical integral, next-round finite-part test or finite-energy
extrapolation was run. The one-correction limit is unchanged.
