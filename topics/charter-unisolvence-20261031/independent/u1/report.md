# Independent adversarial U1 reconstruction and comparison

Rules/base: d36722823441dc40c6e19d69a174459348dd309c. Reviewer: Codex gpt-6-astra xhigh. Date: 2026-10-31. Role: supplementary independent reconstruction and exact execution, **not the final Claude audit**.

Final supplementary status: independent mathematical reconstruction and exact replays complete for the four listed theory files and frozen checker, with no unresolved mathematical finding. Two minor candidate-record corrections are assigned to root integration below; they do not affect the science or code. This remains a supplementary independent review, not the final campaign audit. The orchestrator pins the reviewed mathematical/code contents at commit d5a5efbc6228ea21ef38b438ef976260f90ea83e; this subagent verified content hashes and made no Git query.

## Scope and independence

The task was to challenge U1 under arbitrary field, both parity and m≥0 quantifiers, then compare the producer's proof only after independently deriving an argument. Required rules, full ideas registry/obstruction/disposition tables, current charter, baseline candidates and literature index were read. A mechanism-term search was performed. The separate literature agent's U1-COMPARISON.md and index records37–40 were read later. No original publication was opened by this reviewer; literature coverage limits remain explicit.

Before opening any producer U1 proof or checker, this reviewer derived the characteristic-two counterexample, triangular tensor Gram determinant, complementary-minor identity via barycentric dual polynomials and Jacobi, central factor nonvanishing, and all-characteristic transfer by cancellation in a localized integer polynomial ring. It separately wrote and executed `check_u1.py`. The task assignment had disclosed the producer's parity-Gram route, and a later orchestrator message disclosed its normalized cutoff while the reviewer was independently working on that normalization. This is independent reconstruction and execution with that disclosed exposure, not a blind replication claim.

All writes by this subagent are within this assigned independent/u1 directory. No Git operation or shared file edit was performed.

## Conclusions

1. Original arbitrary-field signed-alternation iff: **refuted in characteristic two**, already at m=0 over F2; the m=1 F4 examples also check directly. Only necessity fails. Original sufficiency survives over every field, because its antecedent is impossible in characteristic two and the theorem holds outside characteristic two.
2. Original criterion under char K≠2: the complete determinant identity proves **both necessity and sufficiency**, with exactly the finite cutoff1,...,L−1. Characteristic zero, m=0, both parities and cross-axis coincidences are covered.
3. Even-index barycentric minors: the corrected all-characteristic iff with cutoff1,...,⌊(L−2)/2⌋ is proved. The seemingly omitted central odd-length minor is automatically nonzero by switching to the smaller odd support. The characteristic-two argument is valid because cancellation occurs in a characteristic-zero integral domain before specialization, with denominators only from distinct node differences.
4. The added Lagrange kernel/discrete cubature file is a correct direct corollary under its stated assumptions. The cubature identity needs only distinctness and char≠2; the kernel additionally needs the minor/unisolvence hypotheses. Its measure is the finite discrete product functional, with no continuous-measure claim.

These are scope-limited independent mathematical assessments, not novelty claims or authorization to bypass the required Claude handoff.

## Producer file comparison

The following content hashes identify the proof texts inspected:

| File under `theory/unisolvence/u1/` | SHA256 |
|---|---|
| all-characteristic-criterion.md | f02b5004a90ded8a7fa425c35ae701aaa30f286d5ebc3494f3afa6763f79655d |
| char2-refutation.md | 7214f3b070e73f1870ed831fde41b941a61b757724c800e64a9cbe744f8ce3ee |
| odd-characteristic-criterion.md | dbbf0eac543887725a695723a3159cb6150bcea3b7ad63c2702dc685d4adb972 |
| kernel-cubature-corollary.md | c486a2f07292bb5feff058b56123dbf46010aea09c61f0256f739489093d7a31 |

No mathematical gap was found in these exact contents. The producer proves complementary minors by pairing Cauchy–Binet terms, while the independent reconstruction uses the inverse Gram matrix in the barycentric dual basis. The term-pair sign cancels because the exponent is even. These are distinct derivations of the delicate complement step.

The producer's triangular Gram determinant is correctly established as an integer polynomial identity before applying it when minors vanish. This avoids circular necessity reasoning. Its all-characteristic proof correctly embeds the localized integer ring in a characteristic-zero fraction field and specializes the resulting denominator-two-free identity. Its normalized product `A_E Q²` equals this reviewer's `C_X C_Y`; the signed node product equals the reviewer's `(-1)^(eN)` times ordinary node weights.

For the kernel, independently let F be the square product-orthogonal-polynomial evaluation matrix, W the signed node weights and D the product norms. The already proved identity gives FᵀWF=D/2. Invertibility and elementary matrix multiplication yield 2FD⁻¹FᵀW=I. Its j-th column gives exactly the claimed cardinal polynomial at every node. The cubature identity follows by applying the ordinary-barycentric cancellation to any monomial of total degree≤2m. No further hypothesis or square root is needed.

The prior-art comparison has hash `f2185c34aebca39c6a8db5b966fb5180b84f82965a2a365806ed3489ab683232`. Its locally written axis-factor-to-Hankel conversion is consistent: the last coefficient rows of the interpolants of t^i/a(t) form a triangular transform of the barycentric Hankel matrix, up to reversal sign. This reviewer did not independently inspect the cited primary publications, so the exact source-to-factor attribution remains the literature agent's bounded source report. The conservative reformulation/corollary classification is appropriate; no novelty acceptance is supplied.

Final producer checker hash: `4216b9944c45345709ba11ffbb59b70799432329b646c0c44446da9be2cff56b`. Final symbolic summary hash: `525e46dc54f02f0f3507e8af579d0bc2f298b4361e4d734dc98248faf092bd92`. The checker was inspected after its optimization. The signed small-axis bridge agrees with Laplace expansion: the evaluation-determinant term after dividing by Vandermonde and the parity resultant has sign `(-1)^(r(a−r))`, while the Hankel Cauchy–Binet term has sign `(-1)^(r(r−1)/2)`. Their ratio yields exactly the source exponent. In canonical differences, the label sign cancels the derivative sign, so signed barycentric weights have no residual sign. The even-axis central factor is the inverse product of cross-parity differences. These observations validate the factored assembly independently of its successful execution.

## Executions actually performed

Full commands, scopes, output paths and source identity are in `evidence.md`.

- Independent own-source run: PASS 9,336 labelled axis pairs /18,672 checkerboards, including exhaustive small fields and singular cases, Q, and binary extensions. This was completed before producer inspection.
- Producer finite checker at SHA256 a1ac30c3...: separate execution PASS 1,650 seeded pairs /3,300 boards plus 288 exhaustive F4,m1 pairs /576 boards, and the explicit F4/F8 examples. Seed differs from the producer's stream.
- Old producer symbolic execution at the same source hash: ABORTED after reported expansion stall, observed exit 130. No completed symbolic result is claimed.
- Final optimized producer checker at SHA256 4216b994...: separate finite replay PASS 1,100 seeded pairs /2,200 boards plus 288 exhaustive F4,m1 pairs /576 boards; separate symbolic replay PASS all six cases. Both output files are byte-identical to the corresponding producer canonical outputs after actual comparison.
- Independent compact-summary checker at SHA256 6a090d79...: PASS all six cases, checking every A/B/Q axis-minor formula, the quartic sign and all displayed determinant factor multiplicities/signs against the independently replayed symbolic JSON.

All finite aggregate results are MEASURED. The universal claims and explicit small counterexample are hand proofs, so there is no unsupported claim that finite enumeration proves the general theorem.

## Findings and residual obligations

No unresolved mathematical finding in the four hashed proof texts or final checker. The negative record already states that global sufficiency survives; the m0 edge and m1 positive-degree counterexample are both explicit. Two minor documentation findings were returned after freeze: candidates.md calls the char≠2 restriction U1c although the current labels place it in U1b, and its U1c result still says the symbolic check is running. Root explicitly took responsibility for these two reference/status corrections during integration. They remain root-owned nonmathematical corrections at this report's freeze; no producer mutation or mathematical rerun is required.

The following integration items remain:

- A path-only move can be recorded without mathematical reaudit when content hashes remain identical; any proof or checker change needs an impact check. Final-ID/reference changes should be separately identified from mathematical changes.
- Preserve that axis factorization is prior art and exact printed all-characteristic/Hankel coverage is unverified. Do not upgrade bounded literature search or this independent reconstruction into a novelty claim.
- Consolidate the independent provisional result labels with the producer records; do not allocate them as duplicate discoveries. Final Claude audit and orchestrator registry/PR work remain required.

## Reconstruction files

`reconstruction-allchar.md`, `reconstruction-oddchar.md` and `reconstruction-char2.md` contain the independent hand proofs. They are durable verification artifacts, not second registrations of the same claims. Initial independent allchar proof considered an ideal-intersection route but did not develop it into a separate theorem; the completed barycentric-dual argument superseded that exploratory route without a negative mathematical claim.

## Mechanical integration check

Root moved the canonical theory to `tracks/unisolvence/theory/u1/` and replaced provisional identifiers with final IDs. The original science/checker checkpoint remains d5a5efbc6228ea21ef38b438ef976260f90ea83e. Historical paths and identifiers in this independent report intentionally identify the executed and inspected inputs.

This reviewer read `topics/charter-unisolvence-20261031/integration-impact.json` and `final-id-map.json`, checked the integrated U1 file hashes, reversed exactly the recorded ID substitutions in memory, and recovered **each of the four original reviewed SHA256 values exactly**. Output is in `integration-check.txt`. Thus the U1 proof-content correspondence was independently checked without Git access, and no new mathematical audit is required solely for that move/ID substitution. Other integration edits and the final Claude handoff remain outside this supplementary proof assessment.
