# Supplementary audit-02: obstruction response and registered claims

Rules/candidate SHA: `cadb35066160e466cb1704b9791ad6f374446422`.
Historical audited candidate: `614709d4a60fb0c2593b05764e8d5aceda1be381`.
Main refresh recorded by the root: `9739a0c`.
Auditor: independent Codex subagent `/root/audit_obstructions`, inherited
user-requested `gpt-6-astra xhigh`; resolved runtime model/effort metadata is
not separately exposed. Date: 2026-11-01.

## Scope

Read current AGENTS, WORKFLOW and Codex rules; the full current 496-line
`state/IDEAS.md`, including the lattice and programme additions and every
obstruction/disposition table; response-01 and addendum; A3–A5 corrections in
the M1/M2/gen2-3 adversarial and candidate records; PD-T?programme-ideas-claude-01
and -03; PD-N?programme-ideas-claude-01, -04 and -05; and the corresponding
`OPEN_TARGETS.md` entries B3/B5/B6/B7. Relevant implementations and committed
outputs were inspected and actually rerun. This supplies mathematical and
evidence-scope review, not fresh historical novelty clearance. No new source
acquisition or fulltext verification was performed, and no universal novelty
claim is accepted here.

Only new `audit-02-support/obstructions-*` files were written. No developer
file, old audit, or Git state was changed. Root supplies candidate identity;
the source/rule/code SHA-256 hashes are in `obstructions-check.json`.

## Accepted within the declared scope

- **A3 / finite Favard (PD-T?…-01).** The recursion through nonzero parent
  pivots makes the constant vector cyclic; simultaneous eigenvectors have
  nonzero first components and one-dimensional joint eigenspaces. The
  resulting positive weighted evaluation matrix is orthogonal and
  invertible, establishing unisolvence and the section representation.
  Positive-diagonal QR supplies existence/uniqueness in the converse and
  the normalized spectral parameter count gives 3N−1. The degree-block
  basis gauge supplies the additional binomial dimension on the stated
  nondegenerate class. The pattern-commutant theorem is no longer inferred
  from these statements. See the small finite-gauge terminology note below.
- **A3 / universal commutant refutation (PD-N?…-04).** Exact Padua n=2 is a
  valid positive-pivot commuting pattern pair. The developer's new exact
  checker independently reconstructs 17 variables, rank 11 and commutant
  dimension 6. Random-instance dimension 3 remains MEASURED; genericity is
  correctly left OPEN in B5. The record's refuted disposition applies to
  the former universal claim rather than to finite Favard.
- **A4 / normalized pencils.** The principal current disposition now
  distinguishes unrestricted GL gauges from the normalized pencil family,
  leaves the latter staircase question OPEN in B6, records the Padua
  threshold as not fired, and describes abandonment as an investment
  decision. The remaining stale sentence is listed below.
- **A5 / product inertia (PD-N?…-01).** The commuting-case sign count is
  correct. For the explicit 2x2 rotated family, both box factors are
  positive definite and the displayed determinant is negative for
  `0<e<(8-2sqrt(2))/11`; thus the formula gives 3/2 although all commuting
  pairs with those marginal spectra have their two points in the box.
  The commutator norm is e²/2, the boundary distance is e/10 and e can
  approach zero. This refutes better-than-square-root thresholds for this
  formula on the stated symmetric-pair class. The text now excludes
  positive-pivot computed sections and other count objects, as required.
- **A5 / functional scope.** Word-order dependence is no longer used to
  exclude every specified-lift theorem; the weak universal PD-N is
  withdrawn and B7 remains open. The univariate error comparison is
  restricted to the finite k<=4 measurements. Strict positivity is
  distinguished from squared-component nonnegativity in the main
  corrected disposition text.
- **Compressed commutator (PD-T?…-03).** Inserting I=P+(I-P) and using
  XY=YX gives minus the boundary skew product; multiplication maps each
  degree<n block into K_n, giving top-block support. Hermiticity and
  unitary similarity give the stated norm invariance. Properness of K_n
  is correctly no longer claimed to force nonvanishing.
- **Fourier mechanism (PD-N?…-05).** The measured nonzero instances refute
  the proposed rounding-level commutation mechanism on those instances.
  Its status remains MEASURED, with the separately proved invariance
  dependency explicit. The finite values reproduce; adjust the small
  evidence-scope inaccuracies noted below.

## Remaining actionable points

### R-O1 — P2: remove the remaining unqualified orbit-count conclusion

`ideas/candidates.md:217` still says the orbit count settles the normal-form
question without a search, while `:214` retains "refuted sub-claims" as the
post-Step-4 verdict. These are not marked as superseded text and conflict
with the corrected normalized-family question and abandonment at `:211`
and `:220`–`:221`. Restrict the orbit-count sentence to the unrestricted
GL-gauged class under its generic stabilizer assumption; mark the old
refutation verdict historical or replace it with the final disposition.
This is a remaining A4 record correction, not a request to pursue the pencil
programme.

### R-O2 — P2: quantify "nearby" before treating B3 as a precise proof target

`OPEN_TARGETS.md:57` asks for a count agreeing with every nearby commuting
pattern pair but gives no distance, neighbourhood radius, or dependence of
that radius on delta. It also does not say whether C may depend on n, the
underlying measure or a conditioning bound. Without this information,
different readings can describe different assertions or a vacuous class
with no nearby commuting pattern pair.

Specify, for example, the pair metric
`d_pair=max(||Hx-Hx'||_2,||Hy-Hy'||_2)`, a quantified radius r(delta) or an
extra radius parameter, the exact class of commuting pairs considered,
existence/non-emptiness assumptions if needed, which spectra define the
boundary gap, and which inputs the constants may depend on. Leave the
claim OPEN. This audit does not supply a proposed universal theorem or
counterexample for that restricted class.

## Minor precision notes

- **PD-N?…-05 evidence range.** Its statement at line 10 should name the
  actually executed ranges: n=1,...,6 for M=64, and n=1,...,8 for
  M=128,512. Line 27 reports identity agreement <=8e-15 without the
  conditioning exception. Both the committed output and this rerun have
  generic-4, n=8 residuals reaching 2e-12; PD-T?…-03 already records that
  exception correctly. This changes neither the measured nonzero
  commutator nor the invariant identity.
- **PD-T?…-01 finite gauge.** The dimension argument is correct, but the
  proof at line 56 calls the block-gauge description a principal bundle
  with fibre G=product O(k+1). Global -I acts trivially on a pair, so the
  action of G has a finite central stabilizer. Say "locally modulo a
  finite sign gauge" or use the effective group G/{+I,-I}; the dimension
  sum is unchanged. The proof need not assert a globally free G-action.
- **B5 proof route.** One exact maximal-rank witness plus nonvanishing of
  a suitable algebraic minor gives the intended genericity argument.
  Analyticity alone on a possibly disconnected parameter domain does not
  make one witness dense in every component. When developing B5, clear
  the Gram–Schmidt denominators/sign factors to obtain the nonzero
  polynomial minor, or handle parameter components explicitly. The OPEN
  status and current finite observations are appropriate.

## Actual executions

From `/workspace/programme-integration`:

```sh
python topics/programme-ideas-20261031/audit-02-support/obstructions-check.py > topics/programme-ideas-20261031/audit-02-support/obstructions-check.json
```

The new audit wrapper ran the following, using Python isolated mode and
one BLAS/OpenMP thread, with source hashes, commands, stdout and stderr
preserved in its JSON:

| Script | Observed result |
|---|---|
| `checks/code/response-01/inertia_two_node_family.py` | Symbolic determinant identity true; all five exact rational instances give 3/2; parsed output equals committed developer output exactly |
| `checks/code/response-02/padua_pattern_commutant.py` | det V=-27/2; exact commutation; all pivots positive; no pattern violations; 17 symmetric variables, map rank 11, dimension 6; parsed output equals committed output exactly |
| `checks/code/adv/gen3-1/commutator_sections.py` | All 66 tested rows executed; norms 0.08333 to 0.5; maximum printed boundary-identity entry error 2e-12; Fourier transformation retains the nonzero commutator |
| `checks/code/adv/M2/m2_favard_commutant.py` | Random commutants 3/2/3 and tangent dimensions 29/44/62/83, 39/64/97/139 reproduced |

The wrapper also uses an independently coded dense QR/residual route for
rhodonea-7 at M=64 and n=1,...,4. It obtains commutator norms
0.25, 0.375, 0.08333333333333316 and 0.241454677859011; the residual-boundary
identity agrees within 2.50e-16 and the separately transformed Fourier
matrices agree within 1.95e-16. These are fresh executions, not reused
audit-01 outputs.

All **125** original files under `checks/code/` were compared byte-for-byte
against the preserved candidate-614709d snapshot, excluding runtime
`__pycache__` files. Every original file is unchanged, including the
invariant-producing/checking code and original numerical outputs. New
response-01/02 scripts are additional files. The JSON records every
historical path and SHA-256 used for that check.

Environment: Python 3.12.14; NumPy 2.3.5; SciPy 1.17.0; SymPy 1.14.0;
Linux x86_64. No run failed. The two small exact checks need SymPy as a
trusted computer-algebra dependency; their explicit finite reductions and
the independent executions are documented. Neither a large conditioning
rerun nor generic all-degree commutant proof was performed.

## Disposition

The registered restricted mathematical statements in this scope are
accepted, subject to the minor precision corrections above. A3's
substantive correction is accepted; A4/A5's main scope changes are accepted.
The two remaining record/target issues should receive explicit developer
dispositions before the campaign is called ready. This does not resolve
the root audit's other scopes or authorize registration of final IDs.

Suggested next prompt: `Claude (Opus 5.5 high): Continue claude/programme-ideas-20261031 — resolve the remaining audit-02 record and quantifier findings without upgrading open targets.`
