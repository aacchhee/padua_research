# Supplementary mathematical review: N5 two-phase defect

2026-11-06. Distinct Codex subagent `/root/review_phase_round4`, assigned
gpt-6-astra high; serving model/effort are not independently exposed.
Input/rules head: `121ae257a71564025ddc2da8f53d19478f5d7dd4`.
AGENTS, WORKFLOW and CODEX were read earlier in this session; their diff
to this head is empty. This supplements the required Claude audit.

**Disposition: ACCEPTED at the stated mathematical scope.** For every
n>=64, J=0 or n, interior q with J+q odd, physical inward alpha and
|alpha|+|beta|<=1/2, the proof establishes the actual-function deficit
strictly greater than 1/2048, and consequently the N1-model deficit
strictly greater than 255/524288. No unresolved mathematical finding
remains. This is not a primitive/model maximum bound, complete physical
square comparison, new degree certificate, effective onset or PD-T099 proof.

## Frozen inputs and scope of review

| Input | SHA-256 |
|---|---|
| theory/N5-two-phase-defect.md | `de47e7d806f6c4d5107148516c7bec6686ba27c60b1d872572564ec94b7e0646` |
| code/n5_two_phase_defect.py | `fd1402000f2bd0b06477396270ea797237b70d2f4295d09246d03468ef77dc63` |
| evidence/n5-two-phase-defect.json | `76ee7b68c3e0ec553765dba71ba97f2ea3598164c331a67f794be1d74a5aa0f8` |

Read the complete N5-04 proof, developer code/receipt and candidate;
the complete load-bearing N5-03, PD-T366 and PD-T222 constructions;
the earlier [N5 all-edge supplement](independent-checks-n5-all-edge.md);
and N1's full-diamond model statement and definitions. PD-T364's exact
primitive/projection identities were reconstructed in this session's
phase review. The original N1/N5 error theorem is an inherited dependency,
not a new quadrature audit here.

This review assesses the quantitative proof and its implementation
diagnostics, without adjudicating a new mechanism, priority claim or
exhaustive novelty comparison. Under the explicit no-novelty-content
exception, it does not reread the full IDEAS registry. The canonical
prospective-gate qualification remains in [attempts/N5.md](attempts/N5.md),
round4; this review does not upgrade its recorded timing or coverage.
No external theorem or literature claim is transferred.

## Corrected numerator and exact normalization

Let tau=(-1)^r, x=cos u and y=cos v. Since r+k=J modulo2 and J+q is
odd, r+q+k and r+q-k are odd. Direct angle addition gives

    P_n(x)=tau[cos(alpha)(1+x)-sin(alpha) sin(u)],
    P_n(y)=-tau[cos(beta)(1+y)+sin(beta) sin(v)].

Also cos(nu)=tau cos(alpha). Therefore the signed half tau G/2 is

    [(cos(alpha)+cos(beta))(1+y)
       -sin(alpha) sin(u)+sin(beta) sin(v)]/[2(x-y)],

at a regular denominator. This is precisely the claimed A/(x-y).
Subtracting1 would fail away from alpha=0. The exceptional mode remains
in the first coordinate. Finite polynomial values define G at every
collision; only the selected regular terms use the quotient.

For normalization, PD-T364's periodic projection is
(1/(4N)) sum d(G_rs,G_r,2q-s), where d(x,y)=|x|+|y|-|x+y|.
Each common signed G-to-half scaling changes d by a factor2, giving
(1/(2N)) times the periodic half-defect sum. Fold the second periodic
index into physical k=0,...,m. Interior rows occur twice, while the
fixed endpoints have exactly the half factors f_k. The result is
(1/N) sum_k f_k sum_(r+k=J mod2) d(H_+,H_-), as stated. The remaining
periodic first sum must not receive N5-03's physical-edge factor2.
The full defect still satisfies Delta>=Q_v and lambda=S_n-Delta.

## Uniform finite selections

For rho<=1/2, a=(cos(alpha)+cos(beta))/2>=15/16, and the total absolute
sine perturbation is at most1/4. Thus a baseline2/5 yields numerator
at least1/8, and baseline1/2 yields at least7/32. This treats both sine
signs and all reflected orientations without holding either phase fixed.

For endpoint distance s=1,...,4, the displacement of the selected
middle lines is l*pi/n-eta*pi plus or minus (m/n)alpha. Its base
magnitude is at most5*pi/8. Including beta costs at most65/128,
which is strictly less than3*pi/8. Hence b-t<w<b+t strictly, for both
bottom and top constructions. All selected r,k are interior, and the
folded targets remain in [3*pi/10,3*pi/5]. Clearing denominators gives
the stated linear budgets, whose worst n=64 values are pi/2 and2pi.
Both actual baselines, including the top case's 1-minus-cos, exceed2/5.

The bottom parity is r+k=eta=J modulo2, since eta=1-s modulo2.
At the top it is r+k=n+eta=J, since eta=s modulo2 and J=n+s modulo2.
Distinct l give distinct physical second rows. Opposite nonzero
denominators have magnitude at most their cosine span, less than27/m.
Thus each half has magnitude greater than m/216 and each pair defect
greater than m/108. At least n/16 selected rows with weight1/(nm)
give Q_v>1/1728>1/2048. No limiting corner defect is assumed.

For s>=5, gamma=min(phi,pi-phi) exceeds4*pi/n: the required inequality
reduces to n(pi-1/2)>4*pi, valid for all n>=64. Top reflection sends
b to pi-b' and gives exactly cos(gamma+b'),cos(gamma-b'); changes
in actual sine signs are already covered by the absolute perturbation
bound. The shifted first parity grid retains spacing2*pi/n. The chosen
intervals lie strictly inside(0,pi), so none of the infinite-grid
representatives counted there falls outside r=0,...,2n-1.

For gamma<=pi/6, the row band has at least m/12 rows, and the first
interval has at least n*gamma/(4*pi) representatives of either required
parity. Both numerator baselines are at least1/2. The opposite
denominators have span at most2*gamma, hence the pair defect is at
least7/(32*gamma). With weight1/(nm), the total lower bound is
7/(1536*pi)>1/2048.

For gamma>=pi/6, the row count is at least m/16 and the first count
at least n/48. The target span is at most1, giving pair defect at
least7/16 and total at least7/12288>1/2048. All selected intervals
remain strictly separated from their pole targets, including equality
in a band endpoint. At gamma=pi/6 both constructions apply. These
three cases exhaust every stated complementary interior q; q=0,m
remain excluded, as required by their zero-phase zero defect.

## Model margin and strictness

The N1 theorem applies to this subset of its full phase diamond,
including transitions and polynomial collisions. Its upper error bound
gives lambda<M_n+r_n-1/2048. Using pi^4<100, pi^3<32 and H_n<=n,

    r_n < 7/(18 n^4)+56/(225 n^3).

The right side decreases with n; its n=64 value multiplied by524288
is 7/576+112/225=66087/129600<1. Therefore r_n<1/524288. Since
1/2048=256/524288, the final strict deficit is255/524288. The weak
intermediate bounds in the adaptive branches do not lose strictness:
their final floors strictly exceed1/2048.

## Actual independent diagnostic execution

New script [check_n5_two_phase.py](code/check_n5_two_phase.py), SHA-256
`32669967f6bb78909aa5221d04c1ab2ba052797061107b0f822054bc34c96813`.
Actual command:

    python topics/padua-argmax-bridge-20261105/code/check_n5_two_phase.py

The script imports no developer code. Its polynomial oracle is the
finite triangular cosine sum with the exceptional coefficient explicitly
corrected, evaluated using an accumulated second-index sum. At90decimal
digits, the final run passed13 selected-block cases:4near,5small and
4middle. They cover both endpoint orientations, the s4/s5 vicinity,
the closest noncorner charts, inward alpha on the radius boundary,
mixed phases, both sides of gamma=pi/6, and both valid constructions
at that exact transition. No unchanged108-case campaign was repeated.

Three small-degree checks separately compared direct individual physical
cardinal sums against the four-copy periodic formula, and the physical
half-defect formula against the periodic projected defect. These include
both endpoint orientations and an excluded nonnode corner whose defect
is zero. They test normalization identities; no n<64 deficit theorem
is claimed. Exact Fraction checks verify the rational constants.

Largest selected polynomial/quotient discrepancy was5.49818468113e-88;
largest direct-cardinal/normalization discrepancy was2.45454673265e-90.
The smallest selected subset defect was0.011111051507839463. These are
MEASURED diagnostics with comparison tolerance1e-75, not interval proofs
or premises for the uniform theorem. Final process CPU was1.640237821seconds.
Source hashes were checked before and after execution.

One earlier reviewer-harness invocation completed the selected cases
but stopped at the normalization assertion: its interior1/N weight was
accidentally evaluated by Python binary-float division. The reviewer
changed that own weight to mpmath arithmetic and reran the bounded
script successfully. No developer formula, source or theorem changed.
This was a diagnostic-harness correction, not a theorem counterexample.

The7078-byte [independent receipt](evidence/independent-n5-two-phase.json),
SHA-256 `39cc70490f6330b8de65b6db647142eb8d4f01e3a1e36eb29fb1a09f649b2ca2`,
records all16 cases, exact frozen input/script identities, command,
environment and actual final execution. The developer's108-case receipt
was inspected as attributed evidence, not presented as this rerun.

## Limits and disposition

The analytic construction supports N5-04's stated all-n, all-phase
scope with the explicit inherited model-error dependency. Neither the
positive defect nor its model margin bounds the model's own maximum.
Actual corner centers, complete physical-square center coverage,
independently optimized whole-cell E-C, effective onset and PD-T099
remain outside this result. The separate phase-checker n17 replay was
not repeated or used as a premise. All prior reports and production
sources remain untouched. No Git or shared-registry mutation was made.
