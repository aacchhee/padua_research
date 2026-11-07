# Independent supplement: N5 all-edge defect

2026-11-05. Distinct Codex `/root/check_rows`, coordinator-assigned
gpt-6-astra high; serving metadata not independently exposed. Rules read
at `3dda890275a7599caa707b0fb8c0b6e6f6a80643`. This is supplementary
mathematical review, not the required Claude audit. No developer file,
previous checker artifact, shared registry or Git state was edited.

## Disposition and frozen inputs

**PASS at the stated scope.** For every n>=64, either physical vertical
endpoint, every interior complementary q and every |s|<=1/2, the proof
establishes the strict actual-function defect >1/1024 and consequently
the strict cotangent-model margin >511/524288. No mathematical blocker
or required correction was found.

Reviewed frozen files (SHA-256):

- `theory/N5-all-edge-defect.md`:
  `1c1492b50b9ab89b9a94d88a01caccc889d4547df677210152b91521a2df6fda`
- `code/n5_all_edge_defect.py`:
  `81ebfb554c297fd444ca2bfa8e6c50459538a3e81949fa32543532a220922381`
- `evidence/n5-all-edge-defect.json`:
  `5a3697a540fda6dd096d3e971714f70bddbae9078ebb9de8d219a902e72ac471`

All three were pinned before and after the independent diagnostic.
The all-edge theorem and candidate record were read in full, as were the
central-edge predecessor and its proof; N1's model statement/interface
was rechecked against the earlier independent N1/N5 reconstruction.
The finite-block method is inherited; this is a domain/constants variant,
not an external historical-priority or novelty certification.

## Independent reconstruction

The corrected polynomial identity can be checked without importing the
central-strip estimate. Write x=cos u, y=cos v, P=T_(n+1)+T_n and
D=[P(y)-P(x)]/(y-x), continued polynomially on the diagonal. For the
reflected grid r, tau=(-1)^r and P(x)=tau*(1+x). Complementarity and
physical parity give tau*(-1)^(q+k)=-1. Since m v=(q +/- k)pi+s,

    P(y)=(-1)^(q+k)*[cos s*(1+y)+sin s*sin v].

Substitution into (tau D-1)/2 gives precisely

    [cos^2(s/2)*(1+y)+(sin s/2)*sin v]/(x-y).

Here `(sin s/2)` denotes sin(s) divided by2. The exceptional highest
mode remains in x. Multiplying the corrected actual cardinal by tau
preserves its absolute value and yields the sum of these two halves.
The triangle defect is therefore nonnegative pointwise. Reflecting the
first grid and unfolding q+k,q-k modulo2m gives the odd periodic board,
because r+q+k is odd. Physical endpoint factors supply exactly the fold
multiplicities. Thus the physical two-copy primitive is the same S_n(0,s)
as in N1, with no discarded factor2. Collisions in the total identity
remain polynomial values; every selected lower-bound term is regular.

For |s|<=1/2, A>=15/16 and |B|<=1/4. Consequently a baseline
1+cos v>=2/5 gives numerator>=1/8; a baseline>=1/2 gives>=7/32.
These bounds use |sin v|<=1 and hence apply to both phase signs and
both reflected sine orientations.

### Endpoint-distance a=1,2,3,4

For l in [3n/8,n/2], the displacement formula
m(w-b)=l*pi/n-eta*pi has magnitude<=5pi/8. The separation
m*t>=pi-1/2>5pi/8 forces b-t<w<b+t. At the top endpoint the actual
cosines are their negatives, so the strict interlacing still holds;
its numerator baseline is correctly 1-minus-cos rather than 1-plus-cos.

The target band [3pi/10,3pi/5] follows by clearing the two denominators.
The resulting budgets are (3n/40-43/10)pi>=1/2 and
(n/10-22/5)pi>=1/2; at n64 their left sides are pi/2 and2pi, and
both increase with n. On that band both 1-cos and1+cos exceed2/5.
In particular sin(pi/5)^2=(5-sqrt5)/8<7/20<9/25, while the other
end lies below2pi/3. Thus both actual numerators exceed or meet1/8.

The denominator span is <=2t<27/m, since2mt<=8pi+1<27.
Each half therefore has magnitude>m/216 and the opposite signs give
point defect>m/108. The reflected parity is r+k=eta=J at the bottom;
at the top it is n+eta=J, since eta=a mod2. Thus every selected pair
is an interior physical checkerboard point with weight2/(nm), for either
epsilon. There are at least n/8-1>=n/16 selected l, all in distinct
second rows. The resulting defect is strictly >1/864>1/1024.

### Far-center branches and their meeting point

For a>=5, gamma=min(phi,pi-phi) is >(4pi/n). This follows from
n(pi-1/2)>4pi and holds uniformly from n64 onward. Reflecting the
physical second coordinate when phi>pi/2 gives exactly the target
cosines cos(gamma+b'),cos(gamma-b'); it changes sine signs only, already
allowed in the numerator estimate.

For gamma<=pi/6, choose b' in[pi/3,pi/2] and a first interval of length
gamma centered at b'. Its closure lies strictly between the target
angles and within(0,pi). Both numerator baselines are>=1/2 and the
cosine span is<=2gamma. The defect per point is at least7/(32gamma).
The second-row count is>=m/12; either first parity has at least
n gamma/(2pi)-1>=n gamma/(4pi) points. Multiplying the physical weight
gives7/(768pi)>1/1024.

For gamma>=pi/6, choose b' in[pi/12,pi/6] and the first interval of
length b' centered at gamma. Its endpoints remain separated from the
targets by b'/2; even when gamma=b'=pi/6 the lower target0 is not a
selected first angle. The cosine span is<=2sin(gamma)sin(b')<=1,
so the defect per point is>=7/16. The row and first-parity counts are
respectively>=m/12-1>=m/16 and>=n/24-1>=n/48. Thus the total defect
is>=7/6144>1/1024. Both selections are valid at gamma=pi/6.
All these counts are for interior points, so no endpoint half-weight
or forbidden parity can dilute the displayed estimates.

These three cases exhaust the complementary interior q. The proof does
not take a limiting value from a corner or assume a positive defect
at a nonnode corner center.

### Model error and strictness

The previous N1 theorem applies because (0,s) lies in its full phase
diamond, including transition/collision phases. Its error is exactly
r_n=[7pi^4/1800+7pi^3 H_n/900]/n^4. Using pi^4<100, pi^3<32 and
H_n<=n gives r_n<7/(18n^4)+56/(225n^3). This bound decreases with n.
At n64 its product with524288 is

    7/576+112/225=66087/129600<1.

Thus r_n<1/524288, and subtracting it from1/1024 leaves the stated
511/524288 strict margin. The theorem's strict inequalities are justified
also in the two branches whose intermediate defect estimates are weak
inequalities, because each final case floor strictly exceeds1/1024.

## Targeted independent diagnostics

New checker: [code/check_n5_all_edge.py](code/check_n5_all_edge.py), SHA-256
`cf55ccbf3e8c9b76f9ddc32c4edb6cc3a52532442bfaf612aebb3ccce3ad7abb`.
Actual command:

    python topics/padua-argmax-bridge-20261105/code/check_n5_all_edge.py

The checker imports no author code. It computes the finite kernel using
polynomial divided differences through the independent recurrence

    d_0=0, d_1=1,
    d_(k+1)=2y*d_k+2T_k(x)-d_(k-1),
    D_n=d_(n+1)+d_n.

This recurrence has no division and is valid on the diagonal as well.
It is compared with the reviewed quotient only at the selected regular
points. Exact Fraction checks cover the finite rational budgets; the
transcendental diagnostics use mpmath at100 decimal digits and are
**MEASURED checks, not rigorous interval proof premises**.

Twenty-three targeted cases passed:14 near-endpoint,6 far-small and3
far-middle. They include q1 and q=m-1 where admissible, their closest
admissible partners under the other parity, the a4/a5 change, and
n65,m66,q11 and q55 at s=-1/2,0,+1/2 across the exact gamma=pi/6
transition. The central gamma=pi/2 case is also included. No complete
unchanged degree/phase sweep was repeated.

All tested parities, interior weights, row counts, numerator floors,
strict denominator signs and selected-defect case floors passed. The
smallest selected-defect/case-floor ratio was approximately18.07875;
the largest polynomial/quotient discrepancy was6.732195735e-98.
The independent receipt contains the23 cases and exact frozen pins:
[evidence/independent-n5-all-edge.json](evidence/independent-n5-all-edge.json),
10778 bytes, SHA-256
`8a06ffeb853d9f2856e59fad549ec3ec6a3d1d141bd069771ea5bdb75ff1371a`.

The analytic proof, not those finite diagnostics, establishes all n>=64
and every |s|<=1/2. The result does not bound the primitive/model's own
maximum, include nonnode corner centers, enlarge the phase window,
compare independently optimized whole cells, or settle E-C/PD-T099.
No unresolved finding remains within the reviewed statement.
