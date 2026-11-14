# Response to Claude audit-07

2026-11-14. Input audit head `9d3f5e0f8b270d039d78d4ebc0df53269a7892ab`.
Claude accepted the mathematics, regenerated evidence and public replays;
this batch addresses the publication-description MAJOR and related tooling/
editorial items. No theorem, premise, constant, range or numerical core changes.
Authority, models, scope and process details are recorded in [LOG.md](LOG.md).

Paired TeX/Bib freeze: `5f435be21f29f6fbf48e6d8cba15346117d7e151`.
Separate pointer/current-label tooling commit: `daa77deb6371a12f6a6e36ff7b894ebb71a7f232`.
Public adapter/build source: `dce3260b88c11a964168a64c34b168ac37f2a11c`.
New archive: 5,149,206 bytes, SHA256
`b341e6a1c6875550b58576b2cb167766f5a3cf9a4e4fc620b1134d2c490adbaa`.
The previous public and preservation archives remain unchanged.

| Finding | Disposition and evidence |
|---|---|
| P7-01 / E7-01 / M7-01 MAJOR | Developed, supplementary reviewed. Both shipped data statements describe the actual public kit (942 phase/39 polynomial inputs, minimal checker sources, expected results, analytic checks, commands and PDFs) separately from AC's preserved full archive (native histories/runtime payloads/source snapshot). Public paths refer to README and package contents; companion no longer promises a shipped rebuilt binary. New PDFs are hash-validated inputs to the builder; the old preservation receipt is immutable. |
| P7-02 | Resolved by AC's explicit “Retain with explicit disclosure”. README names home/workspace/runtime paths and internal process text preserved in checksum-bound inputs/provenance. No bytes sanitized, no upload authorized or performed. |
| P7-03 | README says embedded checksums/manifest establish internal consistency; authenticity requires the externally trusted published ZIP checksum. Numerical replays have a separate purpose. |
| P7-04 | Strict parser now covers expected JSONL as well as other JSON. Duplicate fields, nonfinite literals and numeric overflow are rejected; new negative controls pass. |
| P7-05 | Fresh polynomial replay compares the certificate hash and bound/corner/split counts with all supported stored receipt formats, in addition to acceptance booleans. All 39 formats are parsed and hash-bound; actual 2/17 smoke passes; tampered n2 counts reject after integrity. No full 39 replay is claimed. |
| P7-06 | README gives observed n33 peak about 1.7 GB and warns higher degrees may need more, alongside the existing long-run time estimate. |
| P7-07 | Python 3.12-or-newer wording identifies reference/audit versions without universal compatibility claims; the None-string corner_gap result is explained for n>=256. |
| P7-08 NOTE | Retained design: replays recompute mathematical checks, not historical execution or every metadata byte. Hash integrity and external authenticity are separately scoped. |
| P7-09 | Payload population is checked against MANIFEST as well as SHA256SUMS; manifest payload sizes/hashes are enforced. Refreshed checksums do not alone admit extra payload. Selected existing audit controls confirm rejection. |
| P7-10 NOTE | New ZIP entries have regular 0644 modes for normal use. Prior ZIP remains byte-identical. |
| P7-11 | Markdown-compatible headings/code blocks in both readable guides, wrapped line, owner-controlled license language without requiring a repository, one clear analytic PASS line; expected results retain the documented None string. |
| M7-02 | Companion names the research article rather than citing itself as a separate unpublished companion. |
| M7-03 | New --built-labels mode uses explicit current output dirs and compares 120 current aux numbers without retired PDFs. BUILD.md documents it. Historical --artifacts remains a separate preservation mode and is not claimed executed. |
| M7-04 | Auditor's dated deposit-README correction retained; current response/package pointers supersede the old deposit table. |
| M7-05 | Relative repository-path convention precedes first use; public data statements give the kit's actual paths/content rather than availability promises for omitted files. |
| M7-06 | New verification outputs distinguished from the 942 inputs (560 retained/382 regenerated); degree 320–510 native campaign named. |
| M7-07 | No deposit or DOI is claimed; DOI assignment language corrected. |
| M7-08 | Local measure-inequality pointer replaces misleading Section 4 reference; CPU/wall costs rounded for journal prose; base_table.py named for Table 2. |
| M7-09 | Paper trust-table footnote and polynomial-replay scope aligned with companion. |
| M7-10 NOTE | Draft dates and AI/author metadata remain AC's; no change. |
| E7-02 / E7-03 | Auditor addenda retained. New records distinguish main size, topic's incremental share and entire topic-branch tree. The evidence-size norm is not falsely applied to source code; large code remains committed as required. |
| E7-04 / E7-05 | Auditor dated corrections retained; current BUILD/README/package records point to this new freeze and artifact while historical records stay historical. |
| E7-06 | Auditor's non-strict containment correction retained: at most 42174 of 43116 stored S uppers, with 942 not validated by that test. No claim that every native endpoint is validated. |
| E7-07 NOTE | This response uses pass-RSS terminology for the 112708 KiB native pass observation; no measurement is relabelled as total memory. |
| E7-08 NOTE | Dated amendment notes added to the native and I25 preregistration prose; immutable machine/code freezes stay unchanged. |
| E7-09 NOTE | Exact 1775-byte historical staging body now committed as code/regeneration_i25_20261114/stage_inputs_20261114.py, SHA256 ef88f9f7192aecb96dc671f8735bc4e7aefabc897e1b13d7f5ffa82f03056e6f. No staging execution repeated. |
| E7-10 NOTE | I25 wait4 observes timeout wrappers which propagate worker exits; no stronger raw-worker observation is claimed. |
| E7-11 NOTE | J03 dated clarification explains pair equality uses a shared within-degree cache and is not 942 independent bound derivations. Frozen result names/values are not rewritten. |
| E7-12 NOTE | The full accepting readback's cf64 reader and final 94ca guard tests remain distinguished. No extra full readback was necessary for this publication-only delta. |
| E7-13 NOTE | Fresh recorded counts were already checked against actual new inputs/results; equality with historical counts does not transfer old outcomes. No extra numerical campaign. |

## Actual verification

Both builds exit 0 at 59/152 pages. Current source 19/86/120, current aux 120,
archival source 13/90/113 and seven baseline controls pass. The copied audit-06
harness changes only HEAD/BASELINE; 13 scenarios have expected outcomes
(S0/S7 pass, eleven actual source mutations reject). Harness SHA256
`c571617de1d7afab4fa068b3f4fe80ee44b6e6e4f6b54acc9a097f9cae1f9b2e`.
Empty-map scanner shows formal blocks identical to e861c752. Changed final
pages are actually rendered and independently inspected; no errors, overfull,
undefined or multiply-defined references. Historical PDF preservation not run.

The new public ZIP has 1,019 files, all mode 0644, 10,229,741 expanded bytes.
Exactly 9 payload/control paths change; 1,010 files, including all 942 phase
and 39 polynomial inputs, remain byte-identical. Its PDFs match the new build
identities in [new delivery receipt](zenodo-public-response07-delivery.json).

Developer bounded README smoke runs once after source freeze: phase 41/511
both records, fresh polynomial compile+2/17, exact analytic and both 60-entry
table checks; actual waitstatus 0, CPU 24.861645 s/wall 25.046612 s, no cleanup,
max RSS 153380 KiB. Distinct review independently extracts the kit and runs
integrity plus the exact quick command: wait 0, CPU 25.855 s/wall 25.914 s,
max RSS 154468 KiB; all pass. Nine selected/strengthened negative controls reject
for intended reasons, including polynomial count tampering after integrity.
No full942/full 39 or native campaign is repeated.

[Supplementary review](supplementary-review-response07-20261114.md) records
exact sources, identities, rendered pages, commands and negative controls.
Only the focused Claude diff review of data statements and ZIP delta remains;
previously accepted mathematics and complete numerical runs are not reopened.
The public candidate is local and unuploaded. AC's global-budget/publication
metadata choices remain; the path-disclosure choice is resolved.
