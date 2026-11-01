# Independent mathematical check 01

Role: independent supplementary Codex adversarial mathematical checker. This is not the required Claude audit and does not authorize merging. Requested audit allocation is gpt-6-astra, xhigh; the exact runtime model/effort is not independently exposed to this worker. No Git operations or changes to developer-owned files were performed.

Rules read at `6920ba632843597c37e1493d077c1df2e89f54cb`; parent synchronized base `806cc7b4509fd93bae652f9545d32d95529f8281`. The working branch remained under the parent orchestrator's control. Files were changing during review, so the authoritative reviewed content identities are the SHA-256/size entries in [independent-math-01.json](../evidence/independent-math-01.json), rather than a claim that every reviewed byte belonged to the initial head. The evidence contains all five independently regenerated degree-12 records, not only local output locators.

## Result and scope

No unresolved mathematical finding was found in the reviewed versions of E1 analytic files 01–03 and finite certificate 04; E3 files 10–11; E4 files 14–15; and E5 files 30–31. Three documentation/scope findings below were returned to their developers and the corrected text was reread. This conclusion covers the specific definitions and restrictions in those files. It establishes no historical novelty, actual IEEE activation theorem, uniform finite-roundoff radius, all-degree drift theorem, universal staircase safety, or PD-T075(U2) result.

The consequential E1 finite certificate was independently **executed**, and all exact endpoints, maximizers, source counts, projector traces, and choices agree identically with the developer's corresponding records. The independent execution requirement for its four decisive cases is discharged within this check's scope. The original KHS-only frozen test remains INCONCLUSIVE. The later Urow certificate proves the separately stated finite separation.

## Reading and predecessor coverage

Read AGENTS.md, WORKFLOW.md and the Codex role; the complete 736-line `state/IDEAS.md`, including every obstruction/disposition table; the E1 direction/freeze records; and the relevant literature INDEX entries, including the existing triangular-substitution/selection and Krylov-subspace/Arnoldi comparison records. INDEX coverage was selective, not a complete fresh literature survey. No original external paper or PDF was acquired or independently verified in this check, and no literature absence or priority claim is accepted from a digest.

Read the full old PD-T029, PD-T032, PD-T041, PD-T050, PD-T053, PD-T054, PD-T055, PD-T069 and PD-T075 theory records. The full registry preserves the relevant prior failures: IDEA-130/131/134/140, 147/148/151/154; PD-N013/015 and the distinction between raw inverse growth, span drift, and implicit-section error. Related registry rows were inspected, but this check does not claim a new audit of every old theorem or every old computational artifact.

## Independent reconstruction

**E1 normal derivative and bounds.** Differentiating the entire projection recursion leaves the frozen recurrence plus scalar multiples of earlier polynomial columns. Induction keeps the difference between the differentiated and frozen responses in the appropriate total-degree polynomial space, including after later coordinate multiplications. Final projection annihilates that difference. The graph formula then gives the spectral principal-angle derivative with fixed unperturbed column scaling. The single-node/source response has rank one, so its Frobenius and spectral norms agree; summing those squared responses gives the Hilbert–Schmidt upper bound. Independently grouping the unprojected response by node gives the Urow upper bound. These bound the spectral-output condition, not merely a Frobenius-output condition. Degree-two-only upper bounds do not upper-bound the all-source map.

The monic source norm is `sum ||f_h||²/||A_h b_parent||²`. The parent-dependent normalization is therefore essential in comparing rules; it is not the norm of independent scalar rounding errors. Exact pivot decisions are frozen, including ties. The proof does not differentiate a changing pivot rule, and it does not depend on staircase condition (C).

**E1 scalar bridge 03.** Reconstructed the full chain rule for the stated left-to-right scalar CGS2 implementation. First-pass product/addition local terms have the listed negative monic amplitudes; the coordinate product and residual subtractions have the stated positive amplitudes; component division contributes `b_k(i)`. Dot-product and norm local errors contribute scalar polynomial combinations. The exact second-pass dot coefficients vanish, so its matrix-vector products and additions have zero local first-order error. The inductive polynomial-kernel argument remains valid for the resulting nonorthogonal perturbed family. The l-infinity bound is separate from E1's Hilbert source norm. This was an analytic reconstruction; an independent dual-number replay of every scalar operation was **not** executed and is not claimed.

**E3.** The computed-coefficient polynomial surrogate retains a triangular nonzero leading coefficient under arbitrary preceding-column coefficients. It therefore spans the exact polynomial space at a complete degree. The normalized row inverse bounds the Frobenius discrepancy, and division by `sigma_min(Qhat)` yields the stated equal-dimensional projector bound. The fixed-degree continuity argument for the filtered exact-data criterion is valid. The polynomial size of its scores and a useful finite-u radius remain unproved. Computability for unrestricted real inputs needed the qualification recorded below.

**E4.** The zero-error counterexample refutes only the explicitly universal-over-all-model-errors reading. It does not supply a finite-storage IEEE counterexample. For file 15, each allowed prior-vector subtraction and nonzero rescaling preserves the enlarged span. Fixed degree-one parents thus force every rule in the stated class to have `V + span(w+epsilon e)`. Orthogonality of V,w,e reduces the angle to a two-dimensional calculation, and the displayed Jq_y identity gives the defect witness. The bounds establish a local O(u) adverse source, not exponential amplification or failure of an O(u poly(s) chi) guarantee.

**E5 radius file 30.** Independently differentiating the two cosine products gives the displayed first derivative and `f''(0)=-(2n+1-2m)cos(m theta)cos(m phi)-2m sin(m theta)sin(m phi)`. The sine difference has cubic leading term `-(k³-k)(md)³/12`; the third derivative bound O(n³) makes the scaled remainder `n^7 R=O(n^-2)`. Thus `n^7 g_m -> -B(r+m³)`. Expanding the certificate gives `9r²/2-30r+46=-4` at r=10/3 and consequently the claimed negative limit. The witness is O(n^-5) from an actual (1,1) Padua node, so it bounds rho from above. This settles only the named-certificate U1 question; `rho<=delta_obs` gives no upper bound on delta_obs.

**E5 square family file 31.** The symmetric split changes exactly the three quadratic moments, each by epsilon. Constructing M,X,Y from those atom moments independently reproduces the determinant and nonzero commutator entry. The double-zero cubic has coefficient l1 norm three and value epsilon under the split measure. Its local bound `|p|<=3 delta²` on each ball is valid, and positivity/unit mass produce the stated lower support radius for gamma<1/3. Allowing residual epsilon makes the original measure admissible at zero spread; the claimed limitation concerning reading (G) is essential and correct.

## Executed checks

All commands used `/workspace/padua_research` as cwd. Working outputs were written under `/workspace/padua-drift-runs/independent`; that directory is temporary working storage, not an asserted permanent archive.

For each pair `(set,rule)` in `(triangle,bj)`, `(triangle,pivot)`, `(rotated,bj)`, `(rotated,pivot)`, `(rotated,alt)`, separately ran:

```sh
PYTHONPATH=/workspace/padua-drift-runs/python-deps python tracks/bivariate-lanczos/code/drift/e1_exact.py --set SET --degree 12 --rule RULE --sources all --output /workspace/padua-drift-runs/independent/SET-n12-RULE-all.json
```

The actual five command lines are preserved inside the run records. Producer SHA-256: `19ce7b774e5a6fa56108eebca3b2ef81f5237328e518d95225adf9f8835e060f`. Environment: CPython 3.12.14 and python-flint 0.9.0. Every run recomputed its exact basis and all 90 source responses. These are independent executions of the inspected developer producer, supplemented by a separately written Fraction implementation below; they are not five independent implementations.

| Independently regenerated comparison | Exact decision | Squared endpoint ratio, display only |
|---|---|---:|
| T24: BJ lower / pivot KHS upper | >100, and >1000000 | 1269287.0314 |
| rotQ24: BJ lower / alternating Urow upper | >100, and >121 | 137.3647597 |
| rotQ24: BJ lower / alternating original KHS upper | <100 | 62.1636099 |
| rotQ24: BJ lower / pivot tightened upper | <100 | 4.6480801 |

All decisions used exact rational parsing/cross-comparison. Python's default 4300-digit parsing limit initially rejected one rotated rational; `sys.set_int_max_str_digits(0)` resolved this without changing the data. Float values were not used for decisions. A separate exact comparison verified identity with the developer's endpoints and other listed mathematical fields for all five runs; the receipt lists every compared key. The theorem's weaker integer thresholds follow strictly from these rational endpoints.

Additional executed commands:

```sh
PYTHONPATH=/workspace/padua-drift-runs/python-deps python tracks/bivariate-lanczos/code/drift/e1_verify.py --output /workspace/padua-drift-runs/independent/e1-derivative.json
python tracks/bivariate-lanczos/code/drift/e1_check.py --evidence topics/padua-lanczos-drift-20261101/evidence/e1-full-sweep.json --output /workspace/padua-drift-runs/independent/e1-exact-check.json
python tracks/bivariate-lanczos/code/drift/check_independent_math.py --output /workspace/padua-drift-runs/independent/independent-math-check.json
```

Results:

- The first command freshly reproduced 360 exact normal-vector equalities and 800 exact basis pairings at degree three over two sets and four rules. Its raw JSON contains the developer script's fixed label “developer execution”; this receipt records the independent execution actually performed here.
- The second independently checked all 88 recorded all-source counts, traces, rational square-root enclosures, and final-degree verdict arithmetic. This is evidence inspection, separate from the five regenerated maps above.
- The own checker imports no developer code for its mathematical reconstructions. It constructs a monomial Gram–Schmidt basis with `fractions.Fraction`, differentiates all coefficient/norm terms, and verifies every input coordinate on a 15-point degree-two triangle. All 1800 normal-vector identities pass across four rules. A separate driver compared its 12 rational Knode/KHS/Urow values against the developer producer on the identical small nodes: all identical.
- The own checker independently evaluates the E4 ten-node w/r polynomials, all required exact projection moments, norms 28/115 and 72/175, product norm 3/2, the J witness identity, and both relative-budget inequalities: PASS.
- The own checker builds the E5 square-family moment matrices from the four atoms in SymPy and checks the determinant, commutator entry, moment differences, and cubic jets: PASS.
- Its mpmath 1.3.0 evaluation at 100 decimal digits corroborates the E5 radius limit for n=10,20,50,100,300,1000,3000. The derivative-identity discrepancies are at most 1.15e-100; at n=3000 the scaled negative value divided by the limiting constant is 1.0128738091, and the scaled distance divided by its limiting constant is 0.9998332205. These are MEASURED corroboration, not rigorous sign certificates or a finite all-n threshold.

## Findings returned and disposition

1. **P2 — Isolated comparator reversal did not kill the best-comparator target.** E1's active DEAD table used an “either comparator” reversal, while the paragraph below correctly required both comparisons for BJ versus the better comparator. Developer corrected the active table at [E1.md:64](../directions/E1.md#frozen-falsifiable-test-and-three-way-verdict), preserving the old wording and amendment context at line 67. Reread: resolved.
2. **P2 — Urow must not be described as an unchanged original frozen test.** The original criterion used KHS. Developer now distinguishes the original KHS-only outcome from the additional tightening in E1.md, freeze.json and finite certificate 04. Reread: resolved. The record discloses that Urow followed an initial restricted degree-two run and that the DEAD logical correction followed a qualitative screen. No claim of untouched preregistration is made. The precise message timestamps were not independently authenticated by this checker; those chronology statements remain attributed to the development/orchestrator record.
3. **P3 — Arbitrary-real computability qualification.** File 11 originally called exact minimization/threshold decisions computable for unrestricted real inputs. Developer now restricts the computational claim to represented rational/real-algebraic inputs and thresholds, with an explicit oracle/representation caveat otherwise (statement line 15). Reread: resolved.

## Remaining limits

The finite exact computations trust CPython integer arithmetic and python-flint. Independent small-scale Fraction reconstruction reduces implementation dependence but does not replace those trusted components at degree 12. No scalar-operation dual replay, actual-rounding realizability experiment, fresh original-paper verification, or complete new audit of historical dependencies was performed. E6 was assigned back to the parent and is outside this report. Changes to the pinned proof, code, input, or essential evidence require an impact check and potentially a new rerun; metadata-only status changes after recording these completed checks should be identified separately. Required Claude audit and final registry integration remain the parent's responsibilities.

## Supplement 01 — formal scalar graph and later proof impact

This supplement extends the original snapshot above; it does not overwrite its provenance. Its exact content identities and essential regenerated outputs are in [independent-scalar-01.json](../evidence/independent-scalar-01.json), 186681 bytes at this receipt, SHA-256 `2d06b3b4e04956f9c9e2f4127c3937543dc92ee071de2926589d0a40c9bf6a10`. The independently authored receipt checker is `tracks/bivariate-lanczos/code/drift/check_independent_scalar.py`, SHA-256 `b711a1035d0709232b1854b3fb9334fe4e4a11cde26810dda08505d97f7d9aa4`. It checks rational equality/enclosures and records provenance; it is not a second implementation of the degree-12 scalar graph.

**Executed scalar checks.** Independently reran both full-graph comparator uppers, both coherent-node BJ lower witnesses, and both BJ multi-node capacity/greedy-sign generators at degree 12. The triangle target is 86 and the rotated target is 90. The prior scalar-source records only select candidate nodes; each run rebuilds the exact basis and relevant responses. The multi-node run uses the independently regenerated coherent-node output. Independently reran the explicit final-normal-projection checker on both regenerated multi-node artifacts. Thus the latter checks did not rely on unregenerated developer capacities.

Every exact endpoint dictionary and each compared choice/target/sign field agrees identically with committed developer evidence. Every one of the 325 triangle and 625 rotated regenerated target capacities also agrees identically with the corresponding developer working artifact. All 12 included rational square-root enclosures passed a separate Fraction check. The compact receipt retains the essential exact endpoints and every node sign; it identifies the large fully regenerated capacities by canonical content hash, since the public generator reconstructs them from the explicit nodes, choices and retained target without hidden input. Local working paths are not asserted to be a permanent archive.

| Independently regenerated full formal scalar model | Greedy lower squared / full upper squared, display only | Exact conclusions |
|---|---:|---|
| T24 BJ / pivot | 657331.0774535049 | >640000, hence >100 |
| rotQ24 BJ / alternating | 62.08553668985878 | >49 and <100 |

Both use the same l-infinity domain of **all** scalar-operation error parameters and spectral output. The upper includes all 90 source columns; it is not a coordinate/division-subset upper. The lower is an admissible sign choice in that full formal graph. The overall factor-ten scalar comparison remains **INCONCLUSIVE**. In particular the rotated endpoint ratio below 100 does not refute the actual capacity comparison. The weaker >7 on both sets and >800 on the triangle are post-hoc endpoint consequences, not replacement preregistered targets. These finite values agree with file 05's mathematical table; status integration is left to the parent, and no conclusion about actual IEEE activation follows.

The producer commands, run separately with `PYTHONPATH=/workspace/padua-drift-runs/python-deps OPENBLAS_NUM_THREADS=1`, were:

```sh
python tracks/bivariate-lanczos/code/drift/e1_cgs2.py --set triangle --degree 12 --rule pivot --output /workspace/padua-drift-runs/independent/cgs2-triangle-n12-pivot.json
python tracks/bivariate-lanczos/code/drift/e1_cgs2.py --set rotated --degree 12 --rule alt --output /workspace/padua-drift-runs/independent/cgs2-rotated-n12-alt.json
python tracks/bivariate-lanczos/code/drift/e1_cgs2_witness.py --scalar-source /workspace/padua-drift-runs/e1/scalar-triangle-n12-bj.json --output /workspace/padua-drift-runs/independent/cgs2-witness-triangle-n12-bj.json
python tracks/bivariate-lanczos/code/drift/e1_cgs2_witness.py --scalar-source /workspace/padua-drift-runs/e1/scalar-rotated-n12-bj.json --output /workspace/padua-drift-runs/independent/cgs2-witness-rotated-n12-bj.json
python tracks/bivariate-lanczos/code/drift/e1_cgs2_multinode.py --witness /workspace/padua-drift-runs/independent/cgs2-witness-triangle-n12-bj.json --output /workspace/padua-drift-runs/independent/cgs2-multinode-triangle-n12-bj.json
python tracks/bivariate-lanczos/code/drift/e1_cgs2_multinode.py --witness /workspace/padua-drift-runs/independent/cgs2-witness-rotated-n12-bj.json --output /workspace/padua-drift-runs/independent/cgs2-multinode-rotated-n12-bj.json
```

The two `e1_sign_check.py` commands and the local primitive checker command are recorded verbatim in the receipt. The independent receipt/check command was:

```sh
python tracks/bivariate-lanczos/code/drift/check_independent_scalar.py --independent-root /workspace/padua-drift-runs/independent --developer-root /workspace/padua-drift-runs/e1 --output topics/padua-lanczos-drift-20261101/evidence/independent-scalar-01.json
```

The independently executed `e1_cgs2_verify.py` checked 34200 exact local graph-gradient identities and 307800 zero-baseline second-pass operation contributions across both grids and all four rules at degree three. All passed and match the developer record. Its raw fixed status label says developer execution; this supplement corrects attribution for this separately executed artifact. It enumerates the local vector arithmetic primitives after the analytic quotient reduction. It **does not** replay every scalar operation of the complete normalized trajectory, including differentiated dot/norm coefficients; that stronger supplementary check remains unperformed. This is the only change to the original report's statement that no scalar-operation dual replay had been performed: local primitive replay is now completed, full trajectory replay is not.

**Analytic reconstruction of added scalar witnesses.** For target t, writing `S_i=sum_h |g_th(i)|rho_hi`, a fixed row l of R gives the stated lower bound by testing the normal target column against the unit vector `R e_l/sqrt(R_ll)`. Independent node signs cancel the off-diagonal terms in expectation, yielding `sum_i R_ii S_i^2/d_t`. In the exact greedy construction, the new cross term is `-2 s_i S_i sum_l b_l(i)c_l/d_l`; the chosen sign makes it nonnegative. The final identity `||s*S||^2-sum_l c_l^2/d_l` is precisely its orthogonal-normal squared norm. These steps validate the coherent, projected-row, expectation and greedy additions in scalar file 03; the code implements their stated l-infinity amplitudes and the full upper, without switching source norms.

**New E5 failed paths, file 32.** Reconstructed all three claims. Equal phase gives `g_m=sin(alpha)sin(m d)` and hence `P=10 sin^2(alpha)sin^2(d)`. On either stated edge, `g_m=b sin(C-m d)` and the consecutive sine Turan identities give `P=b^2[(9/2)sin^2(C-d)+(11/2)sin^2(d)]`. For a fixed nonzero A and increment `A/n^3`, the previously reconstructed Taylor formulas give a first term O(n^-6), second term asymptotic to `-A^2 n^-5`, and remainder O(n^-6). Thus all four `n^5 g_m` tend to `-A^2`, and `n^10 P` tends to `9A^4/2>0`. The threshold may depend on A. This excludes only the fixed-A path and does not exclude the successful n-dependent `A_n=a/n`. No mathematical finding remains in these identities or their stated scope; they do not imply a broader near-path obstruction.

**Post-snapshot content impact.** Reread the changed direction record and proof metadata. Finite aggregate file 04 changes verification status and cites the already completed independent receipt; its mathematical statement, reduction and essential endpoints are unchanged. E3 files 10/11 and E4 files 14/15 retain the reviewed mathematical claims, with source/model/check attribution and the resolved represented-input computability qualification. E1.md preserves the original KHS-only INCONCLUSIVE result and the separate tightened aggregate certificate, and labels the full scalar comparison INCONCLUSIVE. Scalar file 03 adds the support/sign arguments reconstructed above plus local-check attribution; file 05 separately records the finite scalar evidence. No new unresolved finding was identified in this impact scope.

| Current reviewed proof | SHA-256 |
|---|---|
| E1 scalar bridge 03 | `38a58ef2070d8d64d57d695b58668071f9fb6b20ab9bd5895489ff03fd21479d` |
| E1 finite aggregate certificate 04 | `622e76b507e411867239238e4b407dfe5637d6c2dd7f95623348728fb7e4e930` |
| E5 failed paths 32 | `12e8cbfb9c8cc5a114dacdd92fdb88c0c05de6bf8a050f42edff0a77dd8b41b7` |

All other current proof/code identities are in the supplemental receipt. This supplementary check does not replace the required external Claude audit and does not authorize merge. No Git operations, registry changes or developer-proof edits were performed by this checker.
