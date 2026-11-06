# PD-T?padua-3d-codex-T1-01 — reflection-stable finite torus cosets

ID kind: PD-T. Aliases: binary annihilator classification; parity coupling.
Split from: none. Split into: none.

## Statement

Write T=R/Z and c(t)=(cos(2pi t_1),...,cos(2pi t_d)). Let H be a finite
subgroup of T^d invariant under each map R_j that negates coordinate j.
Let m_j be the order of the coordinate projection of H, let
E={j:m_j is even}, and put M=direct sum_j m_j Z e_j.
Its annihilator L={l in Z^d:l·h is integral for every h in H} is precisely

    L = M + { sum_(j in E) (m_j/2)b_j e_j : b in B },             (1)

for a uniquely determined binary linear code B <= F_2^E containing no
coordinate unit vector. Conversely every such pair (m,B) defines a
reflection-invariant subgroup with exactly those projection orders, namely

    H = { (i_j/m_j)_j : i_j mod m_j,
          sum_(j in E) b_j i_j = 0 mod 2 for every b in B }.      (2)

Moreover, A=a+H is invariant under every R_j iff

    r_j=2m_j a_j is integral for every j,
    r_j is even whenever j is active in B.                      (3)

Here active means b_j=1 for some b in B. Equality (3) is interpreted for
any representative of a in R^d; its conditions are representative independent.
Modulo H and integer torus periods, all such A have the canonical form

    t_j=(i_j+epsilon_j/2)/m_j,
    (i_j mod 2)_(j active) belongs to an affine code C,
    epsilon_j=0 on active coordinates; epsilon_j in {0,1}
    freely on inactive coordinates,                              (4)

where C is any affine coset of B-perp. Coordinates outside E have no
parity constraint. Formula (4) can use the full d-dimensional B with zero
inactive columns; parity on odd inactive m_j is ignored.

For d=3, up to coordinate permutation, B is one of

    {0}; span(110); span(111); span(110,101).                     (5)

The three distinct pair choices in span(110) are retained when coordinates
are labelled. For d=2 the list is {0}, span(11).

## Definitions and assumptions

All statements are over the real torus, with finite H and d>=1.
Reflection stability of A is a hypothesis, not a consequence of taking
its cosine image. No cubature, positivity, rank, degree or asymptotic
assumption enters. B-perp uses the usual binary dot product.

## Status by part

Overall status: **PROVED** (written elementary proof; independent audit pending).
The classification and translated-coset normal form are substantive and
are kept separate from the obstruction using them.
Candidate disposition: retained variant of character duality; historical
novelty unverified and not claimed.

## Depends on

Elementary finite-group/character arguments proved below. No external
source theorem or conjectural cubature lower bound is a dependency.

## Checks

The finite exact checker is `../code/t1_reflection_enum.py`; compact actual
run receipt is `../evidence/t1-reflection-enum.json`. Its scope and executed
command are also in `../attempts/T1.md`. Enumeration is a diagnostic of
this hand proof, not its premise. Independent rerun is pending.

## Sources

Closest local records: PD-N032, PD-T081/091, PD-T106; literature comparison
and its reading limits are in `../literature-T1.md`. These motivate the
scope but are not proof dependencies.

## Proof

### Finite duality without an imported torus theorem

A finite subgroup of T is cyclic: if it has a positive element, choose
its smallest representative u>0. Division with remainder shows every
representative is an integer multiple of u, and closure forces u=1/m.
The trivial subgroup corresponds to m=1. Thus H lies in
P=product_j (1/m_j)Z/Z, which is the product of its coordinate projections.

Characters of P are exp(2pi i l·t) indexed by l modulo M. They separate
points. To justify double annihilation directly, let H^perp be the
characters trivial on H. The sum of any character over H is |H| when
trivial, and zero otherwise, by translating by an h with nonunit value.
Summing this identity over all |P| characters, whose sum at a nonzero
point of P is zero by the finite geometric-series formula, gives
|H^perp|=|P|/|H|. Apply the identical argument in the dual product group
to obtain |(H^perp)^perp|=|H|. It contains H and hence equals H.
In particular L/M determines H and M is contained in L.

### The code

Reflection stability of H implies reflection stability of L: substitute
R_j h in the defining integrality condition. If l in L, subtracting R_j l
gives 2l_j e_j in L. By the definition of m_j, the positive generator of
{u:u e_j in L} is m_j. Hence m_j divides 2l_j. If m_j is odd, m_j divides
l_j; if even, l_j is a multiple of m_j/2. Therefore L/M is a subgroup of
the binary group with the latter half-period coordinates, proving (1).
Uniqueness follows from reduction modulo M. A unit vector in B would put
(m_j/2)e_j in L, contradicting the definition of m_j.

Conversely, the set in (1) is a lattice stable under each R_j, since
changing the sign of a half-period changes it by an element of M.
Finite duality gives exactly (2) as its annihilator subgroup. If the
projection order on coordinate j were less than m_j, the corresponding
pure-axis annihilator, reduced modulo M, would be the unit vector of B
(odd m_j has no nonzero half-period option). This is forbidden. Thus the
orders are canonical and the converse is proved.

### Translations and folds

Since R_j H=H, equality R_j(a+H)=a+H is equivalent to
2a_j e_j in H. Membership in (2) first requires r_j=2m_j a_j integral.
Its parity constraints are b_j r_j=0 mod2 for all b, exactly the second
condition of (3). This proves necessity and sufficiency.

Write r_j=2s_j+epsilon_j. Active coordinates have epsilon_j=0.
The integer shift s_j/m_j moves the binary constraints to the syndrome
specified by s; inactive shifts are absorbed in i_j. Every syndrome
occurs, since independent rows of a binary matrix have a surjective
syndrome map. This proves (4), including its sufficiency.

On an active coordinate m_j=2q_j and epsilon_j=0. The cosine image is
the entire Lobatto axis cos(pi i/q_j), 0<=i<=q_j. All its levels occur:
the absence of a unit in B means that the projection of B-perp onto
that bit is surjective. Cosine folding i -> 2q_j-i preserves its parity.
Thus its even/odd level counts are

    e(q)=floor(q/2)+1,  o(q)=ceil(q/2).                         (6)

Inactive coordinates have independent full cyclic grids. Their distinct
cosine counts are floor(m/2)+1 if epsilon=0; if epsilon=1 they are m/2
for even m, and (m+1)/2 for odd m. This follows by pairing grid angles
t with -t: epsilon=0 has one fixed point when m odd and two when m even;
epsilon=1 has one when m odd and none when m even. These formulas include
m=1. Independent axes combine by Cartesian product, subject only to C
on the active parity bits, so folded counts are sums of products of (6).

### The low-dimensional list

In F_2^3, a one-dimensional subspace without units is generated by a
word of weight two or three. A two-dimensional subspace is the kernel
of one nonzero linear functional v·b. It contains no e_j iff every
v_j=1, so it is the even-weight plane span(110,101). Dimension three
contains units and is impossible. This gives (5); the d=2 statement
follows by the same inspection. No enumeration is used here.

## Scope

This is a classification of H stable under all coordinate reflections
and, separately, of those translates A which also have that property.
It does not classify arbitrary translated cosine images, arbitrary
subgroups without reflection stability, or unions of several cosets.

## Open items

Independent mathematical audit and finite rerun. Broader class target:
`t1-open-class.md`; it remains OPEN.

## History

2026-11-06, Codex, assigned gpt-6.1-sol xhigh, rules/input SHA above.
Proof written after the recorded T1 gate. No source novelty is asserted.

## Supplementary check addendum — 2026-11-06

[Distinct Astra high check](../independent-checks-math.md) completed
within its stated scope, including actual separate execution. Earlier
pending-check wording records the development state. Required Claude
substantive audit remains due; this addendum changes no mathematical claim.


## Completed-audit process addendum — 2026-11-06 — m5

[Claude audit-01](../audit-01.md) completed the substantive independent audit
of candidate f1a5b0936d8fb2b033c69af59a6366550f170999, including the recorded
independent executions, after the supplementary Astra checks. Its accepted
mathematical scopes supersede earlier “audit/replay/rerun pending” and
“planned, no run claimed” process descriptions where those refer to that
completed work. This addendum changes no mathematical statement or status;
MEASURED observations remain MEASURED and OPEN targets remain OPEN. The
new response dispositions/ID-kind/evidence changes require focused re-audit,
not another approval of the unchanged accepted mathematics.
