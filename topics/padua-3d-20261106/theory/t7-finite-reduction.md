# PD-T?padua-3d-20261106-codex-T7-03 — finite subgroup and symbolic phase reduction

ID kind: PD-T. Aliases: all-phase coset reduction, HNF phase strata.
Split from: none. Split into: none. Supports the OPEN T7 target.

## Statement and status

Fix d,n,N and seek H≤(R/Z)^d, a∈(R/Z)^d with exactly N distinct
cosine nodes. Then |H|≤2^dN. There are finitely many possible embedded
H. For each H there is a finite explicit partition of phase space into
products of specified rational singleton coordinates and complements of
finite sets. The node count is constant on each such stratum.

On any stratum, the maximum evaluation rank is the rank of one explicit
matrix over a cyclotomic rational function field. Full column rank is
attained somewhere on that stratum iff that symbolic rank is full;
when attained, it holds away from a proper algebraic zero set. Thus
existence at fixed n reduces to finitely many **symbolic** rank tests,
not finitely many literal phases or node sets.

Overall status: PROVED by the proof below. The full n2/n3 census is
OPEN and is not an output of this theorem. No novelty claim.

## Definitions and assumptions

Angles are in turns; c(t)=cos(2πt) coordinatewise. H is any finite
embedded subgroup; a is any real phase, including irrational phases.
Polynomial space is Π_n with the total-degree product-Chebyshev basis.
There is no symmetry quotient in the complete parameterization below.

## Proof: finite groups

For any x, each coordinate of a torus point mapping to x has at most
two possibilities modulo1. Hence c has fibers of size at most2^d.
Its restriction to a+H has the same bound, proving |H|≤2^dN.

Put L=H^⊥≤Z^d. Finite character duality (or the elementary argument
in T7-01) gives [Z^d:L]=|H| and recovers H from L exactly. Sublattices
of index m have unique upper row-Hermite matrices. In dimension3 write

    B = [[a,r,s],[0,b,t],[0,0,c]],
    a,b,c>0, abc=m, 0≤r<b, 0≤s,t<c.

Here L is the integer row span. Existence follows by choosing the
positive generator of the first-coordinate projection, then the
positive generator of the second-coordinate projection in its kernel,
then the last positive pivot, and reducing entries by the later rows.
The projection/kernel choices and reduced remainders also prove
uniqueness. These are Euclidean integer operations. Recover H as
{B^(−1)k mod Z³:k∈Z³}. Taking 0≤k_j<B_jj gives all abc points:
reduce the last coordinate modulo c, then the second modulo b, then
the first modulo a using columns of B. Uniqueness follows in reverse.
In particular the number of labelled embedded subgroups of order m is

    A_3(m) = Σ_{abc=m} b c².

The corresponding d-dimensional triangular construction is finite
for every m. HNF is established prior art; see literature-T7.

## Proof: every phase and collision pattern

The jth projection of H is the unique circle subgroup of some order
m_j: {k/m_j mod1}. Define

    S_j = {a_j:2a_j∈(1/m_j)Z/Z} = (1/(2m_j))Z/Z.

Partition the jth phase circle into each of the 2m_j rational points
of S_j and the single set T\S_j; take their products. This gives
at most ∏_j(2m_j+1) strata. A complement need not be connected and
usually has positive dimension; it is not represented by one point.

For h,h'∈H, equality of the jth cosines is exactly

    h_j=h'_j, OR 2a_j=−h_j−h'_j mod1.

If a_j∉S_j the second option is impossible, because h_j+h'_j is
in the projected subgroup. If a_j is a specified member of S_j,
both alternatives have a fixed truth value independent of every free
coordinate. Thus the equivalence relation on H induced by cosine
equality, and hence the node count, is constant on the stratum. This
also proves that the all-free stratum has no collisions: |X|=|H|.
There are other strata with some free coordinates and some collisions;
they must all be retained.

## Proof: symbolic ranks are sufficient for existence

Use B from [T7-01](t7-general-character.md), now calling the character
matrix C to distinguish it from the HNF matrix. Fix the special phase
coordinates of a stratum and let z_j=exp(2πia_j) for the free ones.
Entries of C are Laurent polynomials in z_j with cyclotomic
coefficients, because all specified coordinates are rational. Its
symbolic rank is therefore well-defined over K(z_j:j free).

Put D=|I_n|=binom(n+d,d), independently of the requested node count N.
If every D-column minor vanishes identically, evaluation cannot have
full rank anywhere. Conversely a nonzero Laurent polynomial cannot
vanish on a nonempty open product of circle arcs: fix all variables
but one, use the one-variable finite-root property, and iterate.
Every free-coordinate complement contains open arcs. A nonzero minor
is consequently nonzero at some allowed real phase, and its zero set
has empty interior there. The same argument applies to the maximal
nonzero minor and proves the maximum-rank assertion. No assertion that
rank is constant everywhere in a stratum is made.

## Why one generic sample does not suffice

Take H={(k/3,k/3):k=0,1,2} in T² and Π_1. Both phases
(1/12,1/12) and (1/12,1/4) lie in the same all-free stratum: neither
coordinate is in (1/6)Z/Z. Both give three nodes. In the first case
x=y and rank2; in the second rank3. Indeed the evaluation columns
are 1 and two linear combinations of cos(2πk/3), sin(2πk/3);
the latter coefficient determinant is sin(2π(a_1−a_2)), zero in
the first case and nonzero in the second. This is a hand proof.

A full-column-rank exact specialization proves a nonzero D-column minor. A deficient
specialization alone never proves a stratum deficient. An exhaustive
claim must enumerate the entire lattice list and perform these exact
symbolic decisions on every target-count stratum. All-special phase
grids omit continuously many strata and may miss existing survivors.

## Checks, sources, scope and open items

The exact count formula is costed by t7_cosets.py; this is not an HNF
enumeration receipt. The phase-rank example has a separate exact finite
check and independent reconstruction. D3 is respected: the bounds and
strata include the Padua cyclic group for every n, and the short-relation
test separately proves Padua admission. No full-class PD-N is claimed.

Next unresolved step: implement complete lattice enumeration with a
verified phase-stratum node-count checker and symbolic rank. Symmetry
quotients need a separate proof that translations and ranks are carried
along. Bibliographic limits are in literature-T7; no external theorem
is used in the proof. 2026-11-06, Codex, assigned gpt-6.1-sol xhigh,
rules e5b6445; provisional ID.

2026-11-06 (audit-03 note): the enumeration and symmetry quotients are implemented and the n2 census completed in [t7-r06-n2-census.md](t7-r06-n2-census.md); n3 remains OPEN.


## Dated audit-02 attribution and split — 2026-11-06

Claude's [handoff04](../handoffs/04-work.md) supplied the fold bound
|H|<=8N and finite-search sketch. The proof above supplies the full symbolic
stratum formulation. Its positive finite reduction remains
PD-T?padua-3d-20261106-codex-T7-03. The rejected one-phase-per-stratum
inference is separately mapped to [PD-N T7-09](t7-one-phase-refutation.md);
its counterexample remains here as proof context.
