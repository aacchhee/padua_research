# PD-T?padua-3d-20261106-codex-D4-lee — elementary double-Lee-sphere bound

ID kind: PD-T. Aliases: C4; DS(3,n−1); packing-free determinant cutoff.
Split from: none. Split into: finite-minima.md for the computational range.

## Statement

For every integer n≥1 and full-rank lattice L⊂Z³ with
min{||v||1:0≠v∈L}≥2n,

    det L ≥ (2/3)n(2n²+1).

## Definitions and assumptions

Determinant means [Z³:L]. B(r)={v∈Z³:||v||1≤r} and
DS(r)=B(r)∪(e1+B(r)). The radius is r=n−1; the minimum is that of the
integer lattice L itself (the topic's dual/annihilator lattice), not a
scaled primal sampling lattice. Distinct vectors of DS have distance at
most2n−1, strictly less than the allowed lattice minimum.

## Status by part

Overall status: **PROVED** by the elementary argument below. No imported
packing density, anticode maximality theorem or Lee-tiling theorem occurs
as a dependency. No historical novelty claimed. The approved C4 record is
retained as IDEA?padua-3d-20261106-claude-04, not assigned a final ID.

## Proof

Two points of the same constituent ball differ in l1 by at most2r;
two points from different balls differ by at most2r+1. Equality is attained
between (−r,0,0) and (r+1,0,0), so diameter DS(r)=2r+1=2n−1.
If distinct a,b∈DS(r) had a−b∈L, the nonzero lattice vector a−b would
have norm≤2n−1, a contradiction. Thus DS(r) injects into Z³/L.

Fix transverse coordinates(y,z) with s=|y|+|z|≤r. Their x-coordinates
in the union fill the integer interval [−r+s,r−s+1], containing
2(r−s+1) points. There is one transverse pair at s=0 and4s at s≥1.
Consequently

    |DS(r)| = 2(r+1)+8 Σ[s=1..r] s(r+1−s)
            = 2(r+1)+(4/3)r(r+1)(r+2)
            = (2/3)(r+1)(2r²+4r+3).

Putting r=n−1 gives the stated bound by injectivity. The argument includes
n=1, where DS(0)={0,e1}.

## Depends on / sources

Only integer coset counting and the explicit cardinality calculation.
S3's report and Horak–AlBdaiwi's anticode discussion are attribution/context
(LITERATURE, scout coverage); neither is used to prove the statement.
The bound does not assert maximality of DS among anticodes.

## Checks and scope

The registered fd4_lee.py checks the cardinality and actual diameter for
n4..7 in exact Python integer arithmetic, as a finite sanity check. Its
unrestricted HNF restart uses the existing audited local reduction
[../theory/r08-lattice-reduction.md](../theory/r08-lattice-reduction.md).
No cosine-fiber size, rank, phase or cubature conclusion follows from
this determinant bound alone. Its leading term4n³/3 is weaker than the
imported38n³/27 cutoff at n>3, but entirely local.

## Open items and history

None for this elementary bound; exact restarted minima are separate.
2026-11-12, Codex, assigned gpt-6.1-sol high; runtime metadata unexposed;
rules04ef28b6139ad15b8cfc31f865c7bb9ba0d56d9b. Written before experiment.
