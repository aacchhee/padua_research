# Supplementary independent MZ-CC mathematical audit

- Auditor: Codex, gpt-6-astra high; delegated mathematical reconstruction.
- Input and rules SHA: `be28d3267bf6117878190b10f2d29840e524eac7`.
- Scope: the entire `tracks/mz-constants/paper/manuscript.tex` mathematical argument, numbered statements, correspondence and provisional CC corollary. No manuscript or development-record edits; no Git operations. Certificate executions, builds, citation provenance and novelty/priority comparison are assigned to the root audit and are not claimed here.
- Rules: AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md read. Full IDEAS text omitted for this bounded proof-translation/reconstruction task; no new mechanism or priority verdict is supplied. The root audit still needs the novelty-bearing manuscript claims covered.

## Verdict

No BLOCKING or MAJOR mathematical finding in the inspected CC text. The two minor record/notation findings below do not change the mathematical verdict. This is supplementary coverage, not the complete topic audit.

## Independent reconstruction and scope checks

1. Sections 2–3: reconstructed the CC moments, positive weights and folded aliases; coefficient floor via the weighted row identity; weighted Schur test by Cauchy–Schwarz/Tonelli; the degree-sensitive sign argument and strictness; and the reflected-positive/transition decomposition for the uniform 5/3 bound. The 5/3 statement retains its non-sharp scope and the full-degree counterexample is separate. Compared statement scopes with PD-T013/015/016/022/526 and the corresponding original theory records.
2. Section 4: read both elementary order proofs, including harmonic-witness endpoint cancellation and the large/small-log split. Checked Volterra square completion and the interpolation bijection. The new norm limit uses the full-space clause of PD-T546, correctly, rather than inferring it from degree N−1 alone.
3. New provisional CC claim: reconstructed all four parts. Positive weights yield positivity of the minimum; 5/3 yields `2−lambda_plus >= 1/3`; the U witness yields the onset N>=57 and the exact defect identity. The condition limit follows by division of the two proved limits. Restriction gives the minimum of the 5/3 and degree-sensitive upper constants; product exactness gives the stated reproduction range. Only the tightened numeric condition-limit interval inherits the computer-assisted lower bound.
4. Appendix A: independently checked the signed-kernel pole/comparable/separated splits, Schur measures, overlap factors, discrete primitive bound, global cotangent split and cross-edge terms. The replacement of PD-T523’s pointwise route by A.1(c) works: energy is O(L), interpolation error is O(L), and hence is o(L^(3/2)); antisymmetry cancels the top Chebyshev coefficient for both parities; sum/integral and oscillatory averaging recover exactly the recorded trial statement. The reverse bound preserves PD-T546’s constants and covers microscopic endpoints, good layers and every bulk index, including the central even-N node. PD-T544/545/546 source statements were compared; the PD-T546 full proof was read for translation correspondence.
5. Section 5 and Appendix B: checked fixed-trial profile factorization, integrable domination, endpoint weight Riemann sums, positivity and the trial family tending to quotient 1. PD-T529 is genuinely weakened by deleting its quantitative fixed-J error constants. Read and compared the complete PD-T530 proof with the translated core-density, continuum identity, weak-profile mass inequality, compact transition and positive-form Fatou argument. Factors 1/2 and the N/4 sinh(y/N) integral agree. No finite rate or numerical norm value is inferred. The omitted PD-T531 is not used.
6. Appendix C: checked absolute convergence, the partial-fraction derivation of off-diagonal mass entries and the diagonal integration-by-parts route. These agree with PD-T548. Read the finite Rayleigh reduction and scalar-enclosure explanation; the upper trial endpoint is explicitly not an upper bound for Lambda_edge. Program reruns are excluded from this supplementary task.
7. Sections 6–8: checked the removal of min(1/K_N,1/3) using increasing K_N and K_2>10^4; the fixed-ratio filtered reconstruction, row/column Schur norms, circle-to-interval conversion and C_*; the exact N=512 rational witness; the generic hyperinterpolation duality estimate and product-exactness reproduction. Compared statement scopes with PD-T017/018/019/023/024/025/527. The general product-exactness assumption is explicitly stated in the paper.
8. Introduction restatements preserve the proved scopes; Section 9 identifies measurements and does not convert the Galerkin proxy to a certified decimal. Detailed priority/citation verification remains outside this supplementary task.

## Executed arithmetic sanity checks

Ran Python 3 with `fractions.Fraction` independently, defining `S(n)=sum(Fraction(1,2*j-1) for j in range(1,n+1))` and `q(n)=(1 if n%2 else Fraction(n*n,n*n-1))/S(n)`:

| N | Exact verdict q_N<1/3 | Float display only |
|---|---|---|
| 56 | false | 0.33405906078701947 |
| 57 | true | 0.332968504314584 |
| 58 | true | 0.33210594134716176 |

These two base checks plus the written odd/even monotonicity establish the claimed threshold; they are not an unproved finite-screen extrapolation. Separate ordinary double arithmetic gave the printed condition-limit interval endpoints 0.08249225113080116 and 0.12319178705621205, interpolation limit 0.28657958412537815 and 1+sqrt(5/3)=2.2909944487358054. The floating displays are sanity checks, not certificates.

## Findings

### CC-M1 — MINOR: correspondence table still describes the pre-integration draft

`topics/padua-mz-paper-20261113/correspondence-cc.md:7–48` labels its initial table as current and promises updates, but rows still say “absent → to add”, carry old numbering, and mark the already independently checked interpolation corollary as “check pending”. The frozen-numbering table and changes log later in the file provide the missing truth, so the mathematical correspondence can be reconstructed, but the advertised current audit map is misleading. Refresh the initial table to final labels/dispositions (including the Schur lemma and appendix lemmas) or explicitly label it historical and add a compact final claim-to-source map. Also reconcile the provisional corollary’s stale `independent check pending` cells/Open items with its already documented independent checks; leave the current Codex audit pending until completed.

### CC-M2 — MINOR: Appendix C uses J for the trial matrix size without the declared mathsf font

At `tracks/mz-constants/paper/manuscript.tex:2181` the finite-reduction matrix is indexed `i,j <= J` although the local dimension is declared `\mathsf J`. Use the declared `\mathsf J` consistently. This is a notation correction only.

## Residual limits

No new theory allocation is proposed here. The Schur lemma is a standard, proved routine supporting step and does not require a new substantive result ID merely because it is numbered. The provisional CC consequences still require final IDs at PR preparation as planned. No novelty claim is approved by this proof-only check; no external fulltext was reread. Certificate correctness at the implementation level and full clean rebuild are covered separately by the orchestrator.
