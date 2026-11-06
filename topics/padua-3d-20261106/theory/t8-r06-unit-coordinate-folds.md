# PD-T?padua-3d-20261106-codex-T8-r06-02 — first-unit phased fold counts

ID kind: PD-T. Aliases: partial inversion pairs; near-order collision
divisors; odd minimal half-grid phase rigidity. Split from: none. Split into: none.

## Statement and definitions

Let M>=3 and z=(1,b,c) modulo M, and take the full cosine image of
a+<z/M>. If 2M a_1 is not an integer, all M nodes are distinct.
Otherwise reparameterizing k and applying coordinate sign reflections
reduces a_1 to h/(2M), h in {0,1}. Put

    J={j in {2,3}: 2a_j-h z_j/M is not an integer},
    d=gcd(M,z_j:j in J),     q=M/d,
    K=d*gcd(2,q) if gcd(2,q)|h, and K=0 otherwise,
    f=gcd(2,M) if gcd(2,M)|h, and f=0 otherwise.

For J empty use d=M. Then the exact number of distinct nodes is

    |X| = M-(K-f)/2.

In particular, when M=2N-1 is odd, |X|=N and b,c nonzero modulo M
force J empty. Up to coordinate signs and cyclic reparameterization,
X is then the zero-phase set with the same generator. Hence arbitrary
phases cannot improve the Lebesgue constant at fixed generator in this
first-unit exact-minimal odd-order class. This does not compare different
generators, or cyclic groups without a unit coordinate.

## Assumptions and status

Overall status **PROVED**, by elementary cosine equality below. Real phases
are arbitrary, including irrational ones. For the last conclusion assume
nonconstant axes b,c!=0; a constant axis already prevents Pi_n injectivity
for n>=1. Candidate retained as a structural reduction, not a global
cyclic or phase-family impossibility. No source theorem or floating premise.

## Proof

If first-coordinate cosines agree at k!=l, cosine equality implies
k+l=-2Ma_1 mod M, which requires 2Ma_1 integer. Shifting the parameter
changes its integer value by an even integer; a first-axis sign reflection
changes it by M. Its parity can therefore be represented by h=0 or1;
all other phase coordinates change by the same parameter shift. Once
a_1=h/(2M), the only possible partner is l=-h-k mod M. Thus node
equivalence classes have size at most two.

For a coordinate j, equality at this partner holds precisely when either
z_j(k-l)=0 mod M, or 2a_j-h z_j/M is an integer. The latter condition is
exactly j outside J. All incompatible coordinates therefore require
M|z_j(2k+h), equivalently q|2k+h, with q=M/d. This congruence has K
solutions modulo M by the elementary linear-congruence count. Of them,
f satisfy l=k (2k+h=0 mod M); each remaining pair is counted twice.
Subtracting (K-f)/2 duplicates proves the formula. A coordinate sign
reflection does not change count, rank or Lebesgue constant.

For odd M, K=d and f=1. Thus |X|=(M+1)/2 forces d=M.
With nonzero b,c, any nonempty J would make gcd(M,z_j:j in J)<M.
Hence J is empty and a_j=h z_j/(2M)+e_j/2 for integers e_j.
For h=0 the nodes differ from zero phase only by the coordinate signs
(-1)^e_j. For h=1, since M is odd, a half parameter step equals an
integer parameter step plus M/2; the latter multiplies axis j by
(-1)^z_j. This again gives a coordinate reflection of the zero-phase
set. Reflection preserves Pi_n and the domain [-1,1]^3, proving equality
of true Lebesgue constants, and equality on the reflection-invariant
fixed Lobatto mesh. No H39 claim is reopened by this reduction.

## D3, finite scope and checks

The argument requires a unit coordinate to bound each node class by two.
The usual 2D Padua cyclic generator (n+1,n) modulo 2n(n+1) has neither
coordinate a unit for n>=2, so this restricted formula does not apply.
The general cosine-collision equality used in the proof includes Padua;
the independent D0 test verifies its exact count and trace through 12.

For M=N+s with small s, this formula tests every first-unit generator's
count by gcds and the two possible h. It is independent of the actual
noncompatible free phases. Rank on each surviving stratum still needs
the T7-03 symbolic-minor argument or an exact positive specialization.
New code tests its predicted count against direct exact folded residues
for every finite candidate it measures. Computational tables remain
MEASURED until independently rerun; the analytic formula is not conditional
on those tables. Every matching finite parameter case is retained by its
parent route's receipt/raw catalogue.

## Sources, scope, open items and history

Known cosine/finite-character mechanisms; no historical novelty claim.
Comparison limits in literature-T8-round06.md. The non-unit-coordinate
phase class and quality across generators remain OPEN. Checker: future
code/t8_r06_near_orders.py, with exact counts and rational modular witnesses.
2026-11-06, Codex assigned gpt-6.1-sol xhigh, rules 7afa6a54, after the
initial half-grid Phi3 and S screens; before the new mixed-stratum run.
