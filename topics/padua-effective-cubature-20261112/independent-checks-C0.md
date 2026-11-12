# Independent check C0: Padua Lebesgue-constant corollary

Checker: Claude subagent, Opus 5.5 (`claude-opus-5-5`), high effort. Role: independent checker only. This supplements the later Codex audit and does not replace it. No Git state was changed, and the reviewed files were not edited.

- Branch: `claude/padua-effective-cubature-20261112`.
- Commit read: `69c44550aa00a93910d626147b5137fc3d8738fb` (`git rev-parse HEAD`).
- The reviewed files cite line numbers at `0abf5e7d…`. `git diff 0abf5e7d HEAD` is empty for every dependency directory, `PROOF_STATUS.md`, `RESULTS.md` and `topics/padua-literature-20261103`, so those line numbers are valid at HEAD.

Rules read: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`.

Files under review:
- `topics/padua-effective-cubature-20261112/theory/lebesgue-constant-corollary.md` (the "theory file" below; provisional ID `PD-T?padua-effective-cubature-20261112-claude-01`);
- `topics/padua-effective-cubature-20261112/novelty-gate-C0.md` (the "gate" below);
- target statement: `BRIEF.md` §2.1–2.3, L108–133.

## Method

1. I reconstructed the claim from the dependency records **before** reading the theory file closely. Each record was reached through its `[record](…)` link in `PROOF_STATUS.md`:
   - PD-T101, row L199;
   - PD-T159, L260;
   - PD-T229, L333;
   - PD-T246, L352;
   - PD-T209, L312; PD-T162, L263; PD-T166, L267; PD-T169, L270; PD-T174, L275; PD-T177, L278; PD-T181, L282; PD-T214, L317;
   - PD-T269, L372; PD-T270, L373; PD-T271, L374;
   - also the indirect dependencies PD-T225, PD-T228 and PD-T210, all PROVED.
2. Reconstructed claim:
   - Fix PD-T101's even-checkerboard nodes and the total-degree interpolation space. For n ≥ 2 the four-corner maximum Λ_c(n) of PD-T159 equals the common non-node corner value used by PD-T229 and PD-T246.
   - The finite records give max_{[−1,1]²} λ_n = Λ_c(n), with the parity-correct pair of maximizers, for every 2 ≤ n ≤ 32.
   - PD-T229 gives the same conclusion for n ≥ N_*, with N_* existential only.
   - PD-T271 gives the three-term expansion of Λ_c(n) for every n ≥ 32.
   - Hence the expansion holds for Λ(Pad_n) when n = 32 and when n ≥ max(32, N_*).
   - This matches the theory file L12–24 and L79–83.
3. I then checked the theory file and the gate line by line against those records.
4. I read the PR #27 branch with `git show` and `git ls-tree`, and its PR state with `gh api …/pulls/27` (read-only).
5. Sanity computation (MEASURED, float64, not a premise): a scratchpad script inverts the Chebyshev Vandermonde at the PD-T101 nodes.

## Verification of items (a)–(i)

**(a) Point set, cardinal convention, domain: MATCH.**
- Theory L30 gives nodes (cos jπ/n, cos kπ/(n+1)), 0≤j≤n, 0≤k≤n+1, j+k even. This is PD-T101 L14–18, PD-T229 L12 and PD-T246 L10, L19–20.
- Theory L31 gives L_B = w_B(K_n − T_n(z₁)T_n(B₁)) with the exceptional (n,0) coefficient set to 1. This is PD-T101 L107 and L120.
- Domain is the closed square: PD-T229 L14 (`max_[-1,1]^2`), and PD-T246's tensor Bernstein form on the closed square. Theory L12 and L87 agree.
- Λ_c(n) has two definitions: the four-corner maximum (PD-T159 L16) and the common non-node value (PD-T229 L25). They are reconciled correctly at theory L32, via PD-T159 L30.
- The "first-family" vs "third family" naming note (L30, L100) is correct (PD-T101 L76).

**(b) Finite range and maximizer sets: MATCH.**
- Coverage, all reread:
  - n = 2: PD-T209;
  - n = 3, 4, 5, 6, 7: PD-T162, 166, 169, 174, 177;
  - n = 8: PD-T181;
  - n = 9..16: PD-T214;
  - n = 17..32: PD-T246, L10–15.
  - No gap.
- Every record gives {(−1,−1),(1,−1)} for even n and {(−1,−1),(−1,1)} for odd n:
  - even n: 2, 4, 6, 8;
  - odd n: 3, 5, 7;
  - 9..16 and 17..32 by parity.
- This is also consistent with the node structure. (−1,−1) has j+k = 2n+1 and is never a node. (1,−1) is a non-node exactly when n is even, and (−1,1) exactly when n is odd.
- MEASURED sanity: the corner values for n = 2..7 reproduce the exact values stated in PD-T209/162/166/169/174/177 to 10 digits. A 121² grid maximum lies at those corners.
- The theory file excludes n = 1 (L90). This is correct relative to the records: PD-T159 defines Λ_c only for n ≥ 2, and no argmax record covers n = 1. See NOTE N1.

**(c) Quantifiers on N_*: MATCH in substance, wording MINOR (m2).**
- Theory L21 and L33 say existence only, non-effective. This is PD-T229 L12 and L21.
- N_* ≥ 32 may be assumed (L33) because the conclusion is monotone in the threshold. PD-T229 L51 in fact takes N_* ≥ ⌈exp(10⁷)⌉.
- Non-effectiveness enters through N_loc of gated-codex-11, which is PD-T225 (PROOF_STATUS L329). Theory L48 is correct.

**(d) Constants and remainder: EXACT MATCH with PD-T271 L12–26, L35–36.**
- Constants: a = 2/π; c₁ = a(γ + log(8/π)); b = 2ac₁ = (8/π²)(γ + log(8/π)) (I checked the identity); c = c₁² + κ; N = n + 1/2.
- Range of validity: n ≥ 32.
- Bound (1) term by term: 604 n^(−1/5), ((log n+2)²+1)/(n+1), A_n/(2n²), 1/(16n⁴), (log N+2)/n, with A_n = a log n + c₁.
- The enclosure of c (open endpoints, 30 digits) is identical.
- κ (theory L34) matches PD-T269 L14–19.
- The n ≥ 32 restriction comes from PD-T269 (2). PD-T270 holds for every n ≥ 1.

**(e) Assembly proof: VALID.**
- (ii) at a given n needs Λ(Pad_n) = Λ_c(n) at that same n, which is (i), and n ≥ 32 for PD-T271.
- (i) is available for n ≤ 32 or n ≥ N_*. Hence the threshold max(32, N_*), plus the remark that n = 32 lies in both ranges (L83). Both are correct.
- The proof at L79–81 uses exactly these steps.

**(f) Status: PROVED as an assembly is supported. No hidden new mathematics.**
- The only steps beyond citation are the conjunction of the cited ranges, the identification of the two Λ_c definitions (already in PD-T159 and PD-T229) and a substitution.
- Every direct and indirect dependency row in PROOF_STATUS is PROVED and lists an audit-01.
- The trust bases of the computer-assisted rows are inherited and disclosed (L39).

**(g) Priority wording: does not exceed p1, with one caveat missing (m3).**
- Quotes L111 and L113 are verbatim copies of p1-comparison L51 and L54.
- L117 restates p1 accurately:
  - KL21 Thm 2.1 leading term (p1 L37);
  - every published remainder found is O(log n) (p1 L38);
  - the search is not exhaustive (p1 L15);
  - do not claim 4/π² as new, and do not attribute the corner lower bound to KL (p1 L52).
- The extension to the constant c is labelled clearly as the record's own inference, since p1 has no PD-T271 row. That is acceptable and matches BRIEF L132.
- LIT-379, LIT-482 and LIT-484 exist in `literature/INDEX.md` with the stated content.

**(h) No registered duplicate: CONFIRMED on main.**
- Searched `PROOF_STATUS.md`, `RESULTS.md`, `state/*.md`, `ID_CROSSWALK.md`, `results/*.md` and the topic trees for T271, `Lebesgue constant`, `Λ(Pad`, `max(32` and `three-term`.
- PD-T271 appears only as the corner-value result or as an input. `programme-ideas-claude-05` uses the alias "Λ(Pad_n) = Λ_c(n)" for the OPEN all-n target PD-T099, not for a proved combined statement.
- The gate's IDEA line numbers and grep counts check out: L504/841/871/877/901/933/1012/1015, and 59 "argmax" / 17 "Lebesgue" / 1 "Lambda_c".
- The unmerged PR #27 branch, however, does contain a stronger statement. See M1.

**(i) PR #27 note: accurate in what it states, but incomplete (M1, m1). Not used as a dependency: CONFIRMED.**
- `gh api` reports PR #27 as open, draft, not merged, with head `8a94ce610594e9f52a23ca6b74b5751719f0d89e` (2026-11-08).
- `C01-effective-argmax.md` L16 and L244 contain N_0 = ⌈exp(10¹²)⌉, as the note says.
- The results file and G01 say:
  - argmax PROVED (computer-assisted) for every n ≥ 2;
  - finite cases 2..40 inherited or native, 41..319 from compact returns, the E14 tail from 320, and the J01 route from 512;
  - "PR27 remains draft".
- The note reports all of this correctly.
- No statement or proof step in the theory file uses the branch (L121).

## Findings by severity

### BLOCKING

None. The claimed status (PROVED, assembly) and the statements (i)–(ii) are supported by the cited registered records.

### MAJOR

**M1. `novelty-gate-C0.md:21`, and by extension L9: the factual claim about PR #27 is false.**

L21 says "That branch proves argmax claims, not the three-term corollary". The branch claims more:
- PR #27's title is "Padua Lebesgue constant: sharp asymptotics and exact corner maximizers".
- The branch's `results/padua-argmax-bridge-20261105.md` L11–13 claims the sharp corner expansion PROVED: Λ_c = 4/π² log²N + b log N + c − 1/N + O(log N/N²), N = n+1/2. The record is `theory/H-sharp-corner-expansion.md`, for all n ≥ 2, with a non-numeric constant C.
- The branch manuscript `paper/sections/introduction.tex` L133–149 states this as Theorem "Sharp corner expansion" and adds "Consequently [the expansion] also holds for Λ_n", using the all-n location theorem.

So the open draft already states a strictly stronger Lebesgue-constant expansion: the extra −1/N term, and every n ≥ 2. Its only weakness is the non-explicit remainder constant, whereas C0's bound (1) is explicit.

L9 says PR #27 "would supersede the first half if merged". In fact a merge would supersede both halves. With G01, PD-T271's explicit bound transfers to Λ(Pad_n) for every n ≥ 32, and H strengthens the form.

Consequences:
- The duplicate verdict against registered results on main still stands, so C0's status is unaffected.
- The gate must instead record that C0 is a weaker variant of an unmerged in-repository statement (PR #27, unaudited), and fix L9 and L21 accordingly.

### MINOR

**m1. Theory file L119–125, PR #27 note.** It omits the branch's sharp expansion and its transfer to Λ_n (see M1). Two places should name it, as an update to make on merge:
- L89, which says the sharp form PD-T098 remains OPEN;
- L125, which lists what a merge would change.

The rest of the note is accurate. "None of these claims is verified here" is appropriate.

**m2. Theory file L14 and L16, wording of N_*.** "N_* the integer of PD-T229" reads as a definite object, but PD-T229 proves existence only. State the quantifier in the Statement itself, for example: "There exists an integer N_* (non-effective; PD-T229) such that (i) holds for n ≥ N_* and (ii) holds for n ≥ max(32, N_*)". L33 already says this; only the Statement wording needs to change.

**m3. Theory file L109–115, priority sentence 1.** This is p1's sentence for the corner value (PD-T156–159). It ends "with an explicit remainder bound valid for all n ≥ 2", which is PD-T158's |rem| ≤ 68. That clause does not transfer to the Lebesgue constant Λ(Pad_n): for Λ(Pad_n), (ii) is proved only at n = 32 and for n ≥ max(32, N_*), and the start is non-effective. The record adds a caveat to sentence 2 (L115). It should add one to sentence 1 as well: the sentence concerns the corner value, and its "all n ≥ 2" does not apply to Λ(Pad_n).

**m4. Theory file L104, item 9.** It gives PD-T229 L29 as an example of retained "required Claude audit pending" wording. L29 actually reads "Claude audit-01 ACCEPTED the mathematics at its stated scope (record fixes pending)". Better examples:
- PD-T271 L49 (already cited);
- `proof-attempts-2-codex-42-degree-six-global-argmax.md` L30, "Required Claude audit remains PENDING";
- similar status lines in the degree-four and degree-seven records (L30).

**m5. Model allocation.** Theory file L135 and gate L3 record Sonnet 5.5 high. `agents/WORKFLOW.md` assigns:
- L11: mathematical development to Opus 5.5 high or xhigh;
- L16: duplicate gating to Fable 5.1 xhigh or Opus 5.5 xhigh.

A citation-only assembly may defensibly be classed as technical work (L9). The record should state that classification so the Codex auditor can rule on it.

### NOTE

**N1. n = 1.** The exclusion is correct relative to the records. For information only, this is MEASURED and not a proof: at n = 1, λ_1 has maximum 2 at exactly (−1,−1) and (−1,1). It also appears elementary to prove. λ_1 is a sum of absolute values of affine functions, hence convex, so its maximum over the square is attained at the vertices. On the edge x = −1, λ_1 = 1 + |y|. Including n = 1 would need its own proved and audited argument plus a definition of Λ_c(1). It is not needed for the BRIEF statement.

**N2. Line references and labels.**
- Theory L30 cites "PD-T101, L12–15" for the nodes, but the parity condition j+k ≡ 0 is at L17 (display L14–18).
- Theory L47 labels all of 2..32 "computer-assisted". PD-T209 is a written exact algebraic proof that also has an exact checker.
- Both are cosmetic.

**N3. Size of the explicit bound.** Bound (1) is explicit but nonvacuous only for very large n: 604 n^(−1/5) < 1 needs n > 604⁵ ≈ 8×10¹³, and at n = 32 the right side is ≈ 303.

MEASURED sanity check (float64, my own run, not a premise):

| n | R_n | −1/N |
|---|---|---|
| 16 | −0.0594 | −0.0606 |
| 32 | −0.0306 | −0.0308 |
| 40 | −0.0246 | −0.0247 |

These values are consistent with (1) and with the −1/N term that PD-T098 conjectures.

**N4. Orchestrator results file.** `results/padua-effective-cubature-20261112.md:7` (not under review) writes "Hence Λ(Pad_n) = …" without the range n = 32 or n ≥ max(32, N_*).

**N5. Later literature search on PR #27.** The PR #27 branch has a later, unmerged literature refresh, `topics/padua-argmax-bridge-20261105/literature-refresh-20261107.md`, with targeted searches such as "Padua Lebesgue constant asymptotic expansion second term" and "Padua 1.846160". It is not a merged source. It may be worth consulting before the priority wording is finalized.

## Remaining uncertainty

- I did not re-audit the proofs inside the dependency records. I checked statements, conventions, quantifiers and registry status only, as an assembly check requires.
- The sanity numerics are floating-point and MEASURED.
- The Codex audit remains required.
