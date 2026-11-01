# Supplementary audit: rejection arguments

Candidate/rules SHA: `614709d4a60fb0c2593b05764e8d5aceda1be381`.
Base main SHA: `07c5f5465d6de306aa81dbe8ca1f615295163864`.
Auditor: independent Codex subagent. User-requested/inherited allocation: `gpt-6-astra xhigh`; runtime model/effort metadata are not independently exposed. No Git changes, developer edits, external messages, new programme proposals, or global ID allocations were performed.

This is supplementary evidence for the orchestrator's cross-agent audit, not an independent approval of the whole campaign. Scope: gen1-2, gen1-3, gen3-1, gen3-3, gen4-1 rejection arguments and the corresponding retained claims in the report, rejected-candidate narrative and IDEA records.

## Coverage and novelty discipline

Read AGENTS.md, agents/WORKFLOW.md and agents/codex/CODEX.md; complete main `state/IDEAS.md` (423 lines), including all disposition and obstruction tables, and complete `literature/INDEX.md`. Read the six scoped adversarial/decisive documents, scoped IDEA records, gate/rejection narrative, report by-product table and handovers, and consequential checker code. Scope includes negative and novelty-bearing content, so no exemption from the full registry read is claimed. This audit generates no candidate or publication-level priority claim.

Inspectability limits: the unmerged Lanczos branch's full LZ registry/theory and the developer's local PDFs/notes were not present in the original pinned snapshot. Source-based ownership/novelty assertions were reviewed as attributed claims, not independently cleared from fulltext. The root audit covers primary-source verification and the original pre-registration history. This report does not endorse competitive ownership judgments inferred merely from a group's active neighbouring programme.

## Blocking finding R1 — false converse in the joint Ritz/saturation claim (Major)

Locations: `checks/adversarial-gen4-1.md:47`, repeated at line 51 and in its Required changes section; `report.md:34`; `gate-rejected.md:153`. The upper estimate on lines 43–45 is valid for positive weights and nodes in the specified square:

`||H_x u_B - x_B u_B|| <= 2 sqrt(1-s_k(B))`, with the analogous y estimate.

It does **not** imply the stated equivalence, a lower estimate, or the later `residual ≍ sqrt(1-s)` claim. Compression can cancel the residual. A positive-degree counterexample is already inside the product-grid family:

- Grid `{-1,-1/2,0,1/2,1}²`, equal weights, total degree `k=2`, node `B=(0,0)`.
- For the monomial evaluation matrix V of Π₂, let `P=V(VᵀV)^(-1)Vᵀ` be the exact orthogonal projector on evaluated polynomials and let `p=P e_B`.
- Exact rational calculation gives `P_BB = s₂(B)=27/175`, while `P X p = P Y p = 0`.
- Thus the normalized projected point mass is a simultaneous eigenvector of both compressed coordinate operators at the node B, with both residuals exactly zero and saturation deficit `148/175`.

The included `rejections-check.py` executes this with SymPy rational arithmetic and asserts the two exact zero vectors. This is not numerical agreement being promoted to an asymptotic theorem. The counterexample invalidates the universal converse in the submitted claim. The cancellation mechanism also has a direct parity explanation: for an origin-symmetric positive measure and even k, the reproducing kernel at the origin is even; testing its x or y product against even test polynomials gives zero by parity, and against odd test polynomials (degree at most k−1) gives zero by reproduction at the origin. Hence the compressed residual at the origin vanishes independently of saturation.

Required response: retain only the proved sufficient bound and the measured one-sided ratios, retract `⇔`/`≍` and any claimed lower estimate, and qualify the handover to (b) L1. If an asymptotic converse is intended under additional separation/localization assumptions, state it as a distinct OPEN/CONDITIONAL claim and supply those assumptions. Reassess the gen4-1 retained-note description after removing the false converse; this finding does not by itself resurrect the programme, whose product reduction and other scope judgments remain separate.

## Additional corrections

### R2 — a proper Krylov subspace need not yield a nonzero commutator (Minor)

`checks/adversarial-gen3-1.md:41` correctly derives the compressed commutator identity and basis invariance, but adds that it is nonzero whenever `K_n != C^M`. Properness is insufficient: at degree zero both compressions are scalars; more generally Y constant gives a zero commutator for proper subspaces of any degree. Cancellation of `B_xᵀB_y-B_yᵀB_x` is possible. Remove the universal nonvanishing clause and retain the specific measured counterexamples to the proposed Fourier cure. The actual rejection of Fourier-basis commutation survives: an independent QR reconstruction for the rhodonea-7, M=64 case gives norms 0.25, 0.375, 0.0833333, 0.2414547 for degrees 1–4, matching the boundary-block identity to `1.67e-16`.

### R3 — qualify the rational-family attribution in the report (Minor)

`report.md:55` says the quoted grid and clustered-sampling gains are "always from the six-pole-pair member". The decisive T2 table gives the best f_B grid result to Pbhh (gain 7.5×), whereas Mpt supplies f_A's 17.1× grid gain and the quoted clustered-sampling gains. Qualify "always" to the cases actually shown. This does not alter the scoped K3 failure or investment disposition.

### Scope caution for the rational-recurrence negative

The independently reproduced instability supports a **MEASURED failure of the tested implementations and parameter sets**. It does not exclude selective reorthogonalization, pole-cancelled candidates, the unimplemented Givens IEP, or all possible stable algorithms at `O(MN^(3/2))`. The decisive document explicitly lists those untested alternatives, which should remain attached to broad phrases such as "only full reorthogonalisation works" and "no stable ... algorithm". The statement "residue killed" is defensible as the campaign's decision on the tested candidate, not as a universal theorem ruling out the rational-function family.

## Actual checks and outcomes

Commands run from `/workspace/programme-audit-614709d`:

```
OPENBLAS_NUM_THREADS=1 python topics/programme-ideas-20261031/audit-support/rejections-check.py > topics/programme-ideas-20261031/audit-support/rejections-check.json
OPENBLAS_NUM_THREADS=1 python topics/programme-ideas-20261031/checks/code/adv/gen1-2/ah_breakdown_exact.py > topics/programme-ideas-20261031/audit-support/rejections-ah-replay.txt
OPENBLAS_NUM_THREADS=1 python topics/programme-ideas-20261031/checks/code/adv/gen3-3/bandwidth_pg_probe.py > topics/programme-ideas-20261031/audit-support/rejections-pg-replay.txt
```

Environment: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0. The first command supplies an independently written exact counterexample and commutator reconstruction, plus actual independent execution of the submitted recurrence library on K3's primary setting. The other two commands are separate actual developer-code replays, not merely output inspection.

| Claim/check | Observed result | Audit implication |
|---|---|---|
| Ritz converse | Exact `s=27/175`, both compressed residuals 0 | R1 established |
| gen1-3 primary K3, Ppt, n=24, M=4096, ε=3e−4 | L3 defects 0.9425 / 0.9844 (far/near); L3c 0.2882 / 0.3979; L4c 0.3041 / 0.4525; LF `3.0e−15 / 5.5e−14` | K3 robustly fires; particular unstable outputs vary with BLAS/library versions |
| Same polynomial control | L3 `9.84e−15`, L3c `7.23e−15`, LF `2.44e−15` | Qualitative rational-vs-polynomial failure reproduced |
| gen1-2 exact rational AH example | Five double points at degree4: rank14/15 and conic-square kernel for all five seeds; four double + three simple control rank15/15; two double points degree2 rank5/6; Padua double-point degree4 rank15/15 | Finite AH/breakdown example reproduced; not an independent proof of the general cited AH theorem |
| gen3-3 PG/bandwidth check | PG band `(3,8)` at n8; symmetric κ exponents `4.46/4.99`, block-preconditioned `4.21/4.67`; recurrence nnz `210,546,1122,2002,3250` at N `15,28,45,66,91`; Pearson bands `(3,3)` pentagon / `(5,5)` heptagon | Claimed finite negative examples and cost-count correction reproduced |

Full long approximation sweeps T1/T2/T2c, 80-bit references, all curve-conditioning sweeps, and exhaustive primary-source novelty checks were not independently rerun here. The choice not to repeat expensive unrelated sweeps does not narrow the exact R1 counterexample.

Input/evidence content identities and sizes: `rejections-manifest.json`. The manifest records the pinned inputs and audit outputs; root provenance records supply the complete connector-fetched file list. No generated artifact is archival cold storage, and no external archival completion is claimed.

## Disposition

Request changes for R1 before accepting the report/by-products for downstream use. R2–R3 are corrections that should accompany the response. This supplementary audit supports the scoped primary K3 failure, the finite AH example, the measured boundary-operator corrections and the Fourier counterexample; it does not supply a full campaign approval or a universal negative result.
