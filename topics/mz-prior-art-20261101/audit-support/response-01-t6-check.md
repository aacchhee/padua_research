# Independent T6 / LIT-299 check

Rules and candidate SHA: `41bbc231be4b5ccc7c3f92e5818a53b950ccc25f` (parent-supplied pinned snapshot; this directory has no `.git`). Date: 2026-11-01. Checker: Codex independent mathematical/source subagent; model and effort inherited from parent, exact runtime model identifier not exposed here. No Git mutations or developer-file edits.

Scope: the newly added T6 translation and LIT-299 statement, including source hypotheses, direction, weights, endpoint scaling, and limits of the inference. This is not an audit of the source's necessity proof, nor a novelty survey. The parent owns the complete IDEAS/novelty read and manuscript audit; this bounded source check does not generate a new mechanism or claim priority. Read AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, literature/INDEX.md, translation.md, the LIT-299 record, response-01 F4, and the manuscript endpoint-witness passage.

## Result

**One P2 correction is required in the scope/response prose. The T6 deduction itself is mathematically consistent conditional on the stated source corollary and its admissibility at r=1, gamma=0.** The source's necessity proof remains explicitly unaudited. Independent visual confirmation of the two non-strict parameter glyphs remains an access limitation, described below; the developer's recorded image inspection is not silently promoted into this checker's inspection.

## Finding F-T6-1 — P2: distinguish the single-U quotient from the squared-log result

Location: `topics/mz-prior-art-20261101/translation.md:86`; repeated at `topics/mz-prior-art-20261101/response-01.md:40`.

These sentences attribute both the 1/log N bound and the squared-log order to the exact CC evaluation of U_(N-1). The evaluation stated there gives Q_N(U_(N-1)^2)=Theta(1) and its continuous squared norm Theta(log N), so its Rayleigh quotient is Theta(1/log N). This proves an **upper bound** lambda_-(N,N-1)=O(1/log N) and therefore the every-N limit zero. It supplies neither an eigenvalue asymptotic of order 1/log N nor the stronger squared-log estimate.

The exact formulas in the manuscript make the discrepancy immediate: with S_N=sum_{j=1}^N 1/(2j-1), the quotient equals 1/S_N for odd N and N^2/((N^2-1)S_N) for even N. Since S_N=(1/2)log N+O(1), both are asymptotic to 2/log N. Multiplying either quotient by (log N)^2 diverges. A distinct harmonic-combination witness is needed for PD-T018, together with the PD-T017 bound for the two-sided squared-log order.

Requested correction: split the sentences into (a) the exact single-U test supplies the O(1/log N) upper bound and full-sequence vanishing on Pi_(N-1), and (b) PD-T017/018 supply the squared-log order through their separate upper-bound and harmonic-witness arguments. The manuscript already makes this distinction correctly at lines 871–873; do not turn this finding into a claim that its harmonic proof is defective.

## Primary-source statement check

Inspected the author PDF text layer, pp. 163–167: <https://www.mi.sanu.ac.rs/~gvm/radovi/n105p163.pdf>. Corollary 2.2 gives the iff strict exponent test and degree m+2r-1. The paragraph immediately before it gives the nodal-to-continuous direction for the general parameter range. The final paragraph permits Christoffel weights in the interior sum. These agree with the recorded source statements. Theorem 2.3 has the matching interpolation-operator condition. No Section 3 proof was audited.

Parameter-glyph limitation: the web extractor prints `r > 1` and `gamma > 0` where the developer reports non-strict glyphs. Screenshot requests for PDF pages 1, 3, and 4 returned only text containing `<<ImageDisplayed>>`, with **no image content or nested image payload**; a second standalone screenshot call confirmed this response structure. An institutional copy (<https://iris.unito.it/retrieve/handle/2318/1870047/1020599/MastroianniMilovanovicNotarangeloPIM2012.pdf>) has the same extraction ambiguity. Its p. 165 explicitly discusses gamma=0 specializations, supporting that boundary, but does not independently resolve every glyph. The environment network policy does not allow either PDF host for shell downloads; no bypass was attempted. This is a verification limit, not evidence that the developer misread the glyphs.

## Independent translation reconstruction

With alpha=1/2, the m interior zeros are cos(k*pi/(m+1)); put N=m+1. Then r=1 makes the interpolation space Pi_N. At gamma=0 and p=q=2, the exponent expression is 1-1/4-1/4=1/2=1/q, so the strict upper inequality fails. Because the opposite norm direction holds, the absent uniform equivalence means that the continuous norm cannot be uniformly bounded by the nodal expression.

For interior nodes, sin(k*pi/N)>=sin(pi/N)>=2/N and 1<=N/m<=2 for N>=2. Thus the source's interior Christoffel scale sin(theta)/m is comparable to sin(theta)/N and hence to the CC weights by T3. For the endpoint term, put a=|P(1)| and b=|P(-1)|. Then a^2+b^2 <= (a+b)^2 <= 2(a^2+b^2), while m^-2 is comparable to N^-2 and w_0=w_N is comparable to N^-2. Finally (A+B)^2 is between A^2+B^2 and 2(A^2+B^2). These comparisons prove Gamma_m(P)^2 is comparable to Q_N(P^2), uniformly in N>=2; m=1 causes no exceptional asymptotic issue.

Consequently the lack of a uniform converse constant gives inf_{N>=2} lambda_-(N,N)=0. Each fixed-N minimum is positive by finite-dimensional unisolvence and positive CC weights, so one can choose a sequence N_j tending to infinity with lambda_-(N_j,N_j) tending to zero. This statement alone gives no rate, no full-sequence convergence, and no failure on the smaller space Pi_(N-1). T6 lines 84–85 and LIT-299's final relation preserve those limits correctly.

Nonblocking precision note: the displayed Christoffel asymptotic in translation.md:72 / the record:63 should be explicitly confined to the interior Jacobi nodes (or to a suitably restricted interior region). It is not a global formula valid at x=+/-1. For example, the definition with orthonormal Legendre polynomials gives lambda_m(1,1)=2/m^2, whereas sqrt(1-x^2)/m vanishes at x=1. T6 itself correctly uses the formula only at interior nodes and handles endpoints separately, so this wording does not break its proof.

## Provenance and executed checks

- Primary-source web open and screenshot requests as described above; searches for DOI `PIM1205163M` located the institutional copy and publisher metadata. DOI resolver open failed; the PDF text opens succeeded. No numerical experiment or proof-checker execution was claimed or needed.
- Local reads used `cat`, `sed`, `nl`, and `rg`; `sha256sum` produced:
  - translation.md: `1f07addcf257f7a877977eaffde4594d532e578a38b3264edb46275ce2cdcc22`.
  - literature/records/mz-prior-art-2026-additions.md: `7370501b0c2cfddb26c34136f1845d82e6c20e08cb2c7bdff8d286983bde2d0d`.
- `git rev-parse HEAD` failed because the pinned snapshot is not a clone; provenance therefore remains the parent's pinned-fetch SHA plus the hashes above.

Suggested next prompt for AC: "Claude Opus 5.5: correct the T6 scope and response-01 F4 item 3 to distinguish the single-U O(1/log N) bound from the harmonic-witness squared-log result, preserving the conditional source dependence."
