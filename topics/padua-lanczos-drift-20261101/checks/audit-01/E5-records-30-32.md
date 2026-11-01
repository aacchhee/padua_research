# E5 audit findings (load-bearing question 6)

Auditor: Claude Opus 5.5, xhigh (independent mathematical auditor, one of four; not the developer). Model/depth chosen because the question is a novel analytic asymptotic plus scoped negative claims (CLAUDE_ROLES "Independent audit": Opus xhigh for adversarial analysis).
Repository `/home/claude/padua_research`, branch `codex/padua-lanczos-drift-20261101`, HEAD `36c93794ce02f92c76c89e5a9ec8095eb238d91d` (scientific source `b09e1dbe…`). No repository file modified, no state-changing git command; `git status --porcelain` empty after all runs. Scratch: `/tmp/claude-0/-home-claude/86053f32-48fa-5413-a794-72c84a52bfb6/scratchpad/audit/E5/`.

Audited content (SHA-256, equal to `e5-manifest.json` and to the hashes pinned by `evidence/independent-math-01.json` / checks Supplement 01):
- record30 `54f90362a5d85a37447a4589fd735fabc966e25c7fa4665968a4ff144b7adc00`
- record31 `50ddbc5d914431a245a84c59832a460b7f0f969db3c9ff37821bf47ee557d7d8`
- record32 `12e8cbfb9c8cc5a114dacdd92fdb88c0c05de6bf8a050f42edff0a77dd8b41b7`
- `e5_exact_checks.py` `548802feeb7be30bbf8a888be8aa95678534655e19c50746e24e697343a8bc8e`; `e5-exact-checks.json` `ba6efdcd…dacd3`; E5.md `b8ecb7cc…593ac`; ideas-e5.md `cbffb519…9d1e9d3`
- predecessors: PD-T075 (claude-319) `f7c1f4f9…181f36`; PD-T069 (claude-313) `edaa5e22…2edb23`; PD-T056 (claude-300) `d44253af…c30070`; PD-T061 (claude-305) `f1a6d410…bbe`; PD-T058 (claude-302) `c63d57f7…34d3`.

## (a) Files read

AGENTS.md; agents/claude/CLAUDE_ROLES.md (Independent audit); agents/WORKFLOW.md (status table, split rules, REJECTED/PD-N rules, lines 65–107 by grep/read); handoffs/02-audit.md (full), 01-work.md (task section); topic LOG.md, report.md, plan.md (E5 row), directions/E5.md, ideas-e5.md, independent-checks.md, checks/independent-math-01.md, evidence/e5-exact-checks.json, evidence/e5-manifest.json, evidence/independent-math-01.json (E5 and input-hash entries), proposed-record-changes.md, local-results-entry.md; code/drift/README.md (setup + E5); `e5_exact_checks.py`; records 30/31/32 (full); predecessors in full: PD-T075 (319), PD-T069 (313), PD-T061 (305), PD-T056 (300, lines 1–66); PD-T058 (302) and PD-T057 (301) by targeted grep of (R1)–(R3), consistency and sections; PD-N022 (N303) and PD-T059 (303) by grep of radius/(e). state/IDEAS.md: targeted grep for radius/positivity/Greenbaum/square-root/backward/Turán/corner plus full rows IDEA-152–176 (the full read is another auditor's). literature/INDEX.md LIT-263 row.

## (b) Commands actually executed (all from my shell; outputs in the scratch dir)

| # | Command | Result |
|---|---|---|
| 1 | `cd repo; PYTHONPATH=/workspace/padua-drift-runs/python-deps /usr/bin/python3.12 -B tracks/bivariate-lanczos/code/drift/e5_exact_checks.py > E5/e5-exact-checks-py312.json` | exit 0, PASS; identical to committed evidence except `"python": "3.12.3"` |
| 2 | same with `python3` (3.13.18) `> E5/e5-exact-checks-py313.json` | exit 0, PASS; identical except python line; SHA-256 `123bf266…44de` = byte-identical to orchestrator's `scratchpad/runs/audit-e5.json` |
| 3 | `python3 -I -B …/e5_exact_checks.py`; `python -B …` (no PYTHONPATH) | `ModuleNotFoundError: sympy` — expected; README lines 17–18, 60–61 document that `-I` ignores PYTHONPATH |
| 4 | `PYTHONPATH=… python3 -B E5/a_series.py` (11.8 s; SymPy 1.14.0) | own exact derivation, all true: from the raw definition (only cos nθ=−1, sin nθ=0, cos (n+1)φ=−1, sin (n+1)φ=0) f(0)=0, f′(0)=(n+1)cos mθ sin mφ−n sin mθ cos mφ, f″(0) formula, sine form, θ+φ=(2n+1)d. Exact Taylor series in h=1/n (all cosine arguments analytic at h=0): h^0…h^6 coefficients of g_m(ζ_n) vanish, h^7 coefficient = −a²−(2/3)aπ³m³ for m=0..3; h^0…h^13 of P vanish, h^14 coefficient = a²(81a²−360π³a+368π⁶)/18 = −6400π¹²/729 at a=20π³/9; n⁵Δx, n⁵Δy → −πa; n⁵·dist → 20√2π⁴/9. Coarse path t=A/n³: n⁵g_m→−A², n¹⁰P→9A⁴/2. Equal-phase and sine-sequence identities exact |
| 5 | `… python3 -B E5/b_numeric.py` (7.9 s; mpmath 1.3.0, 130 digits) | see table below; nearest Padua node to ζ_n is (1,1) for every tested n (brute force over all nodes n≤300; local search above); ζ_n ∈ (−1,1)² always; Chebyshev three-term recurrence vs cos(j·acos) agree to ≤1e-109 relative (n≤2000). Sign sweep n=4..3000 (80 digits): P_n(ζ_n)<0 for every n, first negative n=4 |
| 6 | `… python3 -B E5/c_square.py` (4.9 s) | record31 from the atoms: moment differences exactly e on x², xy, y², 0 elsewhere; mass 1; M,X,Y formed from moments equal the displayed matrices; minors 1, (9e+2)/9, (18e+1)/27; [A,B]₀₁=3e(12e−1)/(1+18e)², zero only at e=1/12; [A,B] kills the constant; orthonormal sections symmetric, commutator zero outside the degree-1 block (consistency), last block entry 3√3e(12e−1)/(18e+1)^{3/2}≠0; original μ sections commute; p jets zero on Z, ‖p‖₁=3, L_{μ_ε}(p)=e, L_μ(p)=0; float grid sup|p|/δ² on K_δ(Z), δ∈(0,1] = 1.795 ≤ 3 |
| 7 | `… python3 -B E5/d_arb.py 300` (Arb via python-flint 0.9.0, 400 bits) | P_n(ζ_n)<0 certified by ball arithmetic for all 297 n=4..300; max upper bound of n⁵|ζ_n−z_n| over that range 305.61 < 306.13. Finite only; not part of the claim |
| 8 | `… python3 -B E5/e_failed_paths.py` (0.4 s) | record32 parts 1–2 from the raw recurrence at 400 random (n≤60, α, θ, φ): max rel. err 2e-55; min sampled edge P 4.5e-6 > 0. Fixed-A n¹⁰P/(9A⁴/2) at n=10⁴: 1.0045 (A=−3), 0.9725 (0.5), 0.9930 (2), 0.9985 (10) |
| 9 | `… python3 -B E5/f_coarse_window.py` (5.7 s) | fixed-A paths have finite-n negative windows (n=4..3000): A=0.25: n∈[191,358]; 0.5: [93,181]; 1: [44,92]; 2: [19,47]; 5: [5,20]; 10: [4,10]; 20: [4,5]. η_{50}(a/50)=ζ_{50}, P=−2.28e-17 (see E5-F1) |

Record30 corroboration (cmd 5): n, n¹⁴P_n(ζ_n)/L, n⁵|ζ_n−z_{11}|/D (L=−6400π¹²/729≈−8.1143e6, D=20√2π⁴/9≈306.127):
4: 3.448, 0.9459 · 10: 3.4766, 0.9517 · 100: 1.37271, 0.99491 · 1000: 1.038531, 0.999499 · 3000: 1.0128738091, 0.9998332205 · 10⁴: 1.003865, 0.99995 · 10⁵: 1.000387, 0.999995. The n=10…3000 values agree with the independent checker's receipt to all printed digits. Ratios behave like 1+3.9/n and 1−0.5/n.

## (c) Per-record dispositions

| Record | Claimed status | Disposition | Reason |
|---|---|---|---|
| PD-T?drift-codex-30 (rho_n=O(n^-5)) | PROVED analytic, named certificate only | **CONFIRMED** | Both derivative identities, sine form, O(n⁻⁵) remainder in D, third-derivative bound n³+(n+1)³ (valid all t, 0≤m≤3≤n), Taylor remainder O(n⁻⁹), n⁷g_m limits, quadratic −4 at r=10/3, limit −6400π¹²/729, distance limit and ρ_n≤|ζ_n−z_n| all reconstructed by hand and by exact series (cmd 4). Nodes/parity/K_δ/Euclidean closed balls match PD-T075/PD-T069 verbatim. Limit ⇒ ∃N with P_n(ζ_n)<0 for n≥N, so limsup bound needs no numerical threshold. U1 exactly as worded in PD-T075:15 is answered; U2 correctly untouched. Only editorial items E5-F4, F8 |
| PD-T?drift-codex-31 (square four-atom family) | PROVED explicit, not reading (G) | **CONFIRMED** | All moments, ε-perturbation in max-monomial-moment norm (dual of coefficient l1), M,X,Y, PD minors, commutator, exact consistency, √(6ε) spread, cubic jets, ‖p‖₁=3, L(p)=ε, local bound |p|≤3δ² (sup actually ≈1.8δ²), and δ≥√((1−3γ)ε/3) reproduced (cmd 6, by hand). (R2) usage correct: E∈H₀, reference L_{μ_ε}, unit-mass ν. Correctly scoped as reading (E); (G) disclaimer accurate (μ itself fits at residual ε, radius 0). Only E5-F3(c), F7 |
| PD-N?drift-codex-32 (three failed paths) | PROVED, scoped | **CONFIRMED-WITH-CORRECTIONS** | Parts 1–3 mathematically correct (cmds 4, 8). PD-N vehicle appropriate (tested mechanisms failing their stated aims, WORKFLOW:91–93; handoff 01 authorizes scoped PD-N). Correction needed: the title/preamble/attempted-mechanism wording over-states case 3 (E5-F1); stale "independent reconstruction pending" (E5-F2) |

Findings by severity: high 0; medium 1 (F1); low 7 (F2–F8).

## (d) Findings

**E5-F1 — medium — record32 case-3 scope wording claims more than is proved.**
Location: `tracks/bivariate-lanczos/theory/drift-codex-e5-32-failed-negative-witness-paths.md:1` (title "fail to provide negative witnesses"), `:14` ("The following proposed paths fail to supply a point with `P_n<0` within their stated ranges"), `:54` ("Attempted mechanism: find an upper-bound witness … at a fixed nonzero common angular displacement A/n^3"). Item 3 itself (`:28–32`), the status row `:48`, IDEA?drift-codex-34 (ideas-e5.md:78, 87) and E5.md:32 are correctly "eventual".
Evidence: what is proved is only that for each fixed A≠0 the path is positive for n≥N(A). Finite-n negative points do lie on fixed-A paths: identically η_{n₀}(a/n₀)=ζ_{n₀}, which is negative for all large n₀ by record30 itself (rigorous), and numerically (cmd 9) A=1 is negative for n∈[44,92], A=0.5 for n∈[93,181], A=10 for n∈[4,10]; such points give finite-n upper bounds on ρ_n. Read with ":38 Cases 1–2 hold at every integer n>=4" in parallel, the preamble invites the false reading "no negative point on these paths".
Required response: reword title, preamble and negative-result scope so case 3 rejects only the *eventual (all-large-n) negative-witness* mechanism at fixed A; add the remark that fixed-A paths do contain finite-n negative points (η_n(a/n)=ζ_n). No change to the theorem in item 3. Propagate the qualifier to the report sentence requested in F6.

**E5-F2 — low — stale "independent reconstruction pending" for record32.**
Location: record32 `:42` ("independent reconstruction pending"), `:132`, `:140`; `directions/E5.md:53`; `evidence/e5-manifest.json:40` ("Pending distinct reconstruction").
Evidence: `checks/independent-math-01.md:119` (Supplement 01) reconstructs all three parts and `:127` pins record32 at `12e8cbfb…`, identical to the current file; `independent-checks.md:53` and `LOG.md:71` also say it was reconstructed.
Required response: metadata-only update of these lines (status remains PROVED).

**E5-F3 — low — developer checker coverage described more broadly than it is.**
Location: `e5_exact_checks.py:14–25`, `:24–25`, `:58–66`, `:72–82`; record30 `:63`; record31 `:89`; E5.md `:36`.
Evidence: (a) `corner_cubic_leading_limit` only checks lim n³·(the displayed cubic), not that −(k³−k)(md)³/12 equals it nor that it is the leading term of D; (b) f is entered already shifted by nθ=(n+1)φ=π, so the node reduction is unchecked; (c) M,X,Y are typed in, and the "moment" check covers only the origin split, so "displayed matrices = moment matrices of μ_ε" is not machine-checked by the developer script. Not load-bearing: the proofs are analytic, and the independent checker (receipt `moment_matrices_built_from_four_atoms: True`) and this audit (cmds 4, 6) cover (a)–(c).
Required response: state the checker's exact coverage in record30:63/record31:89 (or extend the script). No status change.

**E5-F4 — low — record30 understates where the witness lies.**
Location: record30 `:40` ("the explicit witness itself lies in the square for all sufficiently large n").
Evidence: ζ_n is a pair of cosines of angles in (0,π), hence in (−1,1)² for every n (cmd 5 confirms). Consequently the theorem holds verbatim if K_δ(n) is intersected with [−1,1]², which is worth stating for readers using a square-restricted radius.
Required response: editorial rewording.

**E5-F5 — low — literal proposals omit needed propagation for the U1 split.**
Location: `proposed-record-changes.md:41–85`, `:125`; PD-T075 file `…claude-319…md:8` ("Split into: none."), `:60` Open item (2) ("An all-n argument for (U1)"), History; PD-T069 file `…claude-313…md:66` ("neither ρ_n → 0 nor the absence of a uniform obstruction radius is proved. Both questions are OPEN (PD-T?…-319)").
Evidence: the three PD-T075 OLD blocks match exactly once (checked) and the PARTIAL label is rule-compliant (U1/U2 are explicit parts of PD-T075's statement, WORKFLOW:72, 85). But WORKFLOW:85 also requires `Split into:` and History in the original; only a generic sentence at `:125` covers this, and PD-T069:66 would become stale once U1 is PROVED, with no block proposed. Optional: PD-T061 Open item "Explicit constants" could cross-reference record31 as one explicit instance.
Required response: add literal OLD/NEW blocks for PD-T075 `Split into`, Open item (2) and History, and for PD-T069:66, before preparation.

**E5-F6 — low — report omits the new PD-N.**
Location: `report.md:84–106`; `local-results-entry.md:28` ("Failed witness paths retained").
Evidence: PD-N?drift-codex-32 and IDEA?drift-codex-32–34 are new durable records under audit but are not named in the report; plan.md:24 and LOG.md:62 do name them.
Required response: one report sentence naming PD-N?drift-codex-32, its three scopes and the case-3 "eventual" qualifier (F1).

**E5-F7 — low — IDEA?drift-codex-31 names the wrong closest predecessor and mixes two dispositions.**
Location: `ideas-e5.md:27–38`, especially `:29`, `:33` and `:37`.
Evidence: (a) the closest entries listed are PD-T056/058/059/060 and PD-N020/022. The closest predecessor is actually PD-T061 (claude-305: every triangle n=1, δ*≍√ε with abstract constants, Open item "Explicit constants"), with IDEA-157. Record31:5 itself cites PD-T061. (b) The entry is titled "residual-aware nonexact reading-(G) construction" with alias "actual computed section data", but the delivered result is a reading-(E) instance, and one disposition combines "retained (E) refinement" with "(G) deferred". A registry row built from it could be read as (G) progress. The kill/separation criterion is present.
Required response: name PD-T061/IDEA-157 as the closest predecessor. Then either split the entry into a deferred (G) IDEA and a retained (E)-instance IDEA, or retitle it.

**E5-F8 — low (optional, not a defect) — a sharper constant is available within the same construction.**
Location: record30 `:30`, `:115–131`; Open item `:143`.
Evidence: cmd 4 gives lim n¹⁴P_n(ζ_n(a)) = a²(81a²−360π³a+368π⁶)/18 for general a>0. This is negative iff a/(2π³/3) ∈ (10/3−2√2/3, 10/3+2√2/3), so a=20π³/9 is the vertex, not the smallest admissible a. Letting a decrease to the lower root gives limsup n⁵ρ_n ≤ 2√2π⁴(10−2√2)/9 ≈ 219.54 (claimed: 306.13). The claimed bound remains valid.
Required response: none required. Optionally mention it under "sharper upper witnesses".

## (e) Remaining uncertainty

- The symbolic and series checks trust SymPy 1.14.0, mpmath 1.3.0 and Arb (python-flint 0.9.0). The hand reconstruction of record30/31 does not depend on them.
- The Arb sign certificate for n=4..300 and the numeric sweep to n=3000 are finite checks I added. They do not by themselves give an explicit all-n threshold. Combined with explicit constants in the D-remainder they could, but I did not do this, and the record makes no such claim.
- PD-N bundling: record32 puts three IDEA mechanisms (32/33/34) in one PD-N. WORKFLOW:93 ("A separate evidenced mechanism failure still gets its own PD-N") is ambiguous on whether that means one PD-N per mechanism. Registry precedent PD-N029 bundles two mechanisms. This is left to AC or preparation; I raise no finding.
- Novelty: I did not read state/IDEAS.md in full; that read belongs to another auditor. Targeted searches found no prior all-n Padua radius witness. No historical novelty is claimed in the records, and none is endorsed here.
- I did not audit PD-T075's cited reviewer lower bounds b_n (n=4..12). They are consistent with the new upper bound: the n=12 sampled negative radius 3.46e-4 is below 306/12⁵≈1.23e-3, and 6.55e-8 ≤ ρ_12.
