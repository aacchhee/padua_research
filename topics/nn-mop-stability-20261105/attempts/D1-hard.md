# D1-hard — decisive all-N lower law and G3 obstruction

Developer: Codex, requested gpt-6-astra ultra under handoff01 for the decisive
all-N conditioning step; justification recorded by coordinator in LOG.
Rules/source: 823cf6a4ef7c01b4ef3d2a6fec3e9f19d4b4f6f1.
Main/base: b4d292eea5eed373002506d5e16a3761bd7ae10e.
Ownership: only D1-hard attempt/gate, conditioning-lower theory and
conditioning_lower code files. No Git or shared-file writes.

## Outcome

Written analytic PROVED result, pending mandatory Claude audit:
[conditioning-lower-krawtchouk.md](../theory/conditioning-lower-krawtchouk.md).
For M=N−1>=1 and the exact requested Krawtchouk parameters,

    kappa_N >= 5^M/M,
    kappa_N >= (4sqrt(6))^M/[4M(M−1)],                 M>=2,
    kappa_N >= 5/(2M^2)[(5+2sqrt(6))^(M−1)
                         +(5−2sqrt(6))^(M−1)],        M>=1.

Thus liminf kappa_N^(1/N)>=5+2sqrt(6)>9.89. These are exact inequalities,
not fits. The first bound comes from one near-axis mixed polynomial; the
stronger bounds use all terminal mixed polynomials. Every bound is attained
or bounded below by an explicit second-weight parity direction with zero
mass and fixed nodes. The full coefficient field scale is proved exactly.
The original sharp-rate/matching-upper-bound target remains OPEN.

The coordinator's normalized-parity continuation also yields the PROVED
scoped negative result
[conditioning-lower-proximity.md](../theory/conditioning-lower-proximity.md).
At each fixed N>=4, p1=2/5,p2=q=2/5+delta<=1/2,

    kappa_N(delta) d_min >=20q^M/[M^2 delta^(M−2)]→infinity.

This disproves kappa=O(1/d_min) as the two measures approach proportionality
in this family and metric. It upgrades the finite G3 concern to a specific
analytic obstruction while preserving the original prediction. Nothing is
asserted for Hahn or at the singular endpoint delta=0.

## Derivation and retained routes

Prospective full registry/obstruction gate:
[novelty-gate-D1-hard.md](../novelty-gate-D1-hard.md). No new primary source
was opened or cited, and no historical novelty claim is made.

The first successful route uses the scalar generating function to annihilate
all degrees below M with an alternating binomial direction. The stronger
route encodes terminal polynomial values by H(z), whose constraints become
zeros at the weight-ratio points 2/3 and1. Its differentiated Hermite jets
reduce exactly to positive coefficients. Central binomial averaging proves
the base4sqrt(6) bound; summing across all terminal pairs proves the stronger
base5+2sqrt(6) bound. The weaker successful route is retained, not rejected.
No matching upper bound was attempted after these bounded improvements;
that remains a separate open task, as does actual-rounding activation.

## Executed developer diagnostic

Command from the snapshot root:

```bash
python3 topics/nn-mop-stability-20261105/code/conditioning_lower_witness.py --sizes 2 3 4 6 8 12 --dps 120 > /tmp/conditioning-lower-witness-120.json
```

Returned exit0. Python3.12.14, mpmath1.3.0, elapsed wall0.881seconds; no
randomness. All29 terminal sites with m>=1 were checked. Maximum derivative
error normalized by max(1,|exact derivative|): 9.85182e-110. Maximum b2
field-scale discrepancy: 7.44279e-114. AtN2 the directional identity was
exact at the working precision. This is floating AD evaluation of the
pre-existing NN map versus an exact rational formula, not an interval
certificate or a computer-proof premise.

| Artifact | SHA256 | Bytes / role |
|---|---|---|
| code/conditioning_lower_witness.py | 36669d041d945bb6f36ceca0962d787dd99bd18dc21d1ac6e3c65ddb1c19a279 | Reproducible diagnostic driver |
| Imported code/conditioning.py | 11c4b49be8541697e74d383b908db47b42480e11c60f92c35821340eacea929c | Existing analytic AD implementation |
| Frozen predecessor code/c4_float_baseline.py | 9ce76ae88fb798f73127f75819bcdfb6c7bffb0d9cd092d70957164cb9b6a2e8 | Exact family input generator |
| /tmp/conditioning-lower-witness-120.json | dab3df3bbb65b3e2fbfd56394e6f863003444297414e438c7c6fc6b71f81df5c | 6797bytes; local temporary output, archival pending |

The JSON preserves each exact input hash and every checked terminal row.
It is regenerable; no unrelated cold-storage destination was invented.

## Supplementary checks and freezes

The distinct D1 worker independently checked the written initial proof,
including the jet reduction, sign factors, formal substitution and central
bound. It also executed a separate AD diagnostic at N3,4,6,8,12,120dps,
all28 terminal sites, with maximum scaled discrepancy9.85182e-110:

```bash
python3 topics/nn-mop-stability-20261105/code/conditioning_parity_check.py --sizes 3 4 6 8 12 --dps 120 > /tmp/conditioning-parity-check120.json
```

Driver SHAaea27c7d601758a2c5a29bbc17f73e22099435bf8f7bc2f5f65d1a9e2ed0a3bd;
output SHAb10fc817ffcf5db872facba41fbc9bc3627c68b84757264dfd495a0e4225c7a0.
This uses the same underlying AD graph and is not an independent exact
moment implementation.

The separate Astra independent-check worker executed a Fraction direct
mixed-moment Jacobian replay at N2,3,4,6,8, checking every terminal response,
both b fields, exact mass zero, exact b2 field scale, weaker axis bound and
the squared central lower bound. It reviewed the initial proof and found
no flaw. Its final report records exact commands and hashes; the sharper
summation addendum and proximity theorem were submitted for separate
recheck before publication. These checks do not replace Claude audit.

Final theory freezes sent to the independent worker:

- conditioning-lower-krawtchouk.md:
  9047c95c8bc8b6ca6ecb0dae5eab6ff1517be428bee501c9f16ee2bff164c53e.
- conditioning-lower-proximity.md:
  c8939f19ad9f3504375d67b58db5171f1ee545a459d8816145048680dd62e4ca.

Initial lower-proof hash before the dated summation addendum:
409f625a57d6c0e004781f666ef35f71fbcd25b447f0cc5c938da74d77340b0f.
No theorem depends on the finite computations. Pending final supplementary
receipt links and mandatory Claude audit are administration/verification,
not missing steps in the written analytic proof.

Final supplementary completion: the independent worker reviewed both final
theory freezes above and found no flaw. It separately checked the exact
Q-sum recurrence for L=0,...,30 and replayed the proximity witness at N4
for delta=1/10,1/20,1/40 and at N6 for delta=1/20; every exact check passed.
Report: [independent-checks-02.md](../independent-checks-02.md), parity and
proximity sections (other directions in that report may still be pending).
Executed commands, independently reported:

```bash
python topics/nn-mop-stability-20261105/code/independent_check_followup_parity.py > /tmp/nn-mop-independent-parity-final.json
python topics/nn-mop-stability-20261105/code/independent_check_followup_proximity.py > /tmp/nn-mop-independent-proximity.json
```

| Independent artifact | SHA256 | Bytes |
|---|---|---|
| code/independent_check_followup_parity.py | ba31d832f875ca52a11bb8866ae8027da367ab87946d2e2cb3d0650645c060a4 | Code |
| /tmp/nn-mop-independent-parity-final.json | 3308cd745d9790d3d7200adbc5acaf06ab8d830308b3634cf4cbc2d57d0fd806 | 7456 |
| code/independent_check_followup_proximity.py | b2d860fe2e76891cfb5fb6174b4f988f3bda875e0df90b35b896e2689f029fd8 | Code |
| /tmp/nn-mop-independent-proximity.json | 755a0d36d3d65c088c2297e411d443fab96a9a10bf4dd8a27266a25bd158e9f6 | 1537 |
