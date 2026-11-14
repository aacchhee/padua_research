# Handoff 38: answer audit-07 (one paired batch: data statements and a rebuilt public kit)

- Status: done in 687e9d47dec64d9d582c7544a7df4bd0576ebd82
- Previous handoff: 37-claude-audit-public-reproduction.md
- Next agent / model / effort: Codex, gpt-6-astra high coordinator; Sol medium for TeX/README edits, a distinct Astra high agent for the focused re-check.
- Role: orchestrator and developer
- Branch: codex/padua-argmax-bridge-20261105
- Input head SHA: `3ad9beec7f9b5b91c6ef4cf486c86b752b379d94` (audit-07 outputs; in-place MINOR fixes at `820fe13`); this handoff is the following handoff-only commit
- Main / base: `99a9b1d161e41a80c4fd425b63022c681fbe8779`, merged in `5f0e8e4`
- Stage: WORK (one MAJOR publication-coherence finding is open)
- Written by / date: Claude. Orchestrator `claude-sonnet-5-5`; audit work by three Claude Opus 5.5 subagents instructed at xhigh (disclosure in audit-07.md). · 2026-11-14

## Authority

Working-branch commits and pushes and PR metadata stay authorized. No main push, merge, force-push, tag, `.github` or settings change, no external submission or contact, no invented licence, authorship, storage or DOI, no upload. Only AC merges or publishes. AI declaration, ORCID, contributions, funding and the draft marker are AC's. No new native campaign, certificate production, retry, rescue or threshold change; theorem statements, premises and ID ranges stay frozen; no final-ID assignment. No full numerical campaign is requested. Do not ask again for the retired historical artifacts.

## Read first

AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md at the current head (record the SHA); this handoff; [audit-07.md](../audit-07.md) and the reports [audit-07/p7-public.md](../audit-07/p7-public.md), [audit-07/m7-manuscripts.md](../audit-07/m7-manuscripts.md), [audit-07/e7-evidence.md](../audit-07/e7-evidence.md) for locations and the reviewer controls to reuse (P7's checker and 31 negative controls are in [audit-07/code/p7-code](../audit-07/code/p7-code/)).

## Task: one paired batch, then a rebuilt public kit

The MAJOR finding edits frozen TeX, so every wording item rides with it; a changed TeX freeze changes the PDFs inside the public ZIP, so the kit is rebuilt once, with the README and adapter items.

1. **P7-01 (= E7-01 = M7-01, MAJOR).** `paper/main.tex:84-93` and `companion-paper/main.tex:91-100`: the data statements say the reproduction package comprises "a versioned source snapshot, the essential certificate inputs, new native and independent-checker outputs, runtime dependencies, and verification commands". The public kit has none of the snapshot, native outputs or runtime dependencies. Reword both texts to what each artifact really contains, e.g. a public verification kit (942 phase inputs, 39 polynomial inputs, minimal unchanged checker sources, expected results, both PDFs) and, separately, a preservation archive (full native histories, runtime bytes, source snapshot) held by AC, with no repository paths that a kit user does not have. Fix the same claim at `companion-paper/sections/certification-unified.tex:1864-1866` ("rebuilt polynomial checker" is built fresh by the kit). **M7-02**: the companion's data statement cites itself as a separate "unpublished preprint". **M7-05..M7-08** editorial items in m7-manuscripts.md (path rule before first use; "new phase certificates" versus 560 retained and 382 new; name the native campaign; "no DOI has been assigned" instead of "no permanent deposit"; the stray "Section 4" inside Section 4 at companion comparison 3043; CPU times to 10^-6 s; mention `base_table.py` for Table 2); **M7-09** align the paper's trust-table footnote and polynomial-replay wording with the companion. Do not touch a numbered display, theorem, constant or range. New paired TeX/Bib freeze, separate pointer commit, rebuild (59/152 expected), `check_correspondence.py` default and `--archival`, `check_baseline_controls.py`, the 13-scenario mutation harness (copy outside Git; change only HEAD/BASELINE), the rename-aware scanner (empty map expected) and rendered-page inspection of the changed pages.
2. **M7-03** add a mode to `check_correspondence.py` that compares built labels from the current `.aux` files (the committed `--artifacts` mode needs the retired PDFs); update `companion-paper/BUILD.md` (my dated note points to the helper in audit-07/code/m7-code/labels.py meanwhile).
3. **Public kit.** After the TeX freeze: README.txt/README.md (**P7-03**: say that SHA256SUMS and MANIFEST.json are inside the package, so `PASS integrity` shows internal consistency and authenticity needs the externally published ZIP checksum; **P7-06** a memory statement, about 1.7 GB for degree 33 and more for higher degrees; **P7-07/P7-11** "Python 3.12 or newer (3.13.18 with NumPy 2.5.3 also passed the audit)" or equivalent without overclaiming, README.md rendering, the overlong line, no mention of "the repository" a kit user does not have, a single analytic PASS line, `corner_gap` "None" string for n >= 256); `verify.py` (**P7-04** strict JSON for `expected-results.jsonl`; **P7-05** compare the stored receipt's certificate hash/counts in the polynomial replay or say it checks only the three acceptance booleans; **P7-09** check the file population against MANIFEST as well as SHA256SUMS). Any adapter change gives a new identity: freeze a new source commit before building, record it, rebuild once, new ZIP hash, one new bounded smoke (as in zenodo-public-package-20261114.md, caps recorded), plus a distinct-agent check of the ZIP delta (data statements in the shipped PDFs, README commands verbatim, integrity, a negative-control subset). Do not repeat a full 942-record or 39-degree replay.
4. **E7-06..E7-13** and **P7-08/P7-10** are NOTE-level: record dispositions in `response-07.md`; act only where cheap (E7-08 mark amendments; E7-09 commit the I25 input staging script if it exists; E7-11 rename or document the shared per-degree cache; file modes 0644 in the ZIP).
5. Write `response-07.md` with one disposition per finding and update `pr-update-20261113.md` (audit-07 result, open items, budget numbers as corrected in audit-07 F1; the recorded lists must be consistent with the new ZIP). No spacing damage in new records.

## Open decisions for AC (not yours to decide)

1. **P7-02 disclosure.** The 560 retained phase inputs contain `/home/ahomel/a/andreyac/num_tests/padua30/…`, many files contain `/workspace/padua_research/…`, receipts for degrees 37..40 contain `/opt/codex/runtimes/…`, and the required provenance file `proof-attempts-codex-01-padua-corner.md` contains internal process text. These are pinned by hash. You may propose (not execute without AC) a documented sanitised derivative with a recorded transformation and the replay re-run, as was done for the compact polynomial summaries; AC chooses. Until then say plainly in the README that the inputs retain these paths.
2. The global generated-output budget (bound 11,864,226 B against 10,000,000 B; main 9,787,481 B; topic share 2,054,467 B; the topic tree including main counts 11,841,948 B).
3. Whether and where to upload, the DOI, the AI declaration (still omits Sonnet 5.5), ORCID, contributions and the draft marker.

## Frozen

All mathematics, E01–E15, J01..J03, the finite theorems and certificates, the hybrid engine freeze `0d9ce0a5…`, the numerical core (`check.py`, `controls.py`, `runtime_probe.py`), the preservation archive (296,189,961 B, `d3452a17…`), earlier freezes and all audit reports. The previous public ZIP (`15885d34…`) stays as it is; record the new one beside it.

## Publication

At the session boundary commit outputs first; then in a separate commit close this handoff as `done in <sha>` and open the next numbered handoff; exactly one stays open while work remains. After this batch a focused diff review (data statements and the ZIP delta only) suffices; then the topic can proceed to readiness once AC's decisions are made. PR 27 stays a draft; edit its record yourself.
