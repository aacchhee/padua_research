# PD-T?proof-attempts-2-codex-60 — Degree-eight Padua tensor field and specified real embedding

Final ID: **PD-T179**. Provisional ID `PD-T?proof-attempts-2-codex-60` is retained as an alias. Registered after accepted Claude audit-01 and response-01; historical pending-audit notes below are superseded.

Canonical Split from (registration): PD-T100 / OPEN_TARGETS A5 (exact finite case, supporting result or separately OPEN obligation; source measurement retained).

ID kind: PD-T.
Aliases: A5 n8 coefficient field; quartic/cubic tensor basis; native-to-tensor embedding conversion.
Split from: exact arithmetic and real-embedding obligation for the n8 case of A5.
Split into: actual n8 finite count and global value remain separate OPEN targets.

## Statement

Let a be the largest real root of P(t)=t⁴−4t²+2, and b the largest real root of Q(t)=t³−3t−1. Then a=2cos(pi/8), b=2cos(pi/9), the field K=Q(a,b) has degree12, and

    B=(1,b,b²,a,ab,ab²,a²,a²b,a²b²,a³,a³b,a³b²)

is a rational basis. The element θ=a+b generates K and has minimal polynomial

    f(t)=t¹²−24t¹⁰−4t⁹+180t⁸+36t⁷−502t⁶−36t⁵
         +501t⁴−32t³−138t²+36t−1.

The matrix T below converts ascending θ-power coefficients into B-coordinates. Exact outward rational interval evaluation of those coordinates at a in(46/25,37/20), b in(187/100,47/25), refined by their defining polynomial signs, specifies the physical real embedding without relying on a numerical symbolic root selector.

## Definitions

The usual Chebyshev polynomial U_m has degree m; roots of U_m(t/2) are2cos(k*pi/(m+1)), k=1,…,m. Native coefficients are ordered constant through θ¹¹; tensor coordinates use B in the stated order. T's columns are the reduced tensor expansions of(a+b)^r for r=0,…,11.

## Assumptions

Characteristic0 and exact rational/field arithmetic. An implementation must verify its native defining polynomial, native a/b relations, θ=a+b, both directions of the coordinate conversion, and principal rational brackets. All interval operations must enclose the exact result. Fixed precision which cannot resolve a nonzero sign causes failure, never a floating fallback.

## Status by part

Overall status: **PROVED** (written algebraic/analytic representation theorem; required Claude audit pending).

| Part | Status | Evidence |
|---|---|---|
| degree12, tensor basis, primitive polynomial and conversion | PROVED | coprime degrees, exact displayed polynomial identities and determinant |
| principal real embedding and outward interpretation | PROVED | Chebyshev factorizations and rational monotonicity brackets |

The implementation's actual finite receipts and any n8 count require their separate independent checks; this theorem supplies no count or automatic termination assertion.

## Depends on

Elementary field-degree arithmetic, Eisenstein's criterion, the rational-root test, polynomial reduction and determinant arithmetic, Chebyshev recurrence/root identity, and inclusion-preserving interval arithmetic. It does not depend on part1. Later corrected-kernel/cardinal construction separately names `PD-T?proof-attempts-codex-01 (audit pending)` with the task's audit qualification.

## Checks

Developer actually ran `PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_n8_field.py --output topics/padua-proof-attempts-2-20261101/outputs/a5_n8_field_pilot.json`. Python3.12.14, SymPy1.14.0, flint ground backend,160-bit outward fixed dyadics. The field/conversion/principal Sturm controls and all2025 cardinal values plus partition passed;45 cardinals have1828 nonzero monomial coefficients. A different agent `/root/a5_checker` actually reran this pinned source, exit0, as recorded in `../independent-execution-a5-n8-field.md`; python-flint0.9.0/FLINT3.6.0. Its output1895bytes SHA256 `1c7abe81973856f109007f821e48301e34c8bc81c830b1bae7e6a7dada46486b`. These finite regressions do not certify a count; the separately implemented formal-quotient checker is still pending.

## Sources

Registered programme A5, IDEA17 (current alias IDEA206), source06/PD-T100 and current target gate in `../attempts/T-A5-n8.md`. The predecessor is local n6 field theorem40; no n6 statement is silently extended. No novelty/priority claim.

## Proof or evidence

P is irreducible by Eisenstein at2. Q is a monic cubic with no rational root: Q(1)=−3,Q(−1)=1, so it is irreducible. Thus[Q(a):Q]=4 and[Q(b):Q]=3. Let d=[K:Q(a)]≤3. Since3 divides[K:Q]=4d, one has d=3. Consequently[K:Q]=12 and the displayed12 spanning tensor monomials form a basis.

Reduction by a⁴=4a²−2 and b³=3b+1 gives the following integer matrix T:

```text
1 0 0 1 -2 3 -7 -61 -22 -1400 -489 -21558
0 1 0 3 1 -1 6 -238 -113 -4446 -4091 -66363
0 0 1 0 3 1 -21 6 -616 -225 -9990 -7547
0 1 0 0 4 -2 18 -1 -40 26 -2192 -723
0 0 2 0 12 5 42 42 -176 -9 -6796 -6985
0 0 0 3 0 15 6 21 48 -792 -234 -16786
0 0 1 0 4 10 14 203 76 3012 1274 40744
0 0 0 3 0 50 15 707 448 9504 9195 125686
0 0 0 0 6 0 105 21 1484 720 19800 15873
0 0 0 1 0 4 20 14 392 132 5784 3002
0 0 0 0 4 0 84 35 1288 1008 17952 20163
0 0 0 0 0 10 0 189 56 2772 1728 37752
```

Direct exact determinant reduction gives det T=990465713≠0. This can also be verified by recursively multiplying each column by a+b in the quotient algebra and then performing rational elimination. Thus1,θ,…,θ¹¹ are independent and θ generates K. Direct expansion/reduction gives f(θ)=0; equivalently

    Res_u(P(u), Q(t−u))=f(t).

Its degree is12 and θ has degree12, so f is its minimal polynomial. The stated conversion and its rational inverse are now identities between bases, valid in every embedding.

For the real embedding, elementary multiplication yields

    U7(t/2)=t(t²−2)P(t),
    U8(t/2)=(t−1)(t+1)Q(t)(t³−3t+1).

P has negative and positive signs at46/25 and37/20, respectively. Its derivative4t(t²−2) is positive for t≥46/25; the other U7 factors have no root there. Hence its bracketed root is the largest root of U7(t/2), namely2cos(pi/8). Likewise Q has negative and positive signs at187/100 and47/25 and derivative3t²−3>0 thereafter. The remaining cubic t³−3t+1 is already positive at187/100 and strictly increasing thereafter; roots±1 are smaller. Its bracketed root is therefore the largest U8 root, namely2cos(pi/9). The derivative signs also ensure that any sign-straddling rational sub-bracket selects the same roots.

Specifying a and b by these brackets determines one embedding of K intoR. Evaluation of a tensor polynomial at enclosing rational intervals for a,b encloses its value, by induction over addition and multiplication; outward floor/ceiling rounding preserves the enclosure at each operation. The exact native-to-tensor identities ensure that the native element and the interval-evaluated tensor element are the same algebraic element. A symbolic field constructor's approximate root choice is consequently not a proof dependency. ∎

## Scope

Only the coefficient field and physical embedding needed for n8. No n8 local-maxima count, global argmax, completeness or certificate-size claim.

## Open items

Independent implementation replay/checker and complete node/spatial/edge evidence; required Claude audit. The exact field pilot and positive node gaps leave the n8 count OPEN.

## History

2026-11-01, Codex `/root/a2_develop`, requested gpt-6.1-sol xhigh. Rules read at4bd1d65ad36ddded9bf4799c0557d4a6bb83e764, reread unchanged at0d9ad5b803b3fff43080586f5255bfdfcba602e8 after the MZ-only literature integration. Written separately from finite count claims and confined to new n8 files.
