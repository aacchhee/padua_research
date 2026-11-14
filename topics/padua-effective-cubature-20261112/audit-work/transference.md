# Independent audit — transference, uniform theorem and cap

2026-11-13. Codex subagent, `gpt-6-astra`, high. Candidate: `895d85fdd995e9f227dabaf8a212ba4d3b188db0`; rules/current head supplied by orchestrator: `8b27da5ea2e0d363d2a416482b176466dc33efa9`; base: `b5388c25a2a5ccb8d0faf816ab87023cf347bcd3`. Read AGENTS.md, WORKFLOW.md, CODEX.md and handoff 03. No development files or Git state changed.

Scope: independently reconstruct -02, -03, -04, and the sufficient construction/status of -05. Read D1-01, D1-04, D1 sources, r08-lattice-minima, and paper-note-draft sections 2/4. Novelty/priority and candidate coverage are assigned elsewhere; no new novelty claim is made here, and this bounded mathematical check did not read state/IDEAS.md in full. The gamma checker and finite lattice-witness campaign are audited by other workers.

## Findings

### MAJOR T1 — target closure does not preserve the target's compact-support requirement

`theory/explicit-gamma-target.md:8` explicitly asks to exhibit a compactly supported admissible function. Its lines 4 and 14 say that -07 completes that target, and line 14 substitutes `CLOSED` for a permitted epistemic status. But `theory/explicit-gamma.md:70` constructs a nonzero polynomial times a Gaussian, followed at line 76 by dilation and normalization. Such a function is not compactly supported. The proof explicitly invokes the general L1 class in -02(c), not the compact-support class in -02(b) (`explicit-gamma.md:49–56`).

The approximation argument in `delsarte-bound.md:99–110` proves that compactly supported admissible functions approximate its integral; it supplies neither an explicit cutoff parameter nor a certified value for a particular cutoff satisfying the original target. Thus the general explicit bound may be correct while the exact original target has not been exhibited as claimed.

Requested disposition: either retain the original compact-support target with its accurate epistemic status and describe -07 as resolving the general L1 variant, or explicitly record a target change and preserve the original requirement/history, or supply an explicit certified compact-support construction. Use an allowed epistemic status separately from any closed/completed workflow disposition. The resolution changes scope/status or adds proof, so is material and needs focused review. This finding does not challenge the local analytic transference or the general-L1 use of a valid gamma certificate.

### MINOR T2 — the finite-route criterion is sufficient, not the exact loss/necessary condition

`theory/explicit-gamma-target.md:10` begins by describing a sufficient route but then says the construction “loses a factor” `((2L+1)/(2L+r))^3` and that the level “must satisfy” the resulting inequality. With the stated normalization `rho = R/m_(L+1)`, direct calculation gives

```
(3/4) integral(phi) = 6 R / (2L+r)^3
                     = rho * 6 m_(L+1) / (2L+r)^3,
6 m_(L+1) = (2L+1)^3 + 5(2L+1).
```

Hence the displayed criterion is indeed sufficient, but conservative. It is not the exact loss relative to rho, and necessity is not proved. Wording can retain the existing valid criterion by calling it a conservative sufficient criterion and replacing “must satisfy” with “suffices to satisfy.” No result later in the topic relies on the sharper expression.

For completeness, the construction itself checks: normalize c0=1, use a bounded measurable fundamental domain P of volume one, so B(0)=1, B(k)=0 at nonzero integer k, integral(B)=1, and Fourier(B)=|Fourier(1_P)|^2. Thus psi(0)=1, integral(psi)=R, its transform is nonnegative, and its positive part is contained in the l1 ball of radius 2L+r. Dilating that ball to radius 2 gives the formula above. Brunn–Minkowski gives volume(P-P)>=8, while P-P is contained in an l1 ball of volume 4r^3/3; therefore r>=6^(1/3), as stated.

## Accepted mathematics within scope

- **-02(a)–(d): accepted.** The weighted pair sum is bounded above by c0 from complementary exactness/sign frequency ranges, and below by f(0) sum(v_j^2). Cauchy–Schwarz yields the cardinality bound. Gaussian regularization proves integrability of the nonnegative Fourier transform; periodization is used only in L1 and the inequality at zero follows by continuity, so no unjustified pointwise Poisson summation is needed. The autocorrelation cutoff preserves both signs and normalization and converges in integral. General exactness E gives precisely L=(E+1)/2, including boundary orbits and E=0.
- **-03(i)–(iv): accepted with declared literature dependencies.** The KLM definition, essential-difference convention, non-tiling consequence and arithmetic agree with primary text. The local bounds do not depend on KLM strictness. The comparison with D1-04 correctly distinguishes its compactness proof from this transference proof. Exactness 2n−1 gives n rather than n−1/2.
- **-04(a), (b), (b′): accepted.** Under composition with B the Fourier transform gains |det B|^(-1) and B^(-T), giving integral(phi)<=|det B|. The cutoff extends this to the whole admissible class. Averaging over the finite annihilator group gives the finite dual bound, for any exactness E. The critical-lattice proof does not import optimality. The later claim that no E=2n−1 lattice witness can exist above 109 remains explicitly dependent on the separately cited optimal packing result; it is not inferred from merely constructing B.
- **-05:** construction's conservative sufficient inequality is sound, subject to T2; its closure/status requires T1.

## Primary literature actually inspected

Direct `curl -fLsS --max-time 45 https://arxiv.org/pdf/2510.10172v1 -o /tmp/transference-klm.pdf` failed with HTTP 403. The available web reader then successfully opened the versioned PDFs; no PDF or extract was committed.

- [KLM, arXiv:2510.10172v1](https://arxiv.org/pdf/2510.10172v1): pp. 2, 15–16 Definition 5.1/admissibility, p. 23 equation (6.2), pp. 25–26 section 6.5/Theorem 6.4 and its proof dependencies. Definition and theorem transcription match. For an origin-symmetric convex body the essential difference set is the interior of twice the body; the equality case for D is exactly translational tiling. The proof invokes strong duality, dual attainment and weak tiling. Its source proofs were not independently reconstructed. The p. 2 open Turán discussion is correctly applied to the octahedron.
- [Greenfeld–Lev, arXiv:1602.08854v2](https://arxiv.org/pdf/1602.08854v2): pp. 1–3, spectrality definition, tiling discussion and Theorem 1.1. The triangular facet of the octahedron violates the necessary centrally symmetric facet condition.
- [Lev–Matolcsi, arXiv:1904.12262v4](https://arxiv.org/pdf/1904.12262v4): pp. 1–3, especially p. 2 introduction and Theorem 1.1. The introduction directly confirms the already classical tile-implies-spectral direction through lattice tiling and dual lattices. Thus the route used in -03 is corroborated independently of KLM's report. External proofs remain LITERATURE.

## Executed arithmetic and cap checks

Environment: Python 3.12.14. From repository root:

```
python3 -B topics/padua-effective-cubature-20261112/code/cap_critical_lattice.py /tmp/transference-audit-cap.json
```

PASS; code SHA256 `0516daa4af249dfe23f0861f3c0bc9eaba12b09330bd4d9dd9458b519b9a2f44`; determinant −38/27; coefficient bound 3; enumeration radius 3; minimum l1 norm 2; 14 minimal vectors; cap/volume 19/18. All receipt fields match committed evidence except the command/output path.

An independent inline Python/SymPy calculation formed A=3B as the integer matrix `[[2,-1,-3],[3,-2,1],[1,3,-2]]`, found det(A)=−38 and every absolute row sum of B^(-1) equal to 3/2, and enumerated c in [-3,3]^3. It returned min |Ac|_1=6, with 14 minimizers. Thus any vector of norm <=2 is covered by the exact coefficient bound, and the number of minimizers is also justified.

Exact inline Python evaluated the boundary values of the relevant integer differences:

| Comparison | Last failing n, difference | First succeeding n, difference |
| --- | --- | --- |
| 19n^3−18(n+1)(n+2)(n+3) | 109, −9809 | 110, 2312 |
| 19n^2−18(n+1)(n+2) | 54, −36 | 55, 19 |
| 19(2n−1)^3−144(n+1)(n+2)(n+3) | 137, −127197 | 138, 24785 |
| 37n^3−36(n+1)(n+2)(n+3) | 217, −39059 | 218, 8504 |
| 37n^2−36(n+1)(n+2) | 108, −72 | 109, 37 |
| 74n^2−73(n+1)(n+2) | 219, −146 | 220, 74 |

Each expanded polynomial has positive leading coefficient and all remaining coefficients negative, hence exactly one positive root by Descartes' rule and continuity. These adjacent boundary checks prove the claimed eventual thresholds, rather than merely checking a finite window. The last three checks concern only arithmetic consequences of the gamma bound; they do not approve its certificate.

No unresolved defect was found in the local -02/-03/-04 proofs or their cap computation. Overall this assigned scope requests a developer response on T1 and a wording clarification on T2.
