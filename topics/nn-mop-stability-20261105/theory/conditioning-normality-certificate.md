# PD-T?nn-mop-stability-codex-D1-04 — noncircular interior-d normality criterion

ID kind: PD-T. Aliases: scalar exact C4 normality certificate; opposite-corner
converse. Split from: finite Hahn verification. Split into: none.

## Statement

For N distinct real nodes and two strictly positive weight vectors, compute
the two exact marginal Jacobi families. Run the exact C4 layer formulas only
through coefficient degree N−2. If the computation is defined and every
d_nu=b2_nu−b1_nu on degrees0,...,N−2 is nonzero, then every multi-index of
total degree<=N is normal. Consequently the computed coefficients on this
smaller triangle equal the defining moment coefficients. This gives a finite
exact normality test, without assuming full normality in its premise.

## Definitions and assumptions

PD-T286 moment matrices, monic polynomials and h/t conventions; PD-T289
layer formulas; N>=2; exact arithmetic. Marginal positivity is required.
The algorithm stops before the terminal coefficient layer N−1.

## Status by part

Overall status: PROVED (written analytic implication; independent audit pending).
Finite execution of the Fraction checker is distinct evidence, recorded in
attempts/D1.md. No all-N Hahn-family theorem is inferred from finite runs.
Candidate disposition: retained standard determinant/normality converse.

## Depends on

PD-T286 defining systems and bordered h determinants; PD-T288's successor
difference identity under the three base/successor normalities (its
nonvanishing conclusion used an extra normality, not used here);
the localized layer induction in PD-T289.

## Proof or evidence

Every marginal moment matrix through degree N is a positive definite Gram
matrix: a nonzero polynomial of degree<=N−1 cannot vanish at all N nodes.
Therefore all axis indices are normal. They supply exact marginal data.

Suppose eta, eta+e1 and eta+e2 are normal. The same one-dimensional
orthogonality-kernel argument as PD-T288 gives

    P_(eta+e1)−P_(eta+e2)=d_eta P_eta,

without assuming normality of the opposite corner. Applying
L2(x^(eta_2) .) yields

    h_(eta+e1,2)=d_eta h_(eta,2),

because P_(eta+e2) satisfies that additional second-measure constraint.
The factor h_(eta,2) is nonzero by normality of eta+e2. Thus nonzero
d_eta implies h_(eta+e1,2)!=0. Border the normal moment matrix at
eta+e1 by the next second-measure row/column. The Schur complement is
h_(eta+e1,2), up to the harmless row-order sign. Its nonzero value makes
the opposite-corner matrix normal.

Induct on target degree k=2,...,N. Assume normality through k−1. The
localized exact reconstruction proof computes true coefficients through
degree k−2: every polynomial successor required has degree<=k−1;
producing layer t<=k−2 divides only by d at degree<=t−1, whose opposite
corners have degree<=t+1<=k−1 and hence are normal. This is precisely the
induction in PD-T289, with its unused common-support terminal statement
omitted; no normality at degree k has entered.

For each mixed target nu=(n,m) of degree k, let eta=(n−1,m−1). Its degree
is k−2, so the computed d_eta is the true successor difference under the
induction assumption. The certificate checks it nonzero. The converse
above establishes normality at nu. Axis targets are already normal. This
completes the induction through N, proves the implication and proves that
no circular assumption is hidden in using the smaller exact C4 triangle.

## Checks and sources

code/conditioning_exact_normality.py evaluates the generic scalar graph
with fractions.Fraction, all input coordinates rational, only through N−2.
It checks strict input positivity/distinctness, exact nonzero d values and
Fraction types, and hashes the complete exact coefficient payload. The
finite outcomes and independent rerun must be recorded separately before
any computer-assisted finite theorem is claimed. No external source used.

## Scope

This is a sufficient exact certificate, applicable to any such rational
input. A failed certificate (including zero d) is not promoted into a
broader impossibility statement. The generic proof is independent of the
Hahn family and independent of floating derivative precision convergence.

## Open items

The finite N=4,...,64 Hahn application and separate independent replay are
complete in [conditioning-hahn-normality-finite.md](conditioning-hahn-normality-finite.md).
Mandatory Claude audit remains pending. A direct all-N Hahn-family normality
proof is outside this certificate theorem.

## History

2026-11-05, D1 round2 after checkpoint f75964bd71336aee2a05f4ebb39eb31215be360a;
Codex gpt-6.1-sol xhigh. The original round1 local/coarse proofs are unchanged.
