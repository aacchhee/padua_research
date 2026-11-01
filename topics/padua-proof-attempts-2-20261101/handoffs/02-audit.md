# Handoff 02 — padua-proof-attempts-2-20261101 — independent mathematical audit

- Status: open
- Previous handoff: 01-work.md
- Next agent / model / effort: Claude, Opus 5.5, xhigh
- Role: independent auditor / audit orchestrator
- Branch: codex/padua-proof-attempts-2-20261101
- Input head SHA: `4265bb94f987ce77d89cd5e15a8c435cbd1411d0` (final development outputs; this handoff is published in the following commit)
- Main / base: `28aaa20861d08074b77efc74eaef75cdcb36234d`; original Part1 base `a09d910ae7d5526b1e216066421a0bee7fc20da4`
- Stage: AUDIT
- Written by / date: Codex, gpt-6.1-sol medium requested (root serving-model metadata unexposed) · 2026-11-01

## Task

Audit the exact development candidate above, independently of the Codex supplementary checks. The required Claude audit has NOT been performed. Use Opus 5.5 xhigh for the mathematics. Read the rules at the branch head, record their full SHA and actual model/effort, and verify that the only change after the scientific input is the required handoff publication. Reconstruct proofs, challenge quantifiers and edge cases, inspect computer-proof reductions and exact predicates, and execute independently selected checks with your own outputs. Do not count a receipt read as an actual rerun. Do not silently fix a developer proof and then approve that fix yourself.

All five ordered targets are at their recorded done/deadline stops. This step audits their final claims; it does not restart degree-eight development or pursue stronger open targets. The developer report is `report.md` in this topic. Keep PR12 draft while findings or this audit are pending: https://github.com/aacchhee/padua_research/pull/12 .

## Read first and complete scope

Paths below are repository-relative. Read `AGENTS.md`, `agents/WORKFLOW.md`, `agents/claude/CLAUDE_ROLES.md`, `templates/HANDOFF.md` and the accepted Part1 `audit-01.md` as a record-format reference. Rules were last adopted by development at `d8b878b348a94575e7753e5a756d969d41d5bca8`; outside-topic content at the candidate equals main28aaa20. The user text and authority resolution are recorded in LOG/inputs-review. User's narrower topic-only/no-RESULTS/local-ID instructions override generic integration/results requirements.

Under `topics/padua-proof-attempts-2-20261101/`, read `LOG.md`, `plan.md`, `inputs-review.md`, `report.md`, `evidence-manifest.json`, `proposed-record-changes.md`, every target attempt, all durable `theory/*.md`, `independent-checks.md`, every case-specific independent-check/execution receipt, and the schemas/code/evidence each proof relies on. The index retains dated intermediate checkpoints; its final sections and report give current scope. Supporting results and failed/deferred routes are audit scope too, not only the headline theorems.

Read full `state/IDEAS.md` and applicable obstruction/disposition tables, `literature/INDEX.md`, the logged gates/shortlists, and the relevant full pinned theory/source records. Pins:

- Original programme: `9bd14a6d2c4da69139a10107d8a787f2be0c5c9e`; final programme aliases: `b46b4dea18ce2c933489a211b0b6819dfd32ca70`.
- Part1 original: `a09d910ae7d5526b1e216066421a0bee7fc20da4`; audit: `95279b833bca5967fcf47c1b71a56ff622185b4e`; response: `7b8884a2f98518784ff3698dd2f3f9c49c9cdd62`; final branch: `752ba068589683afe644b505d673f8da1529cbf0`; main squash: `806cc7b4509fd93bae652f9545d32d95529f8281`.
- Lanczos input: `a2dd845b8a231e1b00733e1361e2a9ad3bad222f`, especially local theory304(a). Current B3/B1 context is separately pinned at main28aaa20 in the manifest.

The user-required literal dependency phrase `PD-T?proof-attempts-codex-0N (audit pending)` is historical: Part1 audit accepted, dispositions completed, PR9 merged. Part2 audit is pending. Verify this qualification rather than stripping the required phrase. Literature dependencies remain explicit; no broad novelty claim is intended.

## Claimed results and boundaries to test

- **A2, PROVED:** separate01 lower bound,02 two-sided leading estimate,03 requested b coefficient with absolute remainder68 for all n≥2,04 supporting corner/square comparison. Check all-n analytic bounds separately from finite exact regression and measured sanity fits. KL2021 Thm2.1 is a global upper bound only; borrowed discretisation locators are Lemmas3.5(3.20)/3.6(3.29), with full-paper read recorded. A3 is OPEN, bounded note only.
- **A5, PARTIAL by degree:** count/global pairs06/07,10/11,16/17,41/42,51/52 certify n3–7. Interior/open-edge/non-node-corner/closed counts are respectively7/6/2/15,13/12/2/27,14/9/2/25,25/14/2/41,33/15/2/50. Globals are attained only at the two non-node corners. Audit every consistent-mask/discard disposition, node/crease/crossing/boundary treatment and non-strict plateau exclusion, not just listed stationary roots. Independent formal verifiers import no producer/search code. N8 supporting64 proves at least44 distinct strict INTERIOR maxima, using committed standalone field/root witnesses. Exact interior65, closed count61 and global62 are OPEN: both full interior checks missed the deadline without atomic success; boundary retries exit124/no final artifact. No join/global/repack/READY was run. Never infer completeness from progress152000/153520 or150000/153520. Primary arXiv2605.23299v1 Table3 comparisons are candidate corrections23/39→25/41 at n6 and27/42→33/50 at n7; n8 only interior38 is contradicted by≥44, not its total56. No author contact.
- **A4(a), PROVED at stated central scope:**70 all-four-edge identity,71 exact complementary-grid gaps including essential2/[n(n+1)] singular correction,72 common central-grid limit,73 positive integral/rational alternating series for g,74 uniform phase localization,75 local upper bound retaining sign flips/cusps/collisions/endpoints,76 joint defect limit,77 central-edge envelope expansion `R_cen=Lambda_c−g+o(1)` on both vertical edges with `|t−pi/2|<=pi/(n+1)`, both parities. Strict certified bound `0.548504986190<g<0.548525055355`. Check uniformity, nearest-grid points outside the cell, ties and endpoint limits. Historical R_search/global runner-up identification and full-square A4(b)/(c) remain OPEN; only route notes.
- **B3, scoped REFUTATION:** negative01 proves failure of the specified S(alpha) count in genuine positive sections at fixedn1,N3,M4,p1/10, ALL0<t<=1e−6. Delta>0→0, computed boundary gap≥sqrt(delta)/10; n_box1/2 versus joint count1 for actual fixed commuting reference H(0) within half-gap. Quantifiers cover everyalpha>1/2 andfiniteC(1,p); condition(ii) fails while(i)holds. Positive80 gives a parent residual bound; negative02 rejects only the literal common shrinking two-dimensional cluster route. Check weighted similarity, uniform positive pivots, whole-interval signs, both monomial orders via fixed permutation and reference membership. No arbitrary-rotation surrogate; no refutation of other F/all-n/reference-existence questions.
- **B1, PROVED for precise class:**90–92 exterior real parallel diagonal poles ell_j=x+y−a_j,a_j>2, EVERY fixed positive Pi_(T+1)-determining sample and fixedfiniteT≥3. Top-form leakage detection is an isomorphism for all outward offsets; generic full rank is proved through a coalescent projective witness and NONZERO POLE-ONLY polynomial for EACH fixed data set. Check lower-block transport, rank equality and genericity in offsets without replacing it by generic nodes/weights.93 covers the literal source EVENm≥4 Ldiag taper, both fixed orders, with only finitely many positive parameter exceptions via a nonzero finite real exponential polynomial/Rolle induction. No individual stored taper parameter, exception location, other pole class or stability is certified. These are structural proofs; no mathematical software run or sampled-rank premise was used.

## Reproducible verification

Use a clean checkout of the exact candidate for proof/code identities; preserve the publication handoffs. Python at development was3.12.14, SymPy1.14.0, python-flint0.9.0/FLINT3.6.0 (available locally under `/tmp/padua2-deps`). Reinstall if needed and report actual versions. Use `PYTHONDONTWRITEBYTECODE=1` and `python -B`. The manifest generator is mechanical provenance, not a scientific verifier; it reads INDEX bytes, so do not regenerate it over unfinished audit files and call that candidate validation. Manifest excludes itself, handoffs and caches; handoffs are separately Git-pinned. Candidate has294inputs/378outputs,198generated files totaling4,652,134bytes, largest637163; preserve the5MB/1MB limits.

Read all case receipts for literal executed commands, source guards, accepted pairs, controls and precise allowed timing differences. Rerun into NEW auditor-owned paths under `audit-support/claude-audit-01/` (create this inside the topic), never overwrite developer/independent evidence. Useful command forms from the repository root follow; these are PLANNED audit commands, not new claimed executions:

```sh
git diff --name-status 4265bb94f987ce77d89cd5e15a8c435cbd1411d0..HEAD
git show 4265bb94f987ce77d89cd5e15a8c435cbd1411d0:topics/padua-proof-attempts-2-20261101/evidence-manifest.json
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a2_exact_check.py
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/a5_checker_n7.py topics/padua-proof-attempts-2-20261101/outputs/a5_n7_certificate.json.xz --global-file topics/padua-proof-attempts-2-20261101/outputs/a5_n7_global.json --output topics/padua-proof-attempts-2-20261101/audit-support/claude-audit-01/n7-checker.json
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a4reg_exact_check.py --source-sha256 13e8c524c4c21701bdee2a009cda2245d8f289d6a6cca0dba19afec1842f872e
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a4reg_complementary_check.py --source-sha256 978bf8e00e09f4671d36d9de0e3c8dae531d34491ed7cdec1741aa6542032fca
PYTHONDONTWRITEBYTECODE=1 python -B topics/padua-proof-attempts-2-20261101/code/a4g_series.py --source-sha256 510955136172a93206861f3a8252aa36460daa8c7965770d0fd6354209104ab9
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=/tmp/padua2-deps python -B topics/padua-proof-attempts-2-20261101/code/b3_four_atom_exact.py --expect-source-sha256 b33647b8cff4c1b23e9b9089f9822fe307e1f8980786eec043b8bfc9ad3f9b7b --output topics/padua-proof-attempts-2-20261101/audit-support/claude-audit-01/b3-exact.json
```

For n3–6, controls and standalone n8 witnesses, use their corresponding receipts and final source schemas; select adequate time budgets (n7 full replay took about32minutes). Do not restart unfinished n8 completeness. Verify manifest rows independently against `git show COMMIT:PATH` / candidate paths, Git blob IDs, SHA256 and byte counts; inspect all ten old→new proposals against their exact pins. Check post-stop source/proof freezes and actual different-agent outputs. Repeated full searches are not necessary substitutes for inspection of the separate formal checker. Record actual audit coverage and any unexecuted commands honestly.

## Scope limits

All NEW authored writes stay inside this topic. Local IDs only; **no range**, no final allocation or shared registry/crosswalk/RESULTS.md/root-results/other-topic/.github edits. Literal integration proposals only. The concrete user-requested intended Windows entry is in LOG Runs needed; no bridge/write was available or claimed. Imported root results files remain unchanged. Do not upload third-party paper text, contact authors, delete history, force-push, tag, merge PRs or write main. Only AC merges. Existing handoff instruction bodies are immutable; only their status line may later change. Only the audit orchestrator mutates Git, allocates the next handoff and updates PR metadata.

## Acceptance and outputs

Write `audit-01.md` under this topic with exact audited SHA/hashes, full read/novelty scope, actual model/effort, independently reconstructed arguments, executed commands/output identities, severity-ranked findings/dispositions and residual limitations. Supporting evidence goes in the auditor-owned support directory and stays within the generated-output budget; do not split files/delete prior artifacts to evade limits. If evidence cannot be committed, identify the concrete limitation without pretending the proof audit passed.

Update LOG/PR12 with the audit outcome: findings return Stage WORK and require a Codex response; accepted coverage permits Stage PR only after applicable prerequisites and user scope limits are addressed. Never self-approve a changed proof or infer PR readiness solely from Codex supplementary checks. Preserve every unresolved item and disagreement for AC. No scientific integration/shared edit is authorized in this audit step.

Commit audit outputs FIRST with the required author/trailers. In a FOLLOWING commit change only this handoff's status to `done in AUDIT_OUTPUT_SHA` and add03-response.md (Codex for findings) or the precise next PR-preparation handoff if accepted; publish exactly one open successor. Push before replying. Give AC a concise self-contained audit result and exact next prompt. The complete instruction lives here; requested launch prompt is:

`Claude (Opus 5.5 xhigh): Audit codex/padua-proof-attempts-2-20261101.`
