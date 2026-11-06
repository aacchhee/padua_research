# PD-T?padua-3d-codex-T6-02 — explicit octahedral Fourier L1 lower bound

ID kind: PD-T.
Aliases: facet-coordinate sawtooth bound; positive-frequency vertex test.
Split from: T6 universal Lebesgue lower-bound task, supporting Fourier claim.
Split into: none.

## Statement

For integers `d>=3`, `n>=d-1`, put `m=floor(n/(d-1))` and
`H_m=sum_{a=1}^m 1/a`. On `T^d=(R/(2*pi*Z))^d` with probability Haar
measure `dmu=(2*pi)^(-d)dt`, define

\[
B_n^d=\{k\in\mathbb Z^d:\sum_j|k_j|\le n\},\qquad
D_n^d(t)=\sum_{k\in B_n^d}e^{ik\cdot t}.
\]

Then

\[
\|D_n^d\|_{L^1(\mu)}\ge {H_m^d\over d\,2^d\pi^d}.
\tag{1}
\]

In particular, `d=3,n>=2` gives
`||D_n^3||_1 >= H_floor(n/2)^3/(24*pi^3)`.

## Definitions

Fourier coefficients use `hat f(k)=integral f(t)exp(-ik.t)dmu(t)`.
The one-dimensional sawtooth is `b(t)=pi-t` for `0<t<2*pi`, extended
periodically, with arbitrary values of modulus at most pi at its jumps.

## Assumptions

Only the integer ranges above and probability Haar normalization. Functions
in intermediate steps may be complex-valued; this is a statement about the
displayed real even Dirichlet kernel's absolute integral.

## Status by part

Overall status: PROVED (written developer proof; independent audit pending).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Explicit all-n,d inequality (1) | PROVED | Analytic proof below |
| Bounded exact and float sanity checks | MEASURED | Receipt `evidence/t6-sanity.json`; not a computer proof |

Candidate/claim disposition: retained known-mechanism explicit bound.
Rejection reason: none. No novelty or optimal-constant assertion.

## Depends on

Elementary integration by parts, finite Fourier expansions, and Haar
invariance as proved below. No external lower-bound theorem is a premise.

## Checks

`python topics/padua-3d-20261106/code/t6_sanity.py`
checks the exact d3 support/subset and harmonic identities and labels all
floating mesh averages MEASURED. Its finite checks do not replace this proof.
Independent check: pending at developer handoff.

## Sources

Context only: [literature-T6](../literature-T6.md), provisional
LIT?padua-3d-codex-T6-01 (DEKL2017 Theorem2.3) already gives the Fourier
logarithmic order. It is not used as a proof premise. Exact constant priority
and relation to older polyhedral proofs are unresolved.

## Proof or evidence

**1. A bounded dual test.** Direct integration by parts gives
`hat b(0)=0` and `hat b(q)=-i/q` for every nonzero integer q. Thus for any
finite set `R subset N_0^d` and the polynomial
`F(t)=sum_{r in R}exp(i r.t)`, finite summation gives

\[
\int F(t)\prod_{j=1}^d b(t_j)\,d\mu(t)
 =i^d\sum_{\substack{r\in R\\r_j>0\ \forall j}}{1\over r_1\cdots r_d}.
\]

There is no exchange of an infinite Fourier series with an integral here.
Since `||product b||_infinity<=pi^d`,

\[
\|F\|_1\ge\pi^{-d}
\sum_{\substack{r\in R\\r_j>0\ \forall j}}{1\over r_1\cdots r_d}.
\tag{2}
\]

**2. Integer facet coordinates preserve the L1 norm.** Define the integer
matrix A by

\[
(Ak)_1=-\sum_{j=1}^d k_j,\qquad
(Ak)_j=-\sum_{\ell=1}^d k_\ell+2k_j\quad(2\le j\le d).
\]

Subtracting row1 from each later row shows `det A=-2^(d-1)`, so A is
nonsingular. Set `r(k)=n*1+Ak`. Every coordinate is nonnegative for
`k in B_n^d`: each is n plus a signed sum of the coordinates of k and
is therefore at least `n-sum|k_j|`. A is injective on integer frequencies.
Consequently

\[
F(t)=e^{in\sum_jt_j}D_n^d(A^Tt)
 =\sum_{k\in B_n^d}e^{ir(k)\cdot t}
\tag{3}
\]

has the form required in (2), with every coefficient equal to1.

The map `t -> A^T t` is taken modulo2pi. It preserves probability Haar
measure, including when `|det A|>1`: for a character exp(i k.t), its
pullback integral is integral exp(i(Ak).t), equal to0 unless k=0 and
equal to1 when k=0, because A is nonsingular. Trigonometric polynomial
density then proves preservation for every continuous function, in
particular `|D_n^d|`. The prefactor in (3) has modulus1, so
`||F||_1=||D_n^d||_1`. There is no determinant loss.

**3. A harmonic subset of the positive transformed support.** For integers

\[
1\le a_1\le a_j\le m\quad(2\le j\le d)
\]

choose

\[
k_j=a_j-a_1\quad(j\ge2),\qquad
k_1=n-\sum_{j=2}^d a_j+(d-3)a_1.\tag{4}
\]

These k_j are nonnegative: the first coordinate is at least
`n-(d-1)m+(d-3)a_1>=0`. Their sum is `n-2a_1`, so
`r(k)=2(a_1,...,a_d)`. Thus all retained points have k in B_n^d,
and `r_j>0`. The retained
harmonic sum is

\[
2^{-d}\sum_{1\le a_1\le a_j\le m\ (j\ge2)}{1\over a_1\cdots a_d}
 \ge {H_m^d\over d\,2^d}.
\tag{5}
\]

Indeed every tuple in `{1,...,m}^d` has a minimum coordinate. Summing
its positive weight over the d choices of a minimizing coordinate covers
the full weight sum H_m^d, and the d sums are equal by symmetry. Ties
may count a tuple several times, which is the correct inequality direction.
Equations (2), (3) and (5) prove (1) for d>=3.

## Scope

The theorem is d>=3 (including the requested d3 case). No
logarithmic leading constant, optimality or interpolation upper bound.

## Open items

Independent analytic audit; optional constant improvements only for a
concrete need. No broader polyhedral theorem is needed for the cube result.

## History

2026-11-06, Codex gpt-6.1-sol xhigh, rules SHA above: surveyed primary
literature first, then wrote this explicit known-mechanism proof. During
writeup the general-d inverse-coordinate coefficient was corrected from
d-2 to d-3, and an unneeded d2 extension was removed before acceptance.
The original T6 target was d3 throughout; no 2-D theorem is claimed here.
