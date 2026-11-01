# E3/E4 candidate memory and novelty gate

Codex mathematical developer; requested `gpt-6.1-sol`, xhigh, actual variant/effort not separately exposed. Rules/base read at `806cc7b4509fd93bae652f9545d32d95529f8281`, branch `codex/padua-lanczos-drift-20261101`. New files only; no allocation of final global IDs, shared-state mutation, Git operation or handoff by this subagent.

Response-01 revision (Claude Opus 5.5, xhigh; answering audit-01 E34-F1–F3, F5, F6, F8–F10):

- IDEA?drift-codex-10 and IDEA?drift-codex-14–16 are updated;
- IDEA?drift-claude-17 is new;
- no other entry changed.

Original wording of each changed line is quoted in History at the end.

## Gate performed before mechanism development

Scanned the complete `state/IDEAS.md` headings, IDs, aliases and summary/disposition rows in bounded views, and read its obstruction/disposition tables, including the historical seed dispositions, canonical bivariate entries IDEA-077–176, MZ, lattice and programme-ideas warnings. Broad tables were also searched for span, selection, staircase, inverse, triangular, Krylov, residual, reorthogonalization, orthogonality and commutator. Searched the bivariate theory, registry/negative-results records, old topic report/SPLITS and L2 candidate/review records for those mechanisms and synonyms. Read `literature/INDEX.md` metadata/scope rows and relevant full rows; did not read all literature fulltexts. One attempted search named nonexistent `tracks/bivariate-lanczos/PROOF_STATUS.md`; the existing theory/negative-result records were used instead. A failed path search is not evidence of absent prior art.

Shortlist: PD-T029–055 (in particular full detailed reading of PD-T029/PD-T032/PD-T041/PD-T046/PD-T047/PD-T050/PD-T051/PD-T053/PD-T054/PD-T055); PD-N013/PD-N015; summaries of the remaining PD-T029–080 and PD-N007–031 to check neighboring claims and negative scopes. Read the old topic report and L2 sections of SPLITS; L2 candidates; L2 prior-art and reconstruction reviews. Nearest IDEA records are IDEA-127/130/134/140 (node coefficients, propagators and exact growth), IDEA-147/148/150/151 (formed sections, full-reorth drift and tested selections), and IDEA-079/084 (original reorthogonalization/commutator seeds). The complete canonical summary of each was read; linked detailed L2 records and the theory above supply the hypotheses.

Literature shortlist: LIT-241–243 (Barrio–Peña–Sauer: one coordinate per polynomial, selection freedom and inverse triangular error bounds), LIT-280–284 (Hokanson / Zhu–Nakatsukasa: exact span versus orthogonality and fitting), LIT-251 (Zhang–Su–Li fitted-value bound), LIT-253/255/256/257 (one-operator backward/subspace context), and the Simon/Jia–Li template via the existing L2 review. Existing records include WebFetch digests, secondary accounts and pending fulltexts; these reading limits are inherited. No new PDF was opened, no new external search conducted, and no historical novelty asserted.

Applicable obstructions read in full: partly formed J-columns (OBST-03); full versus truncated orthogonalization (OBST-07); finite exact certificates are not asymptotic statements; PD-N013's full-reorth drift; PD-N015's four-rule failures do not quantify over every selection; (C) gives acyclicity but not residual-size control; the K recursion contains reorthogonalization coefficients and gives no universal lower bound. Moment-cone, cubature and Givens obstructions were screened as neighboring mechanisms; none supplies an E3/E4 conclusion.

The exact E1 setup was coordinated with its developer: T_24 and rationally rotated Q_24, BJ/dev, mirror, alt and pivot rules; aggregate preprojection residual sensitivity; normal projector; no automatic reduction of arbitrary aggregate directions to a standard per-operation error realization. New E1 analytic records are related dependencies only where explicitly cited, not inherited measurements.

## IDEA?drift-codex-10 — Polynomial-surrogate residual certificate and filtered minimax selection

Aliases: computed polynomial surrogate; normalized node inverse; finite staircase certificate.

- Question / scope: obtain a computable sufficient selection criterion for span accuracy, keeping the unrestricted staircase theorem visible.
- Mechanism and hypotheses: computed-coefficient polynomials still form a triangular basis of Π_s; their node-row difference from Qhat is a forced triangular recurrence. A Gram bound converts its norm into a projector-distance upper bound. Minimize a row-normalized exact inverse score over (C)-staircases after filtering by χ. The staircase restriction is not used in the first-order bound (6) and excludes the pivot-adaptive rule. The same bound holds over all 2^(s(s−1)/2) admissible selections, without the (C)-based implicit-section interpretation (PD-T?drift-codex-11 Scope; E34-F5).
- Closest registry entries (read in full): IDEA-127/130/134/140 and their PD-T029/032/037/041 records; IDEA-147/148/151 and detailed L2 records PD-T046/047/050/051/053/054/055, PD-N013/015.
- Separation criterion vs closest entry (and observation that falsifies it): prior node identities/amplification observations do not alone establish the computed polynomial surrogate's exact range or a span upper certificate. A missing triangular leading coefficient, a non-admissible parent, or a source outside the declared residual relation kills this proof. A matching predecessor theorem for this exact span certificate erases any distinction; no novelty is claimed.
- Literature baseline and search limitations: BPS inverse triangular error bounds and selection freedom are known; the additional output quantity is span distance. Existing L2 review separates V+A fitting/orthogonality results from span accuracy. Primary-literature coverage is incomplete as stated above.
- Applicable obstructions and exact hypotheses broken: does not claim (C) bounds inverse norms; does not infer drift from large inverse entries; χ is retained; the source model is explicit; empty acceptance sets remain failures to certify.
- Novelty gate verdict: variant with a documented output distinction; no historical priority claim.
- Cheapest decisive test: prove triangularity of the surrogate and check the row normalization/source scaling before any benchmark computation.
- Kill criterion written before testing: reject the certificate if the surrogate need not span Π_s under the stated support/admissibility assumptions, or if the projector bound needs a hidden coefficient-closeness hypothesis. Reject a global safety claim if it has no independent bound on K and χ.
- Test discriminability: the symbolic proof addresses precisely those two possible gaps; it does not test whether any frozen benchmark selection passes the score.
- Actual test results and committed evidence: analytic proofs in PD-T?drift-codex-10/11. No score computation or computer proof claimed. Codex independent-math-01 ([checks/independent-math-01.md](checks/independent-math-01.md), E3 paragraph and finding 3) accepted the span/inverse/first-order reconstruction and requested a computability representation qualification; that qualification was applied. Claude audit-01 ([checks/audit-01/E3-E4-records-10-15.md](checks/audit-01/E3-E4-records-10-15.md)) CONFIRMED PD-T?drift-codex-10 and CONFIRMED-WITH-CORRECTIONS PD-T?drift-codex-11. Corrections E34-F4 (family-dependent remainder) and F5 are answered in response-01.
- Disposition and precise rejected scope, if any: retained sufficient criterion; unrestricted polynomial staircase safety remains OPEN. Family application is CONDITIONAL on explicitly unverified polynomial score/χ/source bounds. Proposed durable OPEN home: PD-T054's open item, cross-referenced from IDEA-151 (E34-F8; literal blocks in the response-01 proposal).
- Disposition reason: conditional application, not an all-degree success. A computable sufficient condition is substantive but may reject all available candidates.
- Canonical theory / negative-result ID: PD-T?drift-codex-10 and PD-T?drift-codex-11.
- Topic / audit / history: E3; analytic development 2026-11-01; Claude audit-01 2026-11-01; response-01 corrections await re-audit.

## IDEA?drift-codex-11 — Minimize an unqualified inverse norm and omit χ

Aliases: raw-L minimax; unnormalized propagator score; staircase structure alone.

- Question / scope: can the informal phrase “minimize max ||L^*(-1)||” directly yield O(u poly(s)) drift?
- Mechanism and hypotheses: use the old unnormalized L and assume its inverse score is the relevant dimensionless response.
- Closest registry entries (read in full): PD-T032/041 and IDEA-134/140; PD-T046's explicit normalization factor and IDEA-147; PD-T054/IDEA-151.
- Separation criterion vs closest entry (and observation that falsifies it): a correct criterion must preserve the source budget under coordinate scaling and row normalization. Failure to distinguish L^*(-1) from Lbar^*(-1)=L^*(-1)diag(1,β) erases the alleged improvement.
- Literature baseline and search limitations: BPS triangular scaling is prior art; PD-T041 explicitly records coordinate scaling. No novelty claim or new external search.
- Applicable obstructions and exact hypotheses broken: near-breakdown χ can be arbitrarily large; (C) does not bound it or the inverse. PD-N015 preserves failures even for staircase rules.
- Novelty gate verdict: unqualified variant, consolidated into IDEA?drift-codex-10 after correction.
- Cheapest decisive test: write the normalized residual f_k/β_k and transform L.
- Kill criterion written before testing: if a factor 1/β_k remains in the source budget, the χ-free reading is unsupported and must not be claimed.
- Test discriminability: this is a scaling/normalization test, not an empirical safety test.
- Actual test results and committed evidence: the source is f_k/β_k; local budgets give χ. PD-T?drift-codex-10/11 state the corrected score and a χ filter. No counterexample theorem is invented from a failed route.
- Disposition and precise rejected scope, if any: consolidated/corrected; unconditional χ-free or (C)-alone theorem not pursued. Existing stronger safety claims remain OPEN or retain their old measured failures.
- Disposition reason: equivalent after correct normalization; a separate PD-N is not warranted merely by this correction or abandonment.
- Canonical theory / negative-result ID: no separate ID; correction in PD-T?drift-codex-11.
- Topic / audit / history: E3; retained failed route, 2026-11-01.

## IDEA?drift-codex-14 — Every-rule, every-error positive BJ drift lower bound (pathwise formalization of PD-T055's quantifier)

Aliases: pathwise universal obstruction; noiseless quantifier test; zero-error quantifier test; noiseless exact-projection counterexample; universal versus worst-case reorthogonalization. Former theory draft «PD-N?drift-codex-14 — A pathwise positive lower bound is false in a model admitting zero errors», withdrawn as a registry vehicle in response-01 (audit-01 E34-F3).

- Question / scope: would PD-T055's (U) be well posed if its unfixed error quantifier were read pathwise, i.e. for every permissible rule and every error realization admitted by an upper-bound perturbation model?
- Mechanism and hypotheses: no mechanism is attempted. The withdrawn draft's line «Attempted mechanism: deduce a positive drift lower bound from BJ's omission of products and the clamped commutator recursion…» described nothing its argument engages. The entry tests a candidate *formalization* under these hypotheses: admissible (in particular BJ) parents, exact positive weights, U(s), an upper-bound model |δ|≤u that admits the zero perturbation, and exact-real full projection.
- Closest registry entries (read in full):
  - PD-T055 (wording and open quantifiers; its (U) concerns “the computed run” in floating point with working-precision storage);
  - **PD-T032 part 2** (“In exact arithmetic Ĥ_J = H_J”), which already contains the exactness of the implicit section;
  - IDEA-148 and PD-N013 (tested real runs); PD-T047 (identity only); PD-N015 (tested selections).
- Separation criterion vs closest entry (and observation that falsifies it): a lower bound with this quantifier must survive the zero-error branch. Nothing separates the refutation from “zero error is admissible” plus PD-T032 part 2. The negative statement is a routine remark, not a mechanism failure, so no distinction is claimed.
- Literature baseline and search limitations: standard perturbation sets include zero; no literature priority claim. The existing L2 review never proved a universal lower bound.
- Applicable obstructions and exact hypotheses broken: working-precision storage is relaxed (exact-real vectors). The refutation must not be transferred to literal IEEE runs or to worst-case readings. The commutator recursion has no positive source lower bound.
- Novelty gate verdict: duplicate in substance (PD-T032 part 2 plus the admissible zero error); recorded only as a quantifier clarification of PD-T055.
- Cheapest decisive test: exact full Gram–Schmidt with all errors zero.
- Kill criterion written before testing: zero defect and exact implicit section contradict every positive proposed lower bound in that model.
- Test discriminability: decides the pathwise perturbation-model quantifier only; does not decide worst-case or actual IEEE quantifiers.
- Actual test results and committed evidence (full mathematical content of the withdrawn draft):
  - *Statement.* Let the allowed perturbation set contain the zero perturbation, and let exact projection against all previous columns and exact normalization be permitted. Take any positive discrete measure satisfying U(s) and any admissible parents (BJ in particular). The exact run is a permissible rule under an allowed (zero) realization: form A_kq_p, subtract its exact orthogonal projection onto all earlier columns, divide by the positive residual norm. It has range(Q̂_t)=S_t and δ_X(t)=δ_Y(t)=0 for 0≤t<s, and an implicit J-section equal to the exact one. Hence no assertion “for every rule and every allowed error realization, max_(t<s) δ_J(t) ≥ cρ^s u||J||”, with c,ρ,u,||J||>0, holds in that model. This remains true when the measure must be non-product: the uniform measure on T_3 satisfies U(3) and has non-Cartesian support.
  - *Proof.* Inductively, each column's polynomial has its intended nonzero leading monomial and only preceding monomials; under U(s) no residual vanishes. At each completed degree t the columns are therefore an orthonormal basis of S_t. X and Y map S_t into S_(t+1), so both defects vanish. The formed J-columns are exact, and the implicit section equals H_J in exact arithmetic by PD-T032 part 2. (The draft re-derived this from JY=YJ, PD-T047's acyclic BJ implicit recursion, and the induction JQ_(s−1)=Q_sH_J.) The zero perturbation contradicts every strictly positive lower bound.
  - *U(3) on T_3.* The row-factor proof is now in PD-N?drift-codex-15. T_3 is not Cartesian: both marginals contain 0 and 3, and (3,0) and (0,3) are present, but (3,3) is absent.
  - *Quantifier table.*

    | Proposed quantifier | What is decided |
    |---|---|
    | Every rule, every model-admissible error sequence | Refuted, trivially (this entry) |
    | Every rule, some model-admissible adverse error sequence | Not refuted; PD-N?drift-codex-15 gives only a fixed-degree O(u) example |
    | Every rule, its actual specified IEEE output | OPEN; a different assertion |
    | Some tested rules, measured actual outputs | PD-N013/PD-N015; unchanged |

    There is no zero-rounding argument against the second or third row. Exact-real projection is not claimed to satisfy literal finite working-precision storage. Any final formalization of PD-T055 must choose one model rather than interchange them.
  - *Checks.* Claude audit-01 run 2 (`checks/audit-01/scripts/E34/e4_rec14_zero_error.py`): exact zero-error Gram–Schmidt with BJ parents on T_3 (s=3) and T_5 (s=4) gives exact spans and A S_t⊆Ŝ_(t+1) for every t<s: PASS; rerun in response-01: PASS. Codex independent-math-01 (E4 paragraph) confirms that only the universal-over-all-model-errors reading is refuted.
- Disposition and precise rejected scope, if any: REJECTED: refuted, as an **ill-posed formalization of PD-T055's quantifier**. It refutes only the “every admissible error realization” reading, in a zero-admitting model with exact-real vectors. Deterministic IEEE behaviour, literal working-precision storage and a worst-case-over-errors obstruction are not refuted. PD-T055 remains OPEN and unchanged apart from the proposed quantifier note.
- Disposition reason: refuted: the negation is established in the stated model. No PD-N, for three reasons: the negative statement is a one-line consequence of the admissible zero error and PD-T032 part 2; it engages no mechanism; and the refuted reading was introduced by this campaign. Following AC's L5 decision and the IDEA-175 precedent, it stays an IDEA disposition plus a PD-T055 note.
- Canonical theory / negative-result ID: none. The former draft file `tracks/bivariate-lanczos/theory/drift-codex-e4-14-noiseless-quantifier-refutation.md` is withdrawn, and the orchestrator removes it at preparation. The proposed PD-T055 note is in the response-01 text for proposed-record-changes.md.
- Topic / audit / history: E4. Codex development 2026-11-01. Claude audit-01 finding E34-F3 (mathematics confirmed; PD-N vehicle not endorsed). Converted in Claude response-01, 2026-11-01.

## IDEA?drift-codex-15 — Prior-vector subtraction repairs fixed-degree closure after an adverse raw-product source

Aliases: fixed-degree quotient invariant; fixed-degree projection-only closure obstruction; exact fixed-prefix instance of PD-T055's heuristic span identity. Superseded alias «information-never-formed local obstruction»: its formed/unformed-J reading is withdrawn (audit-01 E34-F1).

- Question / scope: within one degree, keep the exact prefix, the parents and the raw products fixed. Can arbitrary projection coefficients and passes then restore exact (or o(u)) span and X/Y-closure after an aggregate source in one raw product?
- Mechanism and hypotheses:
  - an exact orthonormal prefix through degree t and fixed admissible degree-(t+1) raw products;
  - no revision of earlier vectors and no extra products;
  - arbitrary finite prior-subtraction coefficients and passes;
  - one source with a nonzero normal part;
  - U(t+1) and M>N_(t+1), on any positive measure.
- Closest registry entries (read in full):
  - **PD-T055's recorded heuristic**: span Q̂_(≤k)=span(Q̂_(<k), B_kq̂_(p(k))−f_k), so the step-k coefficients change the spans only through f_k. Also PD-T055's OPEN target.
  - IDEA-148/151, PD-T047/050/053 and PD-N013/015.
- Separation criterion vs closest entry (and observation that falsifies it): the span identity itself is PD-T055's. The heuristic is first-order and lets parents change; with a fixed prefix it becomes exact for all coefficients. The only additions are closed forms that give the angle and both defects exactly:

  θ=||f_⊥||/sqrt((1+α)²b²+||f_⊥||²),   δ_A=κ_Aθ,   κ_(A_m)≥b,

  together with the explicit T_3 constants. A predecessor stating the exact fixed-prefix identity with a rule-independent defect formula would erase the distinction; none was found in the documented search. A permitted operation that adds a vector outside the current product plus prior span, or revises a parent, kills the invariant.
- Literature baseline and search limitations: elementary quotient-space linear algebra; no historical novelty claim, no new external search.
- Applicable obstructions and exact hypotheses broken: strengthens tested-schedule failure to all coefficients within one degree. It does not freeze the coefficients in the old clamped recursion or assume they never change K. It does not explain PD-N013(b)'s J/F asymmetry: the fixed-degree defect is O(u) in whichever operator's image of S_t meets the perturbed column.
- Novelty gate verdict: **variant — an exact fixed-prefix, single-degree instance of PD-T055's recorded heuristic span identity**, with closed-form angle and defect constants and an explicit T_3 instance. No new mechanism and no historical priority.
- Cheapest decisive test: derive the completed span with one source, compute the angle and the defects exactly, and check the T_3 instance by its ten-row certificate.
- Kill criterion written before testing: if later allowed raw products restore the missing exact direction, the adverse source cannot certify persistent closure failure. If the defect remains only O(u), do not promote it to the exponential PD-T055 target.
- Test discriminability: the exact identity decides closure repair for all declared coefficient rules within one degree; it does not decide amplification or IEEE realizability.
- Actual test results and committed evidence: PD-N?drift-codex-15 proves the general fixed-degree lemma and the T_3 instance (span V⊕span{w+εe}, ||w||²=28/115). In the instance, δ_X(1)=(2/sqrt(3))bθ_2 (the former bound (8), with equality) and δ_Y(1)=bθ_2. Checks:
  - Codex independent-math-01 ([checks/independent-math-01.md](checks/independent-math-01.md), E4; [evidence/independent-math-01.json](evidence/independent-math-01.json), `independent_own_checker.E4`): PASS for the T_3 polynomials, moments, norms, the Jq_y identity and the u inequalities.
  - Claude audit-01 run 1: exact reconstruction; 48 sampled rules; equality in (8); δ_Y; controls.
  - Response-01 checker `tracks/bivariate-lanczos/code/drift/e4_closure_check.py` → [evidence/response-01-e4-closure.json](evidence/response-01-e4-closure.json): 28 exact instances.

  The temporary SymPy calculation used in the original derivation has no recorded command, output or hash, and it is not evidence. No computer-proof status is claimed.
- Disposition and precise rejected scope, if any: REJECTED: refuted for the claimed fixed-degree exact-closure/o(u) remedy against admissible raw-product sources, in the rule class and parameter range of PD-N?drift-codex-15. The obstruction itself is PROVED; O(u poly(s)χ) stability is not refuted.
- Disposition reason: every permitted rule has the same completed span, with θ_(t+1)>0 and δ_(A_m)(t)≥bθ_(t+1). For the T_3 relative source, θ_2≥2u, δ_X(1)≥u and δ_Y(1)≥u.
- Canonical theory / negative-result ID: PD-N?drift-codex-15.
- Topic / audit / history: E4. Analytic fixed-degree development by Codex, 2026-11-01. Claude audit-01 findings E34-F1/F2. Rescoped and recredited in Claude response-01, 2026-11-01.

## IDEA?drift-codex-16 — Extend the quotient invariant to exponential every-rule drift

Aliases: multi-degree information obstruction; universal adverse-source amplification.

- Question / scope: prove the strong PD-T055-type result for every projection-only rule on one explicit non-product family, with an adverse source and controlled χ/reference conditioning.
- Mechanism and hypotheses: propagate the fixed-degree missing-direction quotient across many degrees while allowing the parent basis to change under earlier projections.
- Closest registry entries (read in full): PD-T041's exact finite inverse growth; PD-T047/050's coefficient-dependent residual recursion; PD-T055's OPEN target and its heuristic, whose parent-change term B_kv is exactly what a multi-degree argument must control; IDEA-140/148/151 and IDEA?drift-codex-15.
- Separation criterion vs closest entry (and observation that falsifies it): must prove invariance or a lower response bound after **all** allowed earlier basis changes, not just arbitrary coefficients within a degree whose parents are fixed. A rule-dependent parent change that can cancel the chosen direction kills this proof route unless controlled.
- Literature baseline and search limitations: no new external search. Existing prior-art reviews are bounded and do not prove absence of such a theorem.
- Applicable obstructions and exact hypotheses broken: K changes with reorthogonalization; large unprojected inverse does not imply large normal drift; arbitrary aggregate sources need not be per-operation realizable; zero errors prohibit a pathwise positive lower bound.
- Novelty gate verdict: continuation of the existing OPEN target, not a newly proved mechanism.
- Cheapest decisive test: identify a multi-degree invariant that is unchanged by every permitted parent-gauge change; alternatively construct a valid cancelling rule.
- Kill criterion written before testing: reject a universal deduction if it treats coefficients as invariant, neglects normal projection, or switches from “some adverse error” to “every actual error.”
- Test discriminability: failure of that argument leaves the theorem OPEN; it does not refute the theorem.
- Actual test results and committed evidence: the fixed-degree invariant is proved in -15, now for any fixed degree, positive measure, admissible selection and single raw-product source. It does not survive arbitrary parent revision by the argument given. No multi-degree lower bound obtained. Rules that repair parents or inject a reference basis are retained separately as IDEA?drift-claude-17.
- Disposition and precise rejected scope, if any: deferred/OPEN, not REJECTED. Resume with a genuinely invariant quotient or controlled parent-gauge argument plus a realizable error generator.
- Disposition reason: missing substantive mathematical step; insufficient evidence is not a negative theorem.
- Canonical theory / negative-result ID: original PD-T055 remains the durable OPEN target; no new PD-N for an unfinished proof route.
- Topic / audit / history: E4; all stronger wording retained as OPEN, 2026-11-01.

## IDEA?drift-claude-17 — Parent-repair and reference-basis rules against the BJ span drift

Aliases: parent reorthogonalization against an extended-precision basis; reference-basis injection; PD-T055's “cheapest discriminating experiment”; rules outside the projection-only class of PD-N?drift-codex-15.

- Question / scope: can a rule *outside* the class R of PD-N?drift-codex-15 remove the fixed-degree obstruction there, and more importantly the multi-degree BJ span drift on non-product measures, with vectors stored in double precision? Such a rule changes the raw products by repairing the parent before the product is formed, or uses vectors from a well-conditioned or extended-precision reference basis.
- Mechanism and hypotheses: before forming B_kq̂_(p(k)), reorthogonalize the stored parent q̂_(p(k)) against an extended-precision orthonormal basis of the computed or the exact previous space, then round back to double. A variant injects reference-basis directions. In the fixed-degree lemma, the repaired product differs from the R-product by B_k(Δparent), which can carry the missing component along w. Hypothesis (H17): such a repair reduces max_(s<n) δ_J(s) and the reference drift on the L2/E1 non-product benchmarks to poly(n)·u.
- Closest registry entries (read in full):
  - PD-T055: its open item names exactly this experiment as a structurally different rule within (U). (U) excludes rules that change the selection or store vectors in higher precision.
  - PD-T043(c): long-double storage scales the loss with the storage precision.
  - IDEA-154/PD-N016: extended-precision window dot products fail as a coefficient-channel remedy; drift-insensitivity P3 survives.
  - IDEA-148/PD-N013: full reorthogonalization drifts. IDEA-151/PD-N015: tested selections.
  - PD-N?drift-codex-15 (fixed-degree obstruction for R) and IDEA?drift-codex-16 (multi-degree route).
- Separation criterion vs closest entry (and observation that falsifies it): the rule must change the raw products, not only the coefficients. It adds to a parent or product a vector outside the stored double-precision span, computed from information that the stored columns do not carry. The separation is erased in three cases: (i) the repair is equivalent to storing all vectors in higher precision, which is outside (U) and covered by PD-T043(c); (ii) it amounts to a different selection; or (iii) its measured drift matches plain BJ+full CGS2 within the factor 2–3 already recorded for the tested rules in PD-T055.
- Literature baseline and search limitations: no new external search; the existing L2 prior-art review is the baseline. Reference-basis reorthogonalization is standard practice, so no novelty is claimed.
- Applicable obstructions and exact hypotheses broken:
  - The repair breaks R's “fixed raw products, nothing outside the stored span” hypotheses, so PD-N?drift-codex-15 does not apply. PD-N013 covers only the tested rules.
  - A reference basis must itself be accurate to poly(n)u, as (U) presupposes, and its conditioning must be recorded; ill-conditioned references do not certify drift.
  - Whether parent revision is admitted in (U)'s rule class must be fixed together with (U)'s formalization.
- Novelty gate verdict: variant — a continuation of PD-T055's recorded open-item experiment; no novelty claim.
- Cheapest decisive test: PD-T055's experiment, run as follows.
  - Rule and benchmarks: BJ with full CGS2 against all previous columns, vectors stored in double, on rotπ/4 and the triangle (L2 benchmarks) or the frozen T_24/rotated-Q_24 grids. Before each product, reorthogonalize the parent against an orthonormal basis of the previous computed space held in extended precision (e.g. mpmath at 50 digits).
  - Measurements: max_(s<n)δ_J(s), δ_F(s), and the drift against a well-conditioned reference (u·κ recorded), at n=16, 20 and the largest recorded degree (rotπ/4 n=24, triangle n=20), compared with the unrepaired rule on the same nodes.
- Kill criterion written before testing: REJECTED: failed if, on both rotπ/4 and the triangle at their largest recorded degree (n=24, n=20), the repaired rule's max δ_J/(2||J||) and reference drift are within a factor 10 of the unrepaired BJ+full-CGS2 values. Survives (MEASURED, finite scope) if both fall to ≤1e−12 at those degrees on both sets. Inconclusive if the reference's u·κ exceeds the measured drift, or if the values fall between these thresholds.
- Test discriminability: the test separates “drift generated by rounding and propagated by the selection independently of the rule” (the content of (U)) from “drift removable by a parent repair that keeps double storage”. It does not decide (U) for all rules, and it does not separate the effect of extended-precision parent information from that of extended-precision storage unless the cost and precision used are recorded.
- Resources / cost ledger: extended-precision reorthogonalization of each parent costs O(M·N) operations per column at multiprecision speed. This is expected to be feasible for M≈1681, n≤24 (an estimate, not measured); it is not run in response-01.
- Actual test results and committed evidence: none. Not run.
- Disposition and precise rejected scope, if any: deferred; not REJECTED.
- Disposition reason: deferred. It is outside the scope of response-01, which answers audit findings and adds no new experiment. Resume when two conditions hold: (U)'s rule class is fixed, including whether parent revision is admitted; and a harness for the frozen benchmarks with a recorded well-conditioned reference is available. The kill criterion above must be preregistered before the run.
- Canonical theory / negative-result ID: none. PD-T055 remains the durable OPEN target; its open item already names the experiment.
- Topic / audit / history: E4; added in Claude response-01 to audit-01 E34-F9, 2026-11-01. New provisional ID uses the `claude` agent tag, since Claude created it.

## History

- 2026-11-01 (Claude response-01, Claude Opus 5.5 xhigh): E34-F3. IDEA?drift-codex-14 is converted to an IDEA-only disposition: REJECTED, refuted as an ill-posed formalization; no PD-N; PD-T032 part 2 cited; the withdrawn draft's content is incorporated. Original lines: «- Novelty gate verdict: variant/quantifier correction to the supplied OPEN target.»; «- Canonical theory / negative-result ID: PD-N?drift-codex-14.»; «- Actual test results and committed evidence: analytic proof for every admissible measure, with a row-factor proof for explicit T_3, in PD-N?drift-codex-14.»
- 2026-11-01 (Claude response-01, Claude Opus 5.5 xhigh): E34-F1/F2/F6. IDEA?drift-codex-15 is rescoped to the general fixed-degree lemma, credits PD-T055's heuristic, and has a new novelty verdict and updated check provenance. Original lines: «## IDEA?drift-codex-15 — Prior-vector subtraction repairs a missing J-product under adverse sources»; «Aliases: information-never-formed local obstruction; fixed-degree quotient invariant.»; «Prior records give recursions and tested failures, not this all-coefficient finite quotient calculation.»; «a joint-span identity independent of projection coefficients gives a genuine every-rule statement within this fixed-degree class.»; «- Novelty gate verdict: variant with precise rule-class distinction.»; «its durable command/output/hash record awaits parent integration.»
- 2026-11-01 (Claude response-01, Claude Opus 5.5 xhigh): IDEA?drift-codex-16 now cites PD-T055's heuristic and points to the new IDEA?drift-claude-17 (E34-F9). IDEA?drift-codex-10 now records the E34-F5 staircase note, the E34-F6 check provenance and the E34-F8 OPEN home. Original lines: «- Actual test results and committed evidence: the fixed-degree invariant is proved in -15; it does not survive arbitrary parent revision by the argument given. No multi-degree lower bound obtained.»; «Parent owns the check record and audit.»; «- Topic / audit / history: E3; analytic development 2026-11-01; Claude audit pending.»
