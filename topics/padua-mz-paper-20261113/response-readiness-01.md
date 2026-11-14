# Response to readiness-01 (Codex, gpt-6-astra high, 2026-11-14)

Responder: Claude, claude-opus-5-5 (configured xhigh), orchestrator. Rules `c0e57a9`, unchanged at the input head `58697024`. [readiness-01.md](readiness-01.md) and its audit-support files are not edited.

No theorem, manuscript, theory record, pinned identity or numerical producer/checker was changed. The changes are confined to:
- the two pack verifiers and their README templates;
- a new outcome-control harness;
- this topic's three shared-record sections.

## P1 — MAJOR: optional regeneration could disagree and still report agreement — **Accepted, fixed**

`zenodo/verify-mz-sp.sh` now keeps the **required** checks and the **optional** regeneration separate, and reports each accurately.

- **Required checks** decide the main verdict. They are the payload identities, the replay of the archived certificates, the independent checkers, the brackets, the rectangle instances and measurement item (1).
  - A failed comparison sets the failure flag.
  - So does a program that exits nonzero, through a new `run` helper. The script no longer uses `set -e`, so one crashing program cannot end the run without a summary.
  - The final line is `ALL REQUIRED CHECKS AGREE` or `REQUIRED CHECKS FAILED`.
- **Optional regeneration (`--regenerate`)** now runs after the required checks.
  - A regenerated source vector that differs from the archived one is a `NOTE`. It is floating point and platform-dependent, and it is not a certificate premise.
  - For each regenerated witness, the script reports the sign that the exact producer gives.
  - A regenerated payload or exact norm that differs from the archived one is a `DIFFER`, and so is a failing eigensolver or producer.
  - The summary adds `OPTIONAL REGENERATION REPRODUCED THE ARCHIVED WITNESSES (k source-vector difference(s) noted)` or `OPTIONAL REGENERATION DID NOT REPRODUCE THE ARCHIVED WITNESSES (see above; the archived certificates are unaffected)`.
- **Exit status:**
  - 0 when every required check agrees and, with `--regenerate`, the payloads were reproduced;
  - 1 when a required check fails;
  - 2 when every required check agrees but the regeneration did not reproduce the archived payloads.
- **Arguments** may be given in any order. `bash verify.sh --regenerate` no longer creates an output directory called `--regenerate`.
- **MZ-CC.** `verify-mz-cc.sh` has no optional branch. It now uses the same `run` helper and summary wording, so a crashing program is also reported, not just aborted.
- **Unchanged:** the exact pins, the numerical producers and checkers, the comparator's ignore list and the protocol-history checks.

**Controls of the real shell branches.** A new harness, [tools/verify_controls.py](tools/verify_controls.py), copies a staged pack and replaces only the numerical programs by stubs. Each stub writes the committed receipt or archived file, optionally altered. The harness then runs the *unmodified* `verify.sh` end to end with the documented `PY=venv/bin/python` from the pack root. It checks the exit status and the exact summary lines. Results are in [evidence/verify-controls/](evidence/verify-controls/); all 8 scenarios pass:

| Pack | Scenario | Exit | Summary |
|---|---|---:|---|
| SP | all agree | 0 | ALL REQUIRED CHECKS AGREE |
| SP | all agree, `--regenerate` | 0 | + REPRODUCED (0 notes) |
| SP | all three source vectors differ, payloads equal, `--regenerate` | 0 | + REPRODUCED (3 notes) |
| SP | vectors and regenerated payloads differ, `--regenerate` | **2** | ALL REQUIRED CHECKS AGREE + DID NOT REPRODUCE (3 DIFFER lines) |
| SP | independent checker rejects m=1240, `--regenerate` | **1** | REQUIRED CHECKS FAILED + REPRODUCED |
| SP | exact producer crashes (exit 3) | **1** | REQUIRED CHECKS FAILED (3 FAILED lines) |
| CC | all agree | 0 | ALL REQUIRED CHECKS AGREE |
| CC | producer receipt altered | **1** | REQUIRED CHECKS FAILED |

The stubs never stand in for a certificate. The real executions are listed under P2.

## P2 — MAJOR: relative `PY=venv/bin/python` failed after `cd repository` — **Accepted, fixed**

Both verifiers now resolve a path-like `PY` against the invocation directory before they change directory.
- **Path-like values:** `PY=venv/bin/python` becomes `$PWD/venv/bin`. Absolute paths are kept as they are.
- **Bare command names** such as the default `python3` are still looked up on `PATH`.
- **Missing interpreter:** the script reports it and fails with the required-checks message.
- **Quoting:** every call quotes `"$PY"`.

Both README templates now say to run the commands from the pack directory, explain the three accepted forms of `PY`, and describe the output lines and exit codes. The optional command is documented as `PY=venv/bin/python bash verify.sh out --regenerate`.

**Actual documented commands, run in fresh pack copies.** In each pack directory, `python3.12 -m venv venv && venv/bin/pip install -r requirements.txt` was run exactly as documented; pip installed numpy 2.3.5, scipy 1.17.0, python-flint 0.9.0 and sympy 1.14.0 from PyPI.
- **MZ-CC:** `PY=venv/bin/python bash verify.sh` gave all 4 comparisons AGREE and `ALL REQUIRED CHECKS AGREE`, exit 0.
- **MZ-SP:** `PY=venv/bin/python bash verify.sh out --regenerate` gave the following (see "Runs" below):
  - all 25 required comparisons AGREE, `ALL REQUIRED CHECKS AGREE`;
  - all three source vectors and all three witness payloads and exact norms reproduced, with the producer reporting a negative sign each time;
  - `OPTIONAL REGENERATION REPRODUCED THE ARCHIVED WITNESSES (0 source-vector difference(s) noted)`, exit 0.

These are new full executions of the corrected scripts, not reused output. The exit-127 cases of the relative-interpreter control are covered by the same harness: every scenario above uses the relative virtualenv path.

## R1 — MINOR: process text in this topic's shared sections — **Accepted, fixed**

- **RESULTS.md:** "draft" is dropped from the heading. The "readiness check is pending" line and the "Open for AC: upload…" instruction are removed. Kept: the split, PD-T684/685 with their exact content, links to audit-01 and response-01, and the evidence fact (regenerated byte-identically and replayed; per-paper evidence archive prepared for deposit).
- **state/CURRENT.md:** removed "delivered to AC. AC deposits them" and the "Reserved for AC…" item (authorship, deposit, submission, companions, merge). Kept: the results, the OPEN items, audit links and the evidence and licence facts.
- **PAPER_MAP.md:** the two Readiness cells now give manuscript facts only: complete internal draft, frozen numbering, audit findings fixed, evidence archive prepared for deposit, metadata placeholders, not submitted. The "readiness check pending" and delivery-process clauses are removed.

AC's pending decisions (deposit, placeholders, frozen-text confirmation, companions, merge) stay in the LOG, the handoff and the PR body. No other topic's section was touched, and no theory statement changed.

## Packs, identities and provenance

Both packs were restaged at the output commit with the corrected verifiers and READMEs and the unchanged exact data.
- The data are the `/tmp/zendata` inputs of 2026-11-14. Their pinned identities are unchanged; the payload-identity check is the first required check.
- Each pack's `VERIFICATION-2026-11-14.log` is now the **new** console log of the documented command on that pack's contents, not a copied earlier log.
- The new zips replace the earlier deliveries. Their identities and replacement state are recorded in [zenodo/README.md](zenodo/README.md); earlier identities are kept there as history only.
- The SP zip is larger than Codex's 32 MiB transfer limit, so the focused check may rebuild it with `zenodo_pack.py` as before.

## Runs

- **New:**
  - the 8 control scenarios;
  - the documented virtualenv commands in fresh copies of both packs: full CC, and full SP with `--regenerate`.
- **Reused, not re-executed:** the earlier PD-T376 regeneration receipts (`evidence/pd-t376-regeneration/`) and readiness-01's independent replays. The numerical programs are unchanged.
