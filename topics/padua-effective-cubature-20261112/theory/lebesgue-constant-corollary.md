# PD-T?padua-effective-cubature-20261112-claude-01 — Padua Lebesgue constant equals the corner value, with a three-term expansion

ID kind: PD-T.
Aliases: C0 corollary; Padua Lebesgue constant = Λ_c(n); three-term Lebesgue-constant expansion of the Padua points.
Split from: none (corollary assembly of registered results; no new mathematics).
Split into: none.

All paths below are relative to the repository root `/workspace/padua_research`; "L" means line of the cited file at branch head `0abf5e7d912b41c9b9248d4dc9f4580425683b53`.

## Statement

Let Λ(Pad_n) := max over the closed square [−1,1]² of λ_n, the Lebesgue function of total-degree-n interpolation at the even-checkerboard Padua points of PD-T101 (conventions below).

**(i)** For every integer n with 2 ≤ n ≤ 32, and, for an integer N_* whose existence is asserted by PD-T229 (no value is known), for every integer n ≥ N_*, Λ(Pad_n) = Λ_c(n). The set of global maximizers of λ_n on [−1,1]² is exactly {(−1,−1),(1,−1)} for even n and {(−1,−1),(−1,1)} for odd n; these are the two corners that are not nodes.

**(ii)** For every integer n ≥ max(32, N_*), with N = n + 1/2, a = 2/π, c₁ = a(γ + log(8/π)), b = 2ac₁ (= (8/π²)(γ + log(8/π))) and c = c₁² + κ (κ as in PD-T269),

  Λ(Pad_n) = (4/π²) log² N + b log N + c + R_n,

with, for n ≥ 32 (PD-T271 (1), L21–23),

  |R_n| ≤ 604 n^(−1/5) + ((log n + 2)² + 1)/(n + 1) + A_n/(2n²) + 1/(16n⁴) + (log N + 2)/n,  A_n = a log n + c₁.

Every term on the right tends to 0, so R_n → 0 and Λ(Pad_n) − (4/π²) log² N − b log N → c. The constant c is parity independent and lies strictly between 1.846160310423926079759838737947 and 1.846160310423926079759838737948 (PD-T271 (2), L35–36).

## Definitions

Copied from the records; nothing is redefined.

- **Nodes (PD-T101, L12–15).** B_jk = (cos(jπ/n), cos(kπ/(n+1))), 0 ≤ j ≤ n, 0 ≤ k ≤ n+1, j + k even. This is the node set of Caliari–De Marchi–Vianello 2008 (PD-T101 Sources, L76 calls it that paper's "third family"; PD-T159 and PD-T271 call it the "first-family" convention, same set). There are (n+1)(n+2)/2 nodes.
- **Cardinal functions (PD-T101, L20, L39, L120).** λ_n(z) = Σ_B |L_B(z)|, L_B the cardinal polynomial in Π_n (total degree ≤ n) with the exceptional coefficient at (a,b) = (n,0) equal to 1 rather than 2 (L107): L_B(z) = w_B (K_n(z,B) − T_n(z₁)T_n(B₁)). Weights w_jk = 2ε_jη_k/[n(n+1)] (L20).
- **Corner value Λ_c(n).** PD-T101 gives the exact formula for λ_n at the four corners, all n ≥ 1 (L12–35) but does not use the symbol Λ_c. PD-T159 (L16) defines, for n ≥ 2, Λ_c(n) as the maximum of λ_n over the four corners, and states that the two node corners have value 1 and every non-node corner has the same value (L30). PD-T229 (L25) defines Λ_c(n) as the common value of λ_n at the two physical non-node corners.
- **N_* (PD-T229, L12–21).** An integer such that (i) holds for every n ≥ N_*. Its existence is proved; "no effective value of N_* is supplied" (L21). The proof (L51) takes N_* at least both N_loc (non-effective, from PD-T225) and ⌈exp(10⁷)⌉ (from PD-T228). Any larger integer also works, so N_* ≥ 32 can be assumed.
- **L_n, κ (PD-T159 L16–21; PD-T269 L15–19).** L_n = (2/n) Σ_{r odd ≤ n} d_r csc(rπ/(2n)), d_n = 1/2, d_r = 1 for r < n. κ = lim_n (Λ_c(n) − L_n²) = (8/π) ∫₀¹ t² cot(πt/2) Σ_{l≥1, l odd} 1/(l(l² − t²)) dt.
- γ is Euler's constant, all logarithms natural (PD-T270 L26; PD-T271 L41).

## Assumptions

Exact real arithmetic; the conventions above. Parts of (i) rest on computer-assisted records: PD-T246 and PD-T214/T181 and others rest on exact certificate covers (see Depends on). Their stated trust bases are inherited unchanged.

## Status by part

Overall status: **PROVED**. Assembled from registered, audited results, with no new mathematics and no new hypothesis. The registry rows (PROOF_STATUS.md) show every dependency PROVED with Claude audit-01 listed.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| (i), 2 ≤ n ≤ 32 | PROVED | PD-T209 (n = 2), PD-T162/166/169/174/177 (n = 3..7), PD-T181 (n = 8), PD-T214 (n = 9..16), PD-T246 (n = 17..32). Computer-assisted; stated trust bases inherited |
| (i), n ≥ N_* | PROVED, non-effective | PD-T229; N_* depends on the non-effective N_loc of PD-T225 |
| (ii), n ≥ max(32, N_*) | PROVED, assembly | (i) plus PD-T271 (with PD-T269/T270, PD-T159); the starting point is non-effective, the error bound (1) is explicit |
| Claims for 33 ≤ n < N_* | not claimed | PD-T229 L59: the range 17 ≤ n < N_* beyond PD-T246 is not covered; no finite scan or optimizer closes it |

## Depends on

| Record | Used for | Record path |
|---|---|---|
| PD-T101 | nodes, cardinal functions, corner formula (n ≥ 1) | `topics/padua-proof-attempts-20261101/theory/proof-attempts-codex-01-padua-corner.md` |
| PD-T159 | definition of Λ_c(n), L_n; node corners = 1; equal non-node corner values | `topics/padua-proof-attempts-2-20261101/theory/proof-attempts-2-codex-04-corner-product-comparison.md` |
| PD-T209 | n = 2 | `topics/padua-argmax-alln-20261101/theory/argmax-alln-codex-02-degree-two-global-argmax.md` |
| PD-T162 / T166 / T169 / T174 / T177 | n = 3 / 4 / 5 / 6 / 7 | `topics/padua-proof-attempts-2-20261101/theory/proof-attempts-2-codex-{07-degree-three,11-degree-four,17-degree-five,42-degree-six,52-degree-seven}-global-argmax.md` |
| PD-T181 | n = 8 | `topics/padua-argmax-alln-20261101/theory/argmax-alln-codex-07-degree-eight-global-argmax.md` |
| PD-T214 | n = 9..16 | `topics/padua-argmax-alln-20261101/theory/argmax-alln-codex-08-degree-nine-through-sixteen-global-argmax.md` |
| PD-T246 (uses PD-T210) | n = 17..32; L10–15 states the combined range 2..32 | `topics/padua-argmax-effective-20261103/theory/argmax-effective-codex-01-finite-global-argmax.md` |
| PD-T229 (uses PD-T225, PD-T228) | n ≥ N_* | `topics/padua-argmax-alln-20261101/theory/gated-codex-15-eventual-global-argmax.md` |
| PD-T271 | three-term expansion for Λ_c(n), n ≥ 32 | `topics/padua-lebesgue-followups-20261103/theory/t4-03-corner-constant.md` |
| PD-T269, PD-T270 | κ, error (2) of PD-T269; one-dimensional bound |L_n − A_n| ≤ 1/(4n²) | `.../theory/t4-01-corner-defect-limit.md`, `.../theory/t4-02-one-dimensional-remainder.md` (same directory) |

Registry rows: PROOF_STATUS.md, rows PD-T101, T159, T209, T162, T166, T169, T174, T177, T181, T214, T246, T229, T269, T270, T271. No published theorem enters as a proof dependency.

## Checks

No computation was run for this record. It is a logical assembly; the check performed was reading the cited records' statements, conventions and quantifiers (see Discrepancies with BRIEF). Independent confirmation of the match between this statement and the four dependency files is the separate task named in handoff 01 (C0, item 3).

## Sources

LITERATURE, used only for priority wording, not as proof: Kolomoitsev–Lomako 2021 (LIT-379), Kuznetsova 1995 (LIT-482), Pimenova 1979 (LIT-484); read by the P1 comparison.

## Proof or evidence

**Proof of (i).** Fix n with 2 ≤ n ≤ 32. PD-T246 (L10–15) gives the global maximum Λ_c(n) and the exact two-corner maximizer set for 17 ≤ n ≤ 32, and records that, together with the inherited results for 2 ≤ n ≤ 16, this gives the continuous range 2 ≤ n ≤ 32 (L14–15; inherited list at L44–45: PD-T209 at 2, PD-T162/166/169/174/177 at 3–7, PD-T181 at 8, PD-T214 at 9–16). Each inherited record states the same conclusion with the same maximizer sets (PD-T209 for n = 2: value 3 at (−1,−1),(1,−1); PD-T214: max = Λ_c(n) at the stated corners; the others state the exact value with the same corner pairs). For n ≥ N_*, PD-T229 gives max λ_n = Λ_c(n) and the same maximizer sets (L12–19). The conjunction is (i).

**Proof of (ii).** Let n ≥ max(32, N_*). By (i), Λ(Pad_n) = Λ_c(n). PD-T271 (valid for n ≥ 32, L12) gives Λ_c(n) = (4/π²) log² N + b log N + c + R_n with the bound (1) and enclosure (2). Substituting proves (ii). Each term of (1) tends to 0 (PD-T271 L26), hence R_n → 0 and the limit statement follows.

**Remark (same proof, not part of the registered statement).** Because n = 32 lies in both ranges, the three-term expansion also holds for Λ(Pad_32). No other n < N_* with n ≥ 33 is covered.

## Scope

- The maximum is over the closed square [−1,1]²; Λ(Pad_n) is the maximum of the Lebesgue function of this one node family and interpolation space (total degree ≤ n, exceptional-coefficient convention of PD-T101).
- (ii) is non-effective in its starting point (through N_* of PD-T229) and effective in its error bound (1) and constant enclosure (2).
- Nothing is claimed for 33 ≤ n < N_*. The statement does not give the sharper expansion with −1/N and O(log N/N²); that target (PD-T098) remains OPEN in the registry (PD-T271 L56).
- n = 1 is excluded: Λ_c(n) is defined from n ≥ 2 (PD-T159 L16) and the argmax records start at n = 2.

## Discrepancies with BRIEF

The statement above follows the records. Differences from BRIEF §2.1–2.3:

1. **Symbol Λ_c.** BRIEF calls Λ_c(n) "the exact corner value of PD-T101". PD-T101 has the exact formula for λ_n at the corners but not the symbol; Λ_c(n) is defined in PD-T159 (L16) and PD-T229 (L25). Values agree.
2. **n = 1.** BRIEF says "2 ≤ n ≤ 32" without comment; the records give the reason (Λ_c defined for n ≥ 2; PD-T101 holds for n ≥ 1 but proves no argmax). Stated here as an explicit exclusion.
3. **Coverage of 2..32.** PD-T246 itself proves only 17 ≤ n ≤ 32; 2..16 come from the inherited records (BRIEF §2.2 is correct but compressed).
4. **max(32, N_*).** The threshold n ≥ 32 in PD-T271 was verified (L12). PD-T229's proof takes N_* ≥ ⌈exp(10⁷)⌉, so max(32, N_*) = N_* for that choice. The BRIEF form is kept because the existence statement alone does not fix N_*.
5. **Family name.** PD-T271 and PD-T159 say "first-family"; PD-T101 (L76) records that Caliari–De Marchi–Vianello call the same set their third family. Same nodes (j + k even).
6. **Maximizer sets.** BRIEF says "the two parity-correct non-node corners"; the records give them explicitly (even n: (−1,−1),(1,−1); odd n: (−1,−1),(−1,1)).
7. **Constants.** BRIEF gives only c numerically. The records define b = 2ac₁ = (8/π²)(γ + log(8/π)) and c = c₁² + κ, with the open-endpoint enclosure (2). No numerical value of b is stated in the records, so none is given here.
8. **PR #27 (BRIEF §2.3).** BRIEF says PR #27 would extend (i) to 2..40 and make N_* effective as ⌈exp(10¹²)⌉. See the dated note: the branch head claims more than this, and the quoted number comes from an earlier component.
9. **Status wording inside records.** Several record bodies keep historical "required Claude audit pending" wording (for example PD-T271 L49 vs its dated header L3; the degree-six record L30). *Corrected 2026-11-12 (m4):* PD-T229 L29 records the audit as accepted, with record fixes pending. The PROOF_STATUS.md rows list Claude audit-01 for all of them. This record follows the registry rows; the auditor should confirm.
10. **Provisional ID.** Handoff 01 writes `PD-T?effective-cubature-claude-01`; the task assignment gives `PD-T?padua-effective-cubature-20261112-claude-01`. The latter is used. Mapping to be recorded at PR preparation.

## Priority wording

From `topics/padua-literature-20261103/p1-comparison.md` ("Priority wording for the paper (proposed)", items 2 and 3, L51 and L54), quoted verbatim:

> "The Lebesgue constant of the Padua points satisfies Λ_n = (4/π²) log² n + O(log n) [KL21], with pointwise estimates going back to Kuznetsova [K95]; in particular the corner value is at most this. We show that the corner value has the same leading term, with explicit constants, and give the second term b log n, b = (8/π²)(γ + log(8/π)), with an explicit remainder bound valid for all n ≥ 2."

> "Caliari, De Marchi, Sommariva and Vianello conjectured [CDMSV08] that the maximum is attained at a vertex, and De Marchi [DeM22, §3.3(2)] observed that it lies at the corners not occupied by Padua points. We prove this for 2 ≤ n ≤ 16 and for all sufficiently large n; the intermediate range remains open."

Both sentences need caveats here. The first concerns the corner value Λ_c(n), and its "remainder bound valid for all n ≥ 2" does not carry over to Λ(Pad_n), which equals Λ_c(n) only in the ranges of (i). The second predates PD-T246 (n ≤ 32), so its range should be read as updated by (i). *(m3, 2026-11-12.)*

What the comparison supports, and no more: only the leading term of the Padua Lebesgue constant is published, Kolomoitsev–Lomako 2021 (LIT-379; Thm 2.1 and the unnumbered Padua sentence, p. 4), with pointwise O(log n) work going back to Kuznetsova 1995 (LIT-482, Thm 1; Pimenova 1979, LIT-484, for the m = n trigonometric case). Every published remainder found is O(log n), so none determines the second term b log n (p1 row for PD-T158, L38). The p1 comparison has no row for the constant c (PD-T271); by the same reasoning an O(log n) remainder cannot determine c. This last point is this record's inference from p1, not a p1 sentence. The second and third terms are therefore new as far as the documented search goes; the search was not exhaustive (zbMATH and MathSciNet full-text search unavailable, p1 L15). Do not claim 4/π² as new, and do not claim KL proved the corner lower bound (p1 L52).

## Dated note (2026-11-12): open draft PR #27

Branch `codex/padua-argmax-bridge-20261105` (head `8a94ce610594e9f52a23ca6b74b5751719f0d89e`, 2026-11-08), a draft PR, is **not a dependency** and nothing above uses it. Read on 2026-11-12 with read-only git:

- `C01-effective-argmax.md` on that branch states N_0 = ⌈exp(10¹²)⌉ (L16, L244): this matches the BRIEF's number as an earlier effective threshold.
- The branch's results file `results/padua-argmax-bridge-20261105.md` and `G01-all-degrees.md` claim the argmax PROVED (computer-assisted) for every n ≥ 2: finite certificates for 2..319 (inherited 2..32, native 33..40, compact returns 41..319) and an analytic tail from 320 (E14), with a later route from n ≥ 512 (J01). The same file reports a manuscript pair and says PR27 remains draft with Claude audit pending.
- The branch also claims the sharp corner expansion Λ_c = (4/π²)log²N + b log N + c − 1/N + O(log N/N²), PROVED analytically for both parities (results file L11–13; `H-sharp-corner-expansion.md`). Its manuscript (`paper/sections/introduction.tex` L133–149) says this also holds for Λ_n. *(Added 2026-11-12 after independent check m1.)*
- If merged and audited, it would make (i) hold for all n ≥ 2, make the starting point of (ii) effective, and replace (ii) by a sharper expansion; its remainder constant is not stated numerically. The BRIEF's "2..40, exp(10¹²)" thus understates the branch head. None of these claims is verified here; update this record with a dated note when the PR merges.

## Open items

- Independent check of this statement against the dependency records (handoff 01, C0 item 3).
- Allocation of a final PD-T ID and registry row at PR preparation.
- Optional: ask the P1 author whether c (PD-T271) should get its own row in `p1-comparison.md`.

## History

- 2026-11-12: written by Claude subagent (Sonnet 5.5, high effort) for orchestrator Claude Opus 5.5. Rules read at `0abf5e7d912b41c9b9248d4dc9f4580425683b53`. No computation, no Git state change.

2026-11-12, orchestrator (Claude Opus 5.5 xhigh): applied the fixes from the independent check (`../independent-checks-C0.md`): M1 in the gate, and m1–m4 here. On m5: drafting was delegated to Sonnet 5.5 high as mechanical assembly of registered statements, with no new mathematics, under the WORKFLOW row "Mechanical edits". The mathematical check was done by Opus 5.5 high. The orchestrator (Opus) reviewed and owns the record.
