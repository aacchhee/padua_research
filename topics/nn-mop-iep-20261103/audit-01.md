# Audit 01 — nearest-neighbour MOP IEP (IDEA-117) — independent Claude audit

- Auditor: Claude, `claude-opus-5-5`, effort xhigh (as handoff02 requires: mechanism/novelty audit). Role: independent auditor of Codex development; I did not develop any audited claim.
- Date: 2026-11-05 (UTC).
- Rules read at branch head `6ec5768ef90aeebc918e1a126e2497258e61f507`: AGENTS.md, agents/WORKFLOW.md, agents/claude/CLAUDE_ROLES.md.
- Audited candidate: `ae7e6187e8731b6f83aa444d4d702a0ef779c564` (handoff02 input). `6ec5768` differs only in handoffs/01-work.md (status line) and handoffs/02-audit.md. Base main `440d1079e42c3ef21c40d1cf8870f5b206410c6a` (refetched; unchanged).
- Campaign sources read-only at `d669363c9bce16da2af0f3b7db05a031b911edd5`; not merged.
- **Verdict: findings, stage returns to WORK.** One major finding (F1) concerns how the terminal-divisor result is presented and what it means for C4. Its mathematics is correct. Three minor findings and two coverage notes follow. No proof is wrong; no status upgrade or downgrade is required by me beyond the F1 split question.

## Audited file hashes (SHA-256 at `ae7e618`)

| File | SHA-256 |
| --- | --- |
| gate.md | `9b14ef474ce43282e009369f089a9581ceb44deb86c27833309621e74f7717ce` |
| report.md | `2cc55726b00804f82ab0f57cfcc19fca21d7ff14a3b48069ee95922ab89cfc2a` |
| candidates.md | `cfc99fa052f15ca48bd2d8e134ff5f7eece8aea8ef4f5011bb5d27ccaee01564` |
| literature.md | `d692c898dede23b77923d54fe755a26011eeea0eb559818a84f9471ba5b64e24` |
| exact-runs.md | `3bf1632c3fbfafa00cf345157e9c90e201ccc92eab253bea3311ac796a4d0e72` |
| independent-check.md | `7b4cd33267e2bc12532ba8f0aae8c19e348e626ba90060070bee74dc423256e8` |
| theory/finite-moment-formulation.md | `55ef34e0fc3ae426e9828ca6d129dd2eadb8563dd98e775f1cab9f1bfdfa3413` (= Astra-reviewed) |
| theory/terminal-division-obstruction.md | `8551df5752505a5bf4b933b2b4bc59bf76a07224cf27120275f95a45552b17e2` (= Astra-reviewed) |
| theory/finite-checks.md | `15ba9f7dcfdb3da19afcfb528fedaa13bf16ac91d8547bfbf89bdbeb8c0a364a` |
| theory/fixed-site-dictionary-failure.md | `5635175cb6a425a1dfc12c047c5d76f3ec7b579b54d7de21d8926ff94a7fc988` |
| code/exact_nn_mop.py | `8e420d166f82b3ec7730357a31dcbd684bf8694e3499f5803556a097e745cc7c` |
| code/independent_nn_mop.py | `69b373434958fd3e8f9df4e579e393d3fb4c209f76c15133cd04bbf04b0a3a5b` |
| ALLOCATIONS.md / allocation-scan.json | `59c143b9…e768431` / `345ac07f…a8978836` |
| results/nn-mop-iep-20261103.md | `2bc38dbf4f416f0ab25008b6e46d4dce65acc76bb3ea835466cef5f8d4d5eeb6` |

## Read coverage

- Complete `state/IDEAS.md` (889 lines, all sections), including every obstruction and disposition table: the U1 obstruction table, OBST?bivariate-lanczos-claude-01–15, MZ, lattice, programme-ideas, MZ-2D, drift, PR12 and PR17 tables. Full entries IDEA-031, 090, 111, 117 (seed 041 and final row), 159, 172, 191, 193, 197, and the programme-ideas mechanism warnings.
- PD-T057 theory file in full.
- All topic files listed above, handoffs 01 and 02.
- At `d669363`: the FHV campaign record and P4 memo question B (bullet 38 and the future-work table).
- literature/INDEX.md was not re-read row by row. I accept the gate's statement of which rows it read; I make no new attribution claim of my own.
- **Primary sources: not reached.** arxiv.org and lirias.kuleuven.be are denied by this session's network policy; one WebSearch confirmed only the FHV bibliographic data. So no FHV, Van Assche, Kozhan–Vaktnäs, ADY or ADV locator was verified by me against the primary text (see N1).

## Independent executions (auditor's own runs)

Environment: Linux container, Python 3.13.18. SymPy 1.14.0 (mpmath 1.3.0) was installed into a scratch venv for the second checker. Raw outputs are local and regenerable (scratchpad), not committed.

| # | Command (repo root) | Exit | Output bytes / SHA-256 | Observed |
| --- | --- | --- | --- | --- |
| R1 | `python3 topics/nn-mop-iep-20261103/code/exact_nn_mop.py > $SP/nn-mop-claude-exact.json` | 0 | 12,801 / `63c3e718…668d0` | `all_passed` true; 14 cases; totals exactly as in exact-runs.md (238/84 normality, 1,316 orthogonality, 476 recurrences, 238 successor differences, 224 transfer actions, 70 flatness, 112 fixed-site noncommuting, 168 d≠0, 70 terminal d=0, 84 terminal products, 476 support zeros, 168 terminal h=0, 98 singular degree N+1, 14 proportional singular). |
| R2 | `venv/bin/python topics/nn-mop-iep-20261103/code/independent_nn_mop.py > $SP/nn-mop-claude-small.json` | 0 | 2,271 / `163dcf30…db4a` | `all_passed` true. N=1: 3 normal, 2 recurrences. N=4: 15 normal, 20 recurrences, terminal determinants `(10692000, -102600, 7920, -20520, 972000)`, terminal polynomial `x**4 - 2*x**3 - 5*x**2 + 6*x`, L1/L2 at (1,1) and commutator entry (1,2) `-7804807927/151762234`, as in independent-check.md. |
| R3 | `python3 topics/nn-mop-iep-20261103/audit-01/claude_layer_recursion_check.py > $SP/claude-layer.json` | 0 | 6,367 / `37c86d1d…f25e` | Auditor-written checker (code SHA-256 `13d59af82304a712d792c6e2f96c76f42ec732575dcfa3452a92295071c011b3`); see F1. |

Output identity: R1 and R2 differ from the recorded developer hashes `92e41630…f6` and `97905428…e430` only in the embedded `"python"` field. After replacing `3.13.18` by `3.12.14`, my outputs hash to **exactly** `92e41630aa81a6e9071c2a1a325b353a968f6b15104142206e79ccbb8e2f44f6` and `9790542877736255d0b56d3b2285ff0d5334a4f3504587ffc0be6a96dbaee430`. These are separate executions, not copies. The agreement is finite exact agreement (MEASURED), not a proof.

R3 is my own code; it imports nothing from the topic. It has a ground-truth solver from node-valued orthogonality conditions, NN coefficients by polynomial coefficient matching, and exact Stieltjes marginal recurrences. It then rebuilds all NN coefficients from marginal data alone by the layer recursion of F1. Inputs: the 14 developer cases, the Astra N=4 case, and 9 seeded rational cases N=2..10 (`random.Random(20261105)`, input hashes in the JSON). All 24 cases pass:

- 467 coefficient sites reproduced exactly;
- 256 axis/marginal identities;
- 128 terminal sites with d=0 (all of them);
- 809 divisions, none by zero, with **maximum divisor degree N−2 in every case**;
- 255 of 255 sites with b_{ν+e1,2} ≠ b_{ν,2} (used in F2).

## Reconstruction of the claims

### PD-T?nn-mop-iep-codex-01 (finite formulation) — PROVED accepted

I re-derived every step independently:
- **Square system.** The monic orthogonality conditions are exactly the square system. Uniqueness of the monic solution is equivalent to det M_ν ≠ 0.
- **Denominators.** h_{ν,s} ≠ 0 when ν+e_s is normal: otherwise the padded coefficient vector of P_ν is a null vector of M_{ν+e_s}.
- **Residual.** R = xP_ν − P_{ν+e_j} − b P_ν has degree ≤ k−1 and satisfies the (n−1, m−1) conditions. Those constraints are independent by normality of (n−1, m−1). P_{ν−e1} and P_{ν−e2} are distinct monic polynomials of degree k−1; equality would give a nonzero kernel vector of M_ν. The pairing L_s(x^{ν_s−1}·) gives a_{ν,s} = h_{ν,s}/h_{ν−e_s,s} independently of j.
- **Boundary cases.** The axis and ν=0 cases are correct.
- **b formula and positivity counterexample.** The b formula follows from subleading coefficients. The proportional-weight counterexample is correct.
- **Common coefficients.** R3 confirms by a different method that both directions share the same lower coefficients (asserted at all 467 sites).
- **Classification.** No novelty is claimed. "Standard defining linear algebra" is an honest classification.

### PD-N?nn-mop-iep-codex-01 (terminal divisor) — mathematics correct; scope and significance need F1

- F annihilates both functionals, so normality at degree N forces P_ν = F. Then the two successors of a degree-(N−1) index coincide and b_{ν,1} = b_{ν,2}. Correct.
- Interior part: d_ν = 0 makes the successors equal; their common polynomial lies in the kernel of M_{ν+e1+e2}. Correct. The "successor-difference identity" hypothesis is in fact automatic from normality of ν, ν+e1, ν+e2: P_{ν+e1} − P_{ν+e2} has degree ≤ |ν| and satisfies the conditions at ν. So the hypothesis is harmless but redundant.
- The scope sentences correctly disclaim any refutation of FHV under its own hypotheses. However, the rule the record refutes is not used by the reconstruction it is attached to (F1).

### PD-T?nn-mop-iep-codex-02 (finite checks) — MEASURED accepted

- Counts reproduced (R1, R2).
- Domain arithmetic checked:
  - interior non-axis sites with n+m ≤ N−1 number 2·Σ(N−2)(N−1)/2 = 112;
  - flatness squares with n+m ≤ N−2 number 2·Σ(N−3)(N−2)/2 = 70.
- Transfer matrices re-derived: L1 uses P_{ν+e1−e2} = P_ν + d_{ν−e2}P_{ν−e2}; L2 uses P_{ν−e1+e2} = P_ν − d_{ν−e1}P_{ν−e1}. Both match the code.

### PD-N?nn-mop-iep-codex-02 (fixed-site dictionary) — MEASURED and REJECTED: refuted accepted, wording finding F2

A single exact rational witness already establishes the negation of the literal identification. Keeping MEASURED is conservative and allowed.

### Candidates

All four prescribed candidates are retained with predecessors, separation criteria and kill tests. C1 equivalent, C2 refuted (literal), C3 deferred and C4 known are reasonable dispositions. C4's text needs F1 corrections.

## Findings

### F1 — MAJOR — the terminal zero divisor is never reached by marginal-data reconstruction on the finite domain; the C4 "boundary qualification" is overstated and the positive consequence is missing

**Locations:**
- gate.md, "Correcting C4 and the finite boundary": "Their division hypotheses cannot be extended unchanged through a shared finite-support terminal layer".
- report.md, "Corrected exact baseline and boundary" para 2.
- candidates.md, C4 "Applicable obstruction" and "Disposition".
- terminal-division-obstruction.md, Statement para 2 and "Negative-result scope" ("naive extension of FHV nonzero-divisor propagation through the last shared-support layer (C4)").
- exact-runs.md: "formulas dividing by d cannot be applied naively at that final layer".
- results bullet 2 and gate Decision ("with a finite common-support boundary qualification").

**Mathematics (auditor-derived; written proof sketch below).** Put d_ν = b_{ν,2} − b_{ν,1} and assume all indices with |ν| ≤ N are normal. For |ν| ≤ N−2, expand x(P_{ν+e1} − P_{ν+e2}) = d_ν xP_ν. Use:
- direction-2 recurrence at ν+e1;
- direction-1 recurrence at ν+e2;
- P_{ν+e1−e2} = P_ν + d_{ν−e2}P_{ν−e2};
- P_{ν−e1+e2} = P_ν − d_{ν−e1}P_{ν−e1};
- P_{ν+e2} = P_{ν+e1} − d_νP_ν.

Then compare coefficients in the independent family {P_{ν+e1}, P_ν, P_{ν−e1}, P_{ν−e2}}, with absent axis terms dropped. This requires P_{ν+e1+e2}, hence |ν| ≤ N−2. It gives:

- (A) a_{ν+e1,2} d_{ν−e2} = d_ν a_{ν,2} and a_{ν+e2,1} d_{ν−e1} = d_ν a_{ν,1};
- (B1) b_{ν+e1,2} − b_{ν+e2,1} = d_ν;
- (B2) d_ν b_{ν+e2,1} = d_ν b_{ν,1} − (a_{ν+e1,1} − a_{ν+e2,2} + a_{ν+e1,2} − a_{ν+e2,1}).

Starting from the marginal Jacobi data (the axis NN coefficients equal the marginal three-term coefficients), the coefficients of layer s+1 are computed as follows:
- **a's:** by (A), dividing by d at layer s−1;
- **b's:** by (B2) and then (B1), dividing by d at layer s;
- **axis entries:** taken from the marginal data.

The finite coefficient domain ends at layer N−1, so only divisors with |ν| ≤ N−2 are ever used. These are nonzero by the **interior part of PD-N?nn-mop-iep-codex-01 itself**: the opposite corner ν+e1+e2 has degree ≤ N and is normal. The terminal zero d at |ν| = N−1 could only enter a step producing degree-N coefficients. Those do not exist, because there is no normal degree-(N+1) successor.

R3 confirms this exactly on 24 inputs, N=2..10. All 467 coefficients are reproduced from marginal data, and the maximum divisor degree is N−2 in every case.

So, under full normality through degree N, the marginal-data reconstruction (C4's "simpler exact comparator") needs **no** boundary modification on the common-support triangle. Terminal b_{ν,1} = b_{ν,2} at |ν| = N−1 then reads naturally as a final boundary condition that common-support coefficient arrays must satisfy, i.e. a constraint for a Favard/inverse characterisation. It is not an obstruction.

**Caveat.** I could not read FHV §3.1/§3.3 (network policy). (A), (B1) and (B2) are my own derivation and match the known r=2 compatibility pattern. If FHV's Theorem 3.3 recursion is organised so that some coefficient on |ν| ≤ N−1 requires d at |ν| = N−1, the developer must quote it with its page, and this finding reduces to a wording issue.

**Required response:**
1. Quote FHV Thm 3.3 / (3.11)–(3.13), pp. 20–21, and Van Assche 2011 Thm 3.1, from the primary text. State which layer's divisors are used to produce each layer, and either confirm or refute the auditor's divisor-degree statement.
2. If confirmed:
   - rescope PD-N?…-01 explicitly to "propagation to degree-N coefficients". That propagation lies outside the NN data, which ends at |ν| = N−1.
   - decide, with reasons, whether that scoped negative still describes a failed mechanism anyone would use (WORKFLOW L5), or whether the record should become a supporting lemma inside a positive record. Do not delete the history: preserve the original wording in History.
   - correct gate/report/candidates/exact-runs/results so that C4 on the finite triangle is described as complete under full normality through degree N.
3. Under split-by-default, the interior d ≠ 0 assertion is substantive once a positive result depends on it. Consider a separate PROVED record, e.g. "marginal-data NN reconstruction is well defined on the normal common-support triangle". Give it a written proof, a link to the Kozhan–Vaktnäs Thm 3.6 comparison, and the terminal b-equality as a final boundary condition. Classification is the developer's proposal, subject to re-audit. The auditor's R3 checker may be cited as MEASURED supporting evidence only.

### F2 — MINOR — "shifted versus fixed-site" is not what separates NN flatness from PD-T057; the decisive mismatch is spectral

**Locations:**
- report.md "Precise objects" para 2;
- PD-N?…-02 aliases/statement ("fixed-site versus shifted products");
- candidates.md C2 "Separation / kill criterion".
- Also handoff02 item 4's framing.

**Problem.** PD-T057's interior commutativity is, by its own alias, Xu's block-Jacobi commuting conditions (Xu 1994 (2.5)–(2.7)). Written blockwise, it relates blocks at adjacent degree levels (k, k+1), so it is also a "shifted" product identity. Hence a fixed-site commutator test kills only a literal identification that no source proposes. Keep the result, but do not present it as the discriminating mismatch.

The gate's dictionary section already contains the real mismatch: one variable x versus two coordinates, and a redundant index triangle versus a graded basis. It can be sharpened as follows. The natural lattice operators are the two NN difference operators
  H_j f(ν) = f(ν+e_j) + b_{ν,j}f(ν) + a_{ν,1}f(ν−e1) + a_{ν,2}f(ν−e2).
They have the MOP vector as a joint eigenfunction with the **same** eigenvalue x in both, so H_1 − H_2 annihilates consistent states. By contrast, (H_x, H_y) has joint spectrum {(x_l, y_l)} with two independent eigenvalues; compare the programme-ideas warning "joint spectrum = spec(H_x) plus a pairing".

On full lattice functions H_1 and H_2 do not commute either. The coefficient of f(ν+e1) in [H_1, H_2]f(ν) is b_{ν+e1,2} − b_{ν,2}. That coefficient is nonzero at all 255 tested sites with |ν| ≤ N−2 (R3); this is a finite count, not a theorem.

**Required:** reword report, PD-N?…-02 and C2 accordingly. Statuses are unchanged. Optionally add the H_1/H_2 encoding to the list of encodings tested or not excluded.

### F3 — MINOR — the stopping rationale is acceptable for new-method development, but the C4-only floating-point baseline is executable without any C3 and is not listed as a run needed

**Locations:** LOG "Runs needed" ("No expensive numerical run is pending for a method that has not been defined"); report "Evidence and stopping decision"; gate Decision.

**Assessment.** Handoff01's stop clause allows stopping when "the question [is] answered in the literature, or … C4 subsumes the proposal". Neither condition is met literally:
- the commuting-pair half is answered negatively (literal dictionary fails) by a sound mismatch;
- the updating half reduces to known exact algebra plus the existing step-line updater;
- C4's floating-point stability is unknown, and the developer says so honestly.

So deferring C3 is justified: no distinct coupled updater with stated invariants has been specified, and I agree one cannot be measured before it is defined. But handoff01 Step 3's Kravchuk/Hahn digits-lost measurement can be run for C4 alone, e.g. a floating-point marginal Lanczos/Stieltjes followed by the (A)/(B) layer recursion against exact or high-precision ground truth. Divisions by d_ν and d_{ν−e_j} are a plausible cancellation point. That run is the cheapest decisive datum for whether any C3 is worth defining.

**Required:** record it under Runs needed with purpose, inputs, metric and an exact planned command. Alternatively, run it if the developer judges it within the time box, labelled MEASURED. Correct the LOG sentence. AC decides whether the topic may close without it; the auditor does not regard it as blocking audit acceptance once recorded.

### F4 — MINOR (provenance) — output hashes are environment-dependent

Both checkers embed `platform.python_version()` in the JSON, so the recorded output SHA-256 values reproduce only on Python 3.12.14. Record in exact-runs.md and independent-check.md that output identity across environments requires normalising the `python` (and, for R2, `sympy`) fields. I verified that normalisation reproduces both recorded hashes exactly. No code change is required.

### N1 — coverage note (auditor limitation, no developer action except F1.1)

All LITERATURE statements remain developer-reported, not auditor-verified, for these sources:
- FHV §§2–3 and Thm 3.3;
- Van Assche 2011 Thm 3.1;
- ADY 2020 §1.1 exclusion of finite support;
- ADV 2016 Prop. 4.5;
- ADV 2015 J. Phys. A;
- Kozhan–Vaktnäs Def. 2.8, Thm 3.6 and Thm 3.19;
- the Toda paper.

The reason is that arxiv.org and lirias.kuleuven.be are denied by this session's network policy. The Kozhan–Vaktnäs inapplicability argument is internally sound as stated: mixed rank ≤ N excludes normality at (N, N) if the rectangle is the support-size rectangle. Its premise (what N_j is in Def. 2.8) is the developer's reading. A later audit session with arXiv access, or AC's local copies, should spot-check the FHV Thm 3.3 recursion and KV Def. 2.8 locators.

### N2 — note — shortlist neighbour

IDEA-197 (structure theory of commuting generalized-Hessenberg pairs; PD-T095, PD-N042, PD-T102) is the registry's nearest "commuting structured pair" entry. The MOP step-line operator is a banded Hessenberg matrix. The gate does not list IDEA-197. It does not change C2: IDEA-197 concerns two commuting bivariate sections, not one Hessenberg operator with two weights. A one-line mention in gate.md's closest-entries table would complete the shortlist.

## Disposition table (auditor)

| Item | Developer claim | Audit disposition |
| --- | --- | --- |
| PD-T?…-01 finite formulation | PROVED, no novelty | **Accepted** as PROVED. |
| PD-N?…-01 terminal divisor | PROVED scoped negative; C4 sub-mechanism REJECTED: failed | **Mathematics accepted.** Scope, significance and possible split returned under F1. |
| PD-T?…-02 finite checks | MEASURED | **Accepted**; independently rerun (R1, R2). |
| PD-N?…-02 fixed-site dictionary | MEASURED; C2 literal REJECTED: refuted | **Accepted**; wording per F2. |
| C1 | equivalent / background | Accepted. |
| C2 | refuted (literal) | Accepted; F2 wording. |
| C3 | deferred | Accepted as deferred; F3 Runs needed. |
| C4 | known after correction; naive terminal division failed | Returned under F1. The FHV shift-family and step-line correction (two fixed lines do not fill the lattice; second-measure ambiguity μ2 → μ2 + cμ1 on the step-line) is accepted by my own check: step-line conditions with n ≥ m are invariant under that change. |
| Gate stop | stop new-method development; numerical question OPEN | Accepted with F3. |
| Literature / attribution | bounded, no absence claim | Accepted as developer-reported (N1); no overclaim found in wording. |
| Reservation | T286–293, N100–103, IDEA376–383, LIT562–573, first pushed `a0abe8b` | Provenance confirmed: the ranges are in `a0abe8b:topics/nn-mop-iep-20261103/ALLOCATIONS.md`. The later branches `codex/padua-mz-2d-frontier-20261105` and `codex/padua-lanczos-frontier-20261105` reserve above T293/N103/IDEA383/LIT573 and cite this range, so there is no collision. Not a readiness scan. |
| Shared registries / final IDs | untouched | Confirmed by `git diff --stat 440d107..ae7e618` (topic files and its results file only). |
| Evidence sizes | small receipts; raw local | Confirmed; largest committed topic file 16.5 KB (literature.md, prose). |

## Remaining uncertainty

- The FHV recursion's exact organisation (N1/F1 caveat).
- Whether a coupled NN updater can beat repeated C4: OPEN, unmeasured.
- Floating-point behaviour of C4: unmeasured (F3).
- Nonnormal or partially normal regions: outside every claim here.

The audit concerns only the stated scope. It does not approve readiness or merge.
