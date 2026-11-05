# Supplementary independent mathematical check — P3, P4, P5

2026-11-05. Reviewer: distinct Codex `/root/math_check`, assigned
`gpt-6-astra high` under handoff01. Rules read at
`698802430d333d559668d990123a317f33485064`: AGENTS, WORKFLOW and Codex role.
This is supplementary independent reconstruction of Codex development,
not developer self-approval or the required later Claude substantive audit.
Serving-metadata limitation: [canonical LOG disclosure](LOG.md#2026-11-05--continuation-setup--codex-requested-gpt-6-astra-high).

**Verdict: accepted within the mathematical scope below, with no unresolved
BLOCKING, MAJOR or MINOR mathematical finding.** No developer proof was edited.
P3's protocol history remains subject to the
[canonical timing disclosure](LOG.md#canonical-protocol-disclosure--p3-gate-timing).
Mathematical acceptance does not dispose of that protocol issue.

## Reviewed inputs and boundaries

The review read the full 1,031-line `state/IDEAS.md` in bounded ranges,
recovering truncated portions, including all obstruction and disposition
tables. Closest full candidate entries read were IDEA-133/136/137
(old L1 candidates), IDEA-246/247/248 (drift ideas-e1), and IDEA-414's
original and later SH disposition (frontier ideas-l1-l2). Full nearest
canonical theory reads: PD-T033, PD-T039, PD-T136, PD-T137 and PD-T324.
Read this topic's handoff01, plan, LOG, and P3/P4/P5 gate records. Literature
INDEX's introductory source limitations and relevant initial Padua/product
rows were consulted; no external fulltext was read or used as a premise.
This is a bounded mechanism comparison, with no historical-priority claim.
No exhaustive linked-proof audit of unrelated registry entries is claimed.

The accepted working proof snapshots are identified below by SHA-256;
checkout HEAD during the initial review and first two reruns was the rules
SHA above. Some files were then uncommitted. P3/P5 were subsequently pinned
at published candidate `13c3146d5de3b4b4a23219492476232a7a7155d8`, with
no difference from the reviewed snapshots. The listed P4 working snapshots
include the later definition/transfer/check addenda, also read in full.
All ten listed snapshots subsequently match published candidate
`dbe5c811e0b22498382c8b3a6f2b0f2d9eb66bfc`; the empty scoped diff was checked. These are audit identities, not checker pins of prose.
P3-01's later dated cross-links were read by diff; its admission proof was
unchanged. All ten complete proof records, including the later annulus record below,
were reconstructed.

| File in `theory/` | Reviewed SHA-256 |
|---|---|
| nonproduct-definition.md | a51350193a68a76e507bdeeea40c8874f7d918d650690e323f727c09e2d11ed2 |
| p4-weighted-normal-quotient.md | d06e564fee8ee47585f3d3879d6e23a0c9b688c0cb19bf4575f6abd418e9379f |
| p4-continuous-capacity.md | f3a8b36fd6ec5f56e0090047fe6d983b7eb0912f1706f91344b4282e7290883d |
| p4-moment-capacity-transfer.md | 7525cdcad1e2f048b2847131ac92733cec1d3bce60bc1995280e0be83236de70 |
| p3-01-high-mode-weight-admission.md | e10c58ebdb1278363550c67cf11d6ffc88d9876b12909cb5252ffd669d31b9ba |
| p3-02-exact-moments-creators.md | 711c11648a5fc0020f2079336a8daaecd9a6e62db263a53a61161fd662f876d0 |
| p3-03-uniform-capacity-radius.md | dea9ec5f10e37b287921598d0cbed085dd1b62c2ddaaa0dfa1311df8dcceed18 |
| p5-01-padua-admission.md | 89015d5afd543ca53627bc27f5bf96d6fb003a2cfe66e4b74478454a0f41572c |
| p5-02-padua-polynomial-capacity.md | 302bc2c4fe2ac1bbf5dea64629395ec69659a8eb8b5fc2156e692da5749cb8b7 |
| p4-covariance-capacity-obstruction.md | bb63969874257eda0c6b0e855b2aa686021e9ab683155359eb1c197a2e1004cb |

## Independent reconstruction

### P4: models, normalization and transfer

A full-dimensional compact affine product has a parallelogram hull: the
four factor extrema remain four distinct exposed corners under an
invertible affine map. For a full rectangular grid any putative product
axes must follow the hull edges, so separate coordinate changes and an
exchange are the only possibilities. Thus the positive weight matrix's
rank-one criterion is valid even against arbitrary affine reparametrization.
The triangular-row divisibility proof gives U(n), independently of M>N_n;
nonzero polynomials cannot vanish on an open set of positive density.

In weighted represented coordinates, differentiating the complete
projection leaves the frozen derivative modulo Pi_degree. Normalization
of monic columns contributes exactly D^(-1/2). A unit represented source
coordinate gives the rank-one matrix
sigma_h R e_i [g_kh(z_i)/sqrt(d_k)]_k^T, hence its squared spectral gain is
(1-P_ii) sigma_h^2 sum_k g_kh(z_i)^2/d_k. There is no second node-weight
factor. The Hilbert–Schmidt upper and the row upper both bound the spectral
output, even though neither computes that capacity exactly.

For atomless L2 sources the localization argument is valid without a
smooth density. For each fixed output coefficient vector, unit sources
concentrated on sets of measure tending to zero attain the multiplier's
essential norm while their projection onto the finite-dimensional
polynomial space tends to zero. Absolute continuity of finitely many
integrals of |q_l|^2 supplies the latter step. Taking suprema over source
and output coefficient vectors, with a countable dense output sphere,
justifies the exact max-support singular-value formula. Compact support
makes coordinate multiplication bounded and turns essential supremum
into a maximum for the continuous polynomial response matrix. No
concentration/epsilon limit interchange is needed.

Moment equality through 2n identifies b, d, alpha, sigma and g, but not
ambient orthogonal projectors. The bounded-density argument correctly
compares distances to Pi_n and source norms separately, giving square-root
b/a factors. Atomless equal-support equality and finite cubature's one-way
comparison follow. The explicit three-node triangle rule matches all six
degree-two moments and has zero finite normal space, whereas the continuous
model has positive capacity. This establishes the stated warning; it is
not an admitted M>N_n counterexample and is correctly scoped as such.

### P5: unsaturated Padua capacity

The finite cosine averages are A_r(a)=1 on 2r multiples and zero otherwise,
and the parity average is B_r(a)=1 on a congruent to r modulo 2r. The mixed
parity term first appears at total degree 2m+1, whereas the x marginal
already differs from continuous Chebyshev at degree 2m. Consequently the
two exactness cutoffs, 2m-1 continuous and 2m discrete-product, are distinct
and correct. The positive weights sum to one. The hull proof covers m=1
(triangle), m=2 (pentagon), and every m>=3 (hexagon); a four-vertex affine
product is excluded at every order. For s<m, Gram products are within the
continuous cutoff and injectivity follows.

The normalized Chebyshev pivots are 1/sqrt(2) initially and 1/2 afterward.
An injected chain response is sqrt(2) U_(a-1) at source index 1 and
2 U_(a-c) at source c>=2. BJ's factor p_b(Y) and the transposed mirror
construction each use a source at most once in a given output. On the
actual nodes these factors give C_s=2sqrt(2)(s+1); sigma_h<=1 and two
Cauchy/Frobenius estimates supply exactly C_s(N_s-1), uniformly in m.

The lower survives the actual normal projector: e=T_m(x) has nodal square
one, and its pairing with every degree-s polynomial is a cubature pairing
of degree at most m+s<=2m-1, hence zero. The legal source e/sqrt(2) has
unit relative budget. Its pure-x readouts are one on odd output degrees,
zero on even degrees, proving sqrt(ceil(s/2)). This checks s=1 as well as
m=s+1. A last-column normal source gives the all-fixed-rule floor because
sigma_last>=beta_last>0. Thus the polynomial BJ/best bound is valid without
assuming an upper for alternating/pivot or differentiating switching.

### P3: nonproduct weights and the uniform interval

For m=n+2 the top U_(m-1) mode equals the alternating sign vector. Its
weighted orthogonality to degree<=n polynomials makes the rank-two weight
change invisible through total degree 2n+1; the product of two high modes
first changes the integral at degree 2n+2. Positivity holds precisely on
the displayed open eta interval, and one 2-by-2 minor is 4 eta times a
positive product. Hull edge rigidity excludes any other affine-product
axes. Tensor interpolation gives the required injectivity and dimensions.

The physical leading homogeneous term 2^d x^r(y-2x)^j is triangular in
increasing j, so the stated monic norm 4^-d and normalized creators follow.
All creator/source products lie in the matched moment range. Every pivot
is 1/2; sigma_(n,0)=1/sqrt(2) for n>=2, and mirror's maximum source scale is
sqrt(3/2). In the monic gauge source scaling is 2^(-(d-1)), output scaling
is 2^(-d), and the D^(-1/2) factor cancels the latter exactly.

Most critically, a(s)=U_(n+1)(s) remains a unit normal vector under the
new measure: its norm follows from a^2=1 on the grid, while its pairing
with Pi_n has degree<=2n+1. This does not require all degree-(n+1)
products to stay orthogonal; their pure high-mode cross-pairing is eta.
Injecting e/sqrt(2) at (n,0) produces only final-degree responses, with
successive coefficient -2. Their entire rank-one output is normal and
has squared norm 2(4^(n+1)-1)/3. Mirror's boundary elimination gives the
source coefficient -4 and the latent T recurrence; the subsequent U
responses have disjoint boundary/direct occurrences. Thus its full-source
upper is 2sqrt(6)(n+1)^2(N_n-1), with no eta loss.

Accordingly the original PD-T324 constants extend to every n>=2 and
0<|eta|<1. Eta_0(n)=1/2 is a valid sufficient analytic certificate at
n=2,...,10 and all larger degrees. It is not a maximal radius or strict
small-degree ordering certificate. One fixed eta works, while the mode
and the adversarial source depend on n. No fixed smooth density theorem
is proved.

### P4 added fixed-covariance obstruction

The additional annulus theorem is accepted at its degree-two absolute
capacity scope. With tau=epsilon^2, polar area measure makes R^2 uniform,
so the radial fourth moment is 1+tau/3 and the displayed second/fourth
moments follow. Direct Gram subtraction gives last latent norm
tau(3+tau)/(9(1+tau)). Triangular shearing scales the physical last column
by lambda^2, and its unique parent is lambda T, giving raw squared source
scale lambda^2(c^2+3lambda^2)(3+tau)/24. Their ratio is exactly the claimed
3(c^2+3lambda^2)(1+tau)/(8lambda^2 tau). A free unit normal L2 function
exists because the atomless ambient space is infinite-dimensional. This
last-column witness works for every admissible rule; it does not imply
any BJ/comparator ratio separation. Positive annular width ensures U(n)
and an elliptic, non-parallelogram hull; epsilon=1 remains a valid disk.
For c=1,lambda=2 the covariance eigenvalues are (3+-sqrt(5))/2 and both
physical axes have fixed nonzero principal-axis angles. Thus covariance
and angles alone cannot give a finite absolute capacity upper. The
epsilon=0 recurrence is correctly excluded.

I also read the added P4-04 candidate and its recorded gate/test conditions.
This is a counterexample to the stated finite-degree quantitative
submechanism, not a passed cross-family criterion or an all-degree ratio
iff obstruction.

## Actually executed independent reruns

I inspected all three checker implementations, then executed each separately
from the developer's run. Commands from `/workspace/padua_research`:

```text
python3 topics/padua-lanczos-nonproduct-20261105/code/p5_exact_checks.py --output /tmp/padua-lanczos-nonproduct-20261105/math-review/p5-exact-checks.json
python3 topics/padua-lanczos-nonproduct-20261105/code/p4_weighted_check.py --output /tmp/padua-lanczos-nonproduct-20261105/math-review/p4-weighted-check.json
python3 topics/padua-lanczos-nonproduct-20261105/code/p4_annulus_check.py > /tmp/padua-lanczos-nonproduct-20261105/math-review/p4-annulus-check.json
```

All three returned exit 0 and PASS. P5: m=2,3,4,5, 122 cubature moments, four
sharp-cutoff failures, 202 Gram entries, 60 creators, 20 normal-readout
squares, 124 full-projection derivative directions at m=2,3, and 44
symbolic identities through degree eight. P4: 370 derivative/source
coordinate directions, BJ/mirror at degrees two and three on positive
rational triangular weights. P4 annulus: eight exact radial/angular
moment and physical Gram cases at epsilon=1,1/2,1/4,1/8, c=0/1,lambda=2.
Fresh output matched developer receipts
exactly, after removing only P5's runtime field. P4's literal inherited
`independent_rerun: NOT CLAIMED` field describes the checker author's
receipt; this record establishes the separate reviewer execution.

[Compact rerun receipt](evidence/check-math-reruns.json) records commands,
code SHA-256, fresh output paths/hashes/sizes, deterministic inputs,
Python 3.12.14, SymPy 1.14.0 and platform. These are separate-agent reruns
of developer code, not independently authored replacements. The dual
calculation and frozen response are distinct internal arithmetic paths.
No new P3 numerical execution is claimed; its result was checked by
analytic reconstruction. No finite test is a reduction of an all-degree
theorem. Regenerable outputs stay local; archival availability is not a
premise of these analytic proofs.

## Residual scope and follow-up

No mathematical correction was requested. This check does not cover
P1/P2 proofs, P6 scan endpoints/fits,
registry application, final IDs, a complete protocol audit, or PR readiness.
It does not establish N2 or the P4 prescribed cross-family criterion gate.
Capacity remains worst-case first-order aggregate spectral output under
fixed parents and exact full projection. IEEE/scalar activation, uniform
finite-epsilon remainders, sharp growth exponents, and unrestricted adaptive
switching remain outside the accepted statements. The required Claude
substantive audit and any material post-snapshot change remain to be reviewed.

## Focused round-3 addendum — terminal-degree block

2026-11-05, same distinct reviewer and allocation. **Accepted with no
unresolved mathematical finding.** This adds only the stable terminal-degree
corollary and its check to the scope above. The scoped diff against
`dbe5c811e0b22498382c8b3a6f2b0f2d9eb66bfc` adds the corollary, check
metadata and history; the earlier quotient proof is unchanged. Rules are
unchanged. Read the new P4 delta-gate and corresponding candidate refinement.
The accepted working snapshot of `theory/p4-weighted-normal-quotient.md`
has SHA-256 `f7f53733aab8a71814836900433e6861701d1d74b59d3552b3e0835e7d7b820a`; this supersedes that file's earlier hash for
this focused mathematical addition only.

Independent derivation: zero earlier sources imply zero earlier responses
by causality. Every terminal parent lies in degree s-1, so all coordinate
multiplication terms vanish. The only remaining terms are the scalar
within-degree subtractions, giving A V=f with A unit lower triangular and
G=A^(-1). For represented or function-coordinate sources f_h=sigma_h u_h,
the source norm is exactly the Hilbert–Schmidt norm of the column operator
U. Column normalization divides output column k by sqrt(d_k); hence
W=R_s U S_T^(1/2) G^T D_T^(-1/2)=R_s U M_T^T. The upper follows from
||R_s||<=1 and ||U||_2<=||U||_HS. If a unit normal e exists, choose U=e v^T
with v a unit right maximizing singular vector of M_T. Then ||U||_HS=1
and W=e(M_T v)^T attains ||M_T||_2 exactly. Substituting
r=S_T^(1/2)v produces the displayed generalized Rayleigh quotient.
All sigma,d are positive, so this substitution is invertible. The
zero-normal-space exception and the restriction to exactly terminal
sources are essential and correctly retained. The argument works in a
compact L2 model with atoms as well as without them, provided U(s) and a
nonzero normal space hold; no localization argument is needed here.

This is routine finite-dimensional algebra from the already accepted
normal quotient and common-normal witness. Consolidating it in the
weighted record without a new result ID is appropriate. It supplies a
restricted capacity, hence an all-source lower only; it establishes no
all-source upper, family growth rate, or coordinate-invariant classifier.

Actually executed separately from the developer, from repository root:

```text
python3 topics/padua-lanczos-nonproduct-20261105/code/p4_terminal_check.py > /tmp/padua-lanczos-nonproduct-20261105/math-review/p4-terminal-check.json
```

Exit 0; all 22 exact source vectors PASS across the four degree-2/3,
BJ/mirror weighted-triangle cases. Fresh output is identical to the
developer receipt. Code was inspected: the new simultaneous-source full
projection differentiation is compared to a constant triangular solve;
function-value budgets include their weighted L2 norms. All tested
outputs are collinear with one normal vector, justifying spectral equals
Frobenius in the arithmetic check. No singular-value maximum was computed;
its exact attainment was reconstructed analytically. The updated
[rerun receipt](evidence/check-math-reruns.json) pins this script, its
`p4_weighted_check.py` dependency, inputs and fresh output identity.
The required Claude audit and original scope/protocol limits remain.
