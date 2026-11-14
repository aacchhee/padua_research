# N4 — notation, first-use and named-tool audit of both revised manuscripts

Audit-04 (handoff 30), sub-report N4. Editor/checker: Claude Opus 5.5, xhigh (independent of the
Codex developer). Rules read at branch head `70a50d7b2a72a30fd7a2af3b2ead54ae14470bf9`
(AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md, handoff 30, onset-512 brief).
Audited TeX/Bib freeze `24a98db4c3c4c4d0eede2e3929532956df87911b`; the paper/companion `.tex`
files are byte-unchanged between 24a98db and 70a50d7 [E: `git diff --stat` on `*.tex`, empty].
Read-only on the repository; no git state change. Labels: [D] read at the cited line, [E] from
an executed script, [I] editorial judgment. Locations: `P file:line (p.N)` = paper source line
and printed page; `C line (p.N)` = companion line in the same-named file. File names drop
`-unified.tex`. Section numbers are the revised ones (4.1 model, 4.2 finite comparison,
4.3 scalar gates, 4.4 selected pairs, 4.5 corner descent; 5.1–5.3).

## 0. Coverage, commands, resources

- Paper read in full by hand [D]: introduction, preliminaries, corner (556 l.), localization
  (432), comparison (1641), certification (443), main.tex. Companion (10121 l.): scripted scans
  of all sections plus hand reading of every flagged site and of the tool statements cited below;
  not read line-by-line in full (scope limit, disclosed).
- Trees: `git archive` of f366535 (audit-03 register head), b45e29f, f77b668, 24a98db into
  `n4-code/trees/`. SyncTeX build of 24a98db (template copied from B4's `build/`): 51 and 147
  pages; all compiled label numbers identical to B4's build and pdftotext output byte-identical
  to B4's paper text [E].
- Scripts (python3 stdlib) in `n4-code/`: `scanner/` (copy of audit-03 `notation_scan.py` and
  helpers), `firstuse.py` (new), `tools.py`, `terms.py`, `where.py`, `blocks.py` (new);
  outputs in `n4-code/out/`. Total CPU about 1.5 min including both LaTeX builds.

```
python3 -I scanner/notation_scan.py --repo trees/<sha> --out out/<sha>                     # (a)-(d)
python3 -I scanner/notation_scan.py --repo $REPO --paper-dir trees/f77b668/.../paper \
   --companion-dir trees/f77b668/.../companion-paper --baseline-rev b45e29f... \
   --rename-map $REPO/topics/.../notation-rename-map.json                                    # exit 0
python3 -I scanner/notation_scan.py ... trees/24a98db ... --baseline-rev f77b668... --rename-map empty.json  # exit 1
python3 -I scanner/notation_scan.py ... trees/24a98db ... --baseline-rev 24a98db... --rename-map empty.json  # exit 0
python3 -I firstuse.py --scanner scanner --paper ... --companion ... --paper-synctex ... --out out/firstuse
```

## 1. Scan re-run and rename-aware checks [E]

| Text / revision | lines | math regions | base symbols | def. sites | (unit,token) >1 def | (unit,base) >1 token | bases defined in >1 unit | numbered eqs |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| paper f366535 (register baseline) | 3035 | 1817 | 113 | 367 | 18 | 60 | 61 | 92 |
| paper f77b668 (rename checkpoint) | 3035 | 1817 | 140 | 363 | 19 | 55 | 63 | 92 |
| paper 24a98db (freeze) | 3471 | 2044 | 127 | 354 | 24 | 44 | 64 | 86 |
| companion f366535 | 10593 | 5832 | 125 | 578 | 67 | 89 | 68 | 92 |
| companion 24a98db | 10121 | 5577 | 150 | 545 | 62 | 73 | 70 | 86 |

- Baseline reproduced exactly (paper 18/60/61, companion 67/89/68) [E].
- Codex checkpoint reproduced: f77b668 vs b45e29f with the committed 118-entry rename map —
  PASS 13 statements / 90 displays, PASS rename check, exit 0 [E].
- 24a98db vs f77b668 with an empty map FAILS on content-changed blocks (paper and companion
  identically): statements uc:central-pair, uc:finite-bounds, ul:selected-pairs and one
  certification statement; displays uc:coarse-input, uc:scalar-constants,
  uc:central-pair-general/-bounds, uc:constants, uc:phase-allowance, uc:global-error,
  uc:relative-comparison, uc:absolute-components, uc:sinc-row, uc:origin-variation,
  uc:relative-components, uc:signed-outer, ul:finite-floors, ul:tail-floors, ul:log-series,
  ul:near-base, ul:near-floor [E]. Expected: the onset-512 rewrite is a content change, so
  the rename-aware chain from b45e29f ends at f77b668; 24a98db is the new block baseline.
- 24a98db current-vs-current PASS 19 statements / 85 displays; 24a98db vs 24a98db PASS [E].
- Interpretation [I]: (unit,base) flags fell 60→44 (paper) and 89→73 (companion), consistent
  with the renames; (unit,token) flags rose 18→24, mostly new local roles in the rewrite
  (C, C_*, I, Q, e, k, w in 4.1–4.4; listed in out/24a98db/flags-paper.txt). The statistics are
  heuristic, not a collision count; the hand dispositions in §2–§3 are the result.

## 2. Register disposition (audit-03 n-notation.md, 32 grouped entries / 61 bases) [D]

R = resolved (rename or removal of the old outer-gate section); P = partly; O = still open;
N = new in the onset-512 rewrite. "A" = same subsection/proof, "B" = carried across sections.

| # | Symbol | Disposition at 24a98db |
|---|---|---|
| 1 | ε | R: \hat ε, ε_h, ε_d, e_t, ε_j glyph in §2–3. O(B): weights written e_j,f_k in (24) (P localization:13, p.15) duplicate ε_j,η_k of §2. |
| 2 | T | R: 𝔗, u_−. O(B): T_t (4.1), T_0,T_{0,r},T_out (4.2), 𝒯_c (4.4), 𝒯 (§5). N: trig. polynomial T (P localization:331, p.40). |
| 3 | H | R: \bar L, 𝓥. O: H(w),H_0 beside H_n, H_j(q) (4.1–4.2); H_h; H_rs. |
| 4 | C | R: C_±(v). O: generic C vs C=−1+C_H+C_B (§3); C,D of I(C,D,e). N: C as synonym of A(0) (P localization:263, :299, p.40); C=t_*+2K_D (P comparison:1540, p.36). |
| 5 | D | R: 𝒟_n, w_b. O(A 4.1/4.2): allowance D, D in proof of L.4.3, D of I(C,D,e), D_h, D′. |
| 6 | k,K | R: 𝔨, 𝔨_0, μ. O(A): K = Lip constant (comparison:97), truncation K=3 (:494, N), K(k) (:588), chart K, K=sinc·sinc (:1044), K=L+25log(2m)+193/3 (:1201), K_t, K_D. |
| 7 | j,J | R: 𝔧. N/regression: plain j_* in Cor. 4.6–4.7 (comparison:1514, p.36) instead of 𝔧_*. O: J(x), J(v,s,e), chart J, J_6. N: J=48 term count inside (49) (comparison:500, p.24). |
| 8 | a | R: a=2/π vs c_ec_d (now 𝖺) — the main collision; band a_0; old a_0=337/384 removed. O(B): a_j, a_ρ̄, §5 coordinate a; generic a in "(a log n+c)/n^k" (comparison:1115, p.32). |
| 9 | A | O/worse: A(z), A(v), A_4, A_6, A(u,v), A(b), A_L,A_R, A=398/(11π²), inward A. N: A_* two meanings in one proof (localization:173 vs :287, p.38/40); A_N(q) (comparison:501, p.24); A(h) (comparison:1542, p.36); dummy cot A+cot B (corner:177, p.9). |
| 10 | B | R: 𝒩_n(t). O: B(x), B_0, B, B_β, B_j, B_out, B_n(ρ̄), B_i^n, inward B. N: B(h) (4.3). |
| 11 | g | R: f″, 𝔤. O: g(C,D;t), g_0, g_j, g_n, g_L,g_R, g_ση, §5 descent margin g. |
| 12 | f,F | R: \tilde g, 𝔣. O(A 4.4): f_k weights, f_b(z), generic decreasing f in one proof; f(u,v), f(w), f_j, f_σ, f_ε. |
| 13 | r,s | R: \bar ρ, i. O(A 4.2): s as J-argument, ±y/π, side label, ∫_0^S ds. |
| 14 | L | R: (\bar m,\bar n). O: L_B/L_ℓ, L_n (§3), L_{n,k}, L_c. N: ‖L_n′‖_1 (comparison:1348, p.34) reuses L_n (square reference). |
| 15 | M | R: mesh M. O: M(n), M_∞, 𝓜, M_A, M_*, M of L.5.1; undefined M in "M tan(e/2)" (N4-01). |
| 16–17 | Q, R | O (no rename proposed in audit-03). Companion I_L,I_R (C comparison:1156, p.68) adds an R-labelled I beside bilinear I_R of §5. |
| 18 | γ,κ,ζ,ψ | R: θ_c; companion c_Γ, 𝗎, 𝗁_B. N: ζ = physical phase shift (localization:188, p.39) vs Riemann ζ (comparison:96, p.18). |
| 19 | e | R: upright e^{i·} in §3; 𝔢. O: e_j weights (§4 pre.) vs e_j endpoint comparison (comparison:1226, p.33) — same token. Glyph: italic e^{1/4} (comparison:238, p.20; C 612, p.61). |
| 20–21 | b, c | O. N: undefined c (comparison:1351, p.34). |
| 22 | d | R: d_*. O: d=v/h_*, d(z). N: degree d in Bernstein's inequality (localization:331) vs reserved d of (3). |
| 23 | h | O(A 4.2): h=π/m (:695) and h=π/n (:757). N: h=ρ/2 (:1540). |
| 24 | u,v,w,z | R: v_*. O(A): u angle vs u=1−𝖺 inside Thm 4.5's proof; w argument vs coefficient (4.1); effective angle w vs w_b (4.4). N: w,z of (49) (4.1, z=(1−c_e)(1−c_d) same subsection). |
| 25 | p,P,q | R: q_h. Regression: 𝔭(ρ) became P_n(ρ) (N4-03). N: p,q indices of 𝔞_p,𝔟_q,c_k (comparison:468–472) vs p=sin x, q=sin y (4.1). |
| 26 | δ | O/worse in 4.1: δ=x−y (:306), δ=9/4−C_* (:540), δ=q/2 (:570). N: δ=(x−y)/2 (:1540, 4.3). |
| 27–28 | η,σ,τ; ℓ | R: \hat ℓ, ℓ_h, ℓ_x,ℓ_y. O: ηj (4.2) beside η_±; ℓ_r(x,b); arc length ℓ and row l (4.4). |
| 29–30 | I, E | R: B_n^♯. O: I_s undefined (N4-01); E-family. |
| 31 | S,N,U,V,W,G,Z,Γ | R: old gate 𝒢,𝒦,𝒜 (section removed). N: G(n,ρ_1) vs kernel G_n; U (Cor 4.7) vs U=V=π²/32 (4.5, §5) and U_W; Z_s vs Z(v,s,e), Z_n; Θ (two meanings, N4-03). |
| 32 | α…t | P: α_r only in 3.1, α in 3.3 proof (corner:388, :492). N: ξ=x/π (4.2) vs ξ periodic shift (4.4). |

Net [I]: the register's main A-class collisions with a proposed rename are resolved (a/𝖺, 𝔗, 𝔧,
𝔨, \bar L, C_±, 𝓥, 𝒲, 𝒩_n, ε-family, f″, \tilde g, V_F, 𝒟_n, u_±, \bar ρ, i, θ_c, (\bar m,
\bar n), B_n^♯, w_b, q_h); entries without a proposed rename (K, h, u, w, s, δ, Q, R, E, A, B)
remain; the rewrite adds about fifteen new local collisions, five of them in numbered blocks.

## 3. Findings

**N4-01 — MAJOR (paper; mostly also companion). Symbols used before definition or never
defined.** Reason: AC's criterion "notation must be introduced before use". Impact: a reader
cannot check the step. Each item is a small local fix; together they block the criterion.
- ρ, A, B and the gate P_n first appear in the §4 roadmap table and Fig. 2 (P localization:82,
  :85, :107–114, p.16; C 287–317, p.51–52); ρ=x+y is defined in 4.1 (P comparison:8, p.17;
  C 32, p.52), A,B in L.4.9 (p.40), the gate P_n in Cor 4.7 (p.37). Fix: one sentence before
  the table defining ρ=|α|+|β|, the inward phases A,B and forward-referencing Cor 4.6–4.7.
- I_s(φ,z) and the phase point φ in 𝒞_s and E_n(φ) (P comparison:1387, :1495, p.35–36; C 3586,
  3874, p.99/103): neither I_s nor φ (phase point) is defined in the paper; the companion's
  I_L,I_R (C 1156, p.68) is 2400 lines earlier with another signature. Fix: define I_s(φ,z) as
  the side-s complete cancellation integrand at phase φ and write φ=(x,y).
- M in "heights at most M tan(e/2)" (P comparison:887, p.29; C 2204, p.82): undefined (M(n)
  is the global norm on p.26). Fix: "with M=max(|C|,|D|)".
- c in "(c_e+c_d)/(2c)… c>99/100" (P comparison:1351, p.34; C 3442, p.98): undefined. Fix:
  name the two denominators c=cos(y/(2m)), cos((π−y)/(2m)).
- θ_0 in "Σ|θ_±−θ_0|≤ρ/π" (P comparison:1281, p.34; C 3242, p.95): undefined. Fix: θ_0 =
  value of θ_± at the origin.
- U_{n−1} (P comparison:1334, p.34): undefined in the paper (companion defines it, C 3409, p.97).
- Li_2 (P comparison:441, p.23): dilogarithm undefined in the paper (companion C 1122, p.68).
- D_φ used (P comparison:909, p.29) before its definition in (65) (P :915, p.30); same in C 2263/2278.
- J_end, J_cen (P comparison:694, p.26; C 1574, p.74): split of A_6 never stated.
- Dot derivatives Ḃ_j, U̇_j, ė_j, Ḣ_h, Ḋ_h (P comparison:1240–1323, p.33–34; C 3093, p.93):
  "derivative along the straight phase path" is not stated as notation.
- Lemma 5.1 (P certification:30–39, p.42; C 117–133): M, ω_a, ω_b are not quantified, W_z/W
  and I_R are used before "Here I_R is bilinear interpolation".
- L_{jk} (P corner:59, p.7; localization:16, p.15): never defined (L_B indexed by (j,k)).
- Minor order slips: F_r(θ_j) four lines before its definition (corner:166 vs :170, p.9);
  "leaf" (certification:14, p.42) before the tree definition (:102, p.43); I_n in the
  introduction (introduction:8, p.2) before the node set (:39) and its formula (prelim.:7).
- Abstract: γ undefined in the paper abstract (main.tex:31); the companion adds it.

**N4-02 — MAJOR (paper). Named tools that the paper only names.** Reason: AC's criterion
"named tools must be cited or defined/stated in the actual form used"; the brief requires the
paper to contain its own premises. The companion already states most of them, so the fix is
to move 1–3 lines into the paper. See the table in §4 (rows marked "named"). Most consequential:
the tangent partial fraction (P comparison:396, p.22), the triangular-kernel identity for the
second difference (:241, p.20), Li_2 and its derivative (:441), the discrete layer-cake count
(localization:246, p.39), the centered-cell BV quadrature bound (comparison:1004 etc., p.31),
the Fourier-convergence step behind the cot partial fraction (corner:361–365, p.12), and the
binary64/Horner/pairwise error model, which the paper delegates to the package
(certification:355–363, p.47).

**N4-03 — MINOR (both; numbered blocks). New collisions in the onset-512 gates.**
- P_n = T_{n+1}+T_n (P localization:20, p.15; used comparison:675, p.26) versus the gate
  quadratic P_n(ρ) of (74)–(75) and Cor 4.7 (comparison:1586, p.37), used in Fig. 2 and the
  proof of Thm 4.10 (localization:418, p.41). The notation pass had 𝔭(ρ); the rewrite
  re-used P_n. Fix: 𝔭_n(ρ) (free token, 0 occurrences [E]).
- Θ = half-line correction (62) (comparison:793, p.28) versus Θ=𝔗+j_* in Cor 4.6 and (71)
  (comparison:1514, p.36). Fix: 𝔗_* for the gate curvature (free token [E]).
- G(n,ρ_1) of (71), Cor 4.6, Cor 5.2 versus kernel G_n (7). Fix: 𝒢(n,ρ_1) (free [E]).
- U=𝔗−ē+A_4+j_* (Cor 4.7, comparison:1573) versus U=V=π²/32 (localization:357, p.41;
  certification:252, p.46) and U_W. Fix: U_* (free [E]).
- j_* plain instead of the audit-03 𝔧_* (Cor 4.6–4.7). Fix: 𝔧_* (free [E]); t_* may stay.

**N4-04 — MINOR (both). Same-proof collisions new in 4.4.** A_* is the numerator floor
(localization:173, :210, :218) and, in the same proof, a numeric constant (:287, p.40; C 452
vs 863). C=a_ρ̄−ρ̄/2 (:263) and C=15/16−1/4 (:299) reintroduce the symbol that the rename
replaced by A(0) (localization:257). Fix: A_♯ for the constant (free [E]); write A(0) instead of C.

**N4-05 — MINOR (both). New local collisions in 4.1/4.3.** Elementary-constant block
(comparison:494–517, p.24; C 1268–1290, p.70): K=3 vs K(k)/Lip K; w,z of (49) vs w and
z=(1−c_e)(1−c_d); J=48 vs J(v,s,e); A_N(q) vs A-family and reserved N=n+1/2; Z_s vs Z(v,s,e).
Indices p,q in 𝔞_p,𝔟_q,c_k (:468) vs p=sin x, q=sin y. δ has three meanings in 4.1 (:306,
:540, :570) and a fourth, δ=(x−y)/2, beside h=ρ/2 and local A,B,C,R in the proof of Cor 4.6
(:1540–1544, p.36). ζ as physical phase shift (localization:188) vs Riemann ζ (comparison:96).
Fix: 𝒜_N(q), ζ_{10}(s), \tilde ξ for the physical shift; in the Cor 4.6 proof rename the
locals or state that they are local; leave J (it sits in display (49)) with a remark.

**N4-06 — MINOR (paper; some also companion). Terms of art used without definition.** Listed
in §5; the companion defines most (Cauchy sum, collision, chart centre, leaf, reproducing
kernel, half-line defect, layer cake, Peano kernel, bandwidth). Undefined in both: "board
sum"/"complete signed board sum" (Thm 4.5 statement, comparison:645, p.26; C 1506, p.73),
"global real-phase norm" (localization:67, p.16), "wide domain" (comparison:1220, :1306,
:1319, :1412, p.33–35; C 3056, p.93: a stale term, now only ρ≤1), "linked cyclic vector",
"sine chord", "entropy expression", GRID/TREE (certification:346, p.47: not tied to (85)/(86)).

**N4-07 — MINOR (both). Register items left open** (rows 6, 13, 19, 23, 24 of §2): the K
family (seven meanings in 4.1–4.2); h=π/m and h=π/n in 4.2; u as angle and as 1−𝖺 inside
Thm 4.5's proof; e_j with two meanings within §4; e_j,f_k vs ε_j,η_k for the same weights
(display (24) — touches a numbered block); reserved a,c,d reused generically
(comparison:1115; localization:331).

**N4-08 — MINOR (both). Constants consumed far from their definitions without reminders.**
δ_A, δ_D (localization:361–362, p.41) consume 𝔗, ē, 𝔧, C_4, k_Wy, \overline C_E, K_D from (53)–(54)
(p.25–26); Cor 4.6–4.7 (p.36–37) the same. No \eqref{uc:constants} or \eqref{uc:uniform-allowance}
occurs after 4.2 in either text [E: grep]. The companion's "Returning to the comparison
outputs" table (C localization:324–339, p.104) lists outputs, not these constants.

**N4-09 — MINOR (companion only).** A_N has two conventions in §5: A_N(x), N+1 terms
(C certification:511, p.123), and A_80(q), 80 terms in 1/q (C :1639, p.142); the paper's
A_N(q) has N terms (P comparison:501). "Support I_i" (C comparison:2251, p.83) after the rename
to Ω_1,Ω_2 two lines above. Stale source comment "companion to the frozen 48-page journal
manuscript" (C main.tex:1; not typeset).

**N4-10 — EDITORIAL.** S_n(0) vs S_n(0,0) (localization:73); 𝓔(h_*,v,t) then 𝓔(v,t)
(comparison:1261/1270); "(7)" cited as the divided-difference kernel, which is the unnumbered
form at localization:21 (comparison:671); integers "m,e" in m2^e (certification:362) reuse m=n+1
and e; ν as a measure (comparison:108) vs ν_p; λ_0 vs λ_n; α vs α_r in 3.3.

**N4-11 — NOTE (citations).** Correctly cited: Boas (Bernstein), Lorentz (Bernstein form, de
Casteljau), Mesh2024, Arb/FLINT/MPFR/GMP, Kolomoitsev–Lomako, Kuznetsova, Pimenova. Not cited,
though they are trust premises or classical tools: IEEE Std 754-2019, NumPy/Python, a numerical-
analysis source for Horner and pairwise rounding (e.g. Higham 2002), a Fourier-series uniqueness
theorem, Machin's identity (classical; stated, so optional), interval arithmetic (Moore).

**N4-12 — NOTE (process).** Every proposed paper edit, even prose-only, changes the TeX freeze.
It therefore needs a new source commit and a `check_correspondence.py` FINAL_BASELINE update
(CORRESPONDENCE-REVISION.md). Block-touching renames also need a rename-map entry. Self-test
[E]: renaming the gate P_n to 𝔭_n in both texts passes with a 3-entry map
(`--baseline-rev 24a98db`, exit 0). Without the map the check fails on exactly uc:relative-gate
(Cor 4.7), ul:wide-polynomial (74) and uc:relative-gate-bounds (75), in both texts
(`n4-code/selftest/`).

## 4. Named tools (paper p. / companion p.) [D][E: tools.py]

"stated" = hypotheses and conclusion in the form used; "named" = name or a one-word appeal only.

| Tool | Paper | Companion | Support | Gap |
|---|---|---|---|---|
| Euler–Maclaurin | not used | not used | trapezoid/Peano identity stated instead (corner:319–322) | none |
| Peano kernel (linear / bilinear) | cert:48–49 (p.42), loc:346 (p.41) | C cert:174 (p.118) explicit K_x(t); C loc:993 | paper: sign+mass in words | NOTE: display the kernel in the paper |
| Squared Peano (even f) | loc:343 identity (p.41) | C loc:943–962 derivation | stated | none |
| Bernstein inequality (trig.) | loc:330–335 (p.40) + Boas | C cert:821–835 proof (Riesz-type formula, unnamed) | stated+cited | none |
| Bernstein, exponential type | cert:181 (p.45) + Boas | C 929 | cited only; the trig form suffices | NOTE: say f_ε(·,b) is a trig. polynomial and cite the stated form |
| Digamma ψ, recurrence, ψ(1/2), ψ′(1/2) | corner:139–149, 356 | C corner:68, 1130 | defined/derived | none |
| Termwise differentiation | corner:332–336 | C 1024 | stated | none |
| Cot partial fraction | corner:357–366 (p.12) | C comparison:960–1000 finite products | stated; derivation needs Fourier convergence (unstated) | MINOR: state/cite uniqueness (continuous, absolutely summable coefficients ⇒ equality) or use the companion's finite-product route |
| Tangent partial fraction | comparison:396 (p.22) | C 1023 (p.67) stated | paper: named | MAJOR part of N4-02 |
| Finite sine product / Σcot(z+ℓπ/n)=n cot nz | corner:183 (p.9) | C corner:349 (p.25) stated | paper: named | MINOR: display sin(nz)=2^{n−1}∏sin(z+ℓπ/n) |
| Quadrature L.3.1, trapezoid/midpoint | corner:303–329 | C 945 | stated+proved | midpoint use at corner:234 (p.10) precedes the lemma: add forward reference |
| Centered-cell BV quadrature | comparison:1004, 1093, 1183, 1423, 1458 (p.31–35) | C 1870, 2882 (p.78/91) stated | paper: one sentence in words | MINOR: display once (cell error ≤ (h/2)·Var) |
| Triangular-kernel second difference | comparison:241 (p.20) | C 620 (p.61) stated | paper: named | part of N4-02 |
| Layer cake (continuous) | comparison:252–256 (p.20) | C 637 | stated | none |
| Layer cake (discrete grid count) | loc:246 (p.39) | C loc:724 (p.110) stated | paper: named | part of N4-02 |
| Translate/rearrangement inequality | comparison:255, 580 | C 644, 1373 | one-line reason | NOTE |
| Dominated convergence | comparison:205 (p.19) | C 533 | stated | none |
| Tonelli / Fubini | comparison:571 (p.25) / :247 (p.20) | C 1354 / 630 | stated | none |
| Abel regularization | comparison:195–202 | C 540 | computed explicitly | none |
| BV, Var_per, derivative measure, δ_π | comparison:99–110 (p.18) | C 327–359 | defined | none |
| Lipschitz | comparison:97 | C 328 | defined | none |
| Dilogarithm Li_2 | comparison:441 (p.23) | C 1122 (p.68) defined | paper: undefined | part of N4-01/02 |
| Chebyshev U_{n−1} | comparison:1334 (p.34) | C 3409 (p.97) defined | paper: undefined | part of N4-01 |
| Reflection ψ(1−t)−ψ(t)=π cot πt | comparison:820 | C 1967 | derived from partial fraction | none |
| log/atanh series (49) | comparison:496 (p.24), first used :424 | C 1268 | stated | MINOR: :424 uses it before (49); forward reference |
| Arctangent alternating bounds, Machin | comparison:502–504 (p.24), cert:119, 350 | C cert:506–534 proved | paper: stated without remainder proof | NOTE |
| Sine/cosine alternating partial sums | comparison:1555, 1566 (p.37); cert:119 | C cert:1690 | named | MINOR: one line on the alternating Taylor remainder |
| ζ trapezoid/midpoint brackets; γ from H_256 | comparison:510–516 | C 1277–1290 | stated; monotonicity of H_M−log(M+1), H_M−log(M+½) asserted | NOTE: one-line proofs (companion has the statement) |
| Elementary bounds γ>23/40 etc. | used at comparison:162, :423–426 (p.19/22) | C 414 | proved later at :494–527 (p.24) | MINOR: forward reference |
| Jordan / sin z ≥ 2z/π | corner:256 | C 685 | stated | "sine chord" elsewhere undefined (N4-06) |
| Product-to-sum, geometric sums | corner:66, 79 | C 118, 161 | stated | none |
| Gram matrix, unisolvence, reproducing kernel | prelim:31–35, 77 | C prelim:146, 292 | Gram and unisolvent defined; "discrete reproducing kernel" named | MINOR: one-line definition in paper |
| de Casteljau; power→Bernstein; Chebyshev recurrence | cert:71–80, 113–117 | C 276, 414 | stated + Lorentz | none |
| Positive interpolation L.5.1 | cert:29–65 | C 117–223 | stated+proved | quantifiers (N4-01) |
| Horner, degree-25 Taylor error 84ε_fp t | cert:355–359 (p.47) | C cert:1690–1739 (p.142–143) derived | paper: bound stated, proof delegated to package | part of N4-02 |
| IEEE binary64 RN, subnormals, nextafter | cert:361, Table 1 (p.47–48) | C cert:1615–1632 (p.141) stated | paper: named premise | MINOR: 3-line model + cite IEEE 754 |
| Interval widening, pairwise summation | cert:360–362 | C cert:1789 (p.144) induction | paper: one sentence | NOTE |
| Arb, FLINT, MPFR, GMP | cert:431–432 | C 1589 | cited | none |
| NumPy, Python, C++ compiler | Table 1 | Table 1 | named as trust base | NOTE: cite or version-pin in text |
| Square completion (Cor 4.7) | comparison:1605–1611 | C 3984 | identities displayed | none |

## 5. Terms of art for a reader with university analysis [D][E: terms.py]

| Term | Paper first use | Defined in paper? | Companion |
|---|---|---|---|
| unisolvent | prelim:34 (p.5) | yes (\emph) | yes (C prelim:6) |
| cardinal polynomial | intro:81 (p.2) | yes | yes |
| Gram matrix | prelim:31 (p.5) | yes | yes (C 292) |
| checkerboard | prelim:25 (p.5) | by the displayed product | yes (C intro:123, \emph) |
| Cauchy sum | corner:4 (p.6) | no | yes (C corner:22, p.19) |
| collision | prelim:106 (p.6); corner:101 | no (implicit θ_j=φ_k / cos u=cos v) | yes (C prelim:636, \emph) |
| chart, centre, odd/noncorner centre | loc:25, :153 (p.15/38) | charts by display; "centre" no | yes (C loc:83) |
| eligible projection | loc:122 (p.38) | yes | yes |
| defect, pair defect, reflection loss | loc:49–55 (p.15) | yes (by formula) | yes |
| floor (finite/uniform) | L.4.8 (p.38) | by statement | yes |
| allowance | comparison:610 (p.25) | no ("explicit scalar functions") | partly (C 1441) |
| gate (absolute, relative) | §4.3 title (p.36) | by corollaries | yes |
| guard, seam, tie | cert:228, loc:34, :426 | partly ("tie" explained at loc:34) | partly |
| board sum, complete signed board sum | comparison:645 (p.26) | no | no |
| complete signed (cardinal) sum | cert:7–15 (p.42), first comparison:645 | yes in §5, after first use | yes |
| real-phase norm | loc:67 (p.16) | no | no |
| phase triangle / signed diamond | Fig. 2 caption (p.16), comparison:298/644 | caption only | yes (C comparison:20) |
| wide domain | comparison:1220 (p.33) | no (stale) | no |
| finite part, counterterm, cusp, atom | comparison:111–126 (p.18) | yes | yes |
| entropy expression | comparison:73 (p.18) | no | no |
| half-line defect | comparison:778 (p.28) | by formula only | yes (C 1888, p.78) |
| linked (sinc continuation, cyclic vector) | comparison:713, :1134 (p.27/32) | cyclic vector by display (:1331, p.34); "linked" no | partly |
| leaf, rooted binary tree, witness | cert:14, :102, :122 | yes (:102) after first use | yes (C cert:8) |
| numerical vs analytic far leaf | cert:199, :221 (p.45) | no | yes (C 1106) |
| GRID / TREE norm | cert:346 (p.47) | equations (85)/(86), not named | partly |
| near/far proxy, physical guard | cert:224–241 (p.45) | yes | yes |
| Bernstein basis/coefficients | cert:17–27 (p.42) | yes | yes |
| unit roundoff, binary64 | cert:353–361 (p.47) | ε_fp yes; binary64 no | yes |
| Peano kernel | cert:49 (p.42) | in words | yes (C loc:993) |
| exponential type | cert:181 (p.45) | no (cited) | "bandwidth" defined (C 799) |
| reproducing kernel | prelim:77 (p.5) | no | yes (C prelim:146) |
| effective angle, mesh discrepancy | loc:195–197 (p.39) | by formula | yes (C 518) |
| norm witness, phase cover | absent in both | n/a | n/a |

## 6. Concrete fixes [I]

1. **Symbol tables** (unnumbered `tabular`, as in §3). In the companion they do not touch
   check_correspondence blocks; in the paper they need the freeze update of N4-12.
   - §4 preamble, before the roadmap table: m, 𝖭, a_j,b_k, weights (rename e_j,f_k → ε_j,η_k
     — touches display (24)), J,K, α,β, x,y, ρ, Γ^−, H_rs, S_n, Δ_JK, 𝔡, Q_v,Q_h, P_n=T_{n+1}+T_n,
     inward A,B; "phase triangle", "signed diamond", "centre".
   - start of 4.2: one row per allowance of (53)–(54) and M(n), with meaning and consumer
     (Cor 4.6–4.7, L.4.9). This also fixes N4-08.
   - start of 4.3: j_*/𝔧_*, t_*, 𝔗_*, ρ_1, 𝒢, U_*, ℓ_x,ℓ_y,d_x,d_y, 𝔢,𝔣,𝔤, 𝔭_n.
   - start of §5: R, s,t, B_i^n, F, f_σ, M, ω_a,ω_b, W_z, I_R, q_R, V_R, θ_R, M_*, E, V_E, L_c,
     w_*, D_R, δ_R, r_R, p_±, U,V, W_x,W_y,W_xy, u′,v′, q, g, 𝒯, μ.
2. **Paper-wide renames** (both texts; free-token checked [E]; blocks from `blocks.py` [E]):

| Rename | Scope | Numbered blocks / statements touched |
|---|---|---|
| gate P_n(ρ) → 𝔭_n(ρ) | 4.3, Fig. 2, proof of Thm 4.10 | (74), (75), Cor 4.7 (self-test PASS with map) |
| Θ (gate) → 𝔗_* | 4.3 | (71), Cor 4.6 |
| G(n,ρ_1) → 𝒢(n,ρ_1) | 4.3, Cor 5.2 | (71), Cor 4.6 |
| U (Cor 4.7) → U_* | 4.3 | Cor 4.7 (statement) |
| j_* → 𝔧_* | 4.3 | Cor 4.6, Cor 4.7 |
| A_* (constant) → A_♯; C → A(0) | 4.4 proof | none |
| A_N(q) → 𝒜_N(q); Z_s → ζ_{10}(s) | 4.1 | none |
| ζ (physical shift) → \tilde ξ | 4.4 proof | none |
| e_j,f_k → ε_j,η_k | §4 preamble | (24) |
| local δ,h,A,B,C,R of Cor 4.6 proof → declared locals or decorated names | 4.3 proof | none |
| companion A_N(x) (C cert:511) → one convention | C §5 | none (prose) |

3. **First-use repairs (no blocks):** each item of N4-01, by adding the missing defining clause
   at the cited line. Lemma 5.1: "Let M, ω_a, ω_b ≥ 0 and vertex values W_z ≥ F(z)…". Add
   forward references for the elementary bounds (comparison:162, :423) and for the midpoint rule
   (corner:234).
4. **Tool statements to copy from the companion into the paper:** tangent partial fraction
   (C 1023), triangular-kernel identity (C 620), Li_2 definition (C 1122), U_{n−1} (C 3409),
   discrete layer cake (C loc:724), BV quadrature (C 2882), finite sine product (C corner:349),
   the binary64 RN model with an IEEE 754 citation and Horner bound (C cert:1615–1739, condensed
   to about six lines), and a uniqueness/convergence citation for the cosine-series step (or the
   companion's finite-product route).
5. **Terms:** define "board sum" (or replace it by "signed sum over Γ^−"), "real-phase norm",
   "centre", "Cauchy sum", "collision", "reproducing kernel"; delete "wide domain" (write "on
   ρ≤1"); name the GRID/TREE norms at (85)/(86).
6. **Bibliography (NOTE):** IEEE Std 754-2019; NumPy (Harris et al. 2020); Higham, *Accuracy
   and Stability of Numerical Algorithms*; a Fourier-series text. These are Bib-only changes;
   they also need the freeze update.

## 7. Limits

- The companion was scanned by script; only flagged sites and tool contexts were read. Absence
  of a flag is not proof of correct first use; the definition heuristic misses prose-only
  definitions (false positives were removed by hand) and may accept restatements.
- Severities: N4-01/02 are MAJOR because AC made first use and tool statements explicit acceptance
  criteria. Each sub-item is a local MINOR edit; none changes a claim, proof or status. Applying
  them changes the frozen TeX and is therefore a material source revision for freeze purposes,
  needing a new freeze and helper baseline.
- No mathematical statement was found false in this notation pass. Correctness is outside N4.
