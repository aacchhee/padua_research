# PD-N?nn-mop-iep-codex-01 — common finite support forces a terminal zero divisor

ID kind: PD-N. Aliases: finite support boundary; terminal FHV division; C4 limit.
Split from: none. Split into: none.

## Statement

Under the definitions in finite-moment-formulation.md, every normal index
nu of total degree N has P_nu(x)=F(x):=product_l(x-x_l).
If |nu|=N-1 and nu,nu+e_1,nu+e_2 are normal, then

    P_(nu+e_1)=P_(nu+e_2)=F,  b_(nu,1)=b_(nu,2).

Consequently a reconstruction rule that requires division by
d_nu=b_(nu,2)-b_(nu,1) at every site through |nu|=N-1 fails on these inputs,
even when all indices through degree N are normal and all weights positive.
This refutes only that unmodified finite-boundary rule.

For |nu|<=N-2, if nu,nu+e_1,nu+e_2,nu+e_1+e_2 are normal and the
successor-difference identity holds, then d_nu !=0.

## Assumptions

N distinct real nodes; common support for both measures; exact arithmetic;
normality only as explicitly stated. b is in the monic convention of the
companion formulation. No claim that all normality conditions hold for all
positive weights.

## Status by part

Overall status: PROVED. Candidate disposition: REJECTED: failed, solely for
the rule demanding nonzero d at every site including the terminal layer.
The possibility of a boundary-aware update remains OPEN.

## Negative-result scope

Attempted mechanism: naive extension of FHV nonzero-divisor propagation
through the last shared-support layer (C4), and any C3 proposal imposing
that same requirement. Parameter range: all N>=1 under the statement's
normality conditions. This is not a refutation of FHV's theorem under its
nonzero-divisor hypotheses, or of a stable nearest-neighbour IEP.

## Depends on

PD-T?nn-mop-iep-codex-01 for the b formula and normality convention.
Source identification of the divisors: ../literature.md (FHV Thm 3.3).

## Proof

F is monic degree N and vanishes at every support point, so satisfies all
orthogonality conditions, at every index. Normality at an index of degree N
makes it the unique monic solution there. The subleading-coefficient formula
for b now gives equality of the two terminal b values. Thus the prescribed
division is division by zero.

For the interior assertion, d_nu=0 and the successor-difference identity
would make the two monic degree |nu|+1 successors equal. Their common
polynomial satisfies the union of their conditions, which are precisely
the |nu|+2 conditions at nu+e_1+e_2. It is a nonzero polynomial of degree
less than |nu|+2 in the kernel of that square moment matrix, contradicting
normality there.

## Checks

../exact-runs.md records executed rational cases N=2,...,8 with two positive
weight families, and explicitly tests terminal equality. The written proof
is independent of those finite checks. Independent audit PENDING.

## Scope and open items

Nodes/weights still determine the terminal polynomials and coefficients by
direct moment systems. A vanishing terminal divisor is an obstruction to
the stated division, not to solvability or uniqueness of those systems.
Use F directly at the boundary or supply a separately justified limit rule;
no numerical stability is asserted for either option here.

## History

2026-11-05: Codex, rules/head 320fe07f5231ac7e72a4da45e64a38e5ff381b4a.
Model metadata as disclosed in finite-moment-formulation.md.
