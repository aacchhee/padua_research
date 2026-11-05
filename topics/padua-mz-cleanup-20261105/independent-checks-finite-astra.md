# Supplementary Astra check of the finite C1 certificates

2026-11-05. Separate Codex mathematical checker, assigned
`gpt-6-astra`, high; no independent runtime model-attestation API was
available. Rules read at `ad503cb0603fc017444b0aa732240981eefa4d24`.
Initial candidate `39479ffca76052ea79f90c2e5e0c4bfc80bf1584`; reviewed
the later metadata diff through
`4f9d86fa3c319a9f762ddd6d208499b0f6ee73c3` as well. Producer/checker
source did not change. This check supplements the future required Claude
audit, which remains pending. Only this report was added for this task;
no developer proof/code or Git state was changed.

## Verdict

**PASS within the stated arithmetic assumptions and artifact scope.**
No unresolved correctness finding in the finite reduction, exact
producer, alternate checker bounds, or three claimed rational Rayleigh
brackets. Both m60 paths were actually rerun by this checker and passed.
The saved m1101/1240/1600 witness identities, degree constraints,
nonzero coefficients, saved positive exact norms, and both paths'
bracket implications were checked separately. Their large tensor
evaluations were **not rerun** in this supplementary review; the
previous separate-agent executions are evidenced by the pinned receipts.

One nonblocking presentation caveat: Arb's default printed interval can
be wider than the interval used internally because the center is printed
with fewer digits. In particular, the alternate checker's printed
`q_enclosure` strings at m1240 and m1600 are not themselves contained in
the theorem's tight rational brackets. This does not invalidate the
brackets: the committed exact binary64 `q_center` and outward
`q_absolute_error` reconstruct a narrower valid enclosure, and dividing
it by the manifested positive exact norm verifies every stated bracket.
I performed those comparisons using Arb at 160 bits. A future replay
must use these fields or rerun the checker, rather than compare only the
lossier printed `q_enclosure`. The producer's printed Rayleigh intervals
already suffice for all three brackets.

## Exact input identities

All paths here are relative to this topic.

| Input | SHA-256 |
|---|---|
| theory/finite-indefiniteness.md | `8cfc0d5553256f4f17cd8878f261146a9978e569d626f34232642573f2ce5631` |
| certifier-design.md | `d6a40aa26b6c9a2b265238a6e99283e975dae3f90e5cc53f8e477eeef09698cd` |
| code/rigorous_witness.py | `11f7cabcfb3c431a26224eb0d8df49db5d7de65c4685f979a9037d835a1cd498` |
| code/independent_witness.py | `60c1e6db62fbd1c422fae2fa29476afad2796aa503a1225d7f507745fa08361f` |
| independent-checks-witness.md | `23483a35e0b2bb271c2126b1500533b5ee5372ea6f9b7311d2573058ab8a5223` |
| evidence/witness-producer-m1101.json | `f5c3a58be6f875bcf77baf3e7a29c5c6e9d790304fc1a4121ae0f838ecfdb9cf` |
| evidence/witness-independent-m1101.json | `7b0b36fa7c3f6ef1603fe98345f4355c31c6b06671234d86c1ec8664d4ea8a74` |
| evidence/witness-producer-m1240.json | `a7bf9037d5282aecd6eadaf1bf5eeebc15368c509c12f5b780aafb50c6c6ad67` |
| evidence/witness-independent-m1240.json | `0b4f58ba0c209fecb4ba4300f9c1fec90e321253aad753fde03aa44297c42b5f` |
| evidence/witness-producer-m1600.json | `87b74b1ba8b7ecaa8f79a93b26bcc92115a446aee5cf9d7536bf8c49539d5a4a` |
| evidence/witness-independent-m1600.json | `6b28a7514b41537bb027ae2301188e21f86b6ef0c9cd6e9c106592f8edce6912` |

The frozen definitions were already read for the C2/C3 check; SHA-256
`4ac0e391859a14e4d6f752f1244df0701e99d9b3d8ab8570bd632520f517c7db`.
The accepted cardinal formula is trusted as an upstream theorem, in the
normalization explicitly reconstructed in the earlier math check. This
review does not independently prove all of PD-T101 or verify FLINT/Arb
machine code. It does inspect all source lines of both finite paths and
the complete reduction/design/independent report and six listed receipts.

## Reconstruction of the exact producer

The dense array is interpreted as unnormalized Legendre coefficients
`C_ab/2^56`; the total-degree triangle is checked directly. Conversion
from an orthonormal floating proposal is only a witness-selection rule.
The integer array, rather than the accuracy of that conversion or of an
eigensolver, defines the exact polynomial. Nonzero integer coefficients
and linear independence of the Legendre product basis prove p is nonzero.
Orthogonality gives precisely
`sum 4 C_ab^2/[2^112(2a+1)(2b+1)]`; this is a strictly positive rational.

Each ball recurrence encloses the exact value at an exact rational-angle
node. The returned integer center is accepted only if the **whole ball**
lies within `1/S` of that center divided by S. An inaccurate or widely
wrapped recurrence therefore causes rejection. The strict Arb comparison
has the required semantics; I additionally executed elementary
overlap/sign rejection checks. The initial constant column is exactly
one. There is no assumption of floating trigonometric or recurrence
accuracy in the producer's acceptance path.

For the polynomial tables, the perturbation of each product is at most
`2 eps+eps^2`, since exact Legendre values have modulus at most one.
Summing exact coefficient magnitudes gives the displayed delta_p. The
integer contraction `A C B^T` is scaled by `S^3`, correctly accounting
for both tables and coefficients. Python/FLINT integers do not overflow.

The kernel coefficients are `c_a c_b h_a h_b` on the degree-m triangle.
For even m, the uncorrected `(m,0)` coefficient is `4h_m`; halving it
subtracts the exceptional `2h_m` and leaves `2h_m`. For odd m, h_m=0.
Thus the implementation matches the accepted signed Lebesgue kernel
in both parities. The alternate even-frequency coefficient construction
subtracts `4/(1-m^2)` and gives exactly the same coefficient by a
different assembly. Neither path uses the positive Chebyshev cubature
weights in place of the Lebesgue weights.

For rounded kernel coefficients, splitting table perturbation from
coefficient perturbation gives
`delta_K=L_D(2 eps+eps^2)+E_D(1+eps)^2`, as written. Both L_D and E_D
are computed exactly. Retained-node endpoint multiplicities 1 or 2 and
denominator `2m(m+1)` give precisely rho, with total rho mass one. The
integer accumulators have powers `S^9`, `S^9`, `S^6` for q0,A0,B0,
respectively; no normalization power is omitted.

To check the final error inequality, write p=phat+e and K=Khat+d.
The term involving `d phat^2` is bounded by delta_K B0. The other
terms are bounded using

`sum rho |K| <= L_D`,

`sum rho |K| phat^2 <= A0+delta_K B0`.

Weighted Cauchy--Schwarz then bounds
`sum rho |K| |phat|` by
`sqrt[(A0+delta_K B0)L_D]`. This is exactly the producer's error
formula, including the factor two on the linear polynomial perturbation.
The square root and final additions use outward Arb balls; taking
`error.abs_upper()` makes the radius safely enclose its exact upper
bound. The sign predicates require strict interval separation from zero.
The exact norm is positive, so division preserves negativity. Exactness
of the same signed rule gives Q(1)=4>0: the two directions establish
indefiniteness, not just a failure of a strict lower estimate.

## Alternate checker and its trust boundary

The checker imports no producer code. It constructs its own ball-based
binary64 tables using pi-times-rational cosine evaluation, its own
even-frequency kernel, and floating contractions instead of fixed-point
integer contractions. It shares Arb, the mathematical convention and
the chosen exact integer polynomial with the producer. The m60 rerun
here is a fresh execution of both existing implementations, not a third
independently implemented large certificate algorithm.

The stated IEEE assumption is material: each BLAS dot product must obey
the standard gamma_k bound, with round-to-nearest operations and no
overflow. FMA is compatible. This assumption is explicit in both code
receipts and the independent report; machine-code verification of
OpenBLAS is not claimed. The producer's integer path does not require
this BLAS assumption for acceptance.

For these artifacts the largest coefficient numerator has 57 bits and
bits=56, so integer-to-binary64 conversion has relative error at most u
and power-of-two scaling is exact, normal and finite. Exact coefficient
l1 sums are at most approximately 323247; table bounds are at most
1+2^-48. This also bounds the intermediate contractions far below
overflow. Expanding coefficient error, both table errors and both
dot-product errors gives exactly
`L(1+u)(1+delta)^2(1+gamma_(n+1))^2-L` plus underflow allowance.
The analogous kernel formula has the correct R+1 dot lengths and actual
coefficient-rounding l1 error. Prefactor conversion, one floating
multiplication and endpoint halvings have the separately displayed
allowances. The global weight bound need not be tight near an endpoint
to be valid.

`upward_sum` encloses nonnegative floating sums using a sequential
gamma bound; pairwise summation has no larger worst-case depth. The
remaining products are covered by `(1-u)^-1` or `(1-u)^-2`, and the
signed contraction by gamma_(N+3) times the absolute term sum. The
polynomial and weight perturbation formula is a direct expansion of
`w p^2 - what phat^2`, with every cross term included. Absolute
underflow allowances are many orders larger than the possible summed
minimum-subnormal losses at these dimensions; no amplification by a
large unbounded table value occurs. These conclusions concern the
three actual finite artifacts, not arbitrary enormous user inputs.

The nonzero rational coefficient argument establishes positive norm
without a new full norm computation in the alternate checker. Its
`positive_norm_summand_lower` field is an enclosing ball for a positive
summand, despite the shorthand field name; proof of positivity here
comes from its exact positive rational expression. For a *Rayleigh
bracket*, I used the separately manifested complete exact norm, not
this one summand or the assumption N=1.

## Executions and artifact checks

Working directory `/workspace/padua_research`; Python 3.12.14,
python-flint 0.9.0, NumPy 2.3.5, SciPy 1.17.0. No random seed.
The two actual replay commands were:

```sh
PYTHONPATH=/tmp/mz-cleanup-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-cleanup-20261105/code/rigorous_witness.py --m 60 --witness /tmp/mz-cleanup/cert-m60/witness.json.gz --scratch /tmp/mz-cleanup/astra-finite-m60 --output /tmp/mz-cleanup/astra-finite-producer-m60.json
PYTHONPATH=/tmp/mz-cleanup-deps OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-mz-cleanup-20261105/code/independent_witness.py --witness /tmp/mz-cleanup/cert-m60/witness.json.gz --output /tmp/mz-cleanup/astra-finite-checker-m60.json
```

Producer replay: positive, Q enclosure
`[0.1885934804891 +/- 2.58e-14]`, Rayleigh enclosure
`[0.1885934804891 +/- 2.57e-14]`, 0.0823 seconds.
Alternate replay: positive, exact floating center 0.18859348048909605,
absolute error upper approximately 1.33393380804e-12, 0.0475 seconds.
Both used witness SHA-256
`9a1bb58cce8d8179840a024f045e8bbb32aafe9ad58d7545af4ec74278d566e9`.
Scratch replay receipt hashes:

- producer: `ed3ca24889123736409acba97c85fb0dc8ee97c04cf48395b14c2aeaae9b1f2d`;
- alternate: `1d81d6ad3e659de10c4df24c3b19a5c45583fa6a51e274c415f080cd2c509733`.

An inline Python verification, executed with
`PYTHONPATH=/tmp/mz-cleanup-deps python -`, loaded all six committed
receipts and each referenced saved witness/norm file. For each m it:

1. Recomputed source, witness and norm-file SHA-256 and matched receipts.
2. Decompressed the exact integer array and verified dimensions,
   bits=56, integer types, nonzero content, and every degree constraint.
3. Parsed the saved exact rational norm with FLINT and checked N>0.
4. Parsed the producer's printed Rayleigh enclosure and checked strict
   inclusion in the theorem's exact rational bracket.
5. Reconstructed the alternate energy ball from its binary64 q_center
   and the upper bound of its q_absolute_error, divided by the saved
   exact norm, and checked the same strict bracket inclusion at 160 bits.

**All checks passed at m1101,1240,1600.** This script did not recompute
the full large rational norm; it verified identity/positivity of the
saved exact norm, while the norm formula and computing loop were
reviewed above. The three witnessed integer arrays were actually
available in scratch and matched their committed identities; this
does not claim archival delivery or future scratch persistence.

For reproducibility, the bracket comparison core was exactly:

```python
norm = fmpq(norm_path.read_text().strip())
pq = arb(producer['rayleigh_enclosure'])
cq = (arb(checker['q_center']) +
      arb(0, arb(checker['q_absolute_error']).abs_upper())) / arb(norm)
assert arb(lo) < pq and pq < arb(hi)
assert arb(lo) < cq and cq < arb(hi)
```

Here lo,hi are the exact fmpq values in the theorem table. Elementary
Arb semantics were separately tested by asserting that `arb(0,1)` is
neither strictly positive nor negative and cannot satisfy an absolute
error bound of 1/2, while `arb(-2,1)<0` and `arb(2,1)>0` both hold.
All assertions passed. `git diff 39479ff HEAD --` on the reviewed
theory/design/code files showed only the clarification of the witness
definition from a fixed degree 1599 to generic degree m-1; inspected
and accepted as metadata/statement clarification with identical content
at each of the three listed cases.

## Scope limits and next audit

Novelty gate: not applicable to this additional check. It verifies the
already specified finite certificate, existing weight identity, and
prescribed rational artifacts; no new mechanism, literature claim,
negative-family statement or candidate is generated. The C2/C3 review
separately records the complete IDEAS read.

No full large producer/checker rerun was performed by this Astra agent.
The previous distinct-worker executions remain essential evidence for
the three finite claims, and have now received additional source and
reduction review. Bulk delivery is still pending; no first crossing,
smaller-degree positivity, extremal eigenvalue enclosure, or sharp
asymptotic follows. Required Claude audit and any material-change impact
checks remain outstanding.
