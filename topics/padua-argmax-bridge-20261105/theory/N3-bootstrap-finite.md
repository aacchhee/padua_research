# PD-T?argmax-bridge-codex-N3-bootstrap-02 — Finite energy premise for the maximum bootstrap, n2–128

ID kind: PD-T.
Aliases: N3 round7 finite bootstrap energy; three-quarter weighted
corner energy; fixed127-degree helper.
Split from: none; finite implementation of the energy premise in
N3-bootstrap-corner.md, itself a quantitative IDEA330/457 continuation.
Split into: none. Uniform all-n energy remains a separate OPEN target.

## Statement

For every integer n with 2<=n<=128, let Lambda_c and W_n be the
exact corner mass and physical weighted gradient energy of PD-T227
for the even-checkerboard PD-T101 cardinals. Then

    W_n <= (3/4)*n^4*Lambda_c.                         (F)

It transfers to the other parity-correct nonnode corner by the
inherited node/weight reflection. In particular (F) supplies hypothesis
(E) of N3-bootstrap-corner.md on this
finite range. That analytic result excludes noncorner global maximizers
on the half-phase corner patches; a strict complement cover is still
needed for global equality. No unconditional pointwise corner predicate
or global degree certificate is asserted here.

## Definitions and assumptions

At c=(-1,-1),

    W_n=sum_(L_jk(c)!=0)
        [L_jk,x(c)^2+L_jk,y(c)^2]/|L_jk(c)|.

The removable00 index is retained. Precisely k=0,j>0 even are
omitted from W, while their inward first-variation contributions
remain included in PD-T227 and PD-T251. All derivatives are physical,
with n^4 normalization, not angular derivatives or a squared sum of
absolute gradients.

The unchanged producer uses correctly rounded MPFR4.2.2 pi/cos and
basic interval arithmetic at256 bits, GMP6.3.0 exact rational
conversion, and the recorded compiler/runtime. These are explicit
trusted dependencies of its outward endpoints. A separate GMP integer
interval reconstruction, freshly executed for the new threshold, is
required before this finite computer claim is accepted as PROVED; that
distinct fresh reconstruction has now completed successfully, as recorded
below. The accepted independent proof uses GMP interval arithmetic and
its own Machin/Taylor enclosures, without an MPFR dependency.

## Status by part

Overall status: **PROVED**, computer-assisted finite verification by the
written reduction and distinct fresh GMP reconstruction of the new
threshold for all127 integers. The initial producer launch was
CONDITIONAL; the dated disposition below records the separate execution
that discharges this obligation. The old accepted kappa replay is not
reused as certification of (F). Required Claude audit remains separate.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| Exact implication from valid endpoints and (R) to (F) | PROVED routine reduction | Algebra below |
| Full finite energy assertion (F) | PROVED | Fresh unchanged MPFR127-case producer and distinct fresh GMP new-threshold reconstruction both pass |
| All-n version for every n>=2 | OPEN external target | No extrapolation from this finite range |
| Maximum-cover reduction under the energy premise | Separate PROVED analytic theorem | N3-bootstrap-corner.md |

Candidate disposition: retained bounded quantitative helper under
IDEA?argmax-bridge-codex-N3-bootstrap-01. No new energy arithmetic,
historical novelty or priority claim.

## Depends on and finite reduction

PD-T227 supplies the exact values, physical gradients, zero mask and
removable formulas. The existing outward-algorithm proof in
N3-corner-bounds.md applies to the unchanged C source, not just its old
radius threshold. For each integer n2..128 reconstruct rational
endpoints satisfying

    0<ell<=Lambda_c,
    W_n<=E,
    4E<=3*n^4*ell.                                   (R)

Then W_n<=E<=(3/4)n^4ell<=(3/4)n^4Lambda_c, proving (F).
The factor4, not a factor2 or an old kappa condition, is required.
No global norm upper bound u or K=u/ell is used in this implication.

For completeness the unchanged producer encloses every node cosine
by directed pi/cos, assigns1,-1,0 exactly at known endpoints/midpoints,
and uses outward basic interval operations throughout. At a regular
nonzero cardinal, it evaluates the exact normalized PD-T227 gradients
q_x,q_y and mass V=2w(1-b)/|b-a|, with strict denominator-sign guards.
It sums V(q_x^2+q_y^2) and V. The removable00 case is separate, and
the exact zero row is omitted before division. Thus its lower mass
ell and upper energy E are valid enclosures under the declared MPFR
dependencies. The new wrapper performs (R) with exact Fraction
arithmetic; no binary64 value enters acceptance.

## Executed producer and evidence

All old source-identified MPFR and GMP endpoint comparisons passed
the new threshold before fresh execution. Those were only cheap
countertests. The new wrapper then compiled exactly the frozen C
bytes and executed each n2..128 once at256 bits. Every degree passed
(R):127 requested, attempted, completed and passed, zero failures,
zero process/arithmetic errors and no unrun degree. The count totals
are362045 nonzero contributions and4096 exact zero-cardinal omissions.
The n2 control enclosed Lambda_c=3 and W_2=331/18.

The largest certified E/(n^4ell) occurs at n2 and is the exact fraction

    66540245724916077578475687565756419269847855771401088015729965810102857484127
    /173688133855974293135356477513031861779904976998460846059186376011869694459888,

which is strictly below3/4. Its decimal diagnostic is approximately
0.38310185185185186. The fixed threshold was not changed after this
observation. These finite endpoints supply no uniform all-n premise.

Actual command from the repository root:

```sh
python topics/padua-argmax-bridge-20261105/code/n3_bootstrap_energy.py --output-dir local-output/argmax-bridge-20261105/N3-bootstrap/r01 --mpfr-include local-output/argmax-bridge-20261105/N3/runtime/extracted/usr/include --receipt topics/padua-argmax-bridge-20261105/evidence/n3-bootstrap-energy.json
```

The one fresh sweep used5.048074 total child CPU seconds, including
compiler/helper commands, below its1200-second cap. Summed native
timing was4.468347 seconds; wall time5.229233 seconds. These timings
are measurements, not proof predicates. Python3.12.14, MPFR4.2.2,
GMP6.3.0; no seed. Exact argv, source/header/compiler/runtime identities,
per-degree stdout hashes/CPU and counters are retained in the receipt
and its local raw JSONL. Source and wrapper identities were rechecked
after the run. No energy-source edit, retry, extra degree, adaptive
threshold or phase-source/checker change occurred.

Essential aggregate receipt: ../evidence/n3-bootstrap-energy.json,
8664bytes, SHA256
077294e96a336553f8355e2a2d097b4527622f96dbabd9fa94b86eaa1879e16c.
Wrapper: ../code/n3_bootstrap_energy.py,13788bytes, SHA256
5680d6b1688114a423cb4c692f2e253216d9e0ab40ef9bf2b0df94c986bb5587.
Unchanged C source: ../code/n3_corner_bounds.c, SHA256
a0497ca1219850e28f2bf51e72cb4fc8f78cde238b81fd678262d646511402bd.
Full raw endpoints remain local and regenerable; no cold-storage
retrieval is required as a unique proof input. The accepted independent
path must reconstruct the finite sums from integer n.

## Independent reconstruction and scope

The root assigned a distinct fresh reconstruction of every integer
n2..128 using unchanged GMP checker source
../code/check_corner_exact.cpp, SHA256
3646f4e8b6b16957b9e1114f95ad2f0a7c18eec4687b49d5e6f1947a25eea6e3.
The separate checker actually compiled that source freshly and executed
every integer n2..128 once. It tested4E_own<=3n^4ell_own from its own
valid intervals, the mask/count and n2 controls, all native exits, source
identities and exact complete coverage. No producer endpoint or old
kappa receipt supplied the new predicate. All127 cases passed, with no
failed, partial or unexecuted case counted. The checker also independently
accepted the frozen analytic bootstrap proof at its stated scope.

The complete report is ../independent-checks-bootstrap.md; essential
independent receipt ../evidence/independent-bootstrap-energy.json,
3190bytes,SHA256
f0c48ea7f55e3a926b36537ebe46724b4305cacb9f1254c6417b2abd9676425b.
The separate collector ../code/check_bootstrap_energy.py has SHA256
915c6c7c40e8c9e0c748cf50c2fe278f6760d79a9e725939aed1553269030972.
It imports no producer module or endpoints. Its GMP512-bit interval
path uses rational Machin pi and cosine Taylor error bounds, with the
expanded physical PD-T227 gradients, and the already corrected GMP
canonicalization contract. These differ from the producer's MPFR
normalized-gradient path. Trusted dependencies are the proved formulas,
GMP exact arithmetic, the recorded compiler/runtime, Python and hardware.

Actual independent commands:

```sh
python topics/padua-argmax-bridge-20261105/code/check_bootstrap_energy.py --build
python topics/padua-argmax-bridge-20261105/code/check_bootstrap_energy.py --run
```

The checker, not this developer, executed these commands. Measured
sweep child CPU12.147455 seconds, including fresh build13.823321
seconds, below its1200-second cap. The127-case raw execution manifest
is local,111214bytes,SHA256
a0e8a38fa7d2f9d341bdf43d3555c1851a31e540e8d982116bb02441b63a874a.
The developer read the completed report, receipt and collector and
verified the manifest identity before applying this dated status
disposition. Required Claude audit remains separate.

No all-n energy bound, full phase producer/checker modification,
large-patch pointwise predicate, complete global complement, global
degree extension, effective onset, cost law or PD-T099 proof follows
from this helper step. The original exact3/4 target is preserved.

## History

2026-11-06, Codex developer, parent allocation inherited; actual
serving model/effort metadata unexposed. Rules/input
88e702321cd5d9c3395a551fc8a55a2f7cb8bc10. Candidate and exact
threshold were preregistered before finite countertests. One unchanged
fresh MPFR sweep completed successfully. This initial developer record
was deliberately CONDITIONAL pending the separate new-threshold replay:

> Overall status: CONDITIONAL, pending distinct fresh GMP reconstruction
> of the new threshold for all127 integers.

2026-11-06 dated disposition: the distinct checker completed the exact
new-threshold127-case reconstruction and accepted the frozen analytic
proof, with no unresolved supplementary finding. Only finite status and
verification attribution are upgraded to PROVED. The exact statement,
constant, domain, pure proof, producer code and original conditional
producer receipt are unchanged. The uniform all-n energy and complement
obligations remain OPEN.

All previous proofs, producer/checker arithmetic and receipts remain
frozen. Root alone owns shared records and Git publication.
