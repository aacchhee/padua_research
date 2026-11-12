# Response-05 mathematical wording notes — 2026-11-12

Developer: Codex, assigned gpt-6.1-sol high. Rules/input head: `ae4ab4741265f55ac10847659af89dad05441274`. Root alone owns Git and integration. Scope: H1/H2 wording and source comparisons under handoff21; no new research, proof campaign or numerical execution. This note is a developer response, not independent audit acceptance.

## H1 disposition: fixed, material statement clarification

D1-04 and D1-05 explicitly require all nodes in the closed cube [-1,1]^3. D1-04's formerly unrestricted support wording now restricts locations/support geometry to that cube. D1-05 repeats the hypothesis in the transfer setup, where p(x_i)>0 uses it. D1-01 explicitly imposes closed-cube membership for the reflection lift and its squeeze conclusion; the preceding general polynomial projection identity retains its original R^d assumptions. Boundary nodes remain allowed. Each file has a dated history entry explaining what was implicit and why this clarification is necessary.

The degree-(2n-1) theorem, all quantifiers, fixed-p assumptions, proofs and statuses are preserved. No exterior-node result or strengthening to degree2n-2 is claimed. Submit the explicit hypothesis to the required focused Claude re-audit.

Exact replacement for paper Theorem A (paper owner applies):

> **Theorem A.** There are γ>0 and n₀ such that every positive rule for μ with all nodes in the closed cube C=[−1,1]³, exact on Π_(2n−1), with n≥n₀ and N distinct support nodes, satisfies
>
>     N≥(1+γ)binom(n+2,3).

Preserve the already corrected consequence: “Consequently for every sufficiently large n, no positive rule with N=N_n exists, since N_n/binom(n+2,3)=1+3/n.” The weight-transfer paragraph should likewise say “a ν-rule with all nodes in C” before multiplying weights by p/c.

## H2 disposition: fixed, coverage-labelled attribution correction

The D1 reconstruction, sources and gate now credit fixed-relative-excess LP results in other settings, while preserving the precise source coverage:

- Yudin1997, spherical designs: secondary via Lyubich p2, as read by the D1b auditor. Neither that auditor nor this response worker primary-read Yudin.
- Lyubich, arXiv:math/0703569v1, Theorem4.1, §5 equations(5.9)–(5.10), Proposition5.1: primary-read by the Claude D1b auditor, not this response worker. Strict asymptotic projective-cubature excess has factor 1/kappa_K(m)>1 except RP^1; RP^2 is the antipodal S^2 case.
- Y. Xu, *Lower bound for the number of nodes of cubature formulae on the unit ball*, J. Complexity19(2003),392–402: auditor search/abstract-snippet level only. Positive interior Chebyshev-disk bound reported as 0.13622 s² versus 0.125 s² in the source's s notation; no boundary-node or cube transfer.

The missing Chebyshev reflection-to-Haar step is withdrawn as a reason for the sphere analogue to fail. A transfer of D1's mechanism is simply not proved or claimed here; AMO-type blow-up plus defect pruning is the natural analogue. AMO p15 mentions tight spherical designs; its p16 Remark extends its obstruction to suitable orthogonal nonbasis families. Its Theorem13 excludes infinite orthogonal ball exponentials, so that route need not reproduce D1's completeness argument. These comparisons do not assert a new theorem or deny known LP fixed excess.

Exact paper §2 replacement for the existing attribution paragraph (retain the Kuperberg credit below):

> Theorem A is not stated in the literature checked here; no priority is claimed. It answers negatively, for positive weights and with non-effective constants, the question of Li–Sun–Xu [arXiv:0808.0180v2, pp3,16] whether degree-(2n−1) product-Chebyshev rules with n³/6+O(n²) nodes exist in the cube. Their definition allows real nonzero weights [p1]; the signed-weight question and their n³/4+O(n²) conjecture remain open. The proof combines the Christoffel defect identity and Chebyshev torus unfolding with a kernel blow-up as in Antezana–Marzo–Ortega-Cerdà [arXiv:2101.08064v1, Thm14/proof, pp15–16], density-to-completeness compactness as in Kolountzakis [arXiv:1606.02452, Thm1], and the spectral obstruction of Greenfeld–Lev [arXiv:1602.08854v2, Thm1.1]. Kuperberg [arXiv:math/0405366v2, §6, pp11–14; §7, p14] also gives positive-cubature local-density precedents and the continuous Fourier-cubature density question. The local distinction is the passage from arbitrary near-critical positive Chebyshev frames with nodes in C to a stationary orthogonal law with preserved critical mean intensity, followed by completeness.
>
> Effective fixed relative excess over classical Fisher-type bounds was already known in other settings through Yudin-type linear programming: Yudin1997 for spherical designs (known here through Lyubich p2), and Lyubich [arXiv:math/0703569v1, Thm4.1, §5(5.9)–(5.10), Prop5.1] for positive projective cubature. Lyubich was primary-read by the independent auditor; Yudin's original was not read. Xu [J. Complexity19(2003),392–402], at search/abstract coverage only, reports an improved lower bound for positive interior Chebyshev-disk rules. These results do not supply cube constants. The cube/Chebyshev setting and the non-effective spectral route distinguish Theorem A; no sphere/disk transfer of its positive-frame mechanism is proved or claimed here.

For a standalone manuscript bibliography, do not invent full Yudin metadata from the year-only audit attribution. Identify the indirect Yudin citation through Lyubich unless the bibliography owner actually verifies the original metadata. Source-coverage details stay in `final-d1/sources.md` and the auditor record.

## Validation and scope exception

No novel mechanism, candidate or priority assertion is introduced; this is correction of an existing statement and existing source comparisons. A fresh idea-generation gate is inapplicable. Full closest records and primary coverage remain necessary before any future priority claim. Literature facts stay LITERATURE and become no new load-bearing proof dependency. D1-01/02/03 stay PROVED; D1-04/05 stay PROVED with explicit LITERATURE dependency on GL1.1; D1-06 stays OPEN.

Read AGENTS/WORKFLOW/CODEX, handoff21, audit-05 and fixes, D1a/D1b, the six edited D1 files, literature/INDEX's instructions/section inventory/relevant Li–Sun–Xu rows, its complete Li–Sun–Xu source record and D5's Li–Sun–Xu source coverage. No external source acquisition or primary reading was performed in this response. The mathematical proofs were not reopened. Executed validation: scoped closed-cube/degree/status assertions and every relative Markdown link in the seven assigned files passed. No scientific rerun is needed for these text corrections. Root must review the input-head diff and verify unchanged proof bodies; no Git operation was performed by this worker. For that comparison, SHA256 of text after `## Proof\n` and before the next `\n## ` is `84db7e1260a170632cb4456ec0abd0433b4141f7a9971f56aa590bd74b10802f` for spectral-obstruction.md and `7e820a7564672afa41f97fdc28372bd22acd1a6ae15faf3d9513449c84e5c996` for finite-frame.md. The weight-corollary proof changes only its opening setup to repeat closed-cube membership.
