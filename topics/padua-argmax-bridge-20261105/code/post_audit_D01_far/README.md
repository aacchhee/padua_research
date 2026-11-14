# D01 far implementation and measured outcome

Rules/input `4cf68980fa0538b53e2aea7174ed6e5782a34908`. Developer:
Codex technical worker; inherited runtime model metadata not exposed.
This implements the analyst-owned frozen [SPEC.md](SPEC.md), not a new
model. No original C06/C11 source or shared file was changed.

Reproduction (single numerical attempt; do not overwrite existing artifacts):

```
python3 topics/padua-argmax-bridge-20261105/code/post_audit_D01_far/supervise.py
python3 topics/padua-argmax-bridge-20261105/code/post_audit_D01_far/finalize.py
```

The numerical attempt completed all 12 registered cases with all controls
passing in **182.246419 CPU seconds** including Python imports, compiler,
build helpers, driver and supervisor; wall time175.624561s. Metadata-only
finalization used0.024848 CPU-s separately. There was no numerical failure,
retry, rescue or additional degree. Syntax compilation preceded the run.

The compact receipt is `../../evidence/d01-far.json` (14945 bytes;
SHA256 `10b8b2800b6ac910ce50eb43f50005b409388f664a3d8dc5ea2d62ab59323c1d`).
It preserves the original receipt by path/hash before adding supervisor
identity, inclusive CPU and the gate/coverage dispositions. Raw files remain
in the authorized existing local Padua destination:
`local-output/argmax-bridge-20261105/post-audit-D01/far/`.
`full-manifest.json` pins the preprocessed TU, compiler/linker/assembler,
toolchain dependencies, all included headers, native linked dependencies,
and actual loaded native dependencies before/after, plus all results.
Python/NumPy/SciPy versions are recorded; the complete Python package trees
are not pinned. Native C11 arithmetic closure and floating model dependency
versions are distinct provenance scopes. No archival upload is claimed.

## Implementation

`build.py` creates a fresh snapshot of accepted C11 `point.cpp` and
`partial.cpp`, preserving original files. Two side-channel assignments
capture row norms without altering the point total. The four directly
retained rows recompute their finite polynomial terms for the side channel.
Small n32/n128 controls compare the captured total and unmodified point
entry point exactly and overlap the previously accepted point controls.
The diagnostic native wrapper computes separate exact finite pole norms
with C11 partial cotangent sums: for t=frac(y), split at
ceil(n/2-t), adding positive and subtracting negative cotangent blocks.
Exact rational offsets identify P, collisions, central rows and ordinary
rows. No floating collision tolerance or whole-board O(n²) loop is used.

`model.py` reads the original profile script unchanged, replaces its
truncated g_R evaluation with the specified six-term EM evaluation and
explicit weighted remainder, reflects Phi near its integer limit, and
splits tightened quadrature into fixed central neighborhoods. All registered
phases have p>=q, hence the central logarithm coefficient d=(q-p)+ is0;
no nonzero central logarithm was integrated without subtraction. Separate
tolerance controls and the exact midpoint oracle test this sampled scope.
No general-phase implementation or validated enclosure is claimed.

## Outcome: MEASURED

At n8192, the original model gives:

| Phase | S-M_far | sum of component magnitudes |
| --- | ---: | ---: |
| .25,.25 | .0003783703613 | 8.040526569 |
| 1.38,0 | .0004411598098 | 5.345089409 |
| 1.45,1.45 | .0009264135900 | 2.019325507 |
| pi/2,pi/2 | -.001072314564 | 1.193274200 |

All signed endpoint/mesh/collision/central/interior/E/D/Q components are
in the receipt. Maximum additive telescope discrepancy was8.66e-15.
At8192, max|E|=.000145998956, max|D|=1.12162e-8 and Q_actual=0.
Every collision class was empty for these represented inputs; both central
rows were retained. Only even degrees were requested and executed.

**T1-a success is not passed.** Every requested n violates N1-08's
n>=40213 admissibility: the R64 exact endpoint block lies beyond the
fixed .01 strip, leaving no ordinary endpoint rows. Mesh and interior
quadrature therefore cancel strongly. At8192,.25/.25 their values are
+4.019936864 and−4.019597350. These are exact telescope components,
not evidence that the old e4 error budget applies here. The proposed
asymptotic O(1)>0.3 kill is OPEN: this geometry cancellation does not prove
an irreducible O(1) cancellation obstruction after repartitioning. No B3
run is authorized by this result.

**T1-c is resolved for the unchanged model.** At exact midpoint,
the analytic fixed-strip residue is−.00115002219528744. The independent
constant oracle agrees with tightened quadrature within1.38e-14. Finite-n
S-M agrees with the oracle to below2e-14 at n2048/8192; the maximum discrepancy
over the three tested degrees is6.16e-13 (at n512), within the theoretical remainder
bound1/[4n²(n+1)²]. Halving/quartering delta gives
residues−.0005750118689134112 and−.0002875060308652985. These sensitivity
formulas are diagnostics only; the .01 model remains unchanged.
At (1.45,1.45), tightening quadrature changes
the constant by−4.90e-13, and correcting old g_R changes it by−1.77e-9
(weighted EM remainder<9.04e-22). The signed omitted-strip residual over
z∈[1e-7,.01] is+.000960616235. Coverage below1e-7 is OPEN; this truncated
integral is not presented as the complete limiting error.

No uniform C(L+1)/n bound for the unchanged full-diamond M_far is claimed.
Measurements do not prove any all-phase or all-degree result.
