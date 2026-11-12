# Audit04 — protocol / novelty scope report (independent subagent)

- Auditor: Claude, Opus 5.5 (`claude-opus-5-5`), xhigh (novelty/adversarial-protocol scope). Developer audited: Codex.
- Rules AGENTS/WORKFLOW/CLAUDE_ROLES read at `dafb8c8` (unchanged since `9042e1c`). Audited candidate `e7c9900`; `dafb8c8` adds only handoff 16 status + handoff 17. Range `9042e1c..e7c9900` (47 commits).
- No git state change, no repository edit. Read-only commands only (git log/diff/ls-tree, grep, `python3 -I -B code/artifact_manifest.py --verify` → PASS, 310 artifacts, 1,872,829 B).

## Coverage read

Rules files and templates; **complete `state/IDEAS.md`** (every heading/alias/summary and every obstruction/disposition table, in bounded reads); SHA `d7ec3aa6…` and the 34 table runs recomputed. Relevant INDEX rows (LIT-004/005/303/322/323/336/381/382/385/386/391/413) plus searches for compression/subsampling/design/Leja/Lyness/Lebesgue-point terms. Handoffs 08–17; LOG 461–895; rounds; usable campaign/gate; continuation results; pruning brief/gate/next-questions/protocol/results/summary/manifest; gate parts of usable1–3 and U1 continuation; results file; cold-storage records; manifest envelope; interim-audit verdict; headers/status of all new theory files. Not read: full review sub-reports and line-by-line proofs (other auditors' scope).

## Findings

### MAJOR

**N-M1 — Pruning gate omits the closest literature predecessors (same class as audit-03 E5).**
- `pruning-gate.md:42` reads INDEX rows LIT005,022,104–110,131–134,175–183,336–346,382–383 only. LIT-385 (Christoffel sampling, Cohen–Migliorati; O(N)-sample subsampling via Kadison–Singer/MSS; Bartel–Schäfer–Ullrich) and LIT-386 (Piazzon–Sommariva–Vianello Carathéodory–Tchakaloff compression) are not read. The comparison table `pruning-gate.md:84–96` has no row for measure compression (LIT-005 was read but is not compared) or for frame subsampling/sparsification.
- Yet `handoffs/16-pruning-campaign.md:23,45` calls spectral sparsification an established method, and the immediately preceding `usable-gate.md:131` already lists LIT005/385/386. The `rg` regex at `pruning-gate.md:49` (`backward.elimin|row.delet|fedorov|maxvol|sparsif|prun`) cannot hit LIT-385/386. These sources describe "start from a larger set and remove points while keeping least squares stable, down to O(N) or ≤dim Π_2n points". That is the campaign's question.
- No novelty is claimed, so no status is affected. The gate record, however, lacks its required closest entries and differences. Suggested distinctions for the developer to verify: CATCH keeps Π_2n moments with up to dim Π_2n nodes, which is binom(35,3)=6545 > 1377 at n16, so it cannot compress the parity grid, and exactness is impossible at M≈1.2N. BSS-type results control L2 frame bounds, not sup-norm amplification or integer-budget risk. P1–P5's greedy A/D/L/pair rules are not those algorithms, and their finite failures do not contradict them.
- Also record as a coverage limit that classical optimal-design sources behind PRUNE-A/D have no INDEX record (Fedorov exchange, Kiefer–Wolfowitz, Bos D-optimal/Fekete). `pruning-protocol.md:32–33` labels the rules "known backward design / D-optimal" without a source.
- Fix: a dated gate addendum, propagated to the protocol candidate rows. Not auditor-fixable (it adds substantive comparisons).

**N-M2 — Candidate/negative records and provisional IDs (records; returned because outside auditor-fix limits; class of audit-03 E6).**
- (a) `theory/pruning-p5-pair-boundary.md:1–3` does not follow THEORY.md. It has no provisional ID, ID kind, aliases or split lines, no Attempted mechanism/Parameter range, no Depends on and no History. Its scoped MEASURED negative needs a PD-N provisional ID.
- (b) The gate-stage candidates PRUNE-H (deferred) and PRUNE-FORCE-N (abandoned) at `pruning-gate.md:116–117` have no provisional IDEA records. The executed candidates exist only as protocol table rows or paragraphs, without the IDEA template fields (verdict, prewritten kill, discriminability, disposition reason, canonical ID): prune-A/D/random/lex (`pruning-protocol.md:32–35`), -L (`:188`), -Pareto (`:304`) and -pair (`:498`). There is also no consolidated pruning candidate-disposition table (usable1–3 have one). WORKFLOW:85 requires a provisional template record for every candidate.
- (c) `pruning-next-questions.md:158` still reads "equal-order comparison retained" (prune-next-02), but the campaign stopped at 5/15. Handoff 16 says "stop with evidence when no useful next question remains". Record the deferral, the reason it was not run and the resume condition. next-01 and next-03 became P3 and P5.
- (d) The provisional ID format `<ns>?<slug>-<agent>-<n>` (WORKFLOW:159) is violated by 26 new IDs that omit the agent component. Examples: `PD-T?padua-3d-20261106-usable-U1-{noise,OLS,recipe,measurements}`, `-pruning-{exact12,exact16,target}`, `-prune-P1..P4`, `-u1c-decisions`, `IDEA?…-prune-*` (10), `IDEA?…-U1c-01/02` and `IDEA?…-usable-U1-C1/C2`. Re-key them to `…-codex-…`, keeping the old strings as aliases, by PR preparation at the latest.

**N-M3 — Repository-wide generated-output budget (needs AC decision before PR).**
- WORKFLOW:135 says "Committed generated outputs of the whole repository together stay well below 5 MB". Measured bytes of json/txt/out/gz/stdout/csv files (an upper-bound class):

| Scope | Bytes |
|---|---:|
| main `f70a260` | 6,996,179 |
| `9042e1c` | 7,454,280 |
| `e7c9900` | 8,331,932 |
| this topic | 1,335,753 (largest topic) |
| change since `9042e1c` | +877,652 |
| `evidence/` | 1,029,420 (197 files) |
| rerun/copy receipts | pruning-review 94,517; interim-audit-01 83,777; continuation-review 64,098 |

- No topic record checks the repository total. `COLD_STORAGE.md:40` checks only the per-file threshold. The main branch already exceeds the limit; this PR adds about 19%. WORKFLOW:137 asks for reruns, copies and large manifests to move to cold storage. AC must decide (accept, prune, or move to `Downloads\padua\cold_storage\padua-3d-20261106\`).
- The per-file limit is met: the largest file is `evidence/pdpr-pilot.json` at 16,349 B and the manifest is 16,341 B, both under 16,384.

### MINOR — eligible auditor fixes (wording, links, stale process text, recording documented decisions with links)

- **F1.** `results/padua-3d-20261106.md:319` is a stale next step that contradicts open handoff 17.
  - Replace `` `Codex (gpt-6-astra, high): Continue codex/padua-3d-20261106.` ``
  - with ``Formal combined audit04 per [handoff 17](../topics/padua-3d-20261106/handoffs/17-pruning-audit.md): `Claude (Opus 5.5, xhigh): Continue codex/padua-3d-20261106.` ``
  - Apply this as the audit-session orchestrator holding the open handoff; handoff 17 says "Update LOG/results/PR".
- **F2.** `rounds.md:19–21` has a stale ledger ("Remaining8/7/16rounds persist"). Insert after line 21:
  > Dated 2026-11-08 auditor pointer (no count change): the table above is the first-batch state. The AC seven-round continuation completed 2/4/1 additional rounds (cumulative U1=4/10, U2=7/10, U3=5/20); see [continuation results](continuation-results.md). The separate pruning campaign completed 5/15; see [pruning results](pruning-results.md) and [summary](pruning-summary.md).
- **F3.** LOG handoff links (WORKFLOW:61, "The log links each handoff with one line"); handoffs 15 and 17 are unlinked.
  - In `LOG.md:842`, replace `opening15 for the formal audit` with `opening [handoff15](handoffs/15-combined-audit.md) for the formal audit`.
  - After `LOG.md:895`, add: `- [Handoff16](handoffs/16-pruning-campaign.md) closed done in e7c9900; [handoff17](handoffs/17-pruning-audit.md) opened in dafb8c8 for formal Claude audit04.`
- **F4.** `COLD_STORAGE.md:124` (end of file) has no inventory pointer for the continuation and pruning batches. Append:
  > ## Continuation and pruning batches — 2026-11-07 (pointer added 2026-11-08)
  > No cold-storage delivery. U1/U2/U3 continuation and pruning P1–P5 raw outputs remain local regenerate-only; their paths, bytes and SHA-256 are in the `raw`/`raw_inventory`/`raw_details` fields of `evidence/u1c-*.json`, `evidence/u2c-*.json`, `evidence/u3c-nonunique-quality.json` and `evidence/pdpr-*.json`, with commands in the stream protocols/results. Essential payloads `evidence/pdpr-pruned12-nodes.json` and `evidence/pdpr-pruned16-nodes.json` are committed; see [pruning-artifacts.md](pruning-artifacts.md).
  - `cold-storage.json` has no matching key. Adding one is data, so that part is left to the developer.
- **F5.** Attribution of Claude-originated leads (recording documented facts with links):
  - `usable-campaign.md:26`: replace `the half-shift cubic example has sampledLambda9.79,` with `the half-shift cubic example (lead from [Claude audit-03](audit-03.md), handoff08 item 7) has sampled Lambda 9.79,`
  - `usable3.md:28`: replace `The disclosed cubic lead is the existing M40,` with `The disclosed cubic lead (from [Claude audit-03](audit-03.md), handoff08 item 7) is the existing M40,`
  - `report-round08.md:50`: replace `At n2, the old generators` with `At n2 (Padua-type property first reported in [Claude audit-03](audit-03.md) item 7), the old generators`
  - `theory/r08-lattice-complement.md:93`: replace `listed in [T2](t2-finite-survivors.md), not new sets.` with `listed in [T2](t2-finite-survivors.md), not new sets; their Padua-type cubature property was first reported in [Claude audit-03](../audit-03.md) item 7.`
  - Good existing attribution: `theory/t8-r08-cubic-classification.md:107–108` ("Audit03 supplied the cubic lead").
- **F6.** Formatting: missing word spaces throughout recent LOG/results text. Example: `results/padua-3d-20261106.md:8`, replace `**5/15authorized pruning rounds completed,10unused.**` with `**5/15 authorized pruning rounds completed, 10 unused.**`. The same defect runs through LOG 845–895 and the summaries; it is formatting only.

### NOTE

1. **Chronology** (creating commits, then receipt UTC run times; local commit time = UTC+1).
   - Usable: campaign 08:05 → gate 08:07 → protocols 08:12/08:14 → first result 08:22. Pruning: brief 10:04 → gate 10:08:31 → protocol 10:09:12 (41 s later; generation-after-gate rests on worker attestation) → results 10:18.
   - Receipt run times all follow their protocols: P1 09:14:47 after 09:09:12; P2 09:26:43 after the seed correction at 09:26:25; P3 09:40:57 after 09:37:10; P4 09:54:07 after 09:52:00; P5 10:13:00 after 10:11:33.
   - U2/U3 continuation receipts have no run timestamps (recommend recording UTC). The pruned12 check (09:48 UTC) preceded publication of `pruning-certificate.md` (09:52 UTC); no rule is broken and the proof is unaffected.
   - Protocols were edited in place only for stale status lines and the disclosed pre-run seed correction.
2. **IDEAS reading attestations.** Both gates' 34-run table lists and the registry SHA match the current file exactly. The reading itself is attested, not verifiable.
3. **U2 predecessors.** LIT-336 (Van Barel–Humet–Sorber greedy Lebesgue minimisation/Gauss–Newton), LIT-382 (approximate Fekete / discrete Leja) and the inherited localdet are identified, and the mechanism is labelled known (`usable2.md:45–77`).
   - The classical direct Lebesgue-point optimisation literature is absent from INDEX: Chen–Babuška 1995; Briani–Sommariva–Vianello 2012; Rapetti–Sommariva–Vianello 2012; Heinrichs 2005. Record these as a literature lead or coverage limit at PR preparation.
   - U1 identifies DMVX 2009 (LIT-322) and LIT-005/385/386/391 (`usable1.md:67–68`).
   - Lattice minima cite Cools–Lyness K-optimal tables (`literature-T10.md:5`).
   - No new-mechanism, novelty or priority claim appears anywhere in the new records.
4. **AC authority.** Verbatim AC texts: `usable-campaign.md:5`, `handoffs/12-interim-audit.md:15–17`, `LOG.md:806`, `handoffs/16…:13–14` (other LOG entries paraphrase). Counters: usable 2/3/4 plus continuation 2/4/1 = cumulative 4/7/5, within 10/10/20 under either reading of "up to 7"; pruning 5/15. Repairs, codec work, publication correction and certificate delivery all count 0. Each route stops at its registered gate; the only gap is N-M2(c).
5. **Handoffs.** Supersessions 09→10, 11→12, 13→14 and 15→16 use `superseded by NN: reason`, changed status-only in the commit opening the next handoff (d99e418, 73e94ad, a68f85b, c7afc44), with each AC change in the LOG. Closures are `done in <output sha>`. Exactly one open handoff (17) at every boundary; bodies unaltered.
6. **Status discipline.** The computer-assisted PROVED claims each have a written reduction, exact arithmetic, a committed checker and evidence, a separately executed checker, and stated trusted dependencies: the 455-node set, pruned12/16 rank, T8 old-nine, U3 folded/sparse/mixed.
   - Quality is split out as MEASURED. The pruning target is OPEN, not PARTIAL (`pruning-theory.md:11–25`).
   - E4 labels say "proposed under response03 E4 for AC decision" (`t10-log3-corollary.md:11`, `r08-lattice-minima.md:37`) and are not silently settled. PD-N statuses are appropriate (MEASURED for frozen-rule kills, PROVED for analytic obstructions).
7. **Hygiene.** Shared-registry diff is empty (state, PROOF_STATUS, ID_CROSSWALK, literature, RESULTS, agents, templates, tools, .github); the only out-of-topic change is the topic's results file, written only by root. 47/47 commits carry Agent/Model trailers with allowed prefixes; models match the handoffs (Sol high for code exceeds the table's Sol medium; the Astra high coordinator follows handoff-08 precedent).
8. **Interim Codex audit.** It is correctly framed as "not formal Claude audit04 or readiness approval" (`interim-audit-01.md:10–11`). Its MINOR fixes are a separate commit (55f103b). It is not Claude acceptance.
9. **Size engineering.** The manifest master (v7 codec) has 43 B of headroom; the measured capacity is about 21 more entries (`pruning-manifest.md:69–76`). Receipts store xz/base85 `logical_results_base85` blobs, which are under the limit but opaque to readers. AC may prefer moving the master and large receipts to cold storage over further codec work.
10. **Process text.** Theory files carry process-stage text ("requires focused Claude re-audit"); keep it out of the registries at PR preparation.

## Residual uncertainty

Gate reading and the timing of unstamped runs rest on attestation; proof correctness is out of scope; the size measure (by extension) is an upper bound.
