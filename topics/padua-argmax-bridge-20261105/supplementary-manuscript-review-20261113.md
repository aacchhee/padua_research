# Supplementary manuscript review — 2026-11-13

Status: COMPLETE at the source identities below. Bounded source review and all requested restoration rereads are complete; the coordinator reports both final builds passed. All six supplementary findings and the 32-pair deletion-integrity followups have been repaired and reread. This is not a manuscript-wide correctness acceptance or a substitute for focused Claude review.

Role: independent supplementary Codex manuscript reviewer. Dispatch identity reported by the coordinator: `gpt-6-astra`, high effort, fresh-context subagent. Runtime serving metadata is not exposed in this subagent context. This supplements, and does not replace, the focused Claude review required for changed analytic text.

Rules read at `2f87ee65f93ba056cf9fb3f9a737a362e864e755`: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`. Read handoff 31, `audit-04-manuscripts.md`, and relevant finding/derivation sections of audit-04 C4A–C4D, P4 and N4. Delta base: `941aa335e60ca7058c8a0113faa76e31217f4753`. No Git state mutation, source repair, new scientific claim, novelty claim, or degree campaign was performed. The novelty gate is inapplicable to this bounded revision review.

## Coverage and limits

I reviewed selected source deltas and their surrounding definitions, concentrating on C4B-01, the J1/J2 gate/elementary clauses, P4-07 termwise maxima, C4C-M3 row identities, C4D-01 corner losses, named-tool statements, and formal pairing. I inspected the early companion consolidation where it touches the corrected numerator, sine product, collision count, regularity of B, and exact row folding. I did not read every line of either complete manuscript, did not read all 147 historical companion pages; the subsequent bounded duplicate review covers exactly the 32 pairs listed below. PDF layout/build and archival artifact preservation remain the coordinator's checks.

The finite-certificate execution claims, historical evidence custody, and complete derivation of every existing comparison charge are outside this supplementary review. The bounded final source-freeze and mutation-control executions are recorded below. The arithmetic-model additions were checked for stated scope and consistency, not independently reproved end to end.

## Findings returned to developers

1. **SR-M1 — material boundary qualification (corrected and reread in both texts).** The new strict assertion `f_j>0` iff `|z|<w` is false on the closed boundary where `mathsf a=0`. For example `r=1`, `x=b=pi/2`, `j=0` gives `|z|<w` but `f_j=0`. Requested the equivalence for `mathsf a>0` / `rho<pi`, followed by complete sinc continuation of the identities on the closed boundary. Both manuscript owners were notified. The stabilized paper wording was reread and is correct. This is a qualification of the explanatory derivation; no theorem threshold or numerical constant needs changing.
2. **SR-M2 — control character (corrected).** A raw carriage return replaced the backslash in the companion relative-mesh ending `t <= rho/3`. Returned to the owner. A later byte scan of all TeX files found no prohibited control characters.
3. **SR-M3 — notation table / implementation mismatch (corrected and reread).** The new companion symbol table advertised `h_m`, `h_n`, `K_sinc`, and `r_hl` while the corresponding calculations still used local `h`, `K`, and `r`. Moreover `h_n(t)` already denotes the mesh-tail series. Requested an accurate scoped table or completed local renames, without repurposing that series symbol. Final text uses `h_m`, `h_pole`, `K_sinc` and `r_hl` consistently with their definitions. During completion, I caught double-subscript substitutions in `D_h`, `H_h`, `epsilon_h`, `ell_h`, unbraced fraction denominators, an old `h k` product, and two old `D_h K` denominators. Developers repaired them; final scans and local rereads confirm the repairs. The shared signed-outer display now uses the same `h_m k` in both sources.
4. **SR-M4 — incomplete companion gate clauses (corrected and reread).** The paper supplied the `u>=0`, `j>j_*`, `U_*>=0` justifications, while the companion still lacked part of that requested J1-02 clause and retained a stale plain `G` in monotonicity prose. Returned to the owner for final synchronization. Final companion gates contain the explicit sign and curvature justifications and consistently use the renamed gate.
5. **SR-M5 — punctuation (corrected).** The paper retained an orphan trailing comma after the central-row retained-entry conclusion. Owner reports corrected.

No source was silently repaired by this reviewer.

## Post-build correction and focused cleanup review

The coordinator’s first companion build caught a duplicated `K_{\rm sinc}_{\rm sinc}` subscript in the unnumbered actual-sample formula. My earlier targeted scans did not search that braced repeated-suffix pattern; the earlier claim that final rename checks were complete was premature. The report was reopened. The developer fixed the duplicate. An expanded mathematical-token review then found additional missed products: `M h^2/8`, `M h^2/24` in the companion pole-cell proof, `eta=h t`, `z_j=h j` in the companion shift derivation, and `h F(z_c)` in the paper BV formula. The intended symbols are respectively `h_pole`, `h_m`, and `h_m`. Each was returned to the responsible developer and repaired; I reread the repaired formulas. The `D_h K_sinc` actual-sample denominator was also checked against the sine-chord identity, not merely matched syntactically.

I then read the entire focused comparison/certification cleanup diff against source checkpoint `319acca` and the surrounding retained derivations. The scalar sine-bound argument is now at its first use. The piecewise coefficient integral, dilogarithm primitive and endpoint counterterm, root-free endpoint comparison and dominated boundary limits, I4 polynomial-square estimate, and pole residual/cusp/harmonic-tail arguments remain explicit. The new central-row extra `2 log(pi)/pi` explanation follows by dropping the negative logarithm term before converting the weighted scalar reciprocal terms to Phi. The certification reductions retain the pointwise cover implication and the order of reflected summation before absolute values. I found no unique proof reason lost in this focused cleanup diff. Extending the check to the initial consolidation against `24a98db` then found the omissions recorded below. This distinction matters: reviewing only the last cleanup diff did not cover the earlier deletions.

After those repairs I repeated exact pairing (19/85/116), source label/reference checks, control-byte checks, a generic adjacent-subscript scan (including braced suffixes), and targeted old-product/rename checks. All passed at the interim source identities paper comparison `9175a020…9234`, companion comparison `195bd4f4…03c5`, companion certification `d003aa52…3e4d`. The final candidate hashes below supersede those interim identities; the last restorations were reread and the scans repeated.

## Complete bounded duplicate-deletion check

At the coordinator's request, I compared every one of the audit's 19 C4C-M1(a) and 13 C4B-05 original pairs directly against `24a98db4c3c4c4d0eede2e3929532956df87911b`, including the changes already present in checkpoint `319acca`. I read each removed mathematical sentence and its retained derivation, using the developer's disposition ledger only as an index. This is a survival-of-reasons check for this finite list, not an independent proof audit of every retained inequality or the complete manuscripts. Original line numbers below are the audit's identifiers; source anchors survive line movement.

The first pass had dropped unique explanations. **SR-M6** records the central-reference BV line, wrap-prefactor condition, S<v parameter-integral branch, elementary central-product bounds, cancellation parameter/entropy facts, explicit shift variation domain, and E derivative. The central-reference omission was first noticed by the developer and independently confirmed by this reviewer. All were returned for local restoration, retaining one derivation per pair. All restorations were reread in the actual source at companion comparison SHA-256 `d56a34a9a88c9815ca850b143efecee08d820c91fc93c05148bd418aa5f015af`; they are correct in the stated local scope. No outstanding deletion-integrity finding remains for this list.

| Pair | Original spans | Reviewer check of reasons retained or requested restored |
| --- | --- | --- |
| C1 | 2093–2113 / 2115–2147 | Normalized displacement, tau, wrap, tail, collision, half-line and central charges retained. Wrap condition and central-reference variation-to-quadrature chain restored and reread. |
| C2 | 2180–2196 / 2197–2207 | Equal-sign unimodal heights, opposite-sign monotone minima, pole jumps and factor four retained. |
| C3 | 2214–2222 / 2224–2258 | Small-amplitude case, branch numerator, monotone sine ratio, four-cut count, endpoint/pole changes and coincident-cut coverage retained; centered-cell kernel is stated earlier. |
| C4 | 2345–2353 / 2354–2394 | True scalar bound, curvature plus cusp contribution, integral quotient identity, product variation and supremum arithmetic retained. |
| C5 | 2396–2407 / 2408–2427 | Split integral, S=v and v=0 limits, three monotone pieces, separation and logarithmic product charges retained; S<v monotonicity branch restored and reread. |
| C6 | 2433–2451 / 2453–2494 | Central parameter definitions, coefficient derivative bounds, product integrals, variation/supremum and hole normalization retained; elementary tan-cot and t-log-t steps restored and reread. |
| C7 | 2553–2559 / 2560–2583 | Even/odd near sums, prefactor, sinc and tau estimates, 117/72 to 121/75 arithmetic, final 7/n+317/n² retained. |
| C8 | 2603–2609 / 2622–2651 | Full numerator, reciprocal sums, geometric/displacement split, sine charges and omitted-tail integral retained. |
| C9 | 2689–2737 / 2739–2745 | Centered-cell identity, both tail integrals, paired logarithms, exact mesh rewrite, four component bounds, log-hole concavity and final identification retained. |
| C10 | 2747–2785 / 2787–2796 | Five maxima, quantified correlation minimum, all derivative monotonicity tests, norm and signed reflection application retained; retained-row allowance corrected explicitly. |
| C11 | 3089–3108 / 3110–3157 | Fixed labels, four product coefficients, psi and prefactor derivatives, harmonic/square sums and differentiated missing tails retained. |
| C12 | 3159–3209 / 3164–3242 | Half-line continuity, derivative jump, total variation/integral, matched summability, kernel primitive and extrema, mean telescoping and finite-sum Lipschitz arguments retained. |
| C13 | 3252–3259 / 3261–3283 | Single-row residual bound, normalized coefficient less than two, endpoint/tail, central, ordinary-perturbation and pole assembly retained. |
| C14 | 3334–3359 / 3361–3392 | Positive index set, denominator/multiplicity table, product derivative, geometric coefficient, sine and tau charges retained; elementary sine bound is available earlier. |
| C15 | 3436–3448 / 3450–3499 | Nonzero and zero residues, harmonic lower bound, origin shifts, both denominators, vector motion and separate weight errors retained. |
| C16 | 3522–3527 / 3529–3557 | Differentiated series, paired-tail mean-value bounds, H2 and upper endpoint bounds, D0 weighted difference, final rational coefficient retained. |
| C17 | 3596–3600 / 3602–3610 | Nonnegative monotone remainders, disjoint right rectangles, Q[1]=-3/m and opposite-constant cancellation retained. |
| C18 | 3690–3726 / 3728–3777 | Two root regimes, variation ledger, hole envelopes and concavity integrals retained; parameter range and p log(rho/p) estimate with axis limit restored and reread. |
| C19 | 3778–3797 / 3799–3833 | Exact finite regrouping, disjoint second differences, two boundary terms, M_F calculation and coefficient sum retained; explicit V domain and log m bound restored and reread. |
| B1 | 240–250 / 267–270 | Endpoint entropy expression, sign, monotonicity, s<=v case and threshold continuity retained. |
| B2 | 270–275 / 282–287 | Root support, threshold integral and s<v comparison retained; explicit E derivative and v=0 case restored and reread. |
| B3 | 408–410 / 489–492 | Complete sine-comparison derivative/sign proof moved to first use. |
| B4 | 801–803 / 808–816 | Arc cases and costs remain before complement estimate; two absolute-value inequalities now stated there. |
| B5 | 843–852 / 853–858 | X,Y defined once; three branches, transition points, logarithmic primitive and closed-edge justification retained. |
| B6 | 1038 / 1043 / 1048 | Q_* derivative integration and positive-denominator reciprocal rearrangement retained; 1/(1+k_*') equals 8/pi² by its definition. |
| B7 | 1101–1105 / 1115–1119 | Both scalar bracket reasons, t sin t inequality, linear-coefficient substitution and upper-bound consequence retained. |
| B8 | 1133–1139 / 1144–1153 | Positive-part bound, nonpositive logarithm sign and log-sine integral retained once. |
| B9 | 1141–1143 / 1173–1180 / 1190–1191 | Li2 definition/derivative, full primitive, both endpoint values and finite counterterm retained. |
| B10 | 1182–1201 / 1203–1220 | Root-free inequality before use, reflected parameters, domination, H/model-loss application, E_c(0)=0 and noncircular origin identification retained. |
| B11 | 1364–1371 / 1373–1376 | Jacobian, support, two signs, centered superlevel intersection proof and F definition retained. |
| B12 | 1399–1400 / 1408–1411 | Change of variable, nonnegative square majorant, exact integrated 319/360, strictness and conversion to p retained. |
| B13 | 1774–1799 / 1800–1841 | Residual symmetry/integral, cotangent derivative, cusp removal, both cell errors, odd/even cusp placement, exact tail identity, convexity and final <5 sum retained. |

## Reconstructed or inspected successfully

- **C4B-01:** `t(1/2-t)/(1-t^2)^2 <= 3/40` follows from the completed square polynomial; its use with `Q'` and cosine is now explicit. The `f(0)=k_0/pi` bracket gives `f(0)/8<3/40`. The logarithmic derivative of the sine ratio has the stated sign because `r cot r` decreases, giving the required ratio bound. The derivative of `log cot((pi-s)/4)` is at least `1/2`, which gives the W lower bound. Combining it with the curvature estimate gives exactly `-(pi-3)w^2/(4pi^3)`. The cusp is counted once on the circle, and endpoints are covered by continuity.
- **J1/J2 and absolute gate:** evaluating the decreasing R at `h_1`, and using `A(h_1)>=T_* cos h_1`, justifies the quadratic upper estimate before taking the endpoint limit. The relative proof explicitly sources the `5/12` and `5/48` terms from the central-pair estimate. Elementary logarithm/arctangent/zeta/gamma constructions precede their main use and include `log pi>11/10`.
- **P4-07 / C4C-m7:** the retained-row maximum is bounded only jointly with the `3 bar L/n` allowance. With `bar L=1+L` and `pi>157/50`, the displayed aggregation gap is greater than `(275+219L)/157>0`. The constant bookkeeping and correlation-saving distinction are preserved.
- **C4C-M3:** checked the parity sine shifts giving `4a/(w^2-z^2)`, the paired cotangent partial fraction giving `-sin b/w`, and the finite cotangent-sum intermediate formula for the signed actual row. The positivity boundary exception is SR-M1. The new row-average decomposition correctly retains the cancellation integrand.
- **C4C-m4:** the residual increment now uses the signed `-2w sum E` identity and the exact product difference evaluated at the origin reference in its first term; the prior missing reference evaluation is supplied.
- **C4D-01:** the relative bound yields the axis loss after dropping nonnegative `A_4+rho J_W`; `k_Wy>=k_Wx` allows the same linear allowance on both axes. The lower curvature coefficient is positive in the stated range. At the diagonal the model loss plus origin/global errors gives the displayed loss using `P<3/2` and the central-pair upper bound. The two added re-entry rows identify the dependencies. The three n=256 rational substitutions are consistent with their stated definitions and signs.
- **C4A / N4 tools:** inspected the finite sine product and its constant, Fourier-uniqueness statement behind the cotangent series, BV centered-cell bound, triangular second-difference measure identity, dilogarithm definition, and periodic Bernstein scaling. The restored corner numerator/subtraction, lattice-shell count, Euclid step, and extended smoothness interval for B supply the cited reasons.
- **Evidence language:** the revised paper distinguishes 471 trees from 942 records and states that native numerical endpoints are not premises or certified values. The exact quadratic maximum on the clipped polygon is described with vertices, stationary edge points, and interior critical points; the singular-Hessian explanation is valid. The sine-ratio kernel includes the removable values. These are source-text checks, not fresh certificate verification.

## Executed checks

- Read-only `git diff` against the recorded base and targeted source searches.
- Independently invoked the existing `code/onset512_analytic/check.py` interval API from a fresh `python -B` process and parsed all 15 by 4 new paper table entries as exact fractions. For degrees 192, 256, 295, and 512, separately recomputed L, T, ebar, KD, CE, C4, kWx, kWy, dbeta, M, U*, dx, dy, lx, ly. **All 60 printed intervals contain the exact-rational checker intervals. The check was repeated after the table was split into two panels and passed again.** This is an independent execution of the existing API, not an independently authored interval implementation.
- Scanned all current TeX source bytes for control characters other than tab/newline: none after SR-M2 repair.
- Scanned source `label`, `ref`, `eqref`, and `pageref`: no missing referenced label and no duplicate label in either text at the scan point.
- Called the correspondence helper's parsing functions read-only during development; the remaining differences were confined to late-owner blocks being synchronized. The final read-only call to `compare_pair(current_sources(paper), current_sources(companion))` passed: **19 statements, 85 numbered display environments, 116 labels**, matching headings, label order, numbering setup and bibliography. This deliberately bypasses the old frozen-source identity, which must be updated by the coordinator; it is not a successful final-freeze check.

## Final candidate identity

The identities below were read after the last requested restorations and the coordinator’s addition of the array package to the companion preamble and paired coverage-table en-dash typography. Those final mechanical changes were reread. Any later TeX/Bib change requires checking its delta against this review. Source pairing, byte-level control-character, adjacent-subscript, old-product and reference scans were repeated at this point and passed. The coordinator reports both final builds exited zero (paper 57 pages, companion 150 pages), with no errors, warnings, overfull boxes or undefined references/citations; underfull messages remain. Those builds were executed by the coordinator, not this reviewer. The coordinator also reports no source changes after these identities. The subsequent source-freeze and mutation-control checks were independently executed by this reviewer as recorded below; this report does not declare publication readiness.

The new `companion-paper/check_baseline_controls.py` was inspected as bounded mechanical validation code, then reinspected after the coordinator repaired its target selection. The repaired harness extracts the exact shared first theorem block and changes `n\geq2` to `n\geq3`, selects the numbered node display containing `j+k`, and appends an unnumbered `0=1` formula to copied section dictionaries. These changes correct missing-target and differing-prose-occurrence errors in the initial harness. The coordinator reports preserving those failed attempts in the log; this reviewer executed only the repaired harness. I also inspected the one-line `FINAL_BASELINE` change from `24a98db4c3c4c4d0eede2e3929532956df87911b` to separately committed TeX/Bib freeze `ad908acb21d3589d85635618ff68f63dd01cfbca`. No manuscript source changes were involved in this followup.

The harness mutates only copied dictionaries. Its six paired controls must preserve paired parsing and fail both source freezes; its companion-only statement mutation must fail pairing. No source/Git mutation path was found. The `j+k` to `j-k` example tests exact byte preservation even though the parity meanings coincide. The unnumbered false formula demonstrates that exact freezing rejects content beyond the numbered-block parser. These are bounded mechanical controls, not tests of mathematical correctness or complete parser coverage.

Independently executed from `companion-paper`, all with exit zero:

- `python -B check_correspondence.py`: final source freeze PASS at `ad908acb21d3589d85635618ff68f63dd01cfbca`, 19 statements / 85 numbered display environments / 116 labels.
- `python -B check_correspondence.py --archival`: historical source pairing PASS at the recorded original pair, 13 statements / 90 numbered display environments / 113 labels. This command did not inspect PDF artifacts.
- `python -B check_baseline_controls.py`: all seven controls PASS (theorem quantifier, numbered formula, unnumbered formula, bibliography, extra TeX file, main preamble text, companion-only statement mismatch).

All recorded TeX/Bib hashes were checked again after these executions and remained unchanged. The final code hashes below identify the repaired harness and baseline pointer.

| File | SHA-256 |
| --- | --- |
| `paper/main.tex` | `14c4ba403bff6c6be12db81f91e9be6dd4afe977573f8365e9f480b974816847` |
| `paper/references.bib` | `138871f1d0d1c70a5c753cae8ae2004ba094511c8f3afe031fd2c51210ee39fc` |
| `paper/sections/certification-unified.tex` | `0827c2205f453c4a83027747aa923f09e9f0e13ecb7fe13013b7c26c40b086b2` |
| `paper/sections/comparison-unified.tex` | `9175a020a8b17eae89e79b3aee5697148f68c257bad980b408a1e484d0cb9234` |
| `paper/sections/corner-unified.tex` | `8ecffbf2c27412a425f837543b110a934dc3b0f215218670b86f1e979c4e7b11` |
| `paper/sections/introduction.tex` | `898086d2be870ea56b5619ffa32dedcd1bd6987e2e4df3796aed415fbf5e9916` |
| `paper/sections/localization-unified.tex` | `cac0abf43ec9903fa4c7fe7c5b89a28bf2cefdd542caad1e12040e1e49e59e86` |
| `paper/sections/preliminaries.tex` | `ea22564e8f0ccb2089ed44f59b295801f601420c193128ca86116e1eea046180` |
| `companion-paper/main.tex` | `b3a9eb5f7ae953e19fd39c666430a41c79044a902ea6e97d34f92b867720bcdb` |
| `companion-paper/references.bib` | `138871f1d0d1c70a5c753cae8ae2004ba094511c8f3afe031fd2c51210ee39fc` |
| `companion-paper/sections/certification-unified.tex` | `9bad33ea8c1ba1df1cc68b35690a1ca32d895087282925350621de9f4deba9f9` |
| `companion-paper/sections/comparison-unified.tex` | `d56a34a9a88c9815ca850b143efecee08d820c91fc93c05148bd418aa5f015af` |
| `companion-paper/sections/corner-unified.tex` | `fa59b5959884813d1cc64de93646d13b0102938e629c2ce68b5d3b2f65c0c916` |
| `companion-paper/sections/introduction.tex` | `32d30750c826ad1758c4d9610471b39a61def8c6369d089d273af69b027b82cd` |
| `companion-paper/sections/localization-unified.tex` | `e2c527a24c473bbfc40662aa5ebb0b893bb23a39f3f73bfb6b84ac6a9985df3a` |
| `companion-paper/sections/preliminaries.tex` | `8e536da1be0c2992443b7dcb4b4b4c680fde6de67d45de79b0ee29a6e39f11b1` |
| `code/onset512_analytic/check.py` | `ff2859eeb9ccab91e8cfa996318e4f1129502dc90f5c2fa90754350453a51751` |
| `companion-paper/check_baseline_controls.py` | `ef474bb594d65abf5219e1574fabc2e2acdf3bd53ec344d555afa9ece408e309` |
| `companion-paper/check_correspondence.py` | `bb231904779141fa684076b8afd623e141b001e8c6a04bcaa1d43a892fa7edd8` |


## Dated correction after Claude audit-05 — 2026-11-13

The preceding deletion-integrity checklist overstated survival of three
unique one-line reasons. Audit-05 M5A-02 identifies B5's primitive
`integral T_t = 4a log sin(t/2)`, C1's prefactor identity and wrap charge,
and C10's amplitude bound `A cos x + B sin x <= sqrt(A^2+B^2)`.
Those checklist rows must not be used as evidence that these lines were
retained in ad908acb. The audit-05 response restores them explicitly;
response-05 and the new focused review record the changed source and
checks. The original review and its declared scope remain historical.
