# Audit 05 — D1b: adversarial scope, sources and consistency

Auditor: Claude Opus 5.5 (`claude-opus-5-5`), xhigh, independent of the Codex developer. Date 2026-11-12.
Candidate: `ec5c089f35fa2002a2ed2b293a41034364380170` (branch `codex/padua-3d-20261106`), extracted by `git archive` into `scratchpad/a5-D1b/`. Handoff 20 was read read-only from the working tree at `acf0fbc` (its publishing commit); the candidate does not contain it.
No git state changes or repository edits. The line-by-line proof reconstruction belongs to the companion auditor; this audit covers scope, sources and consistency.

## Executions actually performed (my own)

1. `venv/bin/python -B topics/padua-3d-20261106/code/fd1_controls.py --output scratchpad/a5-D1b-out-fd1.json`, run in the isolated copy. Python 3.13.18, SymPy 1.14.0, 0.40 s. Code SHA256 `e5bf2b92…292d1c` matches the record. All 7 rows are identical to `evidence/fd1-controls.json` and to `evidence/fdc-d1-controls.json` (SHA256 `dae51951…d74e`, 3261 B).
2. Mutations (`scratchpad/a5-D1b-harness/mut.py`): four wrong inputs (parity n3 as n4, a dropped point, Padua n3 as n4, q19 generator (1,2,3)) were all REJECTED; the q19 n=1 positive control passed.
3. Non-lattice control (`d3ctl.py`, mpmath 50 digits; MEASURED) on the D3 20-node degree-5 rule at its 180-bit centre: Σδ_i=10=N−D, max q_i=0.766, row-identity residual 3.7e−51; the lift has M=160=8N, moments 3.3e−51 for 1≤|k|₁≤4, and defect sum 135=M−m₃. The D1-01 identities hold for non-lattice nodes.

## Primary sources read (arXiv PDFs downloaded 2026-11-12; SHA256, bytes)

| Source | Read | SHA256 (prefix) / bytes |
|---|---|---|
| Greenfeld–Lev [1602.08854v2](https://arxiv.org/pdf/1602.08854v2) | Def (1.1), Thms 1.1–1.4, pp1–3 | c9c201be… / 508257 |
| Lev–Matolcsi [1904.12262v4](https://arxiv.org/pdf/1904.12262v4) | §1.1–1.2, Thm 1.1, pp1–3 | 888074b0… / 390590 |
| Antezana–Marzo–Ortega-Cerdà [2101.08064v1](https://arxiv.org/pdf/2101.08064v1) (v1 title "Interpolation by multivariate polynomials in convex domains") | §1, Thm 10, §3.4, Thms 13–14, proof, Remark, pp1–4, 12–16 | ffc65374… / 415944 |
| Kolountzakis [1606.02452v1](https://arxiv.org/pdf/1606.02452) | §1, (1)–(3), Thm 1, Lemmas 1–2, pp1–6 | cb1010d2… / 163637 |
| Kuperberg [math/0405366v2](https://arxiv.org/pdf/math/0405366v2) "Numerical cubature from Archimedes' hat-box theorem" | §3 p5, §6 pp11–14, §7 p14 | abf2d909… / 233981 |
| Lyubich [math/0703569v1](https://arxiv.org/pdf/math/0703569) | §1, Thm 4.1, §5, Props 5.1–5.2 | 12 pp / 199821 |
| Li–Sun–Xu [0808.0180v2](https://arxiv.org/pdf/0808.0180v2) | p1 (weights λ_k∈R\{0}), p3 open question + n³/4 conjecture, p16 §4 open question | 356474 |
| Marzo [math/0611503v1](https://arxiv.org/pdf/math/0611503v1) | Thms 1.6–1.7 | 249635 |

Search level only: Y. Xu, "Lower bound for the number of nodes of cubature formulae on the unit ball", *J. Complexity* 19 (2003) 392–402 (abstract snippets: Yudin's function raises the positive-interior Chebyshev-disk bound from 0.125 s² to 0.13622 s²), and AMO's journal version, CMFT 21 (2021) 831–849. sciencedirect, ams.org and MaRDI were unreachable from this sandbox.

## Task 1: hypotheses and application (PASS)

- **GL p1, (1.1):** a spectrum is a countable Λ such that {e^{2πi⟨λ,x⟩}} is an orthogonal and complete basis of L²(Ω), Ω bounded with positive measure.
- **GL Thm 1.1 (p2), verbatim:** "Let Ω be a convex polytope in R^d. If Ω is a spectral set, then all the facets of Ω must be centrally symmetric."
- **LM Thm 1.1 (p2):** a spectral convex body is a convex polytope that tiles face-to-face along a lattice.
- `sources.md:7–17`, `final-d5/source-records.md:69` and `spectral-obstruction.md:36` quote these correctly. The octahedron O={|x|₁≤1} is a full-dimensional convex polytope, and its facet conv(e₁,e₂,e₃) is a triangle, which has an odd vertex count and so is not centrally symmetric. The application is valid.
- Kol00 (central symmetry) cannot exclude O, because O is centrally symmetric. The record correctly does not rely on it.
- Completeness is required, as the record says (`sources.md:11`). Spectrality is affine-invariant, so the normalisation does not matter.

## Task 2: literature and priority

- **AMO Thm 14** (p15) excludes exact orthogonal reproducing-kernel bases (Gaussian cubature on Π_{2k}) on weighted balls, via a Kroó–Lubinsky kernel limit and Fuglede 2001 (Thm 13: no *infinite* orthogonal exponential set on a ball). The p16 Remark extends it to orthonormal non-basis families with enough local points. The p15 sphere remark reads: "A similar argument can be used on the sphere to study tight spherical designs." AMO covers exact orthogonality on balls only and does not state D1.
- **Kolountzakis Thm 1** with (1)–(3): if bounded Ω has orthogonal exponential sets of upper density arbitrarily close to |Ω|, then Ω is spectral. This is the deterministic form of D1-02/03's density-to-completeness step; the record already disclaims novelty for it (`sources.md:21`, `gate.md:32`).
- **Kuperberg**: Thm 3.2 is lattice-only (octahedron 18/19 ⇒ 19m³/108); §6 ε-nets are for simplex/simple polytopes; §7 poses continuous positive Fourier K-cubature density and asks whether non-lattice rules beat lattice ones. No D1 statement.
- **Li–Sun–Xu** (p3, p16) say explicitly that it is an **open question** whether degree-(2n−1) cube rules with n³/6+O(n²) nodes exist, and they conjecture n³/4+O(n²). They allow real nonzero weights (p1).
- **Bounded searches** (cubature/spectral/Fuglede/positive; Yudin/torus/trigonometric; asymptotic Gaussian/spectral polytope) found no prior statement of D1. Verdict: D1 is not a known stated result within this coverage. It combines known mechanisms (defect identity, Chebyshev unfolding, AMO-type blow-up, Kolountzakis-type compactness, GL 1.1) and partially answers Li–Sun–Xu. Priority is unestablished; the record claims none.

## Findings

| ID | Sev | Location | Finding / evidence | Disposition |
|---|---|---|---|---|
| D1b-1 | **MAJOR** (attribution / source coverage; does not affect D1's truth or status) | `final-d1/reconstruction.md:43–47`, `sources.md:27–35`, `gate.md:22,32`, `paper-note-draft.md:50`; R4 commitment `protocol.md:49` ("compare the actual ball/sphere literature … Read any newly identified closest primary asymptotic result") | The sphere/disk comparison omits known **effective fixed-relative-excess** bounds for positive cubature, obtained by Yudin-type LP. (a) Lyubich Thm 4.1, §5 (5.9)–(5.10), Prop 5.1 (primary): every positive projective cubature of index p on S^{δm−1} asymptotically exceeds the classical Fisher-type LP bound by a factor 1/κ_K(m)>1; the only exception is RP¹, and RP² is the antipodal S² case. (b) Yudin 1997 (via Lyubich p2): the same for spherical designs. (c) Xu 2003 (search level): positive interior Chebyshev-disk rules need ≥0.13622 s² against the classical 0.125 s². The record's "No spherical L2 cubature excess is imported" is literally true but implies no such excess is known. What is distinct about D1 is the cube/Chebyshev setting and the spectral (non-effective) route. | Return to developer (D1/D5): add coverage-labelled sources and revise the comparison and paper-note §2. A torus/octahedron LP route to an effective γ may be recorded only as a deferred, unclaimed idea. |
| D1b-2 | MINOR | `paper-note-draft.md:19,33–35`; `gate.md:18` | Theorem A answers negatively, for **positive weights only** and non-effectively, the open question in Li–Sun–Xu 0808.0180v2 pp3,16. Their signed-weight question and n³/4 conjecture remain open. The frontier sketch said this (`frontier-assessment.md:116`), but the final note only calls their n³/4 assertion "a conjecture". | Return (framing of a published question): add one sentence with page pins. |
| D1b-3 | MINOR | `reconstruction.md:45` | "AMO's remark **allows** an orthogonal nonbasis family when enough local points are present" misreads p16. The Remark **extends the obstruction** to such families. The p15 sphere/tight-design remark is not recorded in the D1 files; the supplemental audit noted it at `d1-audit.md:200`. | Eligible MINOR wording fix in place ("extends AMO's obstruction to"), plus a cite of the p15 sentence. |
| D1b-4 | MINOR | `reconstruction.md:47` | "our exact Chebyshev reflection-to-Haar step is absent there" is a misleading reason. On S² the zonal kernel makes the moving-centre limit uniform by symmetry (auditor background), and the disk has no *infinite* orthogonal exponential set (AMO Thm 13/Fuglede 2001), so completeness is not needed. The sphere analogue is plausibly easier, not harder. No contradiction with D1. | Return together with D1b-1. Reword to "not proved or claimed here; an AMO-type route plus D1-01 pruning is the natural analogue; LP fixed-excess results exist (D1b-1)." |
| D1b-5 | MINOR | `paper-note-draft.md:33` | The quantifier in "positive rules with N=N_n do not exist for all sufficiently large n" is ambiguous. The intended and proved statement is "for every sufficiently large n, no such positive rule exists" (`spectral-obstruction.md:46`). | Eligible wording fix in place. |
| D1b-6 | NOTE | `final-narrowed-report.md:7` | "The independent adversarial review passed" refers to the Codex-Astra supplemental review. Line 3 does say it is supplemental. | Optional wording: "supplemental Astra review". |
| D1b-7 | NOTE | `code/fd1_controls.py:55,73–91` | The controls test cube moments, the cube trace identity, torus exactness and lift defects. They omit per-node cube δ_i≥0 (`nonnegative=False` is dead code) and the row identity, and use lattice/coset inputs only. The record's "trace identities" wording is accurate; execution 3 covers the rest. | No change required. |
| D1b-8 | NOTE | `reconstruction.md:49`; `general-weight-open.md:45` | Li–Xu can become a positive calibration: with all A_d marks 1, deg z^β=⟨λ,θ^∨⟩, so the unfolded body {x:⟨x,α⟩≤1 ∀ roots} is the A_d Voronoi cell (hexagon at d=2, rhombic dodecahedron at d=3), a lattice tile. D1's mechanism therefore *permits* their Gaussian families. Berens–Schmid–Xu similarly give a cube body. Auditor derivation, not checked against their texts. | Optional calibration. |
| D1b-9 | NOTE | `spectral-obstruction.md:9,19`; `paper-note-draft.md:29` | Unclaimed scope facts: (i) Π_{2n−2} exactness suffices (`finite-frame.md:57`); (ii) the argument works verbatim for every d≥3 and gives a torus ℓ₁-degree version; (iii) nodes must lie in the closed cube, so exterior-node positive rules are not covered. | Optional: Theorem A should say "nodes in C". |
| D1b-10 | NOTE | `sources.md:3` | Auditor-downloaded SHA256 and bytes are in the table above. AMO's v1 title differs from its journal title. | Optional for D5. |
| D1b-11 | NOTE | `general-weight-open.md:21–31` | H1/H2 are honestly stated as a sufficient pair and stay OPEN. Unverified leads: Berman–Ortega-Cerdà sampling density and Kroó–Lubinsky bulk universality (AMO refs [2], [10]). | None. |

No BLOCKING findings.

## Task 3: consistency tests

- **2-D diamond (PASS).** Checked: O₂=B[−½,½]² with Λ=B^{−T}Z² of density 2=|O₂|. The Padua lift basis (1,0),(½,n/(2(n+1))) has 2n(n+1) points per period cell and tends to a basis of Λ. My rerun reproduces the defects n+1 and 4n−1 (3/4/5 and 7/11/15).
- **d=1 and tensor-degree (PASS).** For d=1 the interval tiles, and Gauss–Chebyshev attains N=D. Tensor-degree spaces have a cube body, and product Gauss attains N=n³. Both are permitted.
- **Sphere S² (consistent).** No near-Gaussian positive family is known; best known positive rules sit at a fixed excess (auditor background, not primary). Lyubich proves a strict asymptotic excess in the antipodal positive case. Any analogous sphere argument would need the disk, which is not spectral; consistent.
- **Disk/ball, total degree (consistent).** AMO Thm 14; Xu 2003 (ratio ≈1.09).
- **3-D cube (consistent).** No known positive Chebyshev family has ratio →1. Li–Sun–Xu call this open, the best construction has ratio ≈1.5 (n³/4), and folded unshifted lattices need at least 19/18. The topic's n=2 ten-node rule (q19 control) is a finite exception, permitted because the result is non-effective.

## Task 4: scope confirmations

- **Weights.** Covered: product Chebyshev (D1-04), and ν=cμ/p with fixed p>0 on the closed cube (`weight-corollary.md:9–25`). The exactness bookkeeping r=n−⌈k/2⌉ checks. General full-support doubling is OPEN (`general-weight-open.md:15`), with no silent change of support.
- **Nodes.** Arbitrary distinct nodes, phases, unions and boundary nodes with positive weights are covered (`spectral-obstruction.md:19`, `finite-frame.md:20–34`; execution 3).
- **What is not claimed.** No interpolation/Lebesgue, signed-weight or reduced-exactness claim (`spectral-obstruction.md:54`; paper note :8, :17; results :10; final report :7). No effective γ or n₀ (`spectral-obstruction.md:46,54`).
- **No overstatement** in candidate-owned files. The historical `frontier-assessment.md:115` ("whatever … weights") means positive weights and is not editable.

## Recommended attribution and status wording

Status: D1-04/D1-05 stay **PROVED with explicit LITERATURE dependency (GL Thm 1.1)**, pending the companion line-by-line reconstruction. Nothing in this scope audit forces a downgrade. D1-06 stays OPEN.

Suggested paper-note §2 sentence:

> "Theorem A appears not to be stated in the literature we checked. It answers negatively, for positive weights and with non-effective constants, the question of Li–Sun–Xu [0808.0180v2, pp3,16] whether degree-(2n−1) rules with n³/6+O(n²) nodes exist on [−1,1]³. The signed-weight question and their n³/4 conjecture remain open. The proof combines the Christoffel defect identity and Chebyshev torus unfolding with a kernel blow-up as in Antezana–Marzo–Ortega-Cerdà [Thm 14], a near-tiling-density compactness principle as in Kolountzakis [Thm 1], and Greenfeld–Lev [Thm 1.1]. Fixed relative excess over the Fisher-type bound was previously known, with explicit constants, for positive cubature in other settings: for spherical designs (Yudin 1997), for positive projective cubature (Lyubich, Thm 4.1), and for positive interior ball cubature (Xu 2003, coverage-limited). Those proofs use linear programming in homogeneous settings and do not treat the cube."

## Residual risk

Xu 2003 and Yudin 1997 were not primary-read. The Cambridge "Minimal Cubature Rules" book and the AMO journal version were not compared. Bounded searches cannot exclude an unindexed prior statement. The D1-02/03 proof chain belongs to the companion auditor; I only skimmed its statements.
