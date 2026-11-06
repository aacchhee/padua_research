# Audit 02 — focused re-audit of Codex response-01 and full G5 review

- **Auditor:** Claude, Opus 5.5, effort xhigh, as handoff05 requires. Role: independent auditor and topic orchestrator. I developed none of the response's claims or code. I authored audit-01.
- **Date:** 2026-11-06 (UTC).
- **Rules:** AGENTS.md, agents/WORKFLOW.md and agents/claude/CLAUDE_ROLES.md, read at branch head `409e779`. They are unchanged by main `f654e32` (PR #30), which I merged at `8a2b65d`; that merge changes no file of this topic. The proportionate-audit rules of be9a831 apply.
- **Audited response output:** `d6760d7d593ea7e14eb9860f92ef2f3b5e0481d6`. Its diff from the audit-01 handoff head `4e87fc0` is the scope. `409e779` only adds handoff05 and closes handoff04. audit-01.md and audit-01/ are byte-identical at `4e87fc0`, `d6760d7` and `8a2b65d`.
- **Verdict: response-01 ACCEPTED. Stage → PR.**
  - M1–M4 are resolved.
  - The material parts of MINOR 3, 4, 11, 12 and 13 are correct.
  - The other MINOR fixes are confirmed by diff.
  - No BLOCKING or MAJOR finding remains.
  - Eight new MINOR record-hygiene items (R-1 to R-8 below) are to be fixed at PR preparation and confirmed by diff in the readiness check. None changes a claim, status, threshold or result.
  - G5 remains BLOCKED in execution, with an honest record. Access is authorized by AC; the source code is still unreachable from both executors.

## Method and coverage

Three independent Claude Opus subagents audited disjoint scopes:
- **R1** (xhigh): M3, MINOR 12, the evidence manifest and size.
- **R2** (xhigh): MINOR 11, 13, 3 and 4; M1; and whether any accepted PROVED file changed.
- **R3** (high): M2, M4 and MINOR 1, 2, 5–10 and 14–16, plus registry and gate consistency.

I reviewed the G5 record myself and ran my own access attempts. I also ran the three checks handoff05 prescribes.

The subagents changed no Git state. Their scripts are committed under [audit-02/](audit-02/README.md); raw outputs stayed in local scratch storage. There is no novelty content in this round: the five M4 records preserve candidates named in handoff01, and no new mechanism was generated. R3 read the cited IDEA/LIT rows and checked them for existence and relevance, but did not repeat the full `state/IDEAS.md` read from audit-01.

Audit platform: Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, mpmath 1.4.1. The response reference was produced on Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, mpmath 1.3.0.

## Commands run by the orchestrator

| Command (from repository root) | Result |
| --- | --- |
| `python topics/nn-mop-stability-20261105/code/dictionary_probe.py` | exit 0; determinant 46; P11 = (32/23, −75/23, 1); graph tests (0, 0, −30/23) |
| `python topics/nn-mop-stability-20261105/code/conditioning_verify_normality.py` | exit 0, PASS: 61 sizes, 43,676 checks, `code_pins_verified` true; producer `795e1c11…`; 4.8 s |
| `python topics/nn-mop-stability-20261105/code/independent_check_followup_projection.py` | exit 0, PASS against committed reference SHA-256 `37c3c060ad42cad679a78f256d9a5bdf5c129ed338cc8dcda9afbae6a5fef23f` (113,095 bytes); 64 s |
| Same checker, `python -O`, `--reference` pointing to a one-byte-altered copy | exit 1, "committed reference SHA-256 mismatch" in 0.18 s, before reconstruction |

## Findings of audit-01: dispositions

### M1 — resolved

The arithmetic is now exact:
- w1 moments (4,6,14,36) and w2 moments (15,34,90,250);
- equations 4c0+6c1 = −14 and 15c0+34c1 = −90, with determinant 46;
- c = (32/23, −75/23), ⟨P,x⟩ = −30/23 and ⟨P,y⟩ = 0.

R2 recomputed all of this, and the probe output agrees.

### M2 — resolved

All five named records open with the same dated binary64 provenance section (lines 3–14). It names the producer platform, limits determinism to that platform, cites the audit platform's 30.78u Krawtchouk N4 nodeqr case and keeps the 100u conclusions. The "deterministic" lines are qualified, and every unqualified "≤30u" or "below 30u" statement is replaced by "<100u".

R3's token-level numeric diff found exactly one change to a historical value, 30 → 100. No table value, gain or receipt identity was changed, retuned or re-selected.

### M3 — resolved for portable verification

The limitation is disclosed honestly.

**The reference file.** `evidence/projection-reference.json` holds all 12 cases (N4/N8 × Krawtchouk/Hahn × C4/LU/nodeqr). Each case has:
- the complete raw binary64 target as exact hex words;
- the 70-digit rational witness;
- raw and input hashes, metrics, source pins and platform.

**R1's independent exact rebuild** (own Fraction code, no developer imports, polynomial-projection extraction) covers all 12 cases:
- positivity, ordering and unit mass hold;
- all 348 systems are nonsingular;
- 1,104 fields were rebuilt;
- every stored metric (η_d, η_c, √Q and the four per-field corrections) is reproduced with relative difference exactly 0.

R1's exact implicit-derivative stationarity reproduces all six N4 values bitwise. At N8 only Krawtchouk LU was completed (equal to the stored value). I stopped the remaining optional N8 runs because the response does not claim N8 gradients.

**Platform behaviour** (corroboration only, since it re-runs developer code):
- re-running the developer fit on the committed targets reproduces every committed witness hash on the audit platform;
- regenerating the targets reproduces C4, Krawtchouk N4 LU and Hahn LU bitwise, but not nodeqr or Krawtchouk N8 LU.

So committed targets were necessary, and the earlier 30.78u came from a different target.

**Agreement with history.** The new metrics equal both historical tables at their displayed digits, including Krawtchouk N4 nodeqr 29.8852.

**Remaining limitation.** The Nov-5 bytes are lost, and the reference is a new fixed-configuration run; the records state this. The 100-dps agreement and convergence-flag statements remain evidenced only historically (R-7).

### M4 — resolved

candidates-deferred-alternatives.md:14–112 has five provisional records:
- core transformations, biorthogonal Lanczos and multi-path redundancy (handoff01:76–81);
- Vandermonde conditioning and node density (handoff01:58).

Each has closest entries (LIT-347, IDEA-031/087/088/090/117/378/379 and LIT-112/113/365, all existing and relevant), a "deferred, not rejected" disposition, a reason, a resume condition and a line on why A/B were chosen. No D3 work is reopened and no novelty is claimed. Item (d), IDEA-378, stays deferred.

The records repeat boilerplate in places, which is acceptable for unattempted candidates (R3 N1).

### MINOR 11 — resolved

R2 independently reconstructed the localized NN lemma; its argument matches conditioning-normality-certificate.md:61–86 step by step:
- **The NN identity at ν (|ν| ≤ R−1).** Res has degree ≤ s−1 and satisfies the (n−1, m−1) conditions. Its kernel has dimension 2, spanned by independent P_(ν−e1) and P_(ν−e2). The h-ratio gives a, with nonzero denominators.
- **Normality used:** only ν+e_j, ν, ν−e1, ν−e2 and ν−e1−e2.
- **The compatibility square at |η| ≤ R−2:** uses degrees ≤ R.
- **Layers through R−1:** use divisors with corners of degree ≤ R.
- **The degree-k induction** uses normality only through k−1 to produce the d values at degree k−2.
- **Bordering** gives h_(η+e1,2) with sign +1.

Exact tests:
- 19 cases (N=5..8) with a deliberately singular index of degree k and all lower indices normal: every conclusion holds, and the planted index always has d = 0;
- 60 random rational certificates (N=3..7): every passing certificate is fully normal.

The certificate theorem and its use in the finite Hahn theorem are unchanged and noncircular.

### MINOR 12 — resolved

No `assert` remains in either certificate script. The verifier hashes the modules it actually imports and compares each with exactly one pin.

R1's rejection tests on receipt copies all exit 1, with explicit errors and no output, both normally and under `-O`. Altered items:
- the N64 payload;
- the producer pin, including a reversion to the historical `7aa41…`;
- the graph pin;
- a duplicated pin line;
- the N64 count;
- the N4 input.

The 61 table rows, inputs, counts and payload hashes are identical at `4e87fc0` and `d6760d7`. The producer pin equals the new file hash and was updated in the manifest in the same commit; the old pin is disclosed in History.

### MINOR 13 — resolved

backward-local-manifold.md:116–120 now gives the continuity of the spectral left inverse, F(p_j) → y0 ⇒ p_j → p0, before the embedded-image claim. No new global-nearest statement was added.

### MINOR 3 and 4 — material parts correct, three bookkeeping residues (R-2 to R-4)

- **The split C record** (theory/dictionary-copy-obstruction.md) is mathematically identical to the original combined text at `4e87fc0`, with alias and history kept.
- **Dispositions:** G is `REJECTED: refuted` and C is `REJECTED: failed`, both consistent with WORKFLOW. The proximity and dyadic statements are unchanged, and both now say `refuted`.
- **The new OPEN parents** (conditioning-growth-target.md and stable-solver-target.md) are correctly OPEN, not PARTIAL.

### Other MINOR fixes (1, 2, 5–10, 14–16) — confirmed by diff

This covers:
- the completed-check wording;
- Fischer and PD-N118 predecessors;
- LIT-567 and LIT-568 reuse;
- the be9a831 note in proposed-record-changes.md;
- the D1/D2 gate consolidation;
- the canonical AC-decision link;
- N16 gain scoping, the Toda range and Toda start;
- both-family infinite componentwise output, checked exactly at N4;
- the G2 margin 100.6929 ≈ 2.003 digits, with no trigger under ε = 2⁻⁵²;
- unread on-path fields, checked against path_recovery.py:19–27.

For MINOR 9 the decision record is correct, but the consolidation dropped chronology (R-1).

### Accepted PROVED records

R2 confirmed that no statement or proof step changed in:
- conditioning-lower-krawtchouk.md and conditioning-krawtchouk-bound.md;
- the integrable records.

The integrable records only relabel LIT-D4-01/02 to LIT-567/568. Two audit-requested changes are correct:
- the remark in conditioning-local.md:47–50 (see R-6);
- the Toda narrowing to the moment-defined array on its connected normality interval.

### Evidence manifest and size

R1 recomputed all 55 rows (inventory plus 54 files) at `d6760d7`: 0 mismatches, with coverage exactly equal to the manifest's glob set. 5 rows were added, 27 changed and none removed.

The committed topic is 956,180 bytes at `8a2b65d`, plus this audit's scripts. Per AC's instruction, no storage action is taken below 10 MB.

## G5 — full review

**The developer record.** response-01/g5-access.md records Codex's executor at 08:25 UTC:
- the enforced policy lists no extra hosts;
- GitLab Leuven, the SIAM ZIP and arXiv all got proxy CONNECT 403, while a Debian control request got 200;
- bounded web-connector reconnaissance found the GitLab project page title only, and the publisher ZIP was refused as an unsupported content type;
- no mirror was found, and no bypass was attempted.

It claims no source, run or reproduction, and keeps G5 BLOCKED with a concrete next requirement. It correctly says that Claude's observations from another environment cannot describe its own runtime. I find the record factual and the BLOCKED outcome honest.

**The auditor's own attempts,** 2026-11-06 09:19 UTC, in Claude's personal environment `padua_research`. That environment allows gitlab.kuleuven.be, epubs.siam.org and arxiv.org.
- **gitlab.kuleuven.be:**
  - The proxy tunnel opens, and only the 39-byte "Connection Established" reply arrives.
  - The upstream then resets the TLS handshake after about 10 s. curl and git report a connection reset; `openssl s_client` through the proxy gives `write:errno=104`.
  - The proxy status shows `ws_closed_mid_exchange`.
  - No source was retrieved. The reset looks upstream of the proxy policy, but the cause is undetermined.
- **epubs.siam.org supplement ZIP:** HTTP/2 403 with `cf-mitigated: challenge`, a site-side bot protection. It was not bypassed.
- **arxiv.org:** reachable. The source bundle `https://arxiv.org/src/2506.19796v2` (88,273-byte gzip, SHA-256 `f736e8f03b536382141c2c98620c3cd408e0ff2c772ce58f47030e944864d461`) contains 24 files: LaTeX plus `Experiments/*.dat`. It contains **no code**; main.tex:208 and :1222 point to the GitLab project for the MATLAB code.
  - It does contain the paper's experiment-1 data: `data_experiment1_{kravchuk,hahn}.dat`, N = 5..30, with forward errors e_N for IEP_CORE, IEP_KRYL and IEP_KRYLREORTH, biorthogonality loss, and the paper's "conditioning error".
  - These are the reported accuracy levels that G5's criterion (handoff01:130) refers to. The paper uses Kravchuk p1 = 0.4, p2 = 0.5 (main.tex:1231).
  - Nothing third-party is committed; only the hashes above are recorded here.
- **deb.debian.org:** CONNECT 403 in this environment, whereas Codex's executor reached it.

**Assessment.** G5 stays **BLOCKED in execution**: the code needed to reproduce the configuration is unavailable through any route tried, by either executor. This is not a policy block, since AC authorized access on 2026-11-06. The published reference data are now available, which matters if AC supplies the code (for example by attaching the archive downloaded in a browser) or decides whether a comparison with the published data alone has any G5 standing. That decision is AC's. The developer record says a Python substitute does not count as reproduction, and I agree with that reading of handoff01:130.

**Source supplied by AC (addendum, 2026-11-06 10:14 UTC).** After the attempts above, AC uploaded the archive `IEP-MOP-main.zip` to this Claude session.
- 1,020,330 bytes; SHA-256 `cdd0e98d2b411f24cfcecb49d83e16f9d50a7622a0d4f0d3eb17eb334a405145`; MIT licence, copyright Robbe Vermeiren / NUMA.
- Contents, 27 entries:
  - `src/algorithms/` holds IEP_CORE, IEP_KRYL, IEP_KRYLREORTH and their `_MP` variants;
  - `src/experiments/` holds experiment_Hahn_Kravchuk, forward_error, backward_error, experiment_MP and experiment_reorth_strat;
  - `src/utils/` holds hahn_data/exact, kravchuk_data/exact, nodes_weights, LU_nopivot and IEP_initial_data;
  - figures, README and LICENSE.
- The README says only the `_MP` experiments need Advanpix. `experiment_Hahn_Kravchuk.m` uses Kravchuk p1 = 0.4, p2 = 0.5 and Hahn β1 = 1, β2 = 1.5, γ = 1, over N = 5..30.
- It was inspected in an isolated scratch directory and not executed during this audit. It is not committed.

This removes the source blocker. G5 now needs a runtime, which is available: Ubuntu apt mirrors are reachable, so Octave is installable. G5 execution is new development, not part of this audit. It is assigned as a separate Claude development step, because Codex's executor cannot reach the upload, and Codex will audit it (see the LOG and the next handoff).

## New findings (all MINOR; fix at PR preparation, confirm by diff)

- **R-1 — MINOR 9 chronology and an undated edit.**
  - The consolidation deleted dated chronology from three places: novelty-gate-D6-D7.md (old lines 6–8 and 18–25), attempts/D6.md (old 11–14) and novelty-gate-D4.md (old 33). The deleted facts:
    - the gate and its prospective tests were written before the diagnostic;
    - the state/IDEAS.md ranges 639–679 and 564–589 were read afterwards;
    - the initial complete-scan assertion was too strong;
    - D4-C1a was specified before its run, and its durable record was written after it.
  - novelty-gate-D6-D7.md:8 keeps an unqualified heading, "complete state scan".
  - Undated parentheticals were inserted into the Claude-authored AC-decision LOG entry (LOG.md:107). Their content is accurate.
  - Fix: restore the chronology in one dated Codex addendum below the canonical LOG entry, marking the inserted text as Codex's, and qualify the heading.
- **R-2 — split direction.** conditioning-hahn-normality-finite.md:4 still says "Split from: generic certificate application", while conditioning-normality-certificate.md:4–6 says the application is not a split. Use "Split from: none" and keep the certificate under Depends on.
- **R-3 — parent and child split lines.**
  - stable-solver-target.md:5–7 lists four records under "Split into", but each of them says "Split from: none": native-measurements.md:17, backward-local-manifold.md:5, backward-dyadic-obstruction.md:4 and backward-projection-measurements.md:17.
  - dictionary-target.md:4 does not name its sub-target dictionary-lifts.md.
  - Make each relation two-way. conditioning-growth-target.md is already consistent.
- **R-4 — original wording.**
  - conditioning-growth-target.md:47 says the original target wording is retained, but lines 11–18 paraphrase it. They also drop the mechanism bullet and the Done criterion of handoffs/01-work.md:52–62.
  - Quote the original verbatim in History and state the reformulation with its reason, as WORKFLOW requires. The OPEN status is correct.
- **R-5 — stale dependency line.** conditioning-normality-certificate.md:36 still cites "the localized layer induction in PD-T289". Cite PD-T289's algebra and recursion as localized by this file's lemma, plus PD-T288's local four-corner argument.
- **R-6 — axis wording.** conditioning-local.md:47–49: "zero b1 on every marginal-axis site" is true only on the first axis (n,0); for example, Hahn N4 has b1_(0,1) = −79/495. Say "(n,0)".
- **R-7 — historical-only projection claims.** The reference omits optimizer convergence flags and history and the 100-dps runs. In backward-projection-measurements.md (Results), "All 12 fits meet the … threshold at 160 dps" and "agree exactly between the 100/160 dps runs" are evidenced only by the lost Nov-5 receipts. State that scope, or add the flags.
- **R-8 — superseded pins at reused paths.** Old checker and verifier identities and their commands now run different files at the same paths:
  - backward-projection-measurements.md:148–157 and attempts/D5.md:217–221 (checker `3d2ae221…`);
  - conditioning-hahn-normality-finite.md:162–167 (verifier `f9403f53…`);
  - attempts/D1.md:224–225 (producer `7aa41…`, verifier `f9403f…`);
  - independent-checks-02.md:233.

  Label each as historical, with its commit, and point to the manifest for current identities.

## NOTE

- **G-record leftovers** in dictionary-obstructions.md:
  - line 3 keeps the C alias "two-sheet annihilator";
  - line 4's "Split from" refers to the record itself;
  - line 73 says "Neither negative statement", though only G remains.
- **Stale process text** remains in dated receipts: attempts/D2.md:3 and :161, and attempts/D4.md:9. report.md:51/55 and the results file quote binary64 values without the platform pointer. Optional.
- **Checker details:**
  - the projection checker does not itself verify the reference's `source_sha256` or platform; the file SHA covers them, and R1 verified they match;
  - it reports the normality-system count as a formula, which equals the actual 348;
  - `independent_check_moments.direct` keeps three redundant bare asserts (lines 86–88).
- **Reservation:** main PR #30 added PD-T472–494, PD-N178 and IDEA-571/575, all above this topic's reserved ranges, so no collision. The full reservation refresh against main and every open PR belongs to preparation and readiness.
- **G4** stays "forward threshold met; strict backward stability not achieved", never PASS. Sharp growth and the general stable solver stay OPEN, now in durable homes.

## Residual uncertainty

- Exact lemma tests are finite (N ≤ 8); generality rests on the written proof, which was reconstructed by hand.
- N8 returned-witness stationarity was independently checked for Krawtchouk LU only.
- The reference bytes' producer platform is corroborated, not observed: C4/LU targets regenerate bitwise, and all metrics match history.
- The projection fits remain local measurements; no global nearest point is certified.
- The G5 GitLab reset cause is undetermined.

## Next step

Stage PR. Codex, as developer, prepares the PR:
- fix R-1 to R-8;
- apply the shared registries by direct edit;
- assign final IDs from the reserved ranges after the full reservation check against main and every open PR, and record the heads checked.

Claude then performs the readiness check: the reviewed registry `git diff`, confirmation of R-1 to R-8 by diff, and the reservation refresh. This keeps registry application and its check with different agents. G5 stays BLOCKED unless AC supplies the source or decides otherwise. Only AC merges.
