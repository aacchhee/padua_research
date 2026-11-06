# PD-T?nn-mop-cond-codex-C2-03 — all-N Hahn exponential lower bound

ID kind: PD-T. Aliases: Hahn terminal one-cross-step annihilator; base-two
Hahn lower; relative signed-binomial direction with fixed mass.
Split from: none; this lower bound is a supporting dependency of PD-T448,
not a resolved full sharp-Hahn target case.
Split into: none; this is a lower bound, not the sharp Hahn target.

## Statement

For every integer N>=2 set M=N-1 and use the exact Hahn nodes/weights in
`c2-hahn-normality.md`: alpha1=1, alpha2=3/2, gamma=1, z_k=2k/M-1.
Let kappa_N use the PD-T432 input cube |dot z_k|<=1,
|dot w_(s,k)|<=w_(s,k) and relative four-field sup output norm.
Then

    kappa_N >= 2^(M+1)
      /[M(2M+3) binom(M+4,4) (M+1)(2M+1)].               (1)

In particular liminf_(N->infinity) kappa_N^(1/N)>=2. The same inequality
holds with fixed masses and with componentwise-node perturbation bounds,
because the witness changes no nodes and has zero weight mass.

The lower base 2 is explicitly nonsharp. This does not identify or prove
the measured per-node value near11.8, give a matching upper, or close the
sharp Hahn part of PD-T448.

## Definitions and assumptions

The input is normalized to mass one separately for each marginal. The
perturbation leaves that Hahn parameter family, as the unrestricted
PD-T432 input model permits. Exact arithmetic, full normal triangle and
positive field scales are supplied by the separate all-N theorem
`c2-hahn-normality.md`. The proof uses the integer coordinate k first.

## Status by part

Overall status: PROVED (written analytic proof).

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Explicit all-N inequality (1) | PROVED | Terminal scalar complement and finite-difference witness below |
| Fixed-mass and componentwise-node corollaries | PROVED | Same admissible direction |

Candidate disposition: retained weaker quantitative family variant of
IDEA?nn-mop-cond-codex-C2-03 and IDEA-534. No historical novelty claim.
The full sharp Hahn rate/base remains OPEN, not PARTIAL from this lemma.

## Depends on

PD-T286/432 for the moment-defined map and induced norm;
`c2-hahn-normality.md` for every-N normality, the adjacent-kernel rational
identity and the loose field bound ||b2||<=2M+3. The scalar-orthogonal
complement and finite-difference method are the same as PD-T437/PD-N162,
with a separately derived Hahn cross expectation below.

## Proof

### Exact scalar cross expectation

Let K_r be the monic scalar orthogonal polynomial of degree r for the
first Hahn marginal, 0<=r<=M. In the notation of (6),(7) in the normality
file, its rational transformed functional is

    F_r(x)=C_r*prod_(i=0)^(r-1)(x-1-i)/(x+1)_(r+2),
    C_r=(r+1)!/[(M-r)!(r+3)_r].                           (2)

The normalized second expectation is obtained by setting x=3/2 in
that transformed functional. Its row factor divided by the second mass
is M!*(5/2)*(7/2), so

    E_2 K_r=(-1)^r (M)_r^fall (r+1)!/(r+3)_r
                                      *(-1/2)_r/(9/2)_r. (3)

Here (M)_r^fall=M!/(M-r)! denotes a falling factorial, and the other
parentheses are rising factorials. Equation (3) follows from (2) by
prod_(i=0)^(r-1)(1/2-i)=(-1)^r(-1/2)_r and cancellation of the first
two factors of (5/2)_(r+2). It requires no hypergeometric summation or
unread scalar Hahn formula. Every expression in (3) is nonzero.

For r=M-1, including M=1 with empty products, (3) implies

    |E_2 K_(M-1)|
      = M!*(M+1)/binom(2M,M)
                                  *|(-1/2)_(M-1)|/(9/2)_(M-1)
      <= M!*(M+1)/binom(2M,M).                            (4)

The last rising-factorial ratio is at most one term by term.

### Terminal complement and admissible perturbation

At nu=(M-1,1), orthogonality to the first marginal through degree M-2
gives the two-dimensional complement spanned by K_M,K_(M-1). Therefore

    P_nu=K_M-c K_(M-1), c=E_2 K_M/E_2 K_(M-1).            (5)

For M=1 the same statement is simply the full two-dimensional polynomial
space, with no first constraints. It remains valid for sufficiently small
changes only to the second weights.

Define

    C_M=1/[2^M binom(M+4,4)],
    dot w_(2,k)=C_M*(-1)^k*binom(M,k), dot w1=0, dot z=0.  (6)

The exact unnormalized W_(2,k) is at least one. Its mass is
Z2=(9/2)_M/M! <=(5)_M/M!=binom(M+4,4). Thus

    w_(2,k)>=1/binom(M+4,4),
    |dot w_(2,k)|<=C_M 2^M<=w_(2,k).

The direction is admissible; its input norm is at most one, which is
enough for an induced-norm lower bound. Its mass is zero because
sum(-1)^k binom(M,k)=0. Positive weights persist for |epsilon|<1.

The Mth finite-difference identity annihilates every polynomial of
degree less than M and sends a monic degree-M polynomial to (-1)^M M!.
Hence dot E_2 K_(M-1)=0, |dot E_2 K_M|=C_M M!, and differentiating (5)
gives

    |dot c|=C_M M!/|E_2 K_(M-1)|
      >= C_M binom(2M,M)/(M+1)
      >= 2^M/[binom(M+4,4)(M+1)(2M+1)].                  (7)

For the final inequality, the central binomial coefficient is the largest
among the 2M+1 coefficients summing to 4^M, so it is at least their average.

### Convert to the stated output metric

The subleading coefficient of (5) has derivative -dot c, since K_(M-1)
is monic and the first marginal is fixed. The terminal successor is the
fixed support polynomial. Therefore the integer-coordinate terminal
B2 derivative has magnitude |dot c|. Under z=2k/M-1 its b2 derivative
has magnitude 2|dot c|/M. The all-N normality/subleading theorem bounds
its field scale by 2M+3. Dividing this one row's response by that upper
field-scale bound and using (7) proves (1).

The witness is already a fixed-mass direction and changes no nodes, so
both stated restricted-input corollaries follow. Polynomial denominators
in (1) have Nth roots tending to one, proving the liminf bound.

## Checks

`../code/c2_hahn_checks.py` compares the exact expectation (3), terminal
derivative (5)–(7), field/subleading formulas, and kernel determinant
against defining Fraction moment systems. Scope and source hashes are
recorded in `../c2-hahn-checks.json`. These finite identities support
the written proof and are not an all-N computational premise.
Supplementary independent replay and Claude audit are separate records.

## Sources

No new external theorem. Exact input PD-T290; self-contained moment
derivation in the preceding normality theorem; predecessor finite-difference
witness method PD-T437/PD-N162. The prospective C2 gate records the scope.

## Scope and open items

This proves exponential local conditioning for this Hahn family in the
specified monic metric, even with fixed masses. It is much weaker than
the finite observed growth. A balanced-index dual may improve it, but no
such asymptotic is established here. Sharp Hahn rate/base, matching upper,
finite-error radius and actual floating-rounding loss remain OPEN.

## History

2026-11-06: Codex gpt-6.1-sol xhigh, rules/local source
`76ba4214b100c86a44941f5e9a662ce9ce48efb8`, topic pin
`b4a04981d42c7cd872957facf5e3995e4096ca67`. Written after C2 gate;
no predecessor or shared registry edits, no Git mutations.

2026-11-06 response, Codex gpt-6.1-sol high, rules/source `3d5b29d`:
the former “Split from: PD-T448 (sharp matching-growth target, OPEN)”
label is corrected to a supporting-dependency relation (MINOR-6).
The [parent classification proposal](../classification-proposal.md) separates
the proved benchmark Krawtchouk rate conjunct from the remaining OPEN
conjuncts; this Hahn lower is not one of the resolved target cases.
The theorem, proof and PROVED status are unchanged.
