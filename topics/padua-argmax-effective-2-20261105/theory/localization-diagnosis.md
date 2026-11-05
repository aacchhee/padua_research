# PD-T?argmax-effective-2-codex-02 — Conditional localization arithmetic for A0

ID kind: PD-T.
Aliases: A0 log-degree threshold; inherited global-phase entry budget.
Split from: none; quantitative diagnosis of the PD-T216/225 proof route.
Split into: none. This does not state an effective argmax theorem.

## Statement

Fix 0<r≤1/16 and C>0. **Assume** the global primitive bound S_n≤aΛ_c(n)+C log(n+1) holds with this particular C at every degree under consideration, where a=(cos α+cos β)/2. Set A=4/π², q=r²/(2π²), t=log n, and

\[
 T(q,C)=\frac{C+\sqrt{C^2+4qA(54q+C\log(3/2))}}{2qA}.
\]

For every n≥2 with log n>T(q,C), every global maximizer has every selected odd-center representation in the fundamental diamond satisfying |α|+|β|<r. This is only phase-radius localization; exclusion of noncorner centers and strict comparison at a corner need their own hypotheses.

The sharper geometric choice q=1−cos(r/2) also gives the same conditional implication for these r. The arithmetic evaluations below use hypothetical C∈[1.4,1.7], not a proved global constant in that interval.

## Definitions and assumptions

Use PD-T216/225's phases, normalization and Λ_c. Natural logarithms. The quoted rigorous lower bound is Λ_c≥A log²n−54 (PD-T156/157, with the PD-T159 corner-product dependency). The hypothetical specified C is the unresolved hypothesis. The roots below are floating diagnostics; no decimal endpoint is claimed outward rounded.

## Status by part

Overall status: **CONDITIONAL**, because the stated C range has not been proved globally. The algebraic implication is written below; it is not a new established effective threshold. Arithmetic roots are supplementary floating evaluations, with no maximum-certification role.

Candidate disposition: inherited-route diagnostic, not a new mechanism or a refutation of R1.

## Depends on

PD-T216/225 and the exact common primitive; PD-T156/157 lower bound. The zero-remainder quadratic comparison uses PD-T271's coefficients only as a diagnostic; it is not a substitute for that theorem's explicit remainder. No numerical fit supplies C.

## Proof or evidence

At a maximizer λ≥Λ_c, hence (1−a)Λ_c≤C log(n+1). On the full phase diamond,

\[
 1-a\ge(\alpha^2+\beta^2)/\pi^2\ge(|\alpha|+|\beta|)^2/(2\pi^2).
\]

If ρ=|α|+|β|≥r then 1−a≥q. Since log(n+1)≤log n+log(3/2) for n≥2, the sufficient exclusion inequality is

\[
 q(At^2-54)>C(t+\log(3/2)).
\]

Its positive root is T(q,C). The quadratic is increasing past its positive root, proving the conditional statement.

For the sharpened geometry, put x=|α|, y=|β|. If x+y=s, then cos x+cos y=2 cos(s/2)cos((x−y)/2). For 0≤s≤π, cos(s/2)≥0 and the second cosine is at most one, so 1−a≥1−cos(s/2)≥1−cos(r/2). Equality occurs at x=y=r/2. Thus the sharper q is exact for minimizing 1−a over the diamond with ρ≥r; no small-angle approximation is needed.

### Recomputed scale

Executed with `python topics/padua-argmax-effective-2-20261105/code/a0.py`. The table rounds the floating outputs for readability; all entries concern **log n**, not n.

| r | hypothetical C | original geometric lower bound T | sharp phase geometry T |
|---|---:|---:|---:|
| 1/64 | 1.4 | 279291.75 | 113193.50 |
| 1/64 | 1.45 | 289266.44 | 117236.11 |
| 1/64 | 1.6 | 319190.52 | 129363.94 |
| 1/64 | 1.7 | 339139.90 | 137449.16 |
| 1/16 | 1.4 | 17456.12 | 7075.53 |
| 1/16 | 1.45 | 18079.54 | 7328.21 |
| 1/16 | 1.6 | 19949.79 | 8086.26 |
| 1/16 | 1.7 | 21196.63 | 8591.62 |

The leading balance is T≈Cπ⁴/(2r²); this explains the inherited shorthand “log n roughly 3×10⁵” at r=1/64. Inserting the quadratic A t²+b t+c with b=(8/π²)(γ+log(8/π)) and c≈1.8461603104, and **discarding its remainder**, changes the coarse roots by about −3.02 relative to the leading balance. Those quadratic roots are diagnostics only. PD-T271 now proves a corner expansion with an explicit vanishing remainder, but does not make the phase constant C=1.4–1.7 a theorem.

### Gate interpretation and limits

Under the **original written A0 inequality**, both radii give roots above 10⁴, and the order 3×10⁵ claim is confirmed at 1/64. The sufficient root does not prove that actual maximizers require such a huge n; it measures the loss in this proof route. It also does not justify the universal phrase “no sharpening can work.”

The separately displayed exact phase sharpening gives a root below 10⁴ at r=1/16. This is a genuine refinement of the arithmetic and must not be hidden by a blanket closed-R1 verdict. It does **not** reopen an already workable bridge: the inherited noncorner defect theorem is only for r≤1/64, and the inherited strict local corner comparison still requires log n≥10⁷. At r=1/64 the sharpened roots remain above 10⁵. A route extending defect and corner predicates to the larger radius is a separate unresolved option, not a consequence of the diagnostic. Even n≈exp(7076) is far beyond finite enumeration.

## Checks

Source command above uses Python standard-library math and no randomness. Input/rules ed21cc0bf205549936fccde90244a291bc6de324; source file is new in this topic. Independent arithmetic reconstruction is requested separately. The analytic expressions, not rounded printed roots, define the conditional thresholds.

## Sources

Internal proved dependencies and explicit hypothetical C. No external priority claim; no new external source read or transferred.

## Scope and open items

Needed: an explicit globally valid C and stronger defect/corner estimates if this route is pursued. A0 diagnoses the inherited sufficient mechanism; it neither disproves PD-T099 nor supplies an effective N₁. It does not rule out different effective inequalities or quantitative refinements.

## History

2026-11-05, Codex, AC-requested gpt-6-astra ultra mathematical development; runtime metadata not independently exposed. Replaces the handoff's approximate numerical diagnosis with an explicit conditional formula while preserving the original gate and separately recording the sharper geometric observation. No final ID assigned.
