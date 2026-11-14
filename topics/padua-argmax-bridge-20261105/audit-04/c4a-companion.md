# C4A — companion Sections 1–3 (front matter, introduction, normalization, corner): substantive audit-04 part

Part of the substantive Claude audit-04 (handoff 30, brief `claude-audit-brief-onset512-20261108.md`, "Both manuscripts", companion half, Sections 1–3).

- **Auditor:** Claude Opus 5.5, xhigh effort, independent subagent auditor (Claude audits Codex development). Read-only on the repository: no repository file written, no state-changing git command (only `rev-parse`, `status`, `diff --stat`, `archive` to scratch).
- **Rules read** at head `70a50d7b2a72a30fd7a2af3b2ead54ae14470bf9` (Rules 70a50d7): `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`, handoff 30, the onset512 brief, companion `README.md`, `BUILD.md`, `review.md`, `CORRESPONDENCE-REVISION.md`.
- **Audited identity.** Manuscript freeze `24a98db4c3c4c4d0eede2e3929532956df87911b`. `git diff --stat 24a98db..HEAD -- companion-paper paper` touches only README/BUILD/check_correspondence.py, so the audited TeX equals the freeze. SHA-256 at head:
  - `companion-paper/main.tex` `cb915eba…cfa760`
  - `sections/introduction.tex` (489 lines) `67b74457…21c2ea`
  - `sections/preliminaries.tex` (645 lines) `56db9231…0870e`
  - `sections/corner-unified.tex` (1868 lines) `4c88580b…5ba1b`
  - paper `introduction.tex` `95ad6bd5…a55`, `preliminaries.tex` `0256e494…98f`, `corner-unified.tex` `f8a2a115…465`.
- **Coverage.** I read every line of the four companion files above and the matching paper sections (`paper/sections/{introduction,preliminaries,corner-unified}.tex`, 194/108/556 lines). I also read the audit-03 inputs for my range: `audit-03/c1-companion.md` (C1-01…C1-14), `audit-03/h-corner.md` (H-C06/H-C07), `audit-03/n-notation.md` (register §§1–4), `notation-pass.md`, `response-03.md`, and companion `review.md`.
- **PDF.** I used agent B4's fresh build `$A/build/companion/main.pdf`: 147 pages, 1171239 B, SHA-256 `febea006…dcde79`. It is not byte-identical to the recorded `83ca42c8…`; for a fresh build that is expected. Page numbers come from B4's `page-index.md` and `build/text/companion.txt`. I rendered pp. 4, 22, 26 and 46 at 80 dpi and inspected them. I did not build anything.
- **Section pages.** §1 pp. 2–9, §2 pp. 9–19, §3 pp. 19–46. Lemma 2.1 is on p. 12, (8) p. 21, (13) p. 27, (14) p. 30, (15) p. 33, Lemma 3.1 p. 35, Prop 3.2 p. 38, (23) p. 45.
- **Novelty.** None. The companion is expository and adds no novelty, mechanism or priority claim, so the full IDEAS gate does not apply.
- **Evidence labels.** [D] derived or checked by hand; [E] executed computation (mine, this audit); [I] inspection or judgement.

## Verdicts

1. **Mathematics of Sections 1–3, including every added explanation: no error found.** I checked every identity, inequality, worked example and numeric value in the range [D], and recomputed the consequential ones independently [E]. Two judgements follow from that.
   - Nothing is wrong in substance. One stated regularity hypothesis is used beyond the interval where the text establishes it (C4A-04). The fact is true and the gap is one sentence wide, so it is not an error.
   - The numerical checks are consistency checks of analytic statements, not evidence for them.
2. **Pedagogy (companion Sections 1–3): ACCEPT WITH MINOR REVISIONS.**
   - Both audit-03 MAJOR clarity items are resolved in substance. C1-01 (exact corner formula) is fixed. C1-02 (symbol overload) is fixed apart from a small residue, C4A-02.
   - No BLOCKING or MAJOR clarity failure remains for a reader with some university analysis.
   - The main remaining weakness is pacing. The paper's compressed paragraph is kept and followed by one or two expanded re-derivations of the same step (C4A-01). Seven further MINOR items, one EDITORIAL item and two NOTEs follow.
3. **Agreement with the paper: consistent.** The following agree with the paper:
   - Theorem 1.1 and its parity-dependent equality sets.
   - Theorem 1.2 for every n≥2 with one uniform C.
   - The constants (3)–(4), the orientation (2), the exceptional coefficient one in (6), and Lemmas 2.1 and 3.1 and Prop 3.2.
   - All 116 labels and numbered displays, the "analytic corner / location via Thm 1.1" split and the "n≥512 analytic transfer" sentence.
   - The correspondence helper passes [E].
   - The companion replaces the paper's partial-fraction derivation of ψ′(½)/ζ(2) by a finite csc² limit, and replaces "analytic" by "smooth with sinc/Taylor-integral representations" (C1-06). Both are legitimate. The values used are unchanged.

## 1. Audit-03 dispositions checked against the actual text [D][I]

| ID (audit-03 severity) | response-03 status | What the frozen text actually contains | My status |
|---|---|---|---|
| C1-01 (MAJOR): corner formula (8) not reconstructible | FIXED, reviewed | See note (a) below the table. | **Fixed in substance**, residue in C4A-06 |
| C1-02 (MAJOR): symbol overload | FIXED, reviewed | See note (b) below the table. | **Mostly fixed**; residue in C4A-02 |
| C1-03: row bookkeeping told three times; lost antecedent | FIXED, scoped | Now told twice: compressed (corner:371–401, paper text) and "spell out" (403–476). "Row k is written r; entries \|F_r(θ_j)\|" (327–328) and the folded contribution (392–393) are present. A new lost antecedent is "this bookkeeping" (346). | Fixed; residue in C4A-01/C4A-08 |
| C1-04: hidden trig steps | FIXED, scoped | Cotangent/half-angle identities (337–342) and minus-sum reindexing (380–383) are present. The sine product gives X, ω and Π(1−Xω^ℓ)=1−X^n, but not why that holds or the constant 2^{n−1} (349–355). | Fixed; residue in C4A-06 |
| C1-05: ψ and H_k facts used before derived | FIXED, scoped | ψ is named "digamma" with the recurrence, ψ(k+1)=H_k−γ and ψ(R+½) at first use (301–315), with a forward pointer to (16). The one-line H_k expansion step is still absent (315, 1061). Γ′/Γ is not mentioned. | Fixed; residue in C4A-06 |
| C1-06: tools without statements; "analytic" | FIXED, reviewed | The termwise-differentiation criterion is stated (1024–1030). The sinc representation (258–270) and Taylor-integral J₂, v₁ (1471–1481) replace "analytic". | **Fixed** |
| C1-07: misleading parity/N motivation | FIXED, scoped | intro:355–373 now has the requested wording, which I checked [D]. | **Fixed** |
| C1-08: definition order in §2 | FIXED, scoped | Fixed: δ_AB before use (prelim:32), node count and injectivity (15–16), triangular basis change (86–88), trapezoid formula (100–102), "initially" dropped, heading renamed. **New residue:** the highest-mode fix uses h_n^{(n)} at prelim:175, before its definition at 282–283 (C4A-03). | Fixed; new residue in C4A-03 |
| C1-09: repetition, orphan sentences | FIXED, reviewed | Fixed: the orphan "onset 320" and "Near the other endpoint" are gone, the intro enclosure remarks are merged, and the ledger is single. **Not fixed:** the κ-integrand continuity is told three times (intro:304–333; corner:831–834, 882–896, 898–923), (13) is derived three times, ψ estimates (16) and the ψ(½), ψ′(½) values twice, and so on. | **Partially fixed**: C4A-01 |
| C1-10: worked examples | FIXED, scoped | The n=2 table and Λ_c(2)=3 are present (189–199). The optional asymptotic table was not adopted (decision). The n=1 example still does not note Λ_c(1)=2 and the odd pattern. | Fixed as scoped; C4A-09 |
| C1-11: figures | FIXED, reviewed | Fig. 1 and the n=2 even/odd index board with the collision ★ (corner:200–214, p. 22) are legible. F2–F5 were not adopted. | Fixed as scoped |
| C1-12: Prop 3.2 roadmap and ledger | FIXED, reviewed | The seven-step roadmap (1170–1173) and the 1/m ledger table (1812–1825, p. 46) are present and correct [D]. | **Fixed** |
| C1-13 / C1-14 | DECISION | Consistent with the text. | Agree |
| H-C06 (EDITORIAL): paper §3 collisions | FIXED, scoped | Renamed: 𝒟_n, u_±, \mathsf c. Remaining: d_r against d in §3.2, B node against B(x) in §3.1, Q_i/Q_{m,r}/Q, and F_r/F/F_B. | Partially; C4A-02 |
| H-C07 (EDITORIAL): H-file spacing typos | DECISION (leave) | Still present: 4 matching lines in `theory/H-sharp-corner-expansion.md` and 1 in `campaign-H-summary.md` (patterns most17, factor1/m, bigO, PAPERONLY). This is consistent with the DECISION. | Agree (no manuscript impact) |
| n-notation §4.2 companion-only renames | via notation-pass | The other §4.2 aliases are applied (\mathcal R_n, ψ_B→\mathsf h_B, (i₁,i₂), P_±, \boldsymbol1_{n odd}, \mathsf c, ζ(2)/ζ_odd(2), \mathsf E_j, \mathsf L_m/\mathsf c_v). **But R_1 survives at prelim:482**, although notation-pass.md says "R_n → \widetilde K_n throughout preliminaries". The C1-02 offset-cutoff rename M→L₀ was never applied. | C4A-02 |

(a) C1-01: the text now has three things the audit asked for.
- The diamond kernel identity 𝒟_n=G_n+cos(nu) (corner:99–103).
- The corner substitution K_n((−1,−1),B)=𝒟_n(π−θ_j,π−φ_k) and L_{jk}=w_{jk}G_n(θ_{j′},φ_{k′}) (104–114).
- The product-to-sum identities, the four mesh cosine values (161–176), and the constant row sign (239–242).

What remains is three one-line algebra steps (C4A-06). The 127–160 paragraph still mixes the change of variables with the corner reflections.

(b) C1-02, applied renames:
- 𝓡_n for the intro remainder;
- \widetilde K_n for the corrected kernel;
- i₁,i₂ for the diamond indices;
- \mathsf c, \mathsf c_i for the local cosines;
- P_± for the positive and negative row totals;
- \boldsymbol1_{n odd} for the odd indicator;
- ζ(2) for the reciprocal-square sum;
- \mathsf L_m for log m.

A §3 notation table (corner:56–74) and the 𝖭=nm note are present.

## 2. Independent verification of derivations, examples and values

Script: `$A/c4a-code/check_c4a.py`, output in `check_c4a.out`. Follow-up at 40 digits: `check_c4a_fix.py`, output in `check_c4a_fix.out`. These are fresh code and do not reuse the audit-03 scripts.

**Introduction**
- [D] dim Π_n=(n+1)(n+2)/2 and the n=2 index/point list (all six points). [E] The node count equals the dimension for n=1..7.
- [D] The parity-of-one-side counting argument. The corner parities: (−1,−1)↔(n,n+1); (1,−1) is a non-node iff n is even; (−1,1) iff n is odd. The reflection symmetries j↦n−j (even n) and k↦n+1−k (odd n).
- [D] The proof of (1). The worst-case sign data. λ_n≥1 with equality at nodes.
- [D][E] The square identity a²log²N+b log N+c=(a log N+c₁)²+κ=(4/π²)(log N+d)²+κ.
- [D] ℓ²−t²≥(8/9)ℓ² for ℓ≥3, and Σ_{ℓ≥L}ℓ⁻³≤L⁻³+1/(2L²).
- [D][E] lim_{t↑1}t²cot(πt/2)/(1−t²)=π/4. The full κ integrand tends to 2 at t=1.
- [E] κ=0.91971011838849253…, b=1.225522125742012 and c=1.846160310423926 all match the stated decimals.
- [D] log²(n+½)=log²n+(log n)/n+O(log n/n²). I also re-derived the C1-07 claim: in the scale m, Λ_c=A(m)²+κ−(a²log m+1+a²d)/m+O, and the shift to N leaves −1/N.

**Preliminaries**
- [D] Unisolvence ⇔ bijective evaluation. The hat-function extension f_* with |f_*|≤1 and I_nf_*(z_*)=λ_n(z_*).
- [D] The Chebyshev recurrence, and the basis claim via a total-degree-triangular transition.
- [D] The weights (interior 2/(n(n+1)), side ½, corner ¼), bilinearity and symmetry, and the continuous orthogonality integrals.
- [D] The geometric sum: Σ′z^j=(1−σz)/(1−z)−(1+σ)/2=(1−σ)(1+z)/(2(1−z)), (1+e^{iα})/(1−e^{iα})=i cot(α/2), Q_M values and h_p^{(M)}.
- [D] cos((M−p)t_j)=(−1)^j cos(pt_j). The alternating part needs p+r=n and q+s=n+1, which contradicts ≤2n.
- [D] E^TWE=D, F=ED⁻¹E^TW, FE=E, hence F=I. The inverse Gram coefficients are ν_pν_q, except 1 at (n,0).
- [E] L_B(A)=δ_AB from (6) for n=1..7 (maximum error 1.1e−15).
- **n=1** [D][E]: nodes and weights ¼,¼,½; Gram diag(1,1,½); K₁ and the corrected kernel; L_{B₁},L_{B₂},L_{B₃} sum to 1; |a+b|+|a−b|=2max(|a|,|b|); λ₁=max(1,|y|+(1−x)/2) on an 81² grid; maximum 2 exactly at (−1,±1).
- [D] The four-reflection identity for \widetilde K_n, including −cos(nθ)cos(nα).
- [D] The symmetry argument L_{SB}(Sz)=L_B(z), and the collision example Σe^{irt}=e^{i(M−1)t/2}sin(Mt/2)/sin(t/2).

**§3.1**
- [D] 𝒟_n=G_n+cos(nu); T_p(−1)T_p(cos θ)=cos(p(π−θ)); j′,k′ reflection; parity change; weights preserved.
- [D][E] The diamond closed form via (i₁,i₂) and the step-two progression sin((M+1)z)/sin z. The numerator ½(−1)^j(2+cosθ+cosφ). 𝒟_n=(−1)^j(2+cosθ+cosφ)/(cosθ−cosφ), and |𝒟_n−(−1)^j|=2f on the whole odd board for n=2..7.
- [D][E] 𝒟_n(π,π)=(−1)^n(2n+1) (n=2..7). The collision weight 1/(2nm)·2n=1/m. Coprimality leaves (0,0) and (n,m) only.
- [D][E] **n=2 table** 3/2, 1, 1, ½ and Λ_c(2)=(4/6)·4+⅓=3 exactly. The index boards (even/odd, ★ at (2,3)) are correct [D, rendered p. 22].
- [E] **Λ_c(n) from (8) = both forms of (12)** for n=2..12: (8)=(12a) to 2e−20 at 30 digits, and (8)=(12b) to 5.5e−40 at 40 digits. These also equal the kernel corner value from Lemma 2.1 and the other non-node corner value (n≤9, float). Λ_c(1)=2 from the kernel.
- [D] B(0)=1/π, B(1)=−1/π; the sinc identity cot z−1/z=−z∫t²sinc(tz)/sinc z (checked by integration by parts; [E] at z=0.83). Also w≤a/x, and w≤π(1−x) on [½,1] [E].
- [D][E] The F_r cotangent form; Σ_jF_r(jπ/n)=n; the positive samples are exactly −r+1,…,r−1 (n≤11); the absolute row is 2P_r−n.
- [D][E] Σcsc²((ℓ+½)π/n)=n². sin(nz)=2^{n−1}Π sin(z+ℓπ/n), so C_n=2^{n−1} (not stated in the text).
- [D] The plus/minus initial arguments π/2−v/2 and −π/2−v/2+rπ; w tan(v/2)=1.
- [D] The assembly 1/m+n/m−2(m−1)/m=1−2n/m=−1+2/m. The two-pole decomposition and both ψ telescopings give D_{m,r}.

**§3.2**
- [D][E] (13) for n=2..29 (to 1e−29); L_n=(1/n)Σcot y_r; L₂=√2; the n=2 summands total 2.
- [D] The (s,r) bookkeeping, including r=s↔k=0, r=2n−s↔j=n and ¼c_n². (1/n)Σ1/y_r=a(2H_{2n}−H_n). ∫(cot y−1/y)=log(2/π) [E].
- [D][E] 2H_{2n}−H_n=log n+γ+2log2+O(n⁻²). n²(L_n−A(n))→0.04363 (n=50, 200, 800).
- [D] (14): the common-denominator numerator (1+c)(c₁−c₀); the half-angle factors; sin S_i≥cos(u/2)sin(v_i/2); cot(v₀/2)≤π(n−k)/(2k); nk−mj=n(ℓ−1)+(n−j); m−k≤h; (ℓ−1)h≤(ℓ−1)n.
- [E] The maximum of |Δf|/(π²n/(2ℓ²)) over n≤40, 64 and 101 is 0.2026≤1.
- [D] Λ_c−L_n²=Δ_n+(1−L_n²)/m, with the k=n reference row zero. φ_k−θ_j=π(σℓ−t)/m. The local limit h_{σ,ℓ}. The Riemann-sum normalization 4n/m. The endpoint strips ≤2δn+2. The ε/3 choice of M, δ, n. The pairing 2t²/(ℓ(ℓ²−t²)).

**§3.3**
- [D] Lemma 3.1: Peano K(t)=(t−u)(u+h−t)/2, K′(u)=h/2, K″=−1, max K=h²/8. The endpoint cells O(h²(1+|log h|)). The midpoint M₂h³/24.
- [D][E] ψ(½)=−γ−2log2, ψ′(½)=π²/2, ψ(R+½) recurrence (R=1..6), and |ψ″|≤z⁻²+2z⁻³. The finite csc² limit argument [D].
- [E] (16) is uniform on z≥1: sup z²|ψ−log z+1/(2z)|=1/12 and sup z²|ψ′−1/z|=0.645.
- [D][E] (19): shifts r/(2m), s/(2m), s/(2m); lower arguments r, 3s/4, 3m/4; example bound 3/(4m²); the third-shift sign. [E] max m²|D−centred|=0.466 over m≤119 and 301.
- [D] e_r, u_r=O(r⁻²): the cell bound (r+k)⁻⁴/4 and Σ≤4/(3r³). [E] r²e_r→1/24 and r²u_r→−1/12.
- [D][E] The finite recurrence identity (R=1..7). S_u=1+2log2−π²/4=−0.0811067391524 and q₀+S_u=2log2.
- [D] (20): every term, including the cancelling ±1/(2m). [E] max |Q|/(s⁻²+(ms)⁻¹+m⁻²)=0.150. The r≤m/2 and r≥m/2 split.
- [D] (21) assembly. J(0)=d₀, J′(0)=q₀; R(0)=aq₀, R(1)=π−ad₀ [E]. The J₂, v₁ factorizations and (xv₁log x)″.
- [D] The A₁, b, L, P₁ endpoint factorization, giving the correction −(aq₀+π−ad₀)/(2m).
- [D][E] ∫(w−a/x)=a log(2/π). (22) has no reciprocal term (m²·residual stays at −0.0873).
- [D][E] f″=(2log t−3)/t³ and the outer correction −log m/(2m); C_K=−0.0728158499.
- [D] The three singular pieces of M_m: L/m cancels, the L coefficient is ad, and the 1/m coefficient is −(π+aq₀)/2. β_H via aπ=2.
- [D] The smooth part:
  - cell endpoints −t/(2n), t+t/(2n);
  - F_B(0)=a/π=a²/2, G_B(0)=a², F_B(1)=G_B(1)=0;
  - 1/m+1/(nm)=1/n;
  - ∫G_B=I_B+I₂/π.
  - [E] n²·residual of (18) is 0.060–0.061 (n=100, 400).
- [D][E] **(23)**: the integrand identities (checked at x=0.37) and the three boundary terms a², −a²log(2/π), −1. 2I_B−aI₁=−0.41169568858130 on both sides. 2+β_H+β_B=−1−a²d=−1.61276106287101.
- [D] |β_B/n−β_B/m|≤3|β_B|/(2m²). P′, P″ [E sympy]. The m→N Taylor step. The ledger table.
- [E] **C=κ consistency.**
  - C_H(400), C_H(800) extrapolate to 1.5818113 and C_B=0.337898711695. Together −1+C_H+C_B=0.9197100 against κ=0.9197101 (difference −8.7e−8, inside the O(log m/m²) model error).
  - **End-to-end:** N(Λ_c−A(N)²−κ) = −0.7734 (n=2), −0.9610 (10), −0.99725 (50), −1.000607 (200), −1.000432 (1000), −1.000215 (3000).

## 3. Passages that still hide work [I] (exact missing steps; collected in C4A-06)

1. corner:104–106 (p. 21). "T_p(−1)=(−1)^p therefore gives K_n=𝒟_n(π−θ_j,π−φ_k)". Missing: (−1)^p cos(pθ)=cos(p(π−θ)). Likewise at 109, T_n(−1)T_n(cosθ_j)=(−1)^n cos(nθ_j)=(−1)^{n+j}.
2. corner:175–176. The substitution line is missing: numerator = ½[(−1)^j cosθ−(−1)^k]+½[(−1)^j−(−1)^k cosφ]=½(−1)^j(2+cosθ+cosφ), using (−1)^k=−(−1)^j.
3. corner:181. Missing: 𝒟_n−(−1)^j=(−1)^j[(2+cosθ+cosφ)−(cosθ−cosφ)]/(cosθ−cosφ)=(−1)^j·2(1+cosφ)/(cosθ−cosφ).
4. corner:185. 𝒟_n(π,π)=(−1)^n(2n+1) is asserted. Missing: 𝒟_n(π,π)=Σ_{|p|+|q|≤n}(−1)^{p+q}; there are 4s lattice points with |p|+|q|=s≥1, so the sum is 1+4Σ_{s=1}^n(−1)^s s=(−1)^n(2n+1).
5. corner:221–222 (p. 23). Missing: from jm=kn and gcd(n,m)=1 it follows that n|j (Euclid's lemma).
6. corner:260 (p. 23). "Direct integration gives". Missing: ∫₀¹t sin(tz)dt=−cos z/z+sin z/z², so z cos z−sin z=−z²∫₀¹t sin(tz)dt.
7. corner:349–355 (p. 25). The text says "For example, put X=…" (this is the proof). Missing:
   - Π_ℓ(1−Xω^ℓ)=1−X^n, from t^n−1=Π(t−ω^ℓ) with t=1/X;
   - 1−e^{2iθ}=−2ie^{iθ}sinθ, which gives the constant C_n=2^{n−1}.
8. corner:315 and 1061 ("by applying it at k+1"). Missing: log(k+1)−1/(2(k+1))=log k+1/(2k)+O(k⁻²).
9. corner:1131–1132 ("comparing its large-R limit with log R"). Cite the already proved 2H_{2R}−H_R=log R+γ+2log2+o(1) (corner:609–610).
10. corner:1293–1295. "writing k=(k+½)−½ in the finite triangle" is cryptic and superseded by the explicit telescoping proof at 1298–1308. Delete it.
11. corner:1653 (p. 44). "On [−1/4,5/4] the function B and its first two derivatives are bounded" is not established by the text (C4A-04).

All other "directly", "follows", "elementary" and "immediate" occurrences in the three files (40 grep hits) are followed by the actual calculation.

## 4. Standard tools [I]

Stated in the form used:
- geometric sums (proved);
- complex exponential rules;
- product-to-sum and angle addition;
- cot A+cot B, the double angle and the half angle;
- the chord bounds sin z≥2z/π and cos z≤π/2−z;
- Taylor's formula with integral remainder;
- the trapezoid/Peano and midpoint rules (derived);
- Lemma 3.1;
- the termwise-differentiation criterion;
- uniform convergence, the M-test in substance, and continuity of uniform limits;
- integration of a uniform tail;
- monotone integral comparison;
- the logarithmic derivative;
- the ε/3 interchange.

Used without statement; all are acceptable at the stated level:
- differentiation under the integral sign (corner:266–267, 1478–1481);
- Euclid's lemma (item 5);
- the roots-of-unity factorization (item 7);
- Riemann sums of continuous functions converge (corner:804–811).

ψ is defined by its series, which is self-contained. Naming it as Γ′/Γ once would help a reader consult references. "Rhombic" (intro:391, p. 7) is the only unexplained technical word in §1.

## 5. Notation: first use and remaining collisions [I][E]

Run: `notation_scan.py` on a `git archive HEAD` copy, output in `$A/c4a-code/notation/`.
- It PASSes the paper/companion pair: 19 statements, 85 numbered display blocks.
- The companion has 545 candidate definition sites. The flags in Sections 1–3 are restatements: N twice, Λ_c twice, \widetilde K_n twice, B for the node in three forms. I found no new heuristic collision.

**Used before definition**
- h_n^{(n)}: prelim:175, p. 12, defined at 282–283.
- \boldsymbol1_{n odd}: corner:509, defined at 545 (§2 defines indicators in general at prelim:303).
- The midpoint rule: used at corner:579/605, p. 29; derived at 979–1000, pp. 35–36, with a back-reference but no forward pointer.
- The "stated bound on ψ″": claimed at corner:1044, displayed and defined at 1050–1051.
- "Removable singularity": in Remark 2.2 (prelim:641, p. 19), defined at corner:230 (explained in substance at prelim:621–637).
- L_{jk}: corner:111, never introduced as notation for L_B.

**Residual collisions**
- **Undefined after rename:** R₁ (prelim:482, p. 16) should be \widetilde K_1.
- **κ written as K:** K_M and K (corner:846–859, p. 33) are the κ partial and full sums. The text never says K=κ. The same section has the kernel K_n, and §3.3 adds the Peano K(t) (962), the limit variable K (1059, 1110) and C_K.
- **Offset cutoff M** (corner:837–865), alongside Q_M, the progression M (137), M_2, M_m, C_M and M in 1066.
- **Reserved a=2/π reused:** as a generic real in §2 (prelim:118, 227 "a+ib", 497) and in a_{n,j}^{σ,ℓ} (corner:794, p. 32) while a=2/π is live.
- **Same-subsection pairs inherited from the paper:**
  - node B (corner:104) against the function B(x) (245) in §3.1;
  - x_j=cosθ_j (80) against x=r/m (293) in §3.1;
  - weights d_r (496) against the constant d (574) in §3.2;
  - h=n−j (700) against h_{σ,ℓ} (756) in §3.2.
- **Companion-only, minor:**
  - σ=z^M (prelim:237) against the reflection signs σ (554) in §2;
  - m as a count (prelim:578) against m=n+1;
  - c=u+h/2 (corner:980) against the constant c.

The §3 notation table exists. It does not give the scopes of the inherited overloaded letters (h, Q, S, T, D, F, K, M).

## 6. Pacing, transitions, repetition, figures and examples [I]

**Strengths.**
- §1 motivates every definition and gives the n=2 node set before the formula is used.
- §2's Lemma 2.1 proof is model exposition: geometric sum → Gram → alternating part → matrix F=I, followed by a complete n=1 example.
- §3 has a stated three-stage plan, a local motivation for each estimate, an explicit ε/3 interchange, the ψ block and a seven-step roadmap.
- The 1/m ledger table makes the −1 visible.

**Weakness 1: compressed-plus-expanded duplication.** The design keeps the paper paragraph verbatim and then adds "Here is … in detail", so many steps are proved two or three times. For a learner this blurs which derivation is the proof. Full list in C4A-01.

**Weakness 2: transitions.**
- intro:37 restarts with "Polynomial interpolation replaces data…" after 35 lines on interpolation.
- intro:226 repeats 210–211.
- prelim:534–537 says "same correction" twice.
- The prelim:588 heading is followed by blank lines.
- corner:343–346: "this bookkeeping" has no antecedent.
- corner:1033–1036 repeats 1028–1030.
- corner:1533–1535 says "v(1)=−a" twice.

**Figures and examples.** Present: Fig. 1, the n=2 index boards, the n=1 and n=2 worked examples, the L₂ check, the csc² n=2 check, the §3 notation table and the ledger table. The most useful single addition, labelled as an illustration, is a table of Λ_c(n) against the four-term expansion (values in C4A-09).

## 7. Findings

**C4A-01 — MINOR (pedagogy, development-owned). Residual compressed-plus-expanded duplication in §3, and κ continuity told in both §1 and §3.**
- *Locations (companion line, page):*
  - Collisions and the k=m row: 183–188 and again 218–228 (pp. 22–23).
  - (13): 503–512, then 514–535 (geometry), then 544–567 (coefficients) (pp. 27–28), i.e. three derivations.
  - L_n: 569–582 and 584–613 (p. 29).
  - (14) final step: 699–704 and 706–731 (p. 30).
  - Λ_c−L_n²: 733–740 and 742–748 (p. 31).
  - Limit interchange: 787–826 and 836–868 (pp. 32–33).
  - Pairing: 826, 870–880.
  - κ integrand continuity: intro:304–333 (pp. 6–7), corner:831–834, 882–896, 898–923 (pp. 33–34).
  - (16): 1053–1061 and 1107–1124 (pp. 36–37).
  - ψ(½), ψ′(½): 1062–1105 and 1126–1140 (pp. 36–38).
  - e_r, u_r: 1238–1244, 1246–1264 and 1266–1279 (pp. 39–40).
  - S_u: 1287–1296 and 1298–1317 (p. 40).
  - (20): 1326–1328 and 1330–1347 (p. 41).
  - Remainder split: 1349–1357 and 1359–1375 (p. 41).
  - R endpoints: 1437–1441 and 1443–1523 (pp. 41–43).
  - (22): 1536–1539 and 1541–1552 (p. 43).
  - (23): 1729–1734 and 1736–1760 (p. 45).
  - β_B/m: 1762 and 1764–1771 (p. 46).
- *Reason.* Audit-03 C1-09 is closed as "merged". Only some merges were done.
- *Impact.* No error. The reader works through the same argument up to three times and may wonder whether the repetitions prove different things. The section is about 28 pages where 20–22 would do with no loss of explanation.
- *Fix.*
  - (i) Where an expanded derivation immediately follows, make the paper paragraph a one-line statement ("We prove … as follows") or delete it. Paper prose is not a checked block, so the correspondence check is unaffected.
  - (ii) Keep one derivation of (13). The coefficient computation at 544–567 is the clearest; keep the geometry as two sentences.
  - (iii) Replace intro:304–333 by "convergence is proved in §3.2 (after (15))", or replace corner:882–923 by a back-reference.
  - (iv) Merge the two (16) proofs and the two ψ(½), ψ′(½) passages into one "facts about ψ" block.
  - (v) Drop the first S_u justification (1293–1295).

**C4A-02 — MINOR (notation; R₁ and the κ/K/M items are wording-level). Residual notation after C1-02 / H-C06.**
- *Locations.* §5, "Residual collisions".
- *Fix.*
  - R₁→\widetilde K_1 (prelim:482).
  - K_M, K→κ_M, κ, adding "the pairing identity below shows that this is κ of (4)" (corner:846–859).
  - Offset cutoff M→L₀ or ℓ_* (837–865).
  - Peano kernel K(t)→\mathsf K(t) and the limit variable K→J (1059, 1110).
  - a_{n,j}^{σ,ℓ}→α_{n,j}^{σ,ℓ}.
  - Generic a,b in §2→s,t or α,β.
  - d_r→δ_r (corner:496–564), as H-C06 proposed.
  - Add one row to the §3 table: "h, Q, S, T, D, F, K, M carry local meanings stated at use".
  - Correct the notation-pass.md claim ("throughout preliminaries") with a dated addendum.

**C4A-03 — MINOR (definition order, wording-level).**
- *Location.* prelim:173–176 (p. 12) uses h_n^{(n)} before its definition at 282–283.
- *Fix.* Write "doubling the squared norm of the highest first-coordinate mode (1 instead of ½; this is h_n^{(n)} in the notation of the proof below)".

**C4A-04 — MINOR (stated hypothesis used outside its proved domain; one-sentence development fix).**
- *Location.* corner:1653 (p. 44). The paper has the same sentence at paper/corner:494.
- *Reason.* The text proves B∈C^∞ only "across [0,1]" (corner:247–270). The smooth-part cells extend to [−t/(2n), t+t/(2n)]⊂[−¼,5/4], where boundedness of B, B′ and B″ is asserted.
- *Impact.* This is true, since cot(πx) has poles only at integers and those at 0 and 1 are removed, so B is smooth on (−1,2). But for a text whose stated aim is that no step appears without its reasoning, this is a missing justification of the exact hypothesis used.
- *Fix.* Add after 248: "Since cot(πx) has poles only at integers and the two subtracted terms remove those at 0 and 1, the sinc formula (valid for |πx|<π) and its reflection show B∈C^∞(−1,2); in particular B, B′, B″ are bounded on [−¼,5/4], which the smooth part uses."

**C4A-05 — MINOR (circular-looking presentation).**
- *Location.* corner:1102–1105 derives ζ(2)=π²/6 from ψ′(½)=π²/2. Then 1133–1137 displays ψ′(½)=4(1−¼)Σk⁻²=π²/2, as if derived from ζ(2). Only 1138 says the csc² argument supplies the sum (p. 38).
- *Impact.* No logical gap. A careful reader sees an apparent circle.
- *Fix.* Delete the display at 1133–1137, or rewrite it as "equivalently ψ′(½)=4ζ_odd(2)=3ζ(2)", consistent with the values just proved.

**C4A-06 — MINOR (hidden one-line steps; development adds a few lines).**
- *Locations.* §3, items 1–10, mainly pp. 21–25 and 36–40.
- *Reason.* These are the residue of C1-01, C1-04 and C1-05. Each step is elementary, but at the companion's stated depth each costs the reader a page of scratch work.
- *Fix.* Insert the exact lines given in §3. Item 4 (𝒟_n(π,π)) and items 2–3 are the most valuable, because they complete the C1-01 chain into (8).

**C4A-07 — MINOR (ordering and forward pointers, wording-level).**
- *Locations.* §5, "Used before definition".
- *Fix.*
  - Add "(Lemma 3.1 and the midpoint estimate after it)" at corner:579/605.
  - Move the ψ″ display (1049–1051) before the sentence at 1038–1044.
  - Define the odd indicator at its first use (509).
  - Add "removable singularity (see Section 3.1)" to the prelim:621–637 paragraph or move the definition there.
  - Introduce L_{jk}:=L_B for B=(cosθ_j,cosφ_k) at corner:111.

**C4A-08 — EDITORIAL (auditor-fixable wording/format; any TeX edit needs a new paired freeze and helper baseline).**
- `$csc^2$` renders as italic csc (corner:441, p. 26). Use `$\csc^2$`.
- The garbled sentence at prelim:190–192 should read "…G_n, whose four reflected copies assemble \widetilde K_n".
- "this bookkeeping" (corner:346): write "the row sum".
- "For example, put X" (corner:351): write "To see this, put X".
- Delete the duplicate sentences at corner:1033–1036, corner:1535 and prelim:534–535, and the repeated intro:226.
- intro:37 restart: write "In general terms, polynomial interpolation…".
- Remove the blank lines after the prelim:588 heading.
- Stale source comment main.tex:1 ("frozen 48-page"). "Development draft." on the title page (main.tex:49) is AC's call before publication.

**C4A-09 — NOTE (recommended additions).**
- (i) An illustration table after Theorem 1.2 or the ledger, labelled "illustration, not evidence". My [E] values:

  | n | Λ_c(n) | four-term expansion | N(Λ_c−A(N)²−κ) |
  |---|---|---|---|
  | 2 | 3 (exact) | 2.9093673615 | −0.7734 |
  | 3 | 3.7761423749 | 3.7317947250 | −0.8448 |
  | 10 | 6.8771001625 | 6.8733899744 | −0.9610 |
  | 50 | 12.8669170532 | 12.8668624964 | −0.99725 |
  | 200 | 19.7253813780 | 19.7253844047 | −1.000607 |
  | 3000 | 37.6386236318 | 37.6386237035 | −1.000215 |

- (ii) At prelim:521, say that λ₁ already shows the odd-n maximizer pattern of Theorem 1.1, with Λ_c(1)=2.
- (iii) Name ψ=Γ′/Γ once.
- (iv) Explain "rhombic" in one clause (intro:391): Fourier partial sums over the diamond |p|+|q|≤n, the index set of 𝒟_n.

**C4A-10 — NOTE (record hygiene, outside the TeX).**
- `companion-paper/review.md` opens with "Status: **ACCEPT**" for ac945041 and has no supersession pointer. Add a dated line pointing to `../manuscript-onset512-solmax-review.md` and this audit.
- `response-03.md` marks C1-02 and C1-09 "FIXED, reviewed scope". The actual residue is in C4A-01 and C4A-02; record it by cross-reference, without rewriting audit-03.

## 8. Prioritized fix list (companion Sections 1–3)

1. **C4A-04**: one sentence on B∈C^∞(−1,2). This is the only item where a hypothesis is used beyond what the text proves.
2. **C4A-06**: items 2–4 (completing the (8) chain), then 6–8.
3. **C4A-01**: consolidate the duplicated derivations (biggest pacing gain; (13), κ continuity and ψ first).
4. **C4A-02, C4A-03, C4A-07**: R₁, K→κ, M, the h_n^{(n)} forward use, the ψ″ ordering and the midpoint pointer.
5. **C4A-05**: remove the circular-looking ψ′(½) display.
6. **C4A-08**: typos and duplicates.
7. **C4A-09, C4A-10**: optional illustration and record pointers.

**Process note for root (WORKFLOW, third and later rounds).** These items need development-owned changes:
- C4A-04, C4A-05 and C4A-06 add mathematical exposition lines.
- C4A-01 restructures the text.

None is wording-only, so none can be fixed by the auditor in place. My substantive judgement is that none changes a claim or blocks the mathematics. C4A-02, C4A-03, C4A-07 and C4A-08 are wording or notation only. Any TeX edit invalidates the byte freeze 24a98db and requires a new paired source commit, a `FINAL_BASELINE` update, a rebuild and the artifact correspondence check.

## 9. Commands actually run (outputs under `$A/c4a-code/`)

| Command | Result | Resources |
|---|---|---|
| `git rev-parse HEAD`; `git status --short`; `git diff --stat 24a98db..HEAD -- companion-paper paper` | head 70a50d7; clean; TeX unchanged since the freeze | read-only |
| `sha256sum` of the 7 audited TeX files | identities above | — |
| `python3 -B …/companion-paper/check_correspondence.py` (source mode) | **exit 0**, PASS 19/85/116, baseline 24a98db | 0.09 CPU-s |
| `python3 -I prose_cover.py <topic>` | only re-segmented sentences and the replaced ψ′(½)/"analytic" passages are absent | <1 s |
| `PYTHONPATH=$A/../audit3/pylib python3 check_c4a.py` (mpmath 1.3.0, sympy 1.14.0, numpy 2.5.3, Python 3.13.18) | exit 0; three FAILs (none a defect, see note below) | 17.0 CPU-s |
| `… python3 check_c4a_fix.py` (dps 40) | (8)=(12b) to 5.5e−40; B′(0)=1/π−π/3 consistent; C=κ to 8.7e−8 | 11.1 CPU-s |
| `git archive HEAD paper companion-paper \| tar -x` into scratch; `python3 -I audit-03/code/n/notation_scan.py --repo <copy> --out notation` | exit 0; PASS 19/85 | 1.3 CPU-s |
| `pdfinfo`, `pdftoppm -r 80` pp. 4, 22, 26, 46 of B4's build; viewed | 147 pages; layout legible; csc typo confirmed p. 26 | — |

Note on the three FAILs in `check_c4a.py`: all three come from my own tolerances, and none is a defect. They are a 1e−20 threshold against 1.9e−20 at 30 digits, an unextrapolated C_H, and a cancellation in B at x=1±1e−15. `check_c4a_fix.py` resolves all three.

Total CPU is about 35 s, against the ~25 CPU-minute cap.

**Limits.** Numerical runs check consistency only and confer no status. I did not audit Sections 4–5 or the paper's standalone exposition, and I did not rebuild PDFs (B4's build used). Page numbers refer to that fresh build, whose bytes differ from the recorded artifact.
