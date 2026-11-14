# Supplementary review — bootstrap reduction and finite energy threshold

2026-11-06. Distinct Codex checker `/root/check_native_37_40`, parent
allocation Astra high; serving identity/effort not independently exposed.
Rules read earlier at bda45a4 and verified byte-unchanged at published input
`88e702321cd5d9c3395a551fc8a55a2f7cb8bc10`. This supplements the required
Claude audit. No Git, shared files, old arithmetic, old proof or old receipt
is changed by this worker.

## Scope and frozen inputs

Read PD-T227 in full (including zero modes and its endpoint functional
and aggregate Taylor proofs), PD-T251 in full, N3-corner-radius-reduction,
the new bootstrap candidate and complete pure proof, and the complete
corrected independent exact GMP source. This review covers the analytic
implication and independently executed finite threshold, not a historical
novelty verdict or a replacement for the author's candidate gate.

Author-frozen pure proof `theory/N3-bootstrap-corner.md`:
SHA256 `7610728bada4dbe392efde52c7498ff2f9cba8e8b2f788eeea790b576317b229`.
This identity is review provenance only, never a runtime prose guard.
Author wrapper `code/n3_bootstrap_energy.py`:
SHA256 `5680d6b1688114a423cb4c692f2e253216d9e0ab40ef9bf2b0df94c986bb5587`.
The parent supplied these freeze identities before the independent sweep.
Producer endpoints, MPFR arithmetic and producer verdicts are not imported
by this checker. The finite theorem is a separate author-owned record.

## Independent mathematical reconstruction

PD-T227's M is the true maximum of a continuous finite sum of absolute
polynomials on the compact square. It exists, is finite, and is at least
the positive corner value Lambda_c. In the derivative norm argument,
each signed cardinal sum has absolute value bounded everywhere by
lambda_n and hence by M. This requires no known maximizing location or
prior ratio K. The Taylor remainder with M is therefore available before
any global argmax theorem.

At nonzero cardinals the scalar quadratic upper bound permits sign
changes. The exact zero set k=0, j>0 even is omitted only from the
weighted energy W. Both components of each zero gradient agree, so
their absolute inward linear contribution is included in A_n and B_n.
The removable00 index is nonzero and is included in W. PD-T251's
all-degree normalized slope bound applies to these full slopes.

Under W<=(3/4)n^4 Lambda_c, putting z=n^2(h_x+h_y) gives

    lambda_n(c+h) <= Lambda_c*(1-z/8+3z^2/8) + M*R(z),
    R(z)=exp(z)-1-z.

For 0<=z<=1/8, (k+2)!>=2k! proves R(z)<=z^2 exp(z)/2,
and termwise exp(z)<=1/(1-z)<=8/7 proves R(z)<=4z^2/7<=1/112.
Thus 1-R(z)>0 and, for z>0,

    z/8-3z^2/8-R(z)
      >= z*(1/8-(53/56)*z) >= 3z/448 > 0.

Only at a putative global maximizer is the left side replaced by M.
Rearrangement gives M*(1-R)<=Lambda_c*(1-R-3z/448), contradicting
M>=Lambda_c. There is no substitution M=Lambda_c at an arbitrary point,
no prior K, and no circular use of global maximality at a corner.

The parity-valid x reflection for even n or y reflection for odd n
permutes the corrected cardinals. Absolute values and squared physical
gradients are preserved, and inward coordinates transfer the slopes.
Consequently the same energy premise and exclusion hold at both corners.
For the phase diamond, h_x=2sin^2(alpha/(2n)) and the analogous y formula
give, whenever at least one phase is nonzero,

    z < (alpha^2+(n/(n+1))^2 beta^2)/2
      <= (|alpha|+|beta|)^2/2 <= 1/8.

The origin remains the corner. If every point outside the selected two
closed patches is strictly below Lambda_c, an attained global maximizer
must lie in their union. Exclusion removes every noncorner point there,
including patch boundaries, so the two equal-value corners are exactly
the equality set. This proves the conditional cover reduction. The
pointwise strict estimate after substituting M=Lambda_c is available only
after that global closure. It supplies no replacement predicate for an
unchanged phase checker before closure.

**Pure implication: ACCEPTED in the stated scope.** No logical finding.
The all-degree energy premise and strict complement cover remain separate
obligations; finite cases cannot establish the former.

## Prospective independent execution record

Before the new-threshold sweep, freeze the standalone wrapper
`code/check_bootstrap_energy.py`, SHA256
`915c6c7c40e8c9e0c748cf50c2fe278f6760d79a9e725939aed1553269030972`.
It imports no producer module and accepts no producer endpoint input.
The only arithmetic source is unchanged `code/check_corner_exact.cpp`,
SHA256 `3646f4e8b6b16957b9e1114f95ad2f0a7c18eec4687b49d5e6f1947a25eea6e3`,
also checked against its bytes in published input88e7023.

Actual fresh compilation completed, exit0, using:

```sh
python topics/padua-argmax-bridge-20261105/code/check_bootstrap_energy.py --build
```

Binary SHA256:
`cf7522d630958e440e1452963b8de746c84b2c758b2c67c6a4011f740d46fe99`.
Compiler g++ (Debian14.2.0-19)14.2.0; Python3.12.14;
GMP development package2:6.3.0+dfsg-3. Actual compiler argv and CPU/wall
measurements are in local `check-bootstrap/build.json` and the final receipt.

Preregistered next command, not yet run at this paragraph's creation:

```sh
python topics/padua-argmax-bridge-20261105/code/check_bootstrap_energy.py --run
```

Exactly once for each integer2..128, independently reconstruct ell and E
with the frozen GMP source and test **4E<=3*n^4*ell** using exact Python
Fractions. Validate positive ell, interval ordering, precision, full node
count, zero mask, all native exits, and n2 enclosure of Lambda_c=3 and
W_2=331/18. No old kappa receipt supplies this new predicate; although the
unchanged executable still performs its old radius check, its fresh
ell/E outputs must pass the separate new inequality. Stop on any failure;
total child CPU including fresh compile is capped at1200seconds. No
adaptive constant, repeated energy sweep, other degree or phase rerun.

The GMP path uses direct rational Machin and cosine Taylor enclosures
at512-bit scale and expanded physical PD-T227 gradients, independently
of the producer's normalized-gradient MPFR path. Its denominator signs
are certified before division. The n=2 exact control is an enclosure
control, not a claim that interval endpoints equal the exact values.

Raw per-degree bounds, actual argv/status/timing and hashes remain local
under `local-output/argmax-bridge-20261105/check-bootstrap/`. Only the
small aggregate receipt is intended for retention in Git. Reproduction
uses the committed frozen source and new wrapper; no old raw endpoint
table is an input. Deterministic; no seeds.

## Finite result

**ACCEPTED: every integer n=2,...,128**, exactly127 new-threshold checks.
The preregistered command above actually ran once and returned exit0;
all127 native processes returned exit0. No failed, partial, repeated or
unexecuted case is counted. The receipt is
[independent-bootstrap-energy.json](evidence/independent-bootstrap-energy.json).

All own reconstructed bounds satisfy 4E<=3*n^4*ell. Since
W_n<=E and 0<ell<=Lambda_c, this proves

    W_n <= (3/4)*n^4*Lambda_c, for each integer 2<=n<=128.

The maximum certified E/(n^4 ell) occurs at n=2 and is strictly below
383102/1000000 (<3/4). The receipt retains its exact rational value;
the decimal summary is not used in acceptance. The n2 intervals enclose
Lambda_c=3 and W_2=331/18, with5 nonzero cardinals and1 omitted zero
cardinal. Every degree passed the expected zero mask/cardinality checks,
strictly positive energy denominators |L(c)|, and sign-separated divided
differences; those divided differences may themselves have either sign.

Actual measured sweep CPU:12.147455seconds; sweep wall:12.379033seconds.
Including fresh compilation, child CPU:13.823321seconds, below1200.
CPU is the sum of actual child user/system deltas, not elapsed wall time.
The per-degree raw execution manifest identifies every actual argv, exit,
CPU/wall measurement, bound-file hash and exact normalized energy. Its
SHA256 is `a0e8a38fa7d2f9d341bdf43d3555c1851a31e540e8d982116bb02441b63a874a`
and it has111214bytes, retained only locally. Source and binary hashes
matched before and after the entire sweep; the source is also checked
before every degree. The raw output and per-degree executions remain
off Git and are reproducible with the committed source and wrapper.

Combining this finite premise with the separately reviewed pure
implication excludes noncorner global maximizers in its two patches for
these127 degrees. It does not prove the strict complement coverage or
global maximum/equality theorem for any additional degree. It does not
prove the energy bound for n>=129. No full phase run or phase predicate
change was made. The existing independently proved global range2..40
is unchanged by this helper result.

Final source/binary/runner/raw-output hashes, exact degree coverage,
all127 exit statuses and new predicates were checked against the completed
receipt and raw manifest. The wrapper, report and receipt are each below
16KiB. **No unresolved finding within this supplementary scope.** The
new checker block is complete and frozen; the required Claude audit
remains separate.
