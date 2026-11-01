# Literal proposed upstream record changes

Rules/base read at cf89b140530d5838bdb208a8c28f3e7aa676ace3; synchronized main806cc7b4509fd93bae652f9545d32d95529f8281. **Not applied.** Existing theory files stay byte-identical to main. Apply only at PR preparation after the Claude audit, refreshed reservations and final-ID mappings. The blocks below are literal replacements against the current original files, not paraphrases. Provisional IDs must be mapped without changing scientific scope. Reserved ranges live in the shared batch ledger; no final IDs are assigned here.

**Applied at PR preparation, 2026-11-01** (handoff 11, `preparation/prepare.py`): all 15 literal OLD/NEW blocks and the Block-7 History anchor were applied in file order, each OLD matching exactly once. Placeholders were filled, and provisional IDs in the NEW text were replaced by final IDs. The receipt is `preparation/prepare-receipt.json`. The text below is the approved proposal as it stood, kept as history apart from the ID substitution.

## PD-T055: retain OPEN; add quantified scope distinctions

Target: `tracks/bivariate-lanczos/theory/bj-universal-reorthogonalization-obstruction-open.md`.

OLD
```text
## Open items
```

NEW
```text
## Later independent results (original target remains OPEN)

Quantifier note (IDEA-253; an IDEA disposition, not a PD-N). Read pathwise, for every rule and every error realization admitted by an upper-bound model that allows the zero error and exact-real projection, (U) is false for a trivial reason: the zero-error exact run has exact spans, δ_X=δ_Y=0, and Ĥ_J=H_J by PD-T032 part 2. This disposes only of that reading. It does not refute literal working-precision storage, a fixed IEEE implementation or a worst-case-over-errors reading. A final formalization of (U) must choose among the every-error, worst-case-error and deterministic-IEEE quantifiers rather than interchange them.

Fixed-degree instance of the heuristic in Proof or evidence (PD-N062). Take an exact prefix through degree t and fixed admissible degree-(t+1) raw products. Then the span identity of the heuristic is exact for every coefficient choice: after a source f in one raw product, every rule that only subtracts prior vectors and rescales gives the same computed span. Its angle is θ_(t+1)=||f_⊥||/sqrt((1+α)²b²+||f_⊥||²). Its defects are δ_A(t)=κ_Aθ_(t+1), with κ_(A_m)≥b for the operator A_m forming the perturbed column. This holds for any positive measure with U(t+1) and M>N_(t+1), product or not, and any admissible selection. The defect is not specific to J or to unformed products: on T_3 with BJ and the source in Yq_x, δ_Y(1)=(√3/2)δ_X(1). The conclusion is a fixed-degree O(u) obstruction, not exponential amplification; neither implicit-section in-span error nor scalar-operation realizability follows. Parent-repair and reference-basis rules, including the experiment named in Open items, lie outside that class (deferred, IDEA-256). That experiment's literal wording is ambiguous: reorthogonalizing the parent against a basis of a computed span that contains it gives zero. IDEA-256 fixes two nonzero readings, neither yet run. R17a uses the stored columns strictly before the parent's graded index and stays in the computed span. R17b projects the parent onto an extended-precision nested reference basis of the exact span of the monomials through its index; that is the only step where information outside the stored columns enters. Both leave exact parents unchanged, so neither evades the fixed-degree lemma. (U) remains OPEN.

## Open items
```

## PD-T054: register the E3 polynomial-safety target in the existing open item (audit-01 E34-F8)

Target: `tracks/bivariate-lanczos/theory/condition-C-staircase-selections-acyclic-sections.md`.

OLD
```text
A residual description for selections violating (C) (PD-T?…-205 open item); whether the staircase family contains a rule whose coupled residuals stay small on non-product measures (alt is a staircase and is killed on four of six non-product sets, PD-N?…-203; mirror on four).
```

NEW
```text
A residual description for selections violating (C) (PD-T?…-205 open item); whether the staircase family contains a rule whose coupled residuals stay small on non-product measures (alt is a staircase and is killed on four of six non-product sets, PD-N?…-203; mirror on four). This item is also the durable OPEN home of the E3 target of topic padua-lanczos-drift-20261101, in polynomial span-drift form: does some staircase keep the full-reorthogonalization span drift O(u·poly(s)·χ) on a non-product family? The same question is open beyond (C), for some admissible one-relation selection such as the selection the pivot-adaptive rule makes on exact data. OPEN. PD-T142/11 give a computed-data span certificate and a finite exact-data sufficient criterion with a first-order guarantee. Whether any selection passes that criterion with polynomially bounded scores is unproved, and no such bound is claimed on the triangle or rotated-square families.
```

At preparation, also add to the IDEA-151 row of `state/IDEAS.md`, at the end of its disposition cell: “Polynomial span-drift form of the safety question registered as OPEN in PD-T054's open item; sufficient criterion in PD-T142/11 (padua-lanczos-drift-20261101).”

## PD-T056: retain OPEN; record concrete square-case test

Target: `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-300-l3q1-backward-interpretation-target.md`.

OLD
```text
## Open items
```

NEW
```text
## Independent residual-aware square-case example

PD-T145 gives an explicit n=1 square family with moment-infinity perturbation epsilon, exact positive noncommuting sections, support upper sqrt(6epsilon), and residual-aware lower sqrt((1-3gamma)epsilon/3) for unit-mass fits with gamma<1/3. This is reading (E): no recurrence realization with local error u=o(epsilon) is proved. Reading (G), including Padua n=3/4, remains OPEN. The original measure fits at residual epsilon and radius zero.

## Open items
```

## PD-T075: proposed status by the original two-question decomposition

Target: `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md`.

OLD
```text
Overall status: OPEN.
```

NEW
```text
Overall status: PARTIAL: original subquestion (U1) is PROVED in split result PD-T144; original subquestion (U2) remains OPEN. This is a decomposition of the original target, not aggregation with a supporting lemma.
```

## PD-T075(U1): exact row replacement

Target: `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md`.

OLD
```text
| (U1) ρ_n → 0 | OPEN | reviewer-certified lower bounds and floating samples below; no all-n argument |
```

NEW
```text
| (U1) ρ_n → 0 | PROVED | PD-T144: explicit eventual negative witness gives rho_n=O(n^-5) and limsup n^5 rho_n <=20sqrt(2)pi^4/9; analytic proof independently reconstructed |
```

## PD-T075: replace absent-proof paragraph, keep U2 OPEN

Target: `tracks/bivariate-lanczos/theory/bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md`.

OLD
```text
## Proof or evidence

No proof. The routine facts follow from the definitions.
```

NEW
```text
## Proof or evidence

(U1) is proved in split result PD-T144 by zeta_n=(cos(pi/n+a/n^4),cos(pi/(n+1)+a/n^4)), a=20pi^3/9: n^14 P_n(zeta_n) tends to -6400pi^12/729 and n^5 times its distance to the (1,1) node tends to 20sqrt(2)pi^4/9. No matching lower rate or explicit finite negativity threshold is claimed. (U2) stays OPEN. In particular rho_n<=delta_obs(n), so this upper bound for rho_n does not upper-bound delta_obs(n) or disprove a uniform obstruction radius. The earlier certified lower bounds and sampled measurements remain historical evidence, not the proof of decay.
```

## PD-N013: retain MEASURED; add actual-code ordering/fit evidence

Target: `tracks/bivariate-lanczos/theory/reorthogonalization-does-not-restore-graded-spaces.md`.

OLD
```text
## Open items
```

NEW
```text
## Independent public-code extension (MEASURED)

PD-T146 executes actual polyrat 0.2.2 numerical source at commit6903d7af9995c9d88e661fb229626696e00fdfba on the frozen suite. Upstream input [y,x] matches campaign dev including column order; default [x,y] is mirror with reversed within-degree order and is not numerically equivalent to forward mirror. Separate root execution reproduces the rotated-square n24 gap0.004105 and triangle n20 gap0.010164. The post-hoc worst-polynomial training residuals equal those gaps by construction; the worst-polynomial off-sample error depends on the test distribution (1.0e-3 to 1.5e-2 on rotated square). The fixed ridge target exp(x+y) is fit near machine precision on the tested samples. Ill-conditioned/rank-deficient references elsewhere do not certify span drift. This is additional scoped measurement, not an upgrade of this negative result or a proof of every-rule failure. The scalar-operation and aggregate sensitivity statements in the new E1 records remain separately scoped.

## Open items
```

## PD-N015: retain MEASURED; add actual-code ordering/fit evidence

Target: `tracks/bivariate-lanczos/theory/one-relation-selections-do-not-keep-spans-near-Sn.md`.

OLD
```text
## Open items
```

NEW
```text
## Independent public-code extension (MEASURED)

PD-T146 executes actual polyrat 0.2.2 numerical source at commit6903d7af9995c9d88e661fb229626696e00fdfba on the frozen suite. Upstream input [y,x] matches campaign dev including column order; default [x,y] is mirror with reversed within-degree order and is not numerically equivalent to forward mirror. Separate root execution reproduces the rotated-square n24 gap0.004105 and triangle n20 gap0.010164. The post-hoc worst-polynomial training residuals equal those gaps by construction; the worst-polynomial off-sample error depends on the test distribution (1.0e-3 to 1.5e-2 on rotated square). The fixed ridge target exp(x+y) is fit near machine precision on the tested samples. Ill-conditioned/rank-deficient references elsewhere do not certify span drift. This is additional scoped measurement, not an upgrade of this negative result or a proof of every-rule failure. The scalar-operation and aggregate sensitivity statements in the new E1 records remain separately scoped.

## Open items
```

## Preparation and external results

At preparation also update the corresponding PROOF_STATUS rows, split crosswalk, IDEA dispositions and topic indexes, after checking the exact audited source snapshot. Final-ID assignment is still pending. PD-T075 needs a recorded original-to-split mapping for its solved U1; retain original wording/history. The other original target statuses remain unchanged.

### E1 scalar finite split (response-02, audit-02 A02-M2)

At preparation, record the split PD-T140 → PD-T141 in ID_CROSSWALK.md with original-to-split mappings:
- PD-T140 statement table (full-graph comparator uppers, explicit BJ multinode witnesses, squared ratio lower bounds) and its post-hoc consequences K_inf,BJ > 800 K_inf,pivot (T24) and K_inf,BJ > 7 K_inf,alt (rotQ24) → PD-T141, PROVED (finite computer-assisted, formal scalar-CGS2 model).
- PD-T140 keeps the exploratory experiment, MEASURED, with the both-grid factor-ten test outcome INCONCLUSIVE.

Its factor-ten target, "factor ten on both sets", i.e. K_inf,BJ > 10 min(K_inf,alt, K_inf,pivot) on T24 and on rotQ24, is registered as PARTIAL: T24 conjunct PROVED under PD-T141 (c), rotQ24 conjunct OPEN. Give both records PROOF_STATUS rows. If the registry needs the target as its own row, use the PARTIAL status with a dependency on PD-T141. No final IDs are assigned during the response.

Results (superseded 2026-11-01 by the merged PR16 rule, response-02 A02-L8): this topic's results file is the in-repository `results/padua-lanczos-drift-20261101.md`. At PR preparation, add only this topic's section to the root `RESULTS.md`, appended or replaced from that file and preserving every other topic's section. No results are written to AC's machine. The earlier intended local file `C:\Users\andreyac\Downloads\padua\results\padua-lanczos-drift-20261101.md` is a historical copy and AC's to delete. Windows cold-storage delivery of large artifacts is a separate pending item (COLD_STORAGE.md).


## Response-01 additions (Claude developer, 2026-11-01; audit-01 E5-F5)

Literal OLD/NEW blocks; every OLD occurs exactly once in its target at main `e0d9e3d`. Placeholders `<prep-ts>, <preparer>` are filled at preparation.

**Block 1 — `TOPIC/proposed-record-changes.md`, add as a new section after "## PD-T075: replace absent-proof paragraph, keep U2 OPEN". Target: `bivariate-lanczos-claude-319-padua-obstruction-radius-uniformity.md`, "Split into".**

OLD
```text
Split into: none.
```
NEW
```text
Split into: PD-T144 (original subquestion (U1), PROVED: ρ_n = O(n^-5), limsup n^5 ρ_n ≤ 20√2π⁴/9). (U2) is not split and remains OPEN in this file.
```

**Block 2 — same target, title (needed once the status is PARTIAL).**

OLD
```text
# PD-T?bivariate-lanczos-claude-319 — OPEN: dependence on n
```
NEW
```text
# PD-T?bivariate-lanczos-claude-319 — PARTIAL ((U1) PROVED in PD-T144; (U2) OPEN): dependence on n
```

**Block 3 — same target, Open item (2).**

OLD
```text
(2) An all-n argument for (U1), e.g. from growth of the third derivatives of P_n near the corner nodes versus the decay of λ_min(Hess P_n) at (j, k) = (1, 1).
```
NEW
```text
(2) Resolved: (U1) is PROVED in split result PD-T144 by an explicit eventual corner witness at the (1, 1) node (ρ_n = O(n^-5)). A matching lower rate for ρ_n is not part of (U1) and remains open there.
```

**Block 4 — same target, History (append).**

OLD
```text
distinguishing a chosen radius, ρ_n and δ_obs(n) as the audit requested.
```
NEW
```text
distinguishing a chosen radius, ρ_n and δ_obs(n) as the audit requested.
- <prep-ts>, <preparer>: original subquestion (U1) split to PD-T144 (PROVED; Claude audit-01 CONFIRMED, topics/padua-lanczos-drift-20261101/audit-01.md). Overall status OPEN → PARTIAL ((U1) PROVED under the split ID, (U2) OPEN, an explicit decomposition of this file's own Statement); the (U1) row OPEN → PROVED; title, "Split into", Open item (2) and "Proof or evidence" updated. The Statement's questions (U1), (U2) are unchanged. Original wording: title «… — OPEN: dependence on n of the Padua obstruction radius …»; «Overall status: OPEN.»; «| (U1) ρ_n → 0 | OPEN | reviewer-certified lower bounds and floating samples below; no all-n argument |»; «Split into: none.»; «(2) An all-n argument for (U1), e.g. from growth of the third derivatives of P_n near the corner nodes versus the decay of λ_min(Hess P_n) at (j, k) = (1, 1).»; «No proof. The routine facts follow from the definitions.».
```

**Block 5 — target `bivariate-lanczos-claude-313-padua-turan-certificate-all-n.md` (PD-T069), Open items, line 66.**

OLD
```text
Lower bounds cannot bound ρ_n from above, and P_n is one certificate among many: no uniform-in-n obstruction radius is established here, and neither ρ_n → 0 nor the absence of a uniform obstruction radius is proved. Both questions are OPEN (PD-T?…-319).
```
NEW
```text
Lower bounds cannot bound ρ_n from above, and P_n is one certificate among many: no uniform-in-n obstruction radius is established here. ρ_n → 0 is now PROVED, with ρ_n = O(n^-5), by an explicit corner witness in PD-T144 (split from (U1) of PD-T?…-319). The absence of a uniform obstruction radius is not proved: (U2) of PD-T?…-319 remains OPEN, and an upper bound on ρ_n does not bound δ_obs(n) from above.
```

**Block 6 — PD-T069 History (append).**

OLD
```text
sympy (developer's and reviewer's symbolic expansions).».
```
NEW
```text
sympy (developer's and reviewer's symbolic expansions).».
- <prep-ts>, <preparer>: Open items synchronised with the split of PD-T?…-319(U1) to PD-T144 (audit-01 E5-F5); no change to this file's theorem or status. Original wording: «… and neither ρ_n → 0 nor the absence of a uniform obstruction radius is proved. Both questions are OPEN (PD-T?…-319).».
```

**Block 7 (optional) — target `bivariate-lanczos-claude-305-three-node-square-case-sqrt-rate.md` (PD-T061), Open items.** If applied, also append the History line shown.

OLD
```text
Explicit constants.
```
NEW
```text
Explicit constants. One explicit instance, not the universal constants c, C: PD-T145 gives, for the triangle {(0,0),(1,0),(0,1)} with equal weights, a consistent ε-perturbation with an exact positive representation of spread √(6ε), and lower spread √((1−3γ)ε/3) for every unit-mass positive fit with functional residual γε, γ < 1/3 (maximum monomial-moment norm on Π_3, convention (R2)).
```
History anchor: OLD `2026-10-31, Claude Opus 5.5 (xhigh, requested), L3 developer, base 2d8c3ab: created in round R01.` (once). NEW: the same line plus `\n- <prep-ts>, <preparer>: Open item cross-referenced to the explicit instance PD-T145; statement and status unchanged. Original wording: «Explicit constants.».`
