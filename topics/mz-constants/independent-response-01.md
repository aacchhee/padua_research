# Independent focused review of MZ audit-01 response

Date: 2026-10-31. Auditor: Codex independent subagent, explicitly assigned **gpt-6-astra, high** under `agents/WORKFLOW.md`'s mathematical-audit allocation. The runtime does not expose separate effort telemetry. This is supplementary independent review of Codex development, **not the required Claude re-audit**. The auditor edited only this report and `tracks/mz-constants/evidence/astra-response-01-*`; no developer file or Git state was changed by this worker.

Rules were read at `b56c7d65520b4c9a1311342de19fb47c9ba1d8f1`: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`. The orchestrator's response-start rules pin is `6d10a82cf6fd6f7ef6fbe76e68133ccbcbe51994`; the applicable rules are unchanged. The managed-environment runtime skill was read and environment status checked before tool use; external primary-source inspection used the search connector, without storing third-party fulltext.

**Verdict: ACCEPTED within the focused scope: scientific/source commit `2cc1918b39d191ce233d44d9a33dbe83d697dbb0` plus the hashed completion metadata below. No unresolved finding.** The added endpoint corollary and its manuscript translation are analytically correct. The literature response closes audit M2 by naming the unresolved family and documenting a bounded screen; it does not clear historical novelty. Required focused Claude re-audit remains **PENDING**.

## Scope and independent reading

Read `audit-01.md` in full and verified it is byte-identical to the response-start version. Read the complete current `state/IDEAS.md`, including the charter/contextual candidates, all obstruction tables, historical MZ seeds and the 25 current MZ dispositions. Read the full relevant M1/M2/M3 candidate records and their revised dominance addenda; the full scientific and literature responses; `literature/INDEX.md`; the new mean-convergence record and the 20-query response section of M0; relevant `PROOF_STATUS.md` and `ID_CROSSWALK.md` rows; the reconciled ledger and receipt.

Read the full canonical foundation, upper-bound, coefficient-floor, degree-sensitive upper, hyperinterpolation, cardinal lower, harmonic witness, simpler U witness, eta counterexample, Padua compression and both revised OPEN-target files. Reviewed the complete response diff of the manuscript and its surrounding definitions/proof dependencies, plus the paper README/bibliography and report headlines. This is a focused changed-claim review, not a new line-by-line audit of every unchanged proof or every manuscript paragraph. Checked all 21 theory headers/statuses against the original audited package.

Novelty/mechanism scope is in scope, so the full IDEAS reading was performed. No candidate was generated. Closest mechanisms are IDEA-063 and IDEA-073; the new statement is a specialization of an existing proved inequality. Relevant obstructions remain the full-degree cutoff, one-sided Padua compression, and the missing uniform endpoint upper gap. Successful, equivalent, failed, refuted and deferred dispositions remain distinct.

## Mathematical reconstruction and audit dispositions

| Audit item | Independent conclusion |
|---|---|
| M1: explicit endpoint constant | PD-T022 gives `rho=max(2n/N−1,0)^2`. At `n=N−1`, `rho=(1−2/N)^2` for every `N≥2`, so `lambda_plus≤2−4/N+4/N²`. At `N=2`, exactness gives equality at one. For `N≥3`, positive rho makes the existing sign-replacement quadratic form strictly positive, hence the upper inequality is strict. |
| M1: dominance and B | `4−4/N≥2>2/pi` proves strict dominance over `2−2/(pi N)` for every `N≥2`. Monotonicity of rho in n extends this to every integer `0≤n<N`; the old minimum in PD-T025 always selected `1+rho`. Its removal changes no bound. |
| M1: proof graph | The leading manuscript theorem explicitly invokes the later degree-sensitive theorem. That later theorem proves its sign replacement directly from PD-T013's moments/defect and positive definiteness of the continuous mass matrix, without invoking the leading theorem. There is no logical cycle. PD-T014's original weaker statement/proof and PD-T015's independent mass inequality are retained PROVED. |
| L1 | PD-T018 gives `lambda_min(CC,N−1)→0`; the isometric compression in PD-T021 gives `eta_Padua≥1−lambda_min(CC,N−1)`. The liminf at least one is unconditional under the rule's stated hypotheses. No Padua limsup, positivity or genuine two-dimensional upper bound is inferred. PD-T028 remains OPEN. |
| L2 | The witness threshold `log N≥128` differs from non-vacuity against one: `128000/(log N)²<1` iff `log N>sqrt(128000)≈357.7708764`. The new text correctly limits its practical-vacuity statement to feasible full-spectrum computations considered here, rather than all computable integers. Finite scaled values do not establish a limiting coefficient. |
| L3 | The unchanged interpolation inequality holds for every polynomial in `Pi_N`, so the stated minimum-eigenvalue bound holds on the full space. Restriction yields `lambda_min(N,N−1)≥lambda_min(N,N)≥1/K_N`. |
| P2/P3 | MZ registry rows now state actual ID dependencies and mathematical parts. All 25 current dispositions are present. The five scoped negative results explicitly name IDEA-060/061/068/069/070 with the correct refuted/failed reason; equivalent IDEA-064/067/072 retain their separate PROVED results. No theorem is rejected merely because a mechanism fails or an application is dominated. |
| P4 | Reciprocal links name IDs and distinguish historical discussion splits, supporting results and actual proof dependencies. PD-T018 does not falsely depend on PD-T019; PD-N004 does. Neither PD-T027 nor PD-T028 is falsely relabelled PARTIAL. PD-T015 depends on PD-T013, not on its application's theorem. |
| I3 | The odd/even parenthesis correctly distinguishes marginal checks at 10, 20, 31 from the spectrum-table degrees. No measurement changes. |

All original 21 theory statuses are unchanged: **17 PROVED, 3 OPEN, 1 MEASURED**. The three OPEN targets remain PD-T020, PD-T027 and PD-T028. The changed corollary is analytic; no finite experiment supplies its all-N proof.

## M2: source coverage and independent primary spot-check

The source record, index, bibliography and manuscript now name weighted mean convergence and converse quadrature sums as the principal unresolved overlap risk. The five new records are LIT-061–065; Mastroianni–Russo and Xu remain explicitly bibliographic follow-ups. The M0 section lists 20 literal queries with failures and source-specific coverage. This auditor reviewed that execution record; it did **not** independently repeat all 20 queries or attest the developer's prior browser session.

Independent connector opens in this review reached:

- [Lubinsky's author preprint](https://lubinsky.math.gatech.edu/Research%20papers/marzyg98Paper147.pdf), selected introduction and Theorems 1.1/1.2 (printed pp. 1–4), with the returned corollary/example context. This confirms converse inequalities for the full interpolation space and general nodes, with specially chosen coefficients. The exact CC endpoint coefficients and critical logarithmic norm remain unverified; no full proof or final-version comparison was attempted.
- [Askey's 1969 CWI report](https://ir.cwi.nl/pub/7742/7742D.pdf), PDF pp. 3–7. The inspected discussion uses orthogonal-polynomial zeros, distinguishes the mean weight from the node-defining weight, labels its mixed-weight formulation a conjecture and invokes Gaussian quadrature. The corrected 1972 journal body was not read.
- [Erdős–Feldheim's original scan](https://www.renyi.hu/~p_erdos/1936-10.pdf), printed pp. 913–914 selected text. Its reference to earlier notation is explicit; the predecessor node convention was not independently reconstructed. No exact CC norm translation is certified here.
- [Nevai's author bibliography](https://people.math.osu.edu/nevai.1/MYMATH/paul_nevai_publ.pdf), item 58: the 1984 journal/volume/page metadata agree. The theorem and 1990 addendum remain unread.

The Smith Cambridge PDF timed out on two independent opens; its DOI open also failed. Smith's precise theorem summary is therefore developer-reported primary coverage, not independently reverified by this audit. This does not undermine the accepted **named unresolved pending-reference** disposition: no campaign theorem depends on Smith or another unverified source. The remaining journal/follow-up coverage is also not independently audited here. No primary source is promoted to a locally proved dependency, and neither a matching prior theorem nor its absence is claimed.

## P1 and preservation checks

The canonical reconciled ledger has SHA-256 `39dfc9a9abcffcc7e8d28caf0c537a9dcf4536b42186cc00991ee67b33516f56` and Git blob `43c581fb242fd28ebe4d89ee4a42e3bbd660a159`. Independent read-only Git inspection verified:

- MZ ledger commit `b56c7d65520b4c9a1311342de19fb47c9ba1d8f1` stores that blob.
- Programme propagation commit `c989031bacb3d35c711f4ace40a10e8909802106` and Lanczos propagation commit `48f7a02697d7753279e27d3ad462a4817c67ade0` each change **only** `topics/padua-batch-20261031/ALLOCATIONS.md` and contain the same blob.
- Separate GitHub file-API reads of both live branches returned the same blob. Initial local tracking refs were stale, and an assertion exposed that fact; the root orchestrator refreshed them, after which the exact checker passed. No failed propagation is inferred from stale local refs.
- The ledger has one named owner and all active members. Charter was already merged first at `08fafe62d9798385dfafaacc9a41344272737e68`; MZ is next. The deleted/closed charter branch need not be rewritten, and main changes only through AC's later merge. No main mutation was performed by this reviewer.
- The five new literature reservations explicitly consume the formerly free LIT-061–065, so the next free source ID is LIT-066; other next IDs remain PD-T029, PD-N007 and IDEA-077.
- All **105** files under `tracks/unisolvence` and `topics/charter-unisolvence-20261031` are byte-identical to merged main. Its 13 result rows and 41 literature rows remain present verbatim. Original MZ audit and source checker code remain unchanged.

## Actual independent execution and evidence

Working directory: `/workspace/padua_research`. Python 3.12.14, Linux x86_64; exact checks use only standard-library integer/Fraction arithmetic. No seeds or numerical libraries are involved. Commands actually executed:

```sh
python tracks/mz-constants/code/m3_exact_check.py --max-n 25 > tracks/mz-constants/evidence/astra-response-01-m3-replay.txt
python -I tracks/mz-constants/evidence/astra-response-01-check.py > tracks/mz-constants/evidence/astra-response-01-check.json
```

The first independently reruns the unchanged source checker: **324 pairs PASS**, including exactness, upper signs and its existing reconstruction diagnostics. Checker SHA-256: `246bd4b95226182b0231730d7ad6ae6d7716623d31b28193c0e44d932825d2dd`.

The second is newly written independent code with no campaign imports. It checks the endpoint identity and all-degree monotonicity/dominance for **500,499** pairs with `2≤N≤1000`, using the stronger rational comparison obtained from `pi>3`; verifies **21,320** endpoint off-diagonal sign entries and entrywise nonnegative defects for `2≤N≤40`; checks the `N=2` mass/discrete equality; compares all original theory statuses; and verifies ledger/charter/source preservation. **PASS** after the stale tracking refs were refreshed. Its JSON includes its own code hash, the input head `2cc1918b39d191ce233d44d9a33dbe83d697dbb0`, environment and SHA-256/size identities for 46 exact source files. It also verifies all original 65 mappings remain unchanged and the five added mappings are exactly LIT-061–065. The initial failed run produced an empty redirected output and a visible assertion; no success is claimed for that run.

These bounded checks supplement the analytic reconstruction. Full spectra, old fitted laws and the entire reproduction campaign were deliberately not repeated because the response changes none of that code/data and the original audit already reran them. This is not a computer-assisted all-N proof. No third-party PDF, fulltext extract or new numerical-spectrum artifact was created in Git.

## Review findings and residual work

Four low editorial observations were returned to the developer rather than silently fixed: malformed provisional/final source shorthand in the two literature response files; missing explicit dominance wording in the historical IDEA-073/063 direction records; ambiguity between zero-based PDF page 3 and printed page 4 for Lubinsky Theorem 1.2; and stale current report wording about page count/ledger reconciliation. All four corrections were checked at `2cc1918b39d191ce233d44d9a33dbe83d697dbb0` and are resolved. No developer source was edited by the auditor.

The mathematical and source-coverage conclusions above do not certify a future final target manifest or PR text. The refreshed rehearsal was inspected and independently identity-checked in the completion addendum below. The final build receipt was separately inspected: manuscript source SHA-256 `c0037cf857895111b98282e400dd4c0af4d87b4cfdc5abba16f53071c58134af`, bibliography `ea5fbd9afabb30b090003199084aa1fd3448928dc00538375cc23cd678cae6c5`, PDF `a34288ce1a0093c06299ba13ef06d023d11bfd80ace4bbe20535e0200a3a6c83` (430932 bytes, 15 A4 pages) match the README. Final logs contain no actual warnings, undefined references or box diagnostics. This was independent artifact/log inspection, not an independent TeX rebuild. Historical novelty remains unresolved, final source comparisons and cold-storage delivery retain their stated gaps, and the required focused **Claude re-audit remains PENDING**. Only AC decides readiness and merges.

Suggested next prompt: “Claude (Opus 5.5 high): Continue codex/mz-constants-20261031 at the response commit; re-audit the changed corollary, source coverage and protocol response, preserving the named pending-reference gaps.”


## Completion addendum — pinned integration metadata

The final scientific/source snapshot is `2cc1918b39d191ce233d44d9a33dbe83d697dbb0`. All 46 source hashes in `astra-response-01-check.json` still match after metadata integration. The developer's four low editorial corrections are resolved. The final handoff accurately leaves the required focused Claude review PENDING; this supplementary acceptance does not change that stage or authorize merge.

Reviewed the full refreshed `batch-rehearsal.json`, `integration-impact.md`, `AUDIT_HANDOFF.md`, root identity-checker source and its current result. Independently executed:

```sh
python topics/mz-constants/check_response_01.py --output tracks/mz-constants/evidence/astra-response-01-protocol-replay.json
python -I tracks/mz-constants/evidence/astra-response-01-completion.py > tracks/mz-constants/evidence/astra-response-01-completion.json
```

Both PASS. The first verifies 123 historical targets against their original Git objects, all 70 MZ mappings / 34 combined result rows / 65 combined literature rows / 25 current MZ dispositions, all 105 charter files and 54 accepted rows, unchanged producer/audit inputs, actual ledger identity, all 21 uploaded payloads available in this workspace, and public-artifact limits. Its `current_response_targets_verified=0` is explicit: the final response-target manifest is generated after this review. The root must execute its final `--require-targets` check during packaging. This auditor does not claim that future execution; its own pre-manifest replay is retained unchanged. The mutable root `response-01-checks.json` is deliberately not pinned here.

The completion checker independently verifies that the local rehearsal commit `16d90aaf0e9206ed5b1ff52e47426d834f710635` has actual charter main `08fafe62d9798385dfafaacc9a41344272737e68` as its parent and exactly the same complete tree as the response source `2cc1918b39d191ce233d44d9a33dbe83d697dbb0`. The response source descends from that main, consistent with the recorded zero-conflict squash. This is read-only verification of the executed rehearsal's objects, not a second squash operation by this subagent. The ten conflicts in the earlier live main merge are correctly distinguished from zero conflicts in the subsequent squash.

The zero-context shared delta is exactly the independently regenerated `git diff --unified=0` from base to response source on its ten listed paths, with size **86795 bytes** and SHA-256 **ae7a38b0e8942033d10de9e244d8dc1bc95a9a59ba360f3edd7a83ee52e61735**. Receipt and impact narrative agree. The fresh rehearsal's four unavailable ignored uploaded texts are disclosed; this workspace's separate checksum execution verifies all 21 payloads. Neither missing-text report becomes an inherited proof or a fabricated execution.

The completion JSON pins nine metadata/evidence inputs by SHA-256 and size, including the revised rehearsal, exact delta, integration impact and handoff. Final packaging may add the final manifest and update root checker output, provided the accepted scientific/source and reviewed metadata bytes remain unchanged or receive a recorded impact review. No unresolved finding remains in this declared scope. Historical novelty, sharp/2D targets and archival delivery retain their limits; required focused Claude re-audit remains **PENDING**.
