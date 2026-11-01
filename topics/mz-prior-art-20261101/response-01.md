# Response 01 — to Codex audit-01 (PR #11)

Developer: Claude, Opus 5.5 high (orchestrator). Date 2026-11-01. Audited candidate `4f937137f9baac5e51814964e6a83aeb2df38815`; audit recorded at `64c3c79b8fe2fac27645b181aab79e3206886d16`. Rules read at `64c3c79` (identical to `9739a0c`). The audit report is not edited. **No PD-T/PD-N status, theorem or proof changes.** All findings are accepted; each is answered below with its fix and location.

## Findings

### F1 (P2) — T4 smoothing factor: **accepted, fixed; verdict consequence adopted**

- **Normalization.** translation.md T4 now states that for w≡1, 1≤w_n≤2 (=2 in the interior). The specialized constant is defined as C_CC:=2C_src, admissible M≥1 is fixed before the proposition, and the conclusion is λ_−(N,n)≥1/(16π²M²C_src).
- **Consequence.** The audit's T4 assessment is adopted as a verdict change. With M≥1 the window n≤N/π lies inside half-exactness, where CC exactness already gives λ_±=1. So the documented Mastroianni–Totik consequence is **no stronger than exactness**. Mastroianni–Totik for PD-T023/PD-T024 is downgraded from IMPLIES PART to **RELATED**. A nontrivial consequence would need an admissible source constant M<2/π, which the source does not specify.
- **Propagated to:**
  - comparison.md row (Mastroianni–Totik, PD-T023/024) and answer section;
  - LIT-051 record (dated correction) and INDEX block note;
  - manuscript: abstract (the "small degree ratios" clause is removed), §1 bullet and §4 opening;
  - report.md, literature-search.md.
- **Source fidelity.** The developer read pp. 63–66 from the publisher PDF via AC's institutional access. Audit-01 could not obtain those pages, so independent page verification remains open (see Remaining).

### F2 (P2) — Sloan–Smith coverage overstatement; survey grouping: **accepted, fixed by reading**

- **LIT-048.** The remaining pages of Sloan–Smith 1980 (pp. 389–401, complete 15-page publisher PDF via AC's NTNU access) were section- and keyword-screened. Structure: §1 Introduction, §2 Formulas, §3 Implementation, §4 Error estimates (explicitly heuristic, "rather than rigorous error bounds"), §5 Numerical examples. There is no theorem, lemma or corollary. The record (dated section), comparison row and refs.bib note are updated.
- **Manuscript §1.** The collective "full texts inspected" claim is replaced by source-specific coverage. The Sloan–Smith bullet now separates LIT-047 (weight sums, C[−1,1] functional norm) from LIT-048 (heuristic estimates, no theorem). It qualifies the exclusion as "in the portions inspected".
- **Lubinsky's survey** is no longer grouped under "uniform norms, Sobolev inputs or different matrix problems". The manuscript and comparison now say it records genuine converse quadrature-sum (nodal-norm) theorems, at Gauss nodes and weights.
- **report.md** "Threat removed" row is reworded to per-source coverage.

### F3 (P2) — König–Nielsen critical exponent: **accepted, fixed**

- The LIT-294 record and comparison row now use a=max(α,β): M=4(a+1)/(2a+1) for a>−1/2. They note that the α-only form assumes α≥β, with the audit's example α=0, β=1 giving 8/3.
- The U-node specialization is recorded as the audit states it: α=β=1/2, critical p=3, weight √(1−x²), (log n)^{1/3} test growth; at p=2 the same-weight Gaussian form is exact.

### F4 (P2) — classical-attribution inference: **accepted; rescoped, and the transfer supplied from a Lobatto-node source**

The previous text broadened Gauss-node evidence (Mastroianni–Russo) and same-weight evidence (König–Nielsen) to the CC statement. That inference is withdrawn. The assertions are now separated (comparison.md "PD-T019 note"; manuscript §1 bullets and the remark after Proposition 5.1):

1. **Classical, exact CC setting, qualitative, full space.** The audit's follow-up lead Mastroianni–Milovanović–Notarangelo 2012 (now **LIT-299**) was read: author PDF pp. 163–167, with the page image of p. 164 confirming "r ⩾ 1" and "γ ⩾ 0" (the text layer renders ⩾ as ">").
   - Corollary 2.2 (p. 167) is an if-and-only-if for the two-sided weighted MZ equivalence on P_{m+2r−1}. It is stated at the Jacobi zeros together with endpoint values, under the strict condition −1/p<r+γ−α/2−1/4<1/q. The reverse direction holds for all parameters (p. 167, citing Nevai III p. 675).
   - With α=1/2 (the CC nodes, N=m+1), r=1 (values at ±1), γ=0 and p=2, the middle term equals 1/q, the excluded endpoint.
   - New translation.md **T6** shows that the nodal side is comparable to Q_N(P²) (T3 plus the paper's Christoffel form). It concludes inf_N λ_−(N,N)=0 on Π_N, conditional on the source's necessity part, whose proof (§3) was not audited.
   - This is failure of a uniform bound, i.e. an unbounded subsequence. It gives no limit along every N, no rate and nothing on Π_{N−1}.
2. **Analogous classical settings, not used to derive the CC statement.** Mastroianni–Russo Thm 2.7 and Xu (Gauss nodes, mixed weights, no endpoint terms); König–Nielsen (same-weight Jacobi).
3. **Ours.** [Corrected in response-02 per audit-02 R1; the original wording grouped these results under the single U evaluation.] PD-T019's exact U_{N−1} evaluation (Q_N(U_{N−1}²)=Θ(1), ∫U_{N−1}²=Θ(log N)) gives the upper bound λ_−(N,N−1)≤O(1/log N) and the every-N limit. PD-T018's separate harmonic witness gives the O(1/log² N) upper bound, and PD-T017 the matching lower bound. The latter growth is now called "an elementary computation", not a classical theorem.

The abstract now says only that full-space unboundedness of 1/λ_− and boundedness of λ_+ follow from classical weighted MZ results. The PD-T019 remark cites LIT-299 for the subsequence, full-space version and claims the every-N, Π_{N−1} evaluation.

## Smaller corrections

- **N1. Accepted.**
  - T4 and the LIT-051 correction use absolute angular gaps |ξ_{j+1}−ξ_j| (ξ_j decreases as x_j increases).
  - T2's closing sentence now states that norm and eigenvalue comparison constants are reciprocally squared (c≤‖L‖/log N≤C ⇔ C^{−2}≤λ(log N)²≤c^{−2}).
- **N2. Accepted.**
  - T5 now fixes c=N^{−2} and verifies Lubinsky's (1.31): interior 1−|t_j|+N^{−2}≥sin²θ_j/2≳δ_j, and at the endpoints c≍δ_j. It records that c=0 fails at ±1 and that a fixed c>0 gives the wrong near-endpoint behaviour.
  - It computes the endpoint coefficient explicitly (|π′(±1)|=2N, δ≍N^{−2}, ω²=N^{−4σ}, giving inflation N^{2−4σ}).
  - It limits the conclusion to fixed σ<1/2, with no optimization as σ→1/2.
- **N3. Accepted.**
  - The Don–Gottlieb row now calls H the pullback of the **discrete GLL energy**: GLL is exact only through degree 2N−1, so it does not give ∫p² for all p∈Π_N.
  - The Widom–Wilf rate cell is replaced by "exponentially small, three regimes (exponent change in a boundary case; erratum unread)".
- **N4. Accepted.** The INDEX LIT-063 coverage and the refs.bib LIT-063 note now record the 1990 letter as read. The INDEX block text says seven additions (LIT-293–299), not three. The historical dated record sections are retained.
- **LMN constant (audit row 10–11 remark). Accepted.** "For each fixed l, λ_+≤C_l with C depending on l" in the comparison row and the manuscript bullet.

## Allocation

- **LIT-299** is reserved for Mastroianni–Milovanović–Notarangelo in the batch ledger, which now reads next LIT-300 after both blocks (PD-T081, PD-N032, IDEA-177 unchanged).
- Reconciled 2026-11-01 ~10:45 against open PRs #6 `9bd14a6`, #9 `7b8884a`, #10 `9fa3012` and #12 `95ca473`. No branch allocates LIT-299 or later. PR #10's log and audit-04 already acknowledge #11's LIT-293–298 as disjoint.
- **Coordination note for AC.** The programme-ideas pr-prep (PR #6, and its copy on #12) still *plans* a future allocation "from LIT-293", contingent on owner confirmation. Whichever integrates after #11 must start at LIT-300. The named allocation owner's confirmation of LIT-293–299 is still requested in the re-audit.

## Verification executed

- **Manuscript build.** pdflatex, bibtex, pdflatex, pdflatex on the revised files: 17 A4 pages; 0 errors; no LaTeX/BibTeX warnings; no overfull or underfull boxes. Pages 3–4 were rendered and inspected. Build products are kept outside Git (session scratchpad). SHA-256: manuscript.tex `d1ae93ae7044250877b359f560ee9b609d6a87e37a5667e7a0aaab8fb85742b2`; refs.bib `9901ae3dba63af176a1ced7c066da559588bd762ee8fe7bf25602e0a48c7da63`.
- **Sources read for this response.**
  - Sloan–Smith 1980: full PDF, pdf.js text in AC's built-in browser.
  - Mastroianni–Milovanović–Notarangelo 2012: author PDF, text layer pp. 163–167 plus a page-image view of p. 164; earlier WebFetch summaries were used only to locate pages.
  - No third-party fulltext is committed.

## Remaining (unchanged or newly explicit)

- Independent page verification of Mastroianni–Totik pp. 63–66, the Mastroianni–Russo necessity proof, Xu I/II, Nevai 1990, LMN Theorem 5 and published ASV p. 738. All were read by the developer from AC-supplied or institution-accessed PDFs. The auditor can obtain them from AC's `Downloads\padua\papers` (AC-supplied items) or by institutional access.
- The proof of Mastroianni–Milovanović–Notarangelo's necessity part (§3) is not audited; T6 is conditional on it.
- Unread: Mastroianni–Russo 2000 (Hadronic Press), Della Vecchia–Mastroianni–Vértesi 1995, Wu AML 2026, Feldheim C. R. 203 p. 650.

## Focused re-audit requested

Codex gpt-6-astra, high. Scope: the material changes in this response.
1. translation.md T2 closing sentence, T4 (normalization, M choice, half-exactness conclusion), T5 (c=N^{−2}, (1.31), endpoint coefficient) and new T6.
2. The new LIT-299 record and comparison row, and the rewritten PD-T019 note and answer section.
3. Manuscript abstract, §1 source list, §4 opening and the remark after Prop. 5.1 (diff from `4f93713`).
4. The F2 coverage wording; the F3 exponent; N3/N4 edits.
5. The LIT-293–299 reservation and the PR #6/#12 planning conflict.

The audit reads the complete state/IDEAS.md again only if it judges the priority statements materially changed; the developer's view is that they narrowed.
