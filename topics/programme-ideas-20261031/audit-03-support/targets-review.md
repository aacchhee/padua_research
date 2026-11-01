# Supplementary focused review — revised targets and finite gauge

- Candidate and rules SHA supplied by the orchestrator: `0ef90edc5b4d5639474cca7fa8d6d688e684e505` on `claude/programme-ideas-20261031`.
- Role: independent supplementary mathematical reviewer; root alone controls Git and the final audit decision.
- Requested allocation: Codex `gpt-6-astra`, high. Resolved runtime model/effort metadata is not independently exposed; no stronger verification is claimed.
- Rules read: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`. Date: 2026-11-01.
- Scope: response-02 dispositions for audit-02 B3 and B4.3–B4.7; related changed target wording, with accepted prior claims taken as the baseline. No new mechanism, novelty claim, proof campaign, or status upgrade.

## Recommendation

**ACCEPTED within this focused correction scope, with nonblocking proof-preparation notes below.** The substantive audit-02 corrections are present. No newly discovered substantive blocker to the already accepted mathematical records occurs in this scope. The OPEN targets remain OPEN. B3 still needs a small boundary-domain correction before it is used literally as a proof task; its constant/exponent quantifiers also deserve one explicit sentence. These are formulation issues, not evidence of an obstruction inside the computed-section class. The finite-gauge paragraph has the right dimension and effective-action conclusion on its cyclic class, although its justification can be made more precise.

## Remaining precision findings

### T1 — B3 must exclude zero boundary gap

Locations: `OPEN_TARGETS.md:66`, `:69`, `:71`; response summary `response-02.md:14`.

The Weyl consequence at line 66 requires `g(H,Q)>0`. With `g=0`, the radius is zero and a reference pair, if present, is H itself with a marginal eigenvalue on the boundary; the asserted absence of boundary eigenvalues then fails. The condition `g >= C delta^alpha` at line 69 does not exclude this case when `delta=0`. The inherited N01 commuting-count identity explicitly assumes boundary avoidance, so this is also a missing hypothesis for the requested equality, not merely an unnecessary strictness preference.

Add `g(H,Q)>0` independently of the commutator inequality (and write `0<C(n,p)<infinity`). Alternatively separate the exactly commuting case with the same boundary-avoidance condition. For the exponent-obstruction family at line 71, state `0<delta(H^(m))->0`; otherwise an exact-commuting, zero-gap boundary degeneracy is formally permitted and would not test the intended positive-commutator scale.

Classification: minor, local formulation correction; it prevents calling the literal current B3 fully boundary-safe. This review does not construct a new computed-section counterexample or infer any positive-gap theorem to be false.

### T2 — B3's intended exponent quantifier should be explicit

Locations: `OPEN_TARGETS.md:61`, `:69`, `:71`, `:73`.

The metric, radius `g/2`, marginal spectra used for g, reference class and reference-neighbourhood non-emptiness obligation are now explicit. `C=C(n,p)` is explicitly uniform in M, nodes and weights, which resolves the central audit-02 ambiguity. Since the setting fixes n, the natural reading is a per-degree task with a prescribed pivot lower bound. The text should say whether alpha may depend on n and/or p, or whether one exponent must work for all degrees and pivot bounds. The negative family must retain one fixed n and p; with positive delta tending to zero and `g>=c sqrt(delta)`, it defeats every alpha>1/2 and every finite C for those fixed parameters, since `g/delta^alpha -> infinity`.

The closing phrase “at distance approximately c sqrt(delta)” should use “boundary gap” if g is intended; pair distance d is a different defined quantity. Also, the stated negative form is a sufficient way to disprove S, not an exhaustive logical negation of its exponent-existence assertion. No theorem or new mechanism is requested to make these editorial clarifications.

Classification: nonblocking precision notes for a future proof attempt; no hidden measure-dependent constant remains in the displayed C.

### T3 — finite stabiliser versus effective group

Locations: `theory/programme-ideas-claude-01-finite-favard-pattern-pairs.md:56`; `response-02.md:17`.

A finite stabiliser by itself need not be normal or independent of the orbit, so “finite, therefore G/Z is an effective group acting freely” is not a valid general implication. Here the accepted cyclicity supplies exactly the missing short justification: a block-orthogonal U preserves the one-dimensional degree-zero block, so U e_1 = epsilon e_1 with epsilon in {+1,-1}. If U stabilises both matrices it commutes with every polynomial in them. Cyclicity of e_1 then gives U=epsilon I. Thus Z is exactly {+I,-I}, central and common to the class, and G/{+I,-I} really does act freely. Its dimension equals dim G.

Classification: nonblocking explanatory precision. The revised local-orbit statement and dimension are accepted on the stated nondegenerate cyclic class; no substantive theorem is reopened or downgraded. Adding the two-sentence cyclicity justification would make the new quotient language self-contained.

## Corrections accepted within the focused scope

| Audit item | Current location | Assessment |
|---|---|---|
| B3 principal formulation | `OPEN_TARGETS.md:61–73` | Computed/reference classes, norm metric, radius, marginal gap, pivot bound, uniformity and non-emptiness obligation now stated. Accept the substantive repair, subject to T1 and interpretive T2. N01 is not used to reject the narrower class. |
| B4.4 argmax coverage | `OPEN_TARGETS.md:49–51` | Local bounds cover the interiors of corner and midpoint neighbourhoods, with equality restricted as required; the complement and remaining finite degrees are covered. The alternative complete-coverage clause is adequate. No proof of the bounds is asserted. |
| B4.5 corner notation and leading term | `OPEN_TARGETS.md:15`, `:37` | Continuous extension of U is correct for positive integer m. The global KL result yields only the stated corner upper bound; the missing lower bound is explicitly an obligation. No new source claim is certified here. |
| B4.6 finite rational-space hypotheses | `OPEN_TARGETS.md:41–45` | Nonzero node denominators, injective evaluation through t+1, full dimensions and the finite M-dependent degree range are explicit. Pole classes are named and linked; general position is an algebraic exceptional-set obligation. This is adequate as an OPEN target template. A proof must choose the class and specify its real/complex parameter coordinates and exceptional set; listing this obligation does not prove the identity. |
| B4.7 algebraic genericity route | `OPEN_TARGETS.md:21–23` | The new route properly replaces the disconnected-domain real-analytic argument. Given the written similarity convention, conjugating E to F yields the displayed weighted symmetry equation. Diagonal conjugation preserves the pattern, and monic Gram–Schmidt coefficients and squared norms are rational on the positive full-rank data domain. Clearing denominators gives a polynomial rank condition; a nonzero polynomial cannot vanish on an open component of the labelled node/positive-weight domain. The explicit instruction to check the reduction and produce witnesses remains a proof obligation. No exact witness or genericity theorem is claimed by this response. |

For B5, the proof should fix the row/column convention for the monic recurrence matrix and eliminate one normalised weight coordinate before calling the polynomial nonzero on parameter space. These are routine details of the proposed argument, not defects in an asserted completed proof. The three obvious commuting matrices must also be checked to be linearly independent (unisolvent data excludes an affine relation), as the proposed route already requires the inclusion/pattern check.

## Evidence and limits

Read the full 496-line `state/IDEAS.md`, including its obstruction and disposition tables; read audit-02, response-02, OPEN_TARGETS, the complete T01 and relevant N01/N02/N04 records, and the named pole-class definitions. Selected canonical candidate passages were consulted for context. This is a focused correction review, not a new novelty gate, literature-priority assessment, or re-audit of unchanged numerical evidence. No claim of exhaustive novelty is made.

Actual execution: local `cat`, `sed`, `nl`, `rg`, `wc`, and `sha256sum` document inspections; the managed-environment status check. No mathematical scripts, long numerical sweeps, independent numerical reruns, Git mutations, developer edits, or audit-record edits were performed. The only assigned artifact written is this report.

Input SHA-256 values from the inspected working-tree bytes:

| File | SHA-256 |
|---|---|
| `response-02.md` | `7da78e0fc01e408edcfcb2b2bf9cf4ba89af4efb0064fa86570da5306322a473` |
| `OPEN_TARGETS.md` | `7592309df263e136abbb6cf8491e059d15ac5f9364359520cda9cdcd5eecab79` |
| `theory/programme-ideas-claude-01-finite-favard-pattern-pairs.md` | `7d69a3b93c90557a206734c882eed86cc42ab80d1f93430a6d3238b3e3f43479` |

The orchestrator should distinguish acceptance of the retained results and statuses from the minor B3 formulation follow-up; this report does not mark the entire campaign or PR ready.
