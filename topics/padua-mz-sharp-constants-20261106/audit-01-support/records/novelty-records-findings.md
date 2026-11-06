# Novelty / records audit: padua-mz-sharp-constants-20261106

Auditor role: novelty and records sub-auditor for the Claude substantive audit (Opus 5.5). Branch `codex/padua-mz-sharp-constants-20261106`, HEAD `f8942ec9d489218db52d5a828a6d65952aa0d8bf`. The handoff input SHA is `5110954b07fd834982167780daa8cd22bef13ce1`, and `git diff 5110954..f8942ec` touches only `handoffs/01-work.md` (its status line) and `handoffs/02-audit.md`. No repository file was edited and no Git state was changed.

Scope: novelty gates, candidate records, status and disposition labels, original-target mapping, provenance and storage, and literature coverage. The mathematical correctness of the proofs is outside this scope; the separate math auditors check it.

## Files read

- AGENTS.md (23 lines) and agents/WORKFLOW.md (197 lines), complete.
- **state/IDEAS.md, complete: all 1112 lines (1113 including the trailing line, 291,332 bytes).** I read it in sequential chunks: 1–125, 125–295, 295–520, 520–630, 630–740, 738–838, 838–940 and 940–1113. This covers every heading, ID, alias and summary, and every obstruction and disposition table: the U obstruction table, OBST bivariate-lanczos 01–15, MZ obstruction memory, the audit-01 MZ disposition table, Lattice, Programme-ideas, the PR14 2D table PD-N044–053, PR12 addenda, PR19 scoped obstructions, PR23/PR22, cleanup IDEA-466–471, PR25, the Lanczos frontier and nonproduct tables, and NN-MOP.
- literature/INDEX.md (667 lines): header plus targeted rows LIT-035, LIT-042–065, LIT-293–299, LIT-415–417, LIT-511. Records read: literature/records/mz-widom-1966-screen.md (complete), topics/mz-prior-art-20261101/translation.md (T1–T6, keyword pass) and the comparison index.
- Topic, complete: novelty-gate-S1/S2/S3.md; ideas/*.md (8 files); literature-screen.md; literature/basor-ehrhardt-1999.md; LOG.md; report.md; manuscript-insert.md; gates.md; rounds.md; plan.md; handoffs/01-work.md (to line 140) and 02-audit.md; results/padua-mz-sharp-constants-20261106.md; COLD_STORAGE.md; cold-storage.json.
- Topic, headers/statement/status read: all 14 theory/*.md. Longer reads of S1-model, S1-volterra-model, S1-sharp-one-sided, S2-endpoint-model, S2-qualitative-limit, S2-finite-certificate, S3-corner-operator-limit and S3-carrier-family-ceiling.
- Predecessors: PROOF_STATUS rows PD-T013–027 and PD-T294–300, PD-T376–381. Complete target files m2-sharp-constant-open.md (PD-T020), open-upper-limit.md (PD-T027) and sharp-growth-open.md (PD-T381). PD-T018 file (statement and constants). PD-N104 statement. IDEA-386 full record (ideas-f12.md:133–161 and table row 371).
- tools/cold_storage.py (manifest validator) and templates/COLD_STORAGE.md.

## Search terms

Repo-wide over state/, tracks/, topics/ and literature/, case-insensitive, excluding this topic:

| Term | Files |
|---|---|
| volterra | 0 |
| Hardy inequality/operator | 0 |
| sine integral/Si( | 1, unrelated |
| bessel | 1 (laudadio record, unrelated) |
| J_?0( | 3, all Lebesgue/argmax indices |
| mehler | 0 |
| hard.edge | 0 |
| schl.milch | 0 |
| hankel transform | 0 |
| paley.wiener/plancherel | 0 |
| reflected | 96 (IDEA-386 is the relevant one) |
| log/logarithmic envelope | 9, all Padua Lebesgue/argmax envelopes, unrelated |
| Toeplitz-plus-Hankel | 1 |

Topic-internal searches: provisional-ID inventory, IDEA-470, "operationally rejected", OPEN/pending stale text, and exceed/bias. External: one web search confirming that Lubinsky, PAMS 142 (2014) 3575–3584 exists (search result and abstract only; not read).

## Shortlist (closest existing entries)

| New mechanism | Closest entries |
|---|---|
| S1: parity-reflected log envelope / Volterra | IDEA-066/PD-T018 (constant harmonic envelope, constant 128000), IDEA-071/PD-T020 (deferred: "resume with asymptotic operator/control mechanism"), IDEA-385/PD-T294, IDEA-070/PD-N006, IDEA-065/PD-N005 |
| S2: R=M−H+K completion, uniform 5/3 | **IDEA-386** (deferred; resume condition = "quantitative mass-normalized transition-remainder estimate or a specified distributed limit model"), IDEA-384/PD-N104, IDEA-060–063/073, PD-T013/015/022/027, PD-N002/003 |
| S2: endpoint model, limit, finite certificate | IDEA-386 (second resume branch), PD-T027, IDEA-058 |
| S3: Bessel corner operator B, full signed reduction | **IDEA-470** (deferred; resume "only with the stated full-signed global estimate and exact normalization"), PD-N048, PD-T295/377/379, IDEA-469/471 |
| S3: rational carrier improvement / family ceiling | IDEA-469/PD-T379, IDEA-389/390/394/468 |

## Check 1: mechanism verdicts and separation criteria

- **S1 (IDEA?S1-01).** "Variant" of IDEA-066/071 with a variable-envelope obligation: justified. The separation is falsifiable and survives. The constant envelope f≡1 (harmonic-witness type) has model value (π²/2)/(1/3)=3π²/2≈14.80, against the optimum π⁴/8≈12.18; PD-T018's proved constant is 128000. The record would be stronger if it stated the 3π²/2 comparison (NOTE). No repo predecessor was missed. The Volterra norm ‖V‖=2/π is a classical textbook fact (Halmos, *Hilbert Space Problem Book*, Problem 188) and should be acknowledged as such (MINOR F7).
- **S2-01.** IDEA-386 already contains the mechanism: the positive full Hankel core plus a transition remainder in the mass metric. S2-01 is exactly IDEA-386's stated resume condition. The verdict "variant with difference, completing IDEA-386" is accurate in substance. By registry precedent (e.g. IDEA-262 and IDEA-250 continuations "consolidated under this ID … duplicate as a mechanism"), it should be registered as a **resumed continuation consolidated under IDEA-386**, not as a fresh mechanism IDEA (F4). The separation from PD-N104 (no sign erasure) is genuine and falsifiable.
- **S2-02/03/04.** Endpoint operator, compactness and finite certificate: variants with specified operator, domain and compactness. No repo predecessor; the separation criteria are written down. S2-04 (ideas/S2-certificate.md) is not in IDEA-template form (F5).
- **S3-01.** "Known quantitative variant of IDEA-469": justified. The separation (a strict inequality) is falsifiable but quantitatively tiny (0.029641769 against 0.02962). Consolidating it under IDEA-469 is preferable (F4).
- **S3-02/S3-03.** Full signed reduction and compact Bessel corner operator. novelty-gate-S3.md:59 names IDEA-470 as the closest route, and S3-02 meets IDEA-470's exact resume condition: a full signed estimate in the continuous metric with exact normalization. Neither candidate record (ideas/S3-full-form-reduction.md, ideas/S3-corner-operator.md) nor the theory files names IDEA-470 (F5). No repo predecessor for a Bessel corner kernel was found. Classical hard-edge (Mehler–Heine) kernel limits are a literature predecessor of the kernel lemma in spirit (F7).
- **Carrier family ceiling (PD-T?S3-04).** Handled under S3-01; no new mechanism. A PD-T is appropriate rather than a PD-N, because no candidate claimed that the inherited family reaches 0.0915. The S3-01 candidate record does not mention this outcome (F5).

## Check 2: original targets (exact wording and recommended status)

**PD-T020.** "Determine whether there exists c_* in (0,∞) such that lim (log N)² λ_min(CC,N−1)=c_*, and, if the limit exists, determine c_* explicitly." The new result is limsup ≤ π⁴/8, which is a supporting inequality and not a conjunct of the target. **Recommend OPEN**, as the topic states.

handoffs/01-work.md:60 allowed "a PROVED one-sided sharp bound plus a precise PARTIAL". That conflicts with the WORKFLOW PARTIAL rule; the topic correctly followed WORKFLOW (NOTE).

**PD-T027.** "Determine whether λ_max(G_(N,N−1)) converges, identify its exact limit if it does, and prove a uniform constant B<2 independent of N." This is three explicit conjuncts:

- (a) Convergence: PROVED by S2-05.
- (c) Uniform B: PROVED by S2-01 (B=5/3).
- (b) "Identify its exact limit": an operator-norm characterization Λ_edge, with 1≤Λ_edge≤3/2 and computable brackets ε_N→0, but no closed form and no certified decimal.

The record itself says the supplied decimal is "a numerical lead, not an exact proposed value", which suggests (b) asks for a value. Recommendation:

- If AC accepts a variational or operator characterization with a computable convergent bracket as "identifying the exact limit", PD-T027 is **PROVED**, depending on S2-01/05/06.
- Otherwise it is **PARTIAL**: conjuncts (a) and (c) PROVED under split-off IDs, conjunct (b) OPEN.

This needs an explicit AC decision (F1). Either way, S2-01's "Split from: supporting sharpened conclusion" (theory/S2-uniform-upper.md:6) is wrong, because B<2 is a conjunct of PD-T027's own statement (F3).

**PD-T381.** "Determine whether the two limits lim λ_±(m,m−1)/log m exist, and determine their values if they do … both parity questions and their agreement … remain part of the target." Existence (both signs, both parities) and agreement are PROVED by S3-03. The values are characterized as inf/sup σ(B), with a computable norm tail 120/K, but no certified decimal. The only computed decimal (the K128 proxy, −0.1336) disagrees with every finite measurement by 31%, and the error bound 4300/log m is non-informative at accessible m. That strengthens the conservative reading. Recommend **PARTIAL** (existence and agreement PROVED under split-off IDs, values OPEN), unless AC rules that the spectral characterization counts as "values" (then PROVED). The original C3 wording ("determine lim … or the best proved bounds") is satisfied either way (F1).

## Check 3: status and disposition labels

- PROVED/OPEN labels in the theory files are internally consistent with the split rules. No PARTIAL is misused, and supporting lemmas are not aggregated.
- K2 and K4 KILL_MODEL outcomes were **correctly not turned into PD-N refutations**: ideas/S1.md:42–50, gates.md:35 and 74, theory/S1-model.md:143–152.
- "Operationally rejected" (ideas/S1.md:42, theory/S1-model.md:143) is not a WORKFLOW disposition (F2).
- No MEASURED durable record exists for the finite numerical claims (F6).
- One candidate label does not follow the provisional-ID format (F8). The S1-model ID status is ambiguous (F9).

## Check 4: provenance and storage

- fetched-paths.json: 84/84 Git blobs match `2143ad6`, checked here with `git rev-parse`.
- input-snapshot.json: 79/79 blob and SHA-256 entries match.
- evidence-manifest.json: 63/63 bytes and SHA-256 match; no unlisted code, JSON or SVG files. The local `code/__pycache__` is gitignored and untracked.
- File sizes: every committed generated file is under 16 KiB. The largest are input-snapshot.json (16,342 bytes, 42 bytes under the limit) and figures/cc-extrapolation.svg (15,720 bytes); the largest evidence file is 8,915 bytes.
- Repository generated-type total: 6.28 MB at HEAD against 6.05 MB at base, so above the ordinary 5 MB cap. It relies on AC's temporary 10 MB allowance, which is cited from an unmerged branch blob (b930ba8) not available locally (F10, NOTE).
- cold-storage.json is not in padua-cold-storage-v1 format: `tools/cold_storage.py verify` rejects it. Its locators are ephemeral /tmp paths, and one entry lacks source_commit (F10).

## Check 5: literature

- The topic screen (literature-screen.md:16) says WW1966 is unread and that "linked record absent from selected snapshot". The repository record literature/records/mz-widom-1966-screen.md already contains a 2026-11-01 extraction-level reading of LIT-053/054 with verdict RELATED, DIFFERENT SETTING (exponentially small moment-Hankel eigenvalues). It supports the topic's conflation warning and should be cited (F7).
- Possible classical coverage not screened:
  - Lubinsky, "On sharp constants in Marcinkiewicz–Zygmund and Plancherel–Pólya inequalities", PAMS 142 (2014). Its abstract says the sharp MZ constants equal sharp Plancherel–Pólya constants for entire functions; the scaling-limit mechanism is closely analogous to the S2 endpoint model.
  - Lubinsky's later Airy (soft-edge) and "entire cousins" MZ papers.
  - Mehler–Heine and hard-edge Bessel universality (Kuijlaars–Vanlessen, Lubinsky), for the S3 kernel lemma.
  - Halmos for the Volterra norm.
  - Sharp L²-norm asymptotics of Lagrange interpolation at Chebyshev–Lobatto nodes. By translation.md T1, PD-T020 is equivalent to the sharp ‖L_N‖ in nodal ℓ²(w)→L² on Π_(N−1).

  Lubinsky 2014 likely treats p≠2 in the bulk; at p=2 the Gauss/Plancherel–Pólya constants are 1. So it probably does not give these CC constants, but this is unverified. No source read here gives π⁴/8, Λ_edge or B; coverage is search-level only.

## Findings

**F1 — MAJOR (decision for AC; handoff asks for it).** Original-target mapping for PD-T027 and PD-T381 is not decided. report.md:13 defers it to the audit. The value conjuncts of both targets are met only by operator characterizations, with no closed form or certified decimal. Recommend PARTIAL under the conservative reading, or PROVED only if AC explicitly accepts the characterization as "identify/determine the value". Record the choice in each target's History; do not silently narrow the wording. PD-T020 remains OPEN (agreed).

**F2 — MAJOR.** The S1 equality-model disposition "operationally rejected" (ideas/S1.md:42; theory/S1-model.md:143) is not a WORKFLOW disposition. It must not be registered as `REJECTED: failed`, because the K2 evidence does not show failure.

- The fitted intercept 13.061 lies **above** the proved bound limsup ≤ π⁴/8 = 12.176. So the K1 fit cannot be the true limit if the S1-02 theorem holds.
- The finite data rise slowly. From evidence/S4-essential-cc.json, (log N)²λ_min goes 4.33 (N=100) → 6.14 (N=1600) → 7.76 (N=102401), all below π⁴/8 and increasing. That makes a ~5% extrapolation test non-diagnostic.
- theory/S1-model.md:150 notes the compatibility, but report.md, manuscript-insert.md and results.md do not say that the fit lies above the proved bound.
- The matching lower-bound/transfer route (handoff01 S1 4(b), the IMS localization; the hard worker was interrupted, LOG.md:62) has no separate record.

Recommend disposition `deferred` (stopped by the K2 operational rule; resume on AC instruction or with a proved finite-to-model lower bound), or `abandoned` with this reason. Disclose the fit-above-bound inconsistency once in the report, and raise with AC whether K2 should govern given that inconsistency.

**F3 — MINOR.** theory/S2-uniform-upper.md:6 says "Split from: supporting sharpened conclusion for PD-T027". The uniform B<2 is a conjunct of PD-T027's own statement, so this should read "Split from: PD-T027 uniform-gap conjunct". This matters for F1's PARTIAL mapping and for ID_CROSSWALK.

**F4 — MINOR (registry obligation at PR preparation).** Deferred IDEA records that the new work resumes must be updated, and the new candidates consolidated rather than duplicated:

- IDEA-386: resumed by S2-01, and the "specified distributed limit model" branch by S2-02–06. The signed 2D analogue stays deferred.
- IDEA-071 (sharp endpoint limit): resumed by S1-01. IDEA-054: sharp-constant clause.
- IDEA-469: S3-01/S3-04. IDEA-470: S3-02/S3-03 meet its resume condition.

Also update MZ obstruction memory state/IDEAS.md:406 ("Endpoint eta rate needs an upper gap"; the escape is achieved by S2-01/S2-02), the PD-T027 note in state/IDEAS.md:942/938, and open-upper-limit.md "gaps decay like N^−1". Without these, the registry would show deferred IDEA-386/470 alongside new IDEAs doing the same work.

**F5 — MINOR.** Candidate records are incomplete against templates/IDEA.md:

- ideas/S3-full-form-reduction.md and ideas/S3-corner-operator.md lack the fields for closest entries read, verdict, separation and kill criterion, and do not name IDEA-470.
- ideas/S2-certificate.md is not in template form.
- ideas/S3-carrier-variant.md does not record the S3-04 family-ceiling outcome.
- The gate content exists (novelty-gate-S3.md:53–67, 78–103), so the fix is linking and recording.

**F6 — MAJOR.** There is no durable MEASURED theory record (PD-T?…) for the distinct measured claims reported in report.md, results.md and manuscript-insert.md. These are the K1 intercepts, the K3 upper-fit limit 1.0044369723 and J512 proxy, the 16 Padua minima and slopes ≈ −0.092, the K128 B proxies, and the transfer diagnostic. They live only in attempts/S4*.md, gates.md and the evidence files. WORKFLOW requires that "a distinct measured claim gets its own durable registered home"; the precedents are PD-T300 and PD-T380. Add one or two MEASURED records with exact scope before PR.

**F7 — MINOR.** Literature hygiene:

- literature-screen.md:16 should cite the existing LIT-053/054 record reading rather than calling the record absent.
- Acknowledge the Volterra norm 2/π as classical (Halmos) in theory/S1-volterra-model.md.
- Screen, at least at abstract level, Lubinsky PAMS 2014 (sharp MZ = Plancherel–Pólya constants) and the related edge-scaling MZ papers, Mehler–Heine and hard-edge Bessel kernels, and sharp L² Lagrange-interpolation norms at Chebyshev–Lobatto nodes, **before the manuscript-insert statements are adopted**.
- No priority claim is made, so this does not block the statuses.

**F8 — MINOR.** ideas/S3-full-form-reduction.md:1 uses "IDEA-S3-02". That looks like a final ID; it should be `IDEA?mz-sharp-codex-S3-02`. Also `PD-T?mz-sharp-codex-S3-kernel` is non-numeric; acceptable, but map it explicitly at PR.

**F9 — MINOR.** theory/S1-model.md:7 says "ID kind: PD-T" for a CONDITIONAL prediction, but assigns no ID. Either give it a provisional PD-T ID as a CONDITIONAL record of the stopped route, or relabel it as a prediction/attempt record.

**F10 — MINOR.** cold-storage.json does not follow padua-cold-storage-v1 or templates/COLD_STORAGE.md:

- `tools/cold_storage.py verify` fails with "expected a padua-cold-storage-v1 manifest".
- Its /tmp locators are unretrievable after the session.
- The second entry lacks source_commit.
- No claim depends on these files, so either declare them non-retained regenerable provenance or convert them when AC names storage.

The NOTE parts:

- input-snapshot.json is 42 bytes under 16 KiB.
- The repository is at 6.28 MB under the AC 10 MB allowance, which is cited from an unmerged branch blob; verify it at readiness.

**F11 — MINOR (stale text).**

- theory/S2-qualitative-limit.md:7, 21, 58 still say the quantitative error is "OPEN in S2-endpoint-model.md", although S2-06 proves it.
- rounds.md:3 says "Independent K0 replay is pending" (done).
- Theory status lines say "independent audit pending/required"; update after the audit.
- theory/S2-endpoint-model.md is a definition/prediction record marked "PROVED via linked follow-on files". Its status duplicates S2-05/S2-06 claims. Recommend it carry only the definition of Λ_edge, with status pointers, so the same proved claim does not appear under two IDs.

**F12 — NOTE.**

- The handoff's PARTIAL allowance for PD-T020 (handoffs/01-work.md:60, 79) conflicts with WORKFLOW; the topic correctly did not use it.
- The S4 structured solver had no IDEA record; this is acceptable as a routine implementation (LOG.md:37).
- gates.md table rows still showing PENDING are acceptable under its append-only rule.

## Residual uncertainty

Literature coverage is search-level only, so I cannot exclude that a classical edge-scaling MZ result gives Λ_edge or B. I did not check the mathematics. The F1 classification is an interpretive call reserved to AC.
