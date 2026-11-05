# PD-N086 — Individual cardinal signs change inside a degree-four complementary cell

ID kind: PD-N.
Aliases: G7-F; fixed-sign-cardinal envelope; coarse diamond sign obstruction. PD-N?argmax-effective-codex-04.
Split from: none. This is a dated, precisely specified sufficient submechanism of the undefined envelope-existence criterion G7; it does not replace IDEA-319.
Split into: none.

## Statement

For the degree-four even-checkerboard Padua cardinals of PD-T101, define mesh coordinates qx=4 arccos(x)/pi, qy=5 arccos(y)/pi and the open complementary diamond

    D(2,3) = {(x,y): |qx-2|+|qy-3|<1}.

The cardinal L00 associated with the node (1,1) takes both signs in D(2,3). Explicitly,

    L00(1/3,0)=4/405>0,
    L00(3/8,0)=-11/4096<0.

Consequently there do not exist a fixed sign epsilon00 in {-1,1}, a nonnegative real-valued envelope E and a nonnegative real-valued factor a00, defined throughout D(2,3), satisfying L00=epsilon00 E a00 there. In particular a representation of *every individual cardinal* in this form with one cellwise fixed sign per cardinal fails on this cell, whether or not E is common to the cardinals and whether or not the factors are required to sum to one.

## Definitions

PD-T101's coordinates, positive weights and exceptional halved (4,0) mode are used unchanged. This diamond is the standard coarse complementary mesh cell, not a cell of the finer arrangement of all cardinal zero curves. The term “nonnegative” includes zero; neither division by a vanishing E nor an infinite-valued factor is allowed in the displayed representation.

## Assumptions

Exact real arithmetic, degree n=4, and the specified even checkerboard. No all-degree argmax assertion, source theorem or numerical optimization is assumed.

## Status by part

Overall status: **PROVED**, by the elementary analytic calculation below. Supplementary independent reconstruction by gpt-6-astra high accepted the stated scope; Claude [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md) accept the stated scope.

| Mathematical part | Status | Evidence |
|---|---|---|
| Explicit opposite signs within D(2,3), and impossibility of the displayed fixed-sign representation | PROVED | Exact polynomial identity, rational substitutions and radical comparison below |

Candidate disposition: **REJECTED: refuted** for G7-F only (`IDEA-342`). The original IDEA-319 and the effective all-degree target remain **OPEN**. “No cell-wise sign-stable envelope exists” is not the negative statement proved here.

## Negative-result scope

Attempted mechanism: remove the individual cardinal absolute values with a single fixed sign vector on every standard complementary diamond, possibly by extracting a common nonnegative envelope and nonnegative cardinal factors.

Parameter range: exactly n=4 and D(2,3). A universal mechanism containing this case is refuted. Regrouping cardinals, taking absolute values before factoring, using signed factors, allowing sign changes of the envelope, finer sign partitions or a different class of envelopes is outside this statement.

## Depends on

PD-T101's locally proved corrected-cardinal formula, particularly the node weight w00=1/40 and coefficient of T4(x) equal to one. Only Tj(cos t)=cos(jt), the elementary Chebyshev polynomials through degree four and the half-angle identity are otherwise used.

## Proof

At the node B00=(1,1), every Chebyshev node factor equals one. At y=0, the degree-zero through degree-four Chebyshev values are 1,0,-1,0,1. Grouping PD-T101's total-degree sum by the x degree, and subtracting the exceptional T4(x) correction, gives

    40 L00(x,0) = 1 - 2T1(x) - 2T2(x) + 2T3(x) + T4(x).

Indeed the y sums for x degrees 0,1,2,3,4 are respectively 1,-1,-1,1,1; the last x coefficient is one rather than two. With T1=x, T2=2x²-1, T3=4x³-3x and T4=8x⁴-8x²+1 this becomes

    L00(x,0)=(x²-1)(2x²+2x-1)/10.

The two rational substitutions give exactly the values in the statement.

It remains to check their cell assignments rather than infer them from decimal angles. At y=0, qy=5/2. For 0<x<sin(pi/8), monotonicity of arccos gives 3pi/8<arccos x<pi/2, so 3/2<qx<2. Hence |qx-2|+|qy-3|<1. Both selected x values lie in this interval: 0<1/3<3/8 and

    (3/8)² = 9/64 < (2-sqrt(2))/4 = sin²(pi/8).

For the strict inequality, equivalently sqrt(2)<23/16, square the two positive sides and use 512<529. Both points are therefore strictly inside D(2,3).

Finally epsilon00 E a00 has one weak sign on the entire cell for either possible fixed epsilon00. It cannot equal the two opposite nonzero values of L00. This proves the precisely scoped obstruction. ∎

## Checks

The proof is self-contained exact algebra; the following executed calculations are supplementary diagnostics, not finite premises of a computer-assisted proof.

2026-11-03, Python 3 with SymPy in the managed workspace: expanded the PD-T101 sum at n4, subtracted T4(x), divided by40, and factored its restriction y=0. The output was `(x - 1)*(x + 1)*(2*x**2 + 2*x - 1)/10`. A separate standard-library Fraction calculation substituted 1/3 and3/8 and printed `4/405` and `-11/4096`. These two calculations were performed by the same mathematics worker; neither is an independent rerun.

No floating-point sign test or transcendental enclosure is used in the proof. No bulky evidence artifact is needed because every exact coefficient and comparison needed for reconstruction is displayed above.

The distinct gpt-6-astra high checker independently reconstructed the kernel restriction without loading this worker's polynomial output, then checked the two exact values and strict shared-diamond membership. Its [supplementary analytic review](../independent-checks-01.md#exact-degree-four-sign-obstruction-supplementary-analytic-review) accepts the stated G7-F obstruction and its limited scope. This does not replace the required Claude audit.

## Sources

Accepted local PD-T101 only. LIT-312's generating-curve context is motivation, not a transferred theorem. No 1-D maximum-location theorem is used.

## Scope

This obstructs a particularly simple removal of absolute values on coarse complementary diamonds. It does not obstruct a generating-curve identity, a different grouping, a positive envelope for lambda itself, a comparison of cell suprema, E-C, I-B0, or PD-T099. The witness points are arbitrary square points; no claim that they lie on the generating curve is made.

For orientation, the brief's corner check has an elementary answer: if gamma(t)=(cos((n+1)t),cos(nt)) is a corner, both nt/pi and (n+1)t/pi are integers, hence their difference t/pi is an integer. The only reachable corners are therefore (1,1) and ((-1)^(n+1),(-1)^n), exactly the node corners of the stated even checkerboard. The non-node maximizing candidates are off the curve for every n. A bound only on the curve consequently needs an additional comparison before it can address the square. This routine observation does not obstruct a generating-curve *identity for arbitrary square evaluations*.

## Open items

To make original G7 falsifiable, specify the allowed envelope/factor class, normalization, exact cells and what is required to have fixed sign. Retain IDEA-319 until that has been done. Supplementary independent analytic reconstruction is complete; Claude [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md) accept the stated scope.

## History

2026-11-03, Codex mathematics worker, assigned gpt-6-astra ultra under handoff02's explicit AC exception. Rules/input `8a1f394739293953e1566fd24a0a193cc78ff26f`; base `440d107`. The attempt recorded original G7 unchanged, diagnosed its undefined quantifier domain, then registered G7-F before the exact polynomial expansion. Opposite rational signs were found afterwards. No original mechanism was silently widened or rejected in full.

## Final registration — 2026-11-05

Final IDs and preserved provisional aliases: [id-map](../final-id-map.json). Claude [audit-01](../audit-01.md) and [response-check-01](../response-check-01.md) accept the existing stated scopes; no claim, proof or epistemic status changes at registration.
