# PD-T?padua-3d-20261106-codex-D4-reduction — exact finite Lebesgue enclosure

ID kind: PD-T. Aliases: C3; fixed-point residual/mesh transfer.
Split from: none. Split into: results.md for executed finite instances.

## Statement, definitions and assumptions

Let x1,…,xN∈[−1,1]³ be distinct exact dyadic points, N=binom(n+3,3),
4≤n≤16. V evaluates the unscaled product Chebyshev basis of Π_n at these
points; each basis polynomial has absolute value≤1 on the cube. Let
Q be a matrix of exact multiples of2^-24 approximating V and W any exact
matrix of the same kind. Assume rigorous scalar bounds

    max_ij|Vij−Qij|≤β,
    w=||W||∞,
    r0=||I−QW||∞,
    ρ=r0+Nβw<1.

Let M be the exhaustive maximum of ||P(x)W||1 over rounded tensor
Lobatto coordinates of order mn, where P denotes a fixed-point evaluation
matrix, and suppose every evaluation row differs from the exact degree-n
basis row on the corresponding true Lobatto mesh point by at most βm
in each entry. Put e=Nβm w. Then the interpolation projector exists and
its Lebesgue constant obeys

    max(0,M−e)/(1+ρ) ≤ Λ ≤ c_m (M+e)/(1−ρ),
    c_m = 1/cos(π/(2m)).

Replacing c_m by a rigorous rational upper bound preserves the result.
The tensor mesh factor here is dimension independent because the space
has TOTAL degree n; a tensor-degree-n space is a different statement.

## Status by part

Overall status: **PROVED with explicit LITERATURE dependency**, as a
conditional-on-checkable-premises reduction. The local inverse/error
argument is proved below. The final continuum mesh implication imports
Białas-Cież–Kenne–Sommariva–Vianello, arXiv2311.18656v1, Lemma1 and
Proposition1 pp3–4, with primary statement/application checked by the D5
worker. The source's proof is not claimed locally verified. Executed
instances additionally require committed evidence and independent rerun;
unexecuted instances are not theorems. No new mechanism/priority claim.

## Proof

R=I−VW has ||R||∞≤ρ. Therefore I−R=VW is invertible, hence V is
invertible and V^-1=W(I−R)^-1. If p is an exact evaluation row and
ℓ=pV^-1, then pW=ℓ(I−R), so

    ||pW||1/(1+ρ) ≤ ||ℓ||1 ≤ ||pW||1/(1−ρ).

Indeed the row l1 norm obeys ||aB||1≤||a||1||B||∞, and the Neumann
series gives ||(I−R)^-1||∞≤1/(1−ρ). The βm entrywise evaluation bound
implies ||pW−PW||1≤Nβm w=e, giving the two mesh bounds.

The source's Proposition1 applies to an operator
Ln f=Σ_i f(xi)φi with xi in the cube, φi∈Π_n. Here φi are the cardinal
polynomials, which exist because V is invertible. It bounds the actual
projector norm, equal to sup_xΣ_i|φi(x)|, between the mesh maximum and
c_m times that maximum. The Lebesgue function is not itself assumed to
be a polynomial. This establishes the continuum upper bound.

## Exact arithmetic implementation and trusted dependencies

fd4_certify.py uses S=2^24. It rounds numerical evaluations/inverse
proposals to integers A,B and computes QW=AB/S² exactly with int64
multiplication. Before every multiplication it checks
inner_dimension*maxabs(A)*maxabs(B)<2^63; before absolute row sums it
checks column_count*maxabs(product)<2^63. These bounds cover every
partial dot/sum, so no modular wraparound occurs. All residual, Neumann
and final endpoints are Python Fraction values. The inverse proposal is
untrusted: only its independently bounded residual matters.

For exact dyadic coordinates and binary64 unit roundoff u=2^-53, the
implemented Chebyshev recurrence admits errors e0=e1=0 and

    e_(k+1) = 2e_k+e_(k−1)+8u(1+max(e_k,e_(k−1))).

Multiplication by2 is exact. The8u allowance bounds the remaining
multiplication/subtraction even allowing earlier errors; all values stay
in the normal finite range. With e=max(e_(n−1),e_n), two subsequent
products give absolute error at most
3e(1+e)²+γ2(1+e)³, γ2=2u/(1−2u). Nearest-integer rounding to2^-24
adds at most1/(2S). β is this exact Fraction bound rounded UP to2^-40.
The NumPy chebvander recurrence, product order and no overflow/underflow
at the admitted degrees are trusted implementation obligations; an
independent exact/interval checker should challenge them.

Scalar mpmath interval arithmetic at60 decimal digits encloses π and
cosines with directed dyadic endpoints. True Lobatto coordinates lie
in those intervals; the selected binary64 coordinate is clamped to the
cube. An exact Fraction comparison proves coordinate error≤δ=2^-52.
For a multi-index α with |α|≤n, |∂j Tα|≤αj² on the cube; telescoping
coordinate replacements and Σαj²≤n² give βm=β+n²δ. A directed scalar
interval supplies a rational c_m upper bound rounded UP to2^-40.

Trusted libraries are NumPy's stated binary64 recurrence and exact int64
arithmetic under checked bounds; Python integer/Fraction arithmetic;
mpmath's scalar interval π/cos implementation and directed endpoints;
JSON/base85/SHA256 for identities. SciPy QR/eigendecomposition and floating
inversion generate proposals/MEASURED diagnostics only.

## Scope, checks and open items

The finite certificate verifies precisely the stored dyadic coordinates,
not the ideal irrational QR mesh or a historical optimizer trajectory.
Every true mesh point must be evaluated; a cap leaves the continuum
certificate unestablished. Exact endpoints, coordinates, source identities
and timings are retained in the corresponding receipts. Gram eigenvalues
are MEASURED, and no asymptotic Riesz-gap claim follows from finite trends.

The source's m3 factor is 2/sqrt(3)≈1.15470054 relative to the mesh
maximum; its midpoint relative half-width is about7.18%, not a7.7%
multiplicative mesh upper error. The scout's approximate7.7% cube
framing should not be used as the actual theorem constant.

2026-11-12, Codex, assigned gpt-6.1-sol high; runtime identifier unexposed.
Rules/input04ef28b6139ad15b8cfc31f865c7bb9ba0d56d9b. Registered protocol
precedes runs. Primary-source coverage record belongs to D5.
