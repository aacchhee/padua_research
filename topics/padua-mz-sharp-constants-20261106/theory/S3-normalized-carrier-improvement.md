# PD-T533 — a strict normalized carrier improvement

2026-11-06 ID history: `PD-T?mz-sharp-codex-S3-01` → `PD-T533`; statements, original registrations and historical dispositions are preserved.

ID kind: PD-T.
Aliases: rational carrier parameter improvement; inherited Fejer norm tuning.
Split from: supporting development for PD-T381, now PARTIAL; its decimal
values conjunct remains OPEN.
Split into: none.

## Statement

Use the signed Lebesgue Padua rule and continuous unnormalized dxdy norm
of PD-T381. Let A=4 log 2 and J(a)=[A+C(1/a)]/2, where C is exactly
PD-T379 equation (1). Define the exact constant

    c_new = 16(51/200)(49/200) / [9 A J(51/200)].

Then, over all integers m tending to infinity,

    limsup lambda_minus(m,m-1)/log m <= -c_new,
    c_new > 1/[9 A J(1/4)] = c_minus(PD-T379).

The same bound holds separately on even and odd m. No extremal limit or
parity agreement of extremal limits is asserted.

## Definitions and assumptions

The carrier coordinate is x with mesh m for even m and y with mesh m+1
for odd m. For fixed a,b>0 with a+b<1/2 use precisely PD-N105 and
PD-T378's negative carriers. Their limiting normalized coefficients,
proved in PD-T379, are 16ab/[9 A J(a)]. Every parameter limit below is
taken after the m-limit for fixed interior a,b. Boundary parameter
polynomial families are not assumed admissible.

## Status by part

Overall status: **PROVED** (analytic development; independent audit not
performed by this author).

| Mathematical part | Status | Evidence |
|---|---|---|
| strict normalized constant improvement and both-parity one-sided bound | PROVED | derivative inequality below and inherited full signed carrier limit |

Candidate disposition: retained quantitative variant of IDEA-469.

## Depends on

PD-T379 equation (6), with the underlying complete signed sums in
PD-N105 and PD-T378. No measured optimizer, spectral fit, external
theorem or weight-sign classification is a proof premise.

## Proof

For q>2 put h(q)=q^2 log q. Four applications of the fundamental
theorem of calculus give the exact centered finite-difference identity

    C(q) = (1/2) integral_[0,1]^4 h''''(q-2+s1+s2+s3+s4) ds
         = - integral_[0,1]^4 (q-2+s1+s2+s3+s4)^(-2) ds.

Consequently C(q)<0 and

    C'(q)=2 integral_[0,1]^4 (q-2+s1+s2+s3+s4)^(-3) ds >= 2/q^3.

The final inequality follows from convexity of x^(-3) on x>0 and the
fact that the displayed argument has mean q. Equivalently, integrate
the elementary tangent inequality
x^(-3)>=q^(-3)-3q^(-4)(x-q). All arguments stay positive for q>2,
so differentiation under this compact integral is justified.

For a in [1/4,51/200] the positive norm J(a), as proved in PD-T379,
therefore obeys

    0<J(a)<A/2=2 log 2<7/5,     J'(a)=-C'(1/a)/(2a^2)<=-a.

The elementary inequality log 2<7/10 follows, for example, from
1+7/10+(7/10)^2/2+(7/10)^3/6+(7/10)^4/24>2 and the exponential
series with positive remaining terms.

Let N(a)=a(1/2-a). Then -1/100<=N'(a)<=0 on this interval, and

    N'(a)J(a)-N(a)J'(a)
       >= -(1/100)(7/5)+a^2(1/2-a)
       >= -7/500 + (1/16)(49/200)
        = 21/16000 > 0.

Thus N(a)/J(a) is strictly increasing on this whole nondegenerate
interval. Multiplying by 16/(9A)>0 gives c_new>c_minus.

For a=51/200 and every fixed 0<b<49/200, PD-T379 gives, on either
parity,

    limsup lambda_minus/log m <= -16ab/[9 A J(a)].

Let b increase to 49/200 in this scalar inequality. This proves the
stated one-sided bound; combining the two parity limsup bounds gives
the all-integer statement. The proof retains the already proved full
signed-form limit and never subtracts a negative-corner estimate.

## Checks

After saving novelty-gate-S3.md, Python 3 with mpmath (60 decimal
digits) and scipy.optimize.minimize_scalar was executed to explore the
inherited scalar formulas. It suggested a negative optimum near
a=0.2568609385 and a positive optimum near a=0.1253042491. Neither
optimizer output is a global optimum claim or a proof premise.

A separate 60-digit display evaluation at a=51/200 gives approximately
c_new=0.029641769 (rounded orientation only; exact formula above is
authoritative). No independently executed checker has yet been supplied.

## Sources

Local predecessor gate: ../novelty-gate-S3.md. No external source used.

## Scope and open items

This strictly strengthens a supporting one-sided bound. PD-T381 remains
OPEN: no matching opposite bound, extremal eigenvector identification,
existence/value of a spectral limit, parity agreement, effective onset,
or global optimum even within the scalar carrier family is established.
In particular this does not explain or identify the finite measured
minimum branch. The positive carrier constant is unchanged.

## History

2026-11-06; Codex S3, allocated gpt-6.1-sol xhigh, source/rules
2143ad622fa98faf8fe7d5cb8ed2bb7e0062f861. Prospective gate preceded
formula exploration. This is a known carrier-family variant, with no
mechanism novelty or priority claim. Runtime metadata is unexposed.
