# PD-T?padua-3d-20261106-codex-T8-r08-01 — exact cubic half-shift classification

ID kind: PD-T. Aliases: M40 half-shift survivors; exact cubic DCT rank census;
coefficient determinant tie. Split from: none. Split into: none.

## Statement and assumptions

Set n=3,N20,M40 and X_z={cos(2pi(2k+1)z/80):0<=k<40}, with z=(1,b,c),
1<=b<c<40. Among these741 parameter triples, exactly the following eight
have Pi_3-unisolvent20-node images:

    (1,4,11), (1,4,29), (1,6,15), (1,6,25),
    (1,11,36), (1,15,34), (1,25,34), (1,29,36).

All eight have equal absolute product-Chebyshev evaluation determinant.
Thus the preregistered determinant objective with lexicographic ties selects
(1,4,11). This counts parameter triples, not equivalence classes under
coordinate reflection/permutation. No other phase, modulus or generator
class is classified.

## Status by part

Overall status: **PROVED**, computer-assisted finite classification with
an explicit exact reduction, independently executed full census and essential
small evidence. This is a material new finite result for focused Claude re-audit.
No floating quality or global norm statement is proved here.

## Definitions and finite reduction

Let theta_k=(2k+1)pi/M for k0,...,N-1; by the first-coordinate fold argument
in PD-N?padua-3d-20261106-codex-T8-r08-01 these are one representative from
each physical node. Let B_(k,r)=cos(r theta_k),0<=r<N. Elementary discrete
cosine orthogonality gives B^T B=diag(N,N/2,...,N/2), hence B is invertible.
For example orthogonality follows by summing exp(iq theta_k), taking real
parts, and applying2cosu cosv=cos(u-v)+cos(u+v).

For each multi-index alpha with|alpha|<=n, expand

    product_j T_(alpha_j)(cos(z_j theta))
       = (1/8) sum_(eps in{+1,-1}^3) cos((eps*alpha) dot z theta).

Reduce the integer frequency m modulo2M to r in[0,M] by r=min(m,2M-m).
At theta_k, cos(M theta_k)=-1 and sin(M theta_k)=0, so if r>N replace r
by M-r and negate its coefficient. The r=N term vanishes because
cos(N theta_k)=cos((k+1/2)pi)=0. Summing the eight signs forms an integer
N-by-N matrix C_z with V_z=B C_z/8. Therefore real rank(V_z)=rank_Q(C_z).
Exact rational elimination decides deficiencies as well as positive ranks;
no deficient modular rank is used to prove singularity.

## Computer proof and checks

Independent checker [t8_r08_check.py](../code/t8_r08_check.py) builds C_z
from the formula, computes exact rational rank for all741pairs and verifies
actual-node monomial ranks at two fresh splitting primes for all741.
Its complete finite rank histogram is:

| rank | count | rank | count |
|---:|---:|---:|---:|
|4|3|7|21|
|9|35|10|82|
|12|52|13|8|
|14|40|15|132|
|16|64|17|188|
|18|48|19|60|
|20|8|||

The counts sum to741. The producer initially found the same eight positive
triples by actual-node modular determinants, which alone did not prove the
negative cases. The independent exact C-rank calculation supplies that
missing upper bound. Its essential receipt is
[t8-r08-check-census.json](../evidence/t8-r08-check-census.json); raw complete
rank rows are local regenerate-only with full path/size/hash in that receipt.
The whole finite universe and code are committed, so no missing bulk table
is required to reconstruct the proof.

Independent checked-division Bareiss gives|det C_z|=562949953421312=2^49
for all8survivors. The correction runner independently recomputes exact
cubic determinants on all380trace-permitted pairs; the other361 are
excluded by the analytic trace theorem. It finds exactly8nonzero C
determinants, all2^49. Since B and the product-Chebyshev orthonormal column
scalings are common to all z, all8exact objectives tie. See
[t8_r08_tie_correction.py](../code/t8_r08_tie_correction.py) and the
[corrected execution](../evidence/t8-r08-halfshift-corrected.json).
The original numerical tie failure and its correction are recorded once
in [the attempt](../attempts/T8-round08.md).

## Reproduction and trusted dependencies

From repository root, with Python3.12,numpy2.3.5,scipy1.17.0,sympy1.14.0:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/t8_r08_tie_correction.py --receipt /tmp/t8-r08-corrected-replay.json

Independent commands are in
[independent-checks-round08-t8.md](../independent-checks-round08-t8.md).
Trust Python arbitrary-integer arithmetic and the independently implemented
rational/Bareiss eliminations; the positive modular cross-check additionally
trusts NumPy guarded int64 arithmetic and deterministic prime/root checks.
The reduction and coverage are explicit, not a source-reported theorem.

## Sources, scope and history

No external theorem dependency; known Fourier/cosine aliasing mechanism.
Gate/source coverage: [round08 gate](../novelty-gate-T8-round08.md).
This finite classification gives no asymptotic norm bound or degree-uniform
construction. New degrees5/7 are separate finite positive certificates and
MEASURED quality; even degrees are excluded by the separate hand proof.
2026-11-06,Codex assigned gpt-6.1-sol xhigh, rules9042e1c. Audit03 supplied
the cubic lead; root preregistration gate69694f3 preceded these executions.
