# Claude audit-01 — part 3 and the gated campaign (handoff 05)

## Decision

**The mathematics is ACCEPTED for its stated scope. Findings need a developer response first, so the stage is WORK.**

- **PROVED claims.** Every PROVED claim is accepted exactly as stated, with no status change. This covers:
  - codex-02, 03, 04, 05, 07 and 08;
  - gated-codex-01 to 17;
  - the scoped negative statements codex-N01, gated-N01 and gated-N02.
- **MEASURED claims.** codex-01 and codex-06 are accepted as MEASURED.
- **Original target.** PD-T099 (all degrees n ≥ 2) stays **OPEN**. The finite bridge 17 ≤ n < N_* is unresolved and N_* is non-effective.
- **Severity of findings.**
  - No finding is CRITICAL. No finding touches a proof step, checker predicate, certificate value or claimed status.
  - One finding is MAJOR, and it is about evidence protocol only (F1: the T1 evidence file was split to stay under the 1 MB limit).
  - The rest are MINOR records/citation/proposal items (F2–F15) and NOTEs (N1–N14).
- **What happens next.**
  - Codex answers every finding in `response-01.md` (handoff 06).
  - A Claude protocol check of the response follows, and then PR preparation.
  - A full mathematical re-audit is needed only if a response changes a statement, proof, checker predicate or certificate value. Documentation-only corrections and a lossless repackaging whose content hash is verified do not count.

## Identity, rules and audited candidate

- **Auditor:** Claude, configured `claude-opus-5-5` at effort xhigh, as handoff 05 requested.
  - The reason is the allocation-table row for an adversarial mathematical audit of a novel mechanism, an eventual all-maximizer theorem and computer proofs.
  - The runtime exposes no separate serving-model receipt.
- **Role:** independent audit orchestrator and auditor, distinct from the Codex developer (gpt-6.1-sol) and the Astra supplementary checkers. I wrote no developer file.
- **Rules:** read at the branch head `9fcdc2199a44393f522958b36ecadbec57e2de9b`. Files: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`, `templates/HANDOFF.md`, handoff 05 and LOG.
- **Audited scientific input:** `c173fbf7ee66f02cc1d992e52edb43fdbd819474`.
  - `git diff --stat c173fbf 9fcdc21` touches only `handoffs/04` (status line) and `handoffs/05`, so every audited file is byte-identical at both commits.
  - Main is `2b52b432fe59c9a50aef9deebe5152c5d6874465`, unchanged since handoff 05 (refetched 2026-11-02).
  - Open PRs: only draft #17, this topic. Every other repository PR (1–6, 8–16) is merged.
- **Remote access.** I used the session clone with `git push` over the proxy, not the GitHub connector that handoff 05 mentions. The branch, history rules and identity constraints are unchanged. I did not force-push and did not rewrite history.
- **Evidence manifest:** `evidence-manifest.json` sha256 `16eb0708715c3abb5b7ab7011cd9675ab8bcb12b9f371aef927edb1faf19d038`.
- **Audited theory-file hashes.** Short prefixes are listed below; the full hashes are in the sub-reports and the manifest.

| File | sha256 prefix |
|---|---|
| codex-02 | `1040ea4c` |
| codex-03 | `486e346f` |
| codex-04 | `84c4b82e` |
| codex-05 | `21d65ed2` |
| codex-07 | `da4293b3` |
| codex-08 | `a85f6b16` |
| codex-N01 | `b5e01d39` |
| gated-01 | `4e35ff98` |
| gated-02 | `39c2f217` |
| gated-03 | `671353ba` |
| gated-04 | `fd862326` |
| gated-05 | `a54168c4` |
| gated-06 | `89de42bb` |
| gated-07 | `9f3a3edb` |
| gated-08 | `04cd3c9f` |
| gated-09 | `c7018731` |
| gated-10 | `ee0408d6` |
| gated-11 | `42372e73` |
| gated-12 | `94a0c89c` |
| gated-13 | `c0b927c1` |
| gated-14 | `9e46c6c4` |
| gated-15 | `def15397` |
| gated-16 | `ac9e4ed5` |
| gated-17 | `3d7672e8` |
| gated-N01 | `775c4135` |
| gated-N02 | `08c7f7ac` |

## Method and coverage

**Sub-auditors.** I ran six independent Claude sub-auditors, each configured Opus 5.5 at xhigh, read-only on the repository and with no Git authority.
- Each was briefed with the claims to test and the files to read, not with my conclusions.
- Each was told to reconstruct independently and to treat the Astra `gated/checks/*` and `independent-checks-*` reports as supplementary, not as approval.
- The harness did not let sub-agents write their own report files. Each returned its report as text, and I saved it verbatim in substance (condensed) under [`audit-support/claude-audit-01/subaudit-reports/`](audit-support/claude-audit-01/subaudit-reports/).

| Sub-audit | Handoff claims | Scope |
|---|---|---|
| A | 1 | codex-02/03/07/08: finite reduction, checkers, all certificates |
| B | 2–3 | codex-04/05, gated-01…06, gated-N01 |
| C | 4–5 | gated-07…13 |
| D | 6–8 | gated-14/15/16, adversarial |
| E | 9 | gated-17/N02 |
| F | 10 | Candidate, gate, status, evidence and provenance discipline, including the full `state/IDEAS.md` |

**Orchestrator spot checks.** I verified the key cited lines myself before relying on them:
- the PD-T159 versus PD-T156/157 statements in `PROOF_STATUS.md` and the stale citations, by grep;
- that the D3 pre-registration hash matches the first 86 lines of `gated/d3/r01-finite.md`;
- that gated-02's committed hash is `39c2f217` while `checks/d1-r02.md:32` pins `d57b8d07`;
- the "split … to stay below the 1 MB evidence-file limit" sentence at `attempts/T1-T5.md:62-64` and the split in `code/part3/tests_analyze.py:42-50`;
- the slope-premise text at `gated/d2/r01-structure.md:30`;
- that LIT-377 says De Marchi 2022 lists "corner location of Lebesgue maxima" as open (UNVERIFIED, secondary).

I also read `report.md`, `gated/REPORT.md`, LOG, handoff 05 and gated-15 in full.

**Novelty scope.** The scope contains mechanisms and negative statements, so the complete `state/IDEAS.md` was read (lines 1–850, every obstruction and disposition table; sub-audit F).
- Mechanism terms and synonyms were searched across IDEAS, PROOF_STATUS and other topics' theory files: reflect, triangle defect, majorant, cusp, first variation, zero/excluded cardinal, centreward, monoton, cotangent, Bernstein, phase localization, Lebesgue function, corner.
- The shortlist was: IDEA-206/PD-T099, IDEA-305/PD-T189–192, IDEA-303/304, IDEA-290–302, PD-T103, PD-T190, IDEA-048/LIT-388, LIT-377, IDEA-213/222 with PD-N046/048/052, and IDEA-257–261.
- `literature/INDEX.md` was searched, not read in full. It has no Brutman/Günttner/Rivlin record. LIT-301, 312, 330, 377, 379 and 388 were read.
- Verdict: **the gate passes, with the citation gaps in F13.** Every candidate is declared a variant, with a separation criterion and a kill test. There is no duplicate and no priority claim. No literature theorem is transferred; the cotangent, Taylor, Machin and Bernstein facts are derived locally.
- Not done: an external literature search on whether an eventual corner-argmax theorem is already published. The topic makes no novelty claim, and LIT-377 (unverified) reports the corner location as open in 2022.

**Not covered.**
- The inherited accepted records PD-T156/157/159/162–177/179/185–191 were checked at statement level only (PD-T101 §1, PD-T185 and PD-T189 in full).
- n = 3–7 were not re-audited.
- The full ε–δ tube/equicontinuity details of codex-04/05 were accepted at the level of the accepted PD-T191.
- The Astra checkers' own transcripts.
- Standalone `maj.py` whole-square scans (already declared outside replay).
- The original Claude records: plan, ideas, gate, claude-01/02. Claude cannot independently approve them; they keep their separate Codex audit.

## Executions actually performed

All runs used Python 3.13.18, NumPy 2.5.3, SciPy 1.18.1, SymPy 1.14.0 and mpmath 1.3.0 in a 4-core Linux container, from the repository root at `9fcdc21`. Outputs went to session scratch, never over developer evidence. `git status --porcelain` was empty after every run. Small receipts and the independent scripts are committed under [`audit-support/claude-audit-01/`](audit-support/claude-audit-01/) with a hash manifest.

### Handoff minimum set (orchestrator; `orchestrator/run_min.sh`, all rc 0)

| Command | Result |
|---|---|
| `check_evidence.py` | Accepted: 276 entries, 2,447,717 generated bytes, largest 269,669, 79 JSON, 10 certificates, 19 receipts; manifest `16eb0708…`. It rewrites `outputs/part3/packaging-validation.json` (N3); the tree stayed clean, so that rewrite is deterministic. |
| `finite_n2_exact.py` | Accepted, maximum 3 at (±1,−1); identical to the evidence apart from the Python field. |
| `finite_bernstein_check.py` n8 pilot | Accepted (32 bound + 2 corner leaves); certificate `92528fc9…`; 46.9 s. |
| `finite_general_check.py` n12 pilot | Accepted (52 + 2); certificate `f44e2897…`; 5.8 s. |
| `pairing_exact_check.py` | PASS: 6 groups, 13 roots, exact reversal lower bound. |
| `d2_symbolic_r01.py` | Byte-identical to the committed `d2_symbolic_r01.json` (`f3e85314…`). |
| `d3_edge_generate.py` | 10 pairs, 20 leaves. The regenerated certificate differs from the committed `0d660fc7…` only in cpu/wall seconds and `preregistration_note_sha256` (F6). The E-P screen is byte-identical (`3215523e…`). |
| `d3_edge_check.py --controls`, committed and regenerated | Both accepted with checker `5f43f69a…`; 17/17 malformed controls rejected, including the designated E-P witness and uniqueness. |

### Measured-test replays (orchestrator; `OPENBLAS/OMP=1`)

See the "Measured replays" section below. Its results were appended after the runs finished.

### Sub-auditor executions (details and hashes in the sub-reports)

**A: finite certificates.**
- Replays: `finite_general_check.py` on n9, 10, 11, 13, 14, 15 and 16, all accepted with complete partition; `finite_general_controls.py` (14 defects rejected); both committed independent control harnesses, run through a write-redirecting wrapper (N2).
- Its own 90-digit direct Chebyshev-basis interpolation solve (n = 2, 3, 8–16) agrees with the PD-T101 cardinal formula to ≤ 3e-91. Three plausible wrong conventions differ by ≥ 0.0074.
- Its own **independently implemented rigorous kernel** uses an `mpmath.iv` Vandermonde, an exact dyadic approximate inverse, and a rigorous residual ‖R‖ ≤ 7.5e-88. It proves unisolvence without PD-T101 and carries the error exactly to every leaf's Bernstein coefficients. It verifies all ten global certificates and rejects five corrupted controls.
- Exact n2 re-proof by sign vectors.
- Measured grid plus Nelder–Mead search, n = 2, 3, 8–16.

**B: defect and primitive chain.**
- `d1_phase_r01.py` replay is identical.
- `d1_screen_r01.py` replay: all 21,009 numeric leaves identical.
- Its own mpmath Lagrange solver verifies λ = S − Δ, the four-copy identity, (B), Δ ≥ Q, the codex-04/05 decompositions and the numerator identities to ≤ 1.5e-49.
- SymPy exact collisions for n = 2…40.
- Cusp slope equals L_n for n = 2…12, 31, 32 and 64. The actual λ has no linear corner cusp.

**C: theorems 07–13.**
- `d1_constants_r03.py`, `d1_rows_r06.py` and the D2 main/energy screens replay identically.
- Exact number-field Vandermonde cardinals for n = 2…8 verify every theorem-13 identity and (n−1)/6 exactly.
- Exact-rational bookkeeping for 07: quadratic coefficient 241385.1 < 242000.
- Measured probes of 08, 10 and 12.

**D: theorems 14–16.**
- Its own first-principles cardinals.
- The local inequality was tested at 21 degrees, n = 2…201, both corners. The measured remainder ratio is ≤ 0.447 against the claimed 237000, with strict descent at every tested ρ > 0.
- Component bounds are all far below their claimed constants.
- Measured global search at 36 degrees, n = 17…200: the maximum is always at the two nonnode corners; the gap falls from 0.5906 to 0.5524.
- F^h(s) = −F(s,0) holds termwise to ≤ 1.2e-13 at n = 2…41.
- The horizontal-gap limit is consistent with the measured g_h ≈ 0.999. The n = 400 run was killed at the time limit, with no result.

**E: finite edge cells.**
- Its own kernel: an integer-interval Vandermonde, with the PD-T101 coefficients inside its enclosures.
- N02 certified independently: λ₁₂(1, cos 9π/26) − λ₁₂(1, 0) ≥ 0.0393766667 > 39/1000. The developer's integer comparison was reproduced.
- All 10 theorem-17 comparisons were re-certified rigorously by a different method, a second-order angle-Taylor bound.
- 21 extra checker probes.
- Under `python -O` the checker accepts a forged certificate (N1).

**F: protocol.**
- Its own manifest verifier: 276/276 match.
- The pinned hashes in handoff 05 all match.
- `input-snapshot.json`: 236/236 blobs match.
- 216 relative links checked, 0 broken.
- Every file is ≤ 1 MB.
- The ID union on main and the fetched branches has maxima PD-T205 / PD-N077 / IDEA-315 / LIT-459. There is no collision with the reserved PD-T206–245, PD-N078–083, IDEA-316–335 or LIT-460–465.
- `git diff origin/main...HEAD` outside the topic changes only `results/padua-argmax-alln-20261101.md`. No shared registry is touched.

## Claim verdicts

| Claim | Status | Verdict |
|---|---|---|
| codex-02 n=2 global argmax | PROVED | ACCEPT (A) |
| codex-03 Bernstein certificate correctness and constructor | PROVED | ACCEPT; F9 (A) |
| codex-07 n=8 global argmax | PROVED | ACCEPT; F8 registry duplication (A, F) |
| codex-08 n=9–16 global argmax | PROVED | ACCEPT (A) |
| codex-04 vertical compact defect | PROVED | ACCEPT (B) |
| codex-05 horizontal compact defect | PROVED (supporting) | ACCEPT; F4 (B) |
| gated-01 projection / λ = S − Δ | PROVED | ACCEPT; F3 (B) |
| gated-02 global two-phase bound | PROVED | ACCEPT; F5 (B) |
| gated-03 local gain | PROVED | ACCEPT; F2 (B) |
| gated-04 compact-complement gap | PROVED | ACCEPT; F2, F3 (B) |
| gated-05 finite projected defect | PROVED | ACCEPT; F3 (B) |
| gated-06 exact primitive cusp, n ≥ 3; n = 2 exception | PROVED | ACCEPT (B) |
| gated-N01 coset maximality / pure-quadratic primitive envelope fails, fixed n ≥ 3 | PROVED negative statement | ACCEPT. Not transferred to λ; the linear term is retained (B). |
| gated-07 explicit 242000/2048/640 envelope | PROVED | ACCEPT. Valid; quantitatively unusable as stated (C). |
| gated-08 adaptive defect ≥ 1/1536 | PROVED | ACCEPT (C) |
| gated-09 shrinking corner boxes | PROVED | ACCEPT; F2 (C) |
| gated-10 noncorner-coset defect ≥ 1/4096 | PROVED | ACCEPT; F3 (C) |
| gated-11 uniform scaled localization of all maximizers at nonnode corners | PROVED, non-effective | ACCEPT; F2 (C, D) |
| gated-12 row identities, with no partial-sum inequality | PROVED | ACCEPT (C) |
| gated-13 corner first variation and aggregate Taylor upper model | PROVED. Uniform slope/energy premises OPEN. | ACCEPT; F2, F15 (C, D) |
| gated-14 reflection-first local bound, 237000ρ²log(n+1), physical radius 2^-17/n² | PROVED | ACCEPT (D) |
| **gated-15 eventual exact two-corner global argmax** | **PROVED, N_* non-effective** | **ACCEPT** (D, with dependencies by B and C) |
| gated-16 horizontal compact envelope | PROVED | ACCEPT (D) |
| gated-17 ten finite whole-cell E-C comparisons, n = 7, 12 | PROVED (finite, computer-assisted) | ACCEPT; F6 (E) |
| gated-N02 E-P common-phase translation refuted at n = 12 | PROVED negative statement | ACCEPT. Refutes E-P only (E). |
| codex-N01 tie-inclusive pairing order fails on the n4 list | PROVED negative statement | ACCEPT. Exact recheck PASS (orchestrator); scope unchanged. |
| codex-01 T1–T5 tests | MEASURED | ACCEPT as MEASURED; F1 (F). Replay below. |
| codex-06 pairing screens | MEASURED | ACCEPT as MEASURED. Replay below. |
| PD-T099 all degrees | OPEN | Remains OPEN; not narrowed or upgraded (D, F). |

**Main theorem chain (gated-15).** I reconstructed the assembly myself and agree with sub-audit D.
- Gated-11 gives, for each ε, a threshold N_loc. Above it, every global maximizer has an actual-nonnode-corner phase representation with scaled distance ρ = n|θ−θ_c| + m|φ−φ_c| < ε. This is uniform over all maximizers, because the bound ρ² ≤ 2π²C log(n+1)/Λ_c depends on n only (C).
- That ρ is exactly gated-14's phase ρ = α+β, so no unit conversion is involved. The physical radius 2^-17/n² is not used.
- Gated-14 gives λ ≤ Λ_c − ρ²[Λ_c/10 − 237000 log m] with a ρ-independent bracket that is positive once log n ≥ 10^7, by PD-T157(1). So the inequality is strict on the punctured neighbourhood.
- With ε = 1/64 and N_* ≥ max(N_loc, e^(10^7)), every maximizer has ρ = 0. The parity reflection gives both nonnode corners. Node corners have value 1.
- The finite range 2–16 does not cover 17 ≤ n < N_*.

**PD-T099 status.** My view, offered for AC's decision: keeping PD-T099 OPEN, not PARTIAL, is correct under WORKFLOW. PARTIAL needs the remainder to be an explicitly identified case or parameter range. "17 ≤ n < N_*" with N_* unknown is not one. Sub-audit D notes that PARTIAL is arguable; the decision is AC's.

## Findings

Severity scale:
- CRITICAL invalidates a PROVED claim.
- MAJOR is a real gap or rule breach needing a developer response.
- MINOR is a wording, provenance, status-label or proposal issue.
- NOTE is advisory.

Each finding needs a disposition in `response-01.md`.

### MAJOR

**F1 (evidence protocol; affects MEASURED codex-01 evidence only).**
- `attempts/T1-T5.md:62-64` states that the per-degree T1 profiles are "split into `tests_T1_n*.json` to stay below the 1 MB evidence-file limit". `code/part3/tests_analyze.py:42-50,64` performs that split and rewrites `tests_T1.json` in place.
- The split files total 1,339,645 bytes, and the raw producer output's hash is recorded nowhere.
- WORKFLOW (Computation and evidence) says: "Do not split files to evade limits."
- Required:
  - repackage losslessly, as one deterministic gzip (as PACKAGING.md does for D1) or as cold storage plus manifest;
  - record the decompressed-content hash;
  - correct the rationale text with a dated note;
  - refresh the manifest in the response commit, not by overwriting history.
- No claim status depends on this.

### MINOR

**F2 (citation; B-1, C-F1, D-F1).** The lower bound Λ_c ≥ (4/π²)log²n − 54 is still cited to PD-T159.
- PD-T159 states only |Λ_c − L_n²| ≤ 54. The bound is PD-T156 (1), which also appears in PD-T157 (1).
- Locations: `theory/gated-codex-03…:79,327`, `gated-codex-04…:29`, `gated-codex-09…:65`, `gated-codex-11…:61`, `gated-codex-13…:68`, and `gated/d1/r01-phase.md:94,376`.
- Gated-14 and d2/r02 were already corrected.
- Required: a dated documentation correction, keeping PD-T159 wherever it really is a dependency. No mathematical change.

**F3 (stale status lines; B-2, C-F2, D-F3, F-N5).** These still say an independent check is "pending", although the checks are complete:
- `gated-codex-01:31`, `-04:20`, `-05:24,52`, `-10:295`, `-13:57,172`, `-14:36`, `-15:27`;
- the "check pending" phrases in `-09` and `-12`.

`gated-codex-04` calls itself "conditional in the ordinary sense", which invites confusion with the CONDITIONAL status. `gated-codex-N01` has no History section. Update the wording with dated notes.

**F4 (cross-record status; B-4, F-m7).** `theory/argmax-alln-codex-05…:6,58–59,84,207–212` and `attempts/P1-P2-edges.md:41` still say the compact horizontal envelope (P2) "remains OPEN", with no forward link. Meanwhile `report.md` and `proposed-record-changes.md:78` say P2 is PROVED via gated-16. Add a dated supersession pointer to gated-16, and to gated-04 for the upper half.

**F5 (provenance; B-3, F-m10).** `gated/checks/d1-r02.md:32` pins gated-02 at `d57b8d07…`. The only committed version, which is also in the manifest, is `39c2f217…`, and there is no impact note.
- Sub-audit B diffed the committed proof text against `gated/d1/r01-phase.md` §1–2 (identical) and reconstructed the committed version in full.
- So this audit resolves the mathematical impact.
- Required: a dated impact note. Do not refresh the frozen receipt.

**F6 (provenance; E-F1).** The committed D3 certificate records `preregistration_note_sha256` `03e877…`. That is exactly the hash of the first 86 lines (5115 bytes) of `gated/d3/r01-finite.md`; the file at HEAD hashes to `94e873…`.
- The post-run edit only appended the completion record (lines 87–208). No limit, phase grid, threshold or acceptance text changed.
- The note was first committed together with the results in `c173fbf`, so its content before the final run is attested only by the developer's records.
- The public pre-registration `gated/d3/r01-contract.md` (`71f49e5`, unchanged) fixes the decisive parameters.
- Required: document the prefix relation and the reproducing command (`head -n 86 … | sha256sum`), and state plainly that the note was not committed before execution.

**F7 (pre-registration provenance; F-M1, downgraded by me).** These contracts were first published in the same commit as their results:
- D1 r2 (`98b5622`), r3 (`68edd27`) and r5 (`aa1883f`), and D2 r1 (`fdee651`);
- also `d1/r04-next-lattice.md` and `d2/r01-next-reflection.md`.

So git does not show that they were registered before execution. WORKFLOW does not literally require a separate commit, and the records are consistent. I rate this MINOR because the decisive acceptance criteria are strict mathematical statements whose truth does not depend on timing.
- Required: a "first-published commit" column in `gated/ROUND_LEDGER.md`, with an honest statement that pre-execution registration for those rounds rests on developer records.

**F8 (registry duplication; A-M3, F-m9b).** The target of PD-T181 is word-for-word the statement of codex-07.
- `proposed-record-changes.md:14,17–30` both upgrades PD-T181 to PROVED and registers codex-07 as a new split ID. That would put one theorem under two IDs.
- Choose one at PR preparation:
  - either codex-07 becomes the proof record of PD-T181 with no new ID;
  - or PD-T181 is marked proved by the new ID with an explicit crosswalk.
- Locations: `codex-07:5`, `report.md:59`.

**F9 (dependency and statement; A-M1, M2).** In `theory/argmax-alln-codex-03…`:
- "Depends on" (lines 56–64) says there is no external theorem. The general-constructor appendix (lines 159–172), which codex-08 relies on, uses PD-T101 §1.
- The all-n constructor's enclosure soundness and the reflection equality of the corner values appear only in the appendix (lines 153–216), while codex-08 cites both.

Add the dependency, and state these as explicit parts or status rows. No mathematical change is needed.

**F10 (results and proposals; F-m8, m9a/c).**
- `results/padua-argmax-alln-20261101.md:7` credits codex-02/03/07/08 with every 2 ≤ n ≤ 16. Degrees 3–7 are inherited PD-T162/166/169/174/177.
- The proposed RESULTS block in `proposed-record-changes.md` uses an H1 heading and `../topics/` links, which break at the repository root.
- Literal proposals are missing for:
  - the IDEA rows;
  - the new PROOF_STATUS rows;
  - PD-T099's "Split into" line;
  - the IDEA-206/299 dispositions.

Fix these in the response or at PR preparation.

**F11 (durable homes for measured content; F-m1, m2).** These gated MEASURED screens have no durable MEASURED theory record:
- the D1 r1 screen;
- the D2 r1 slope/energy screen, which is cited as "finite numerical support";
- the D1 r6 row grid;
- the D3 E-P float screen.

Measured failures are recorded as IDEA dispositions with "no PD-N" (`ideas-codex-fallback.md:22-23`, O-R) or inside MEASURED codex-01 (the T2/T3 raw-profile kills). AC's L5 rule and registry precedent (PD-N035/037/038/040/043/049) point to scoped MEASURED PD-N records. Propose dispositions for PR preparation, and refer to AC if disputed.

**F12 (IDEA records; F-m4, m5).**
- `ideas-codex-fallback` record 03 carries both E-C (OPEN) and E-P (refuted). Record 02 carries O-L (deferred) and O-Lt (refuted). Split each at PR preparation.
- Claude candidates need closing out at PR preparation:
  - claude-01 → REJECTED: refuted, linking gated-N01;
  - claude-02's disposition after T2/T3/T4, since its erase criterion at `ideas.md:31` fired within the measured scope.

These are Claude's own records. The PR-preparation orchestrator applies them, and Codex reviews them.

**F13 (gate citations; F-m3).** No duplicate and no priority claim, but the closest prior entries should be cited:
- PD-T103's excluded-zero-cardinal certificate, for gated-04/05;
- PD-T190's explicit C|s| cusp term and plan P3's "cusp-linear" remark, for gated-06/N01;
- LIT-377 (De Marchi 2022 lists the corner location of Lebesgue maxima as open; UNVERIFIED secondary) and LIT-388, as the literature baseline for gated-15, whose headline is the "strongest new result".

The D2 gate did not search other topics' theory files.

**F14 (LOG; F-m6).**
- The header omits the PD-T226–245 reservation.
- Lines 9–10 still call claude-02/-05 "active in part 3".
- The claims block lists no gated claims.
- The heading at line 71 is empty.
- Handoffs 01, 02 and 04 are not linked (WORKFLOW: "The log links each handoff with one line").

This audit adds a LOG entry and the handoff 05/06 links. The developer fixes the rest.

**F15 (characterization of an OPEN premise; D-F2).** Theorem 14 (9), with ρ² ≥ 2n²h_x + 2m²h_y, gives A_n ≤ −2n²(Λ_c/10 − 237000 log m), and the same for B_n with m², whenever log n ≥ 10^7. So the eventual slope premise of `gated/d2/r01-structure.md:30` (A_n, B_n ≤ −a n²Λ_c) holds eventually, for every a < 1/5.
- `gated/REPORT.md:55`, `gated/d2/REPORT.md:5`, `gated/CANDIDATES.md:55` and `gated-codex-13:6` call uniform slope/energy "OPEN" without qualification. That is accurate only if "uniform" means all n.
- Required: the developer checks the implication and adds a clarifying clause. The energy premise and all-n uniformity remain OPEN.

### NOTES

- **N1 (A-N1, E-F2).** Every checker acceptance predicate is an `assert`. Under `python -O` or `PYTHONOPTIMIZE`, the checkers accept without checking; sub-audit E demonstrated this for D3 with a forged certificate. All recorded runs had assertions enabled. Suggest explicit raises, or refusing to run when `not __debug__`.
- **N2 (A-N2).** `outputs/part3/independent_general_controls.py:28` and `independent_n8_controls.py:60` write to hard-coded repository paths, so re-running them would overwrite committed evidence.
- **N3 (F-N1).** `check_evidence.py:73` rewrites the committed `packaging-validation.json` on every run. It is deterministic; the tree stayed clean.
- **N4 (B-5, C-F4).** Notation clashes: N_δ means different things in gated-04 and gated-05, and N_* in gated-09 is not the N_* of gated-15.
- **N5 (B-6).** `gated-codex-06:28` attributes the nonzero values to coprimality. They are nonzero because 1 + cos v ≠ 0; coprimality only excludes other collisions.
- **N6 (B-7, C-F3, C-F5).** Small editorial points:
  - gated-03's section numbering and heading levels are inconsistent;
  - `d2/r01-screen.md:96` quotes the scalar inequality with 2b²/|a| where theorem 13 has b²/(2|a|) (both are true);
  - "after gated05" at `CANDIDATES.md:55` is ambiguous.
- **N7 (D-F4).** `gated-codex-15:37` credits PD-T101 with the common nonnode-corner value; that equality is stated in PD-T159 and proved at gated-15:51. PD-T156/157 define Λ_c as the maximum over four corners, while 14/15 use λ_n at a nonnode corner. They are equal, but one clause should say so.
- **N8 (E-F3, F4, F6).**
  - `r01-finite.md:22-24` says the limits are "per pair", while the code has one global deadline.
  - The certificate's `source_checkpoint` `3aebb29` predates the D3 sources; identity holds by SHA-256.
  - The wording "interval roots" at `theory17:123` is unclear.
- **N9 (D-F5, measured).** The local constant 237000 is about 10^6 times larger than the measured remainder ratio (≤ 0.447). Effectivity is limited by the non-effective global entry, as the developer states.
- **N10 (F-N2, for AC).** The 5 MB limit holds per topic: this topic has 2.45 MB of generated outputs before this audit. Repository-wide, generated outputs are about 18.0 MB on main and about 20.5 MB at HEAD. AC may want to clarify whether the limit is per topic.
- **N11 (F-N4).** There are byte-identical n2 copies and near-duplicate independent T2–T4 outputs, about 196 KB in total.
- **N12 (F-N9, N10).**
  - Commit trailers omit the Astra checker on the commits that contain its reports.
  - Its independent raw outputs were in ephemeral /tmp.
  - AC's authorization is paraphrased, not quoted.
  - Provisional ID formats deviate from WORKFLOW's `<namespace>?<topic-slug>-<agent>-<n>`: there is a `gated-` sub-slug and `codex-fallback-0N`, and suffixes are reused across namespaces. Map them explicitly at PR preparation.
- **N13 (F-N3, N6–N8, passes recorded for completeness).**
  - T4's ≈1.33×10^14 is everywhere called non-rigorous.
  - T1's literal trivial KILL and its dated finite-scope RETAIN are both disclosed.
  - The general-β series and center-minimality are OPEN everywhere they are relevant.
  - There is no quota-based continuation: every GO cites a new lemma or mechanism with a kill test, every STOP matches its contract, and the rounds were 6/2/1 against a cap of 7.
- **N14.** This audit used `git push` from a clone rather than the GitHub connector that handoff 05 names. The connector's noreply-identity limitation therefore does not apply to the audit commits.

## Residual uncertainty

- The sub-auditors' independent kernels (A, B, D and E) are unreviewed code. They trust `mpmath.iv` enclosures and Python integers. They support but do not replace the developer's exact checkers, whose arithmetic is shared between producer and checker (as disclosed).
- The analytic chain was reconstructed to the level of the stated lemmas. The densest ε–δ limits of codex-04/05 were checked at the level of the accepted PD-T191, not line by line.
- The 2–16 range relies on the inherited n3–7 records, which were not re-audited here.
- The timing of four pre-registrations (F7) and of the D3 note before the final run (F6) cannot be established from git.
- No external literature search was made on whether eventual corner argmax is already known.
- Measured results (grid searches, ratios, replays of screens) are finite float evidence only.

## Measured replays

These were run by the orchestrator in `orchestrator/G/`, from the repository root with `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`. They re-execute the developer's own code, so they are replays of the developer's measurement code, not an independent kernel. Independent kernels appear only in the sub-audits.

| Command | rc / time | Comparison with committed evidence |
|---|---|---|
| `tests_T1.py $G/tests_T1.json` | 0 / 165 s | The raw unsplit producer output (1,342,719 B, sha256 `4d7792e6…`) is exactly equal, leaf by leaf, to the 12 committed `tests_T1_n*.json` profile files and to the non-profile top-level fields of `tests_T1.json`. Timing fields excluded; no tolerance used. This supplies the raw-producer hash that F1 notes is missing. |
| `tests_T2_T3.py T2 $G/tests_T2.json` | 0 / 125 s | 2542 leaves, exactly equal (timing excluded); sha256 `5b5fff90…` |
| `tests_T2_T3.py T3 $G/tests_T3.json` | 0 / 9 s | 2548 leaves, exactly equal; `942197ad…` |
| `tests_T4.py $G/tests_T4.json` | 0 / 39 s | 319 leaves, exactly equal; `8ebab003…` |
| `pairing_screens.py --output $G/pairing_screens.json` | 0 / 46 s | 2540 leaves, exactly equal; `f60c671c…` |

The comparison scripts are `orchestrator/G/compare.py` (relative tolerance 1e-12) and `compare_exact.py` (exact); both report zero mismatches. The full replay JSONs stay in session scratch and are not committed, because they duplicate committed evidence. Their hashes are above and in the support manifest.
