# Readiness support — pack/comparator/protocol/licence review

- Auditor: Codex, gpt-6-astra high (configured/inherited assignment), 2026-11-14.
- Input/rules: `9705c75876a74ac6bcce5625d20a45e3676c1992`; read AGENTS, WORKFLOW, Codex role and handoff 08 with its licence addenda. No mutable Git operations or manuscript/theory edits.
- Scope: handoff 08 B2–B4 and licence/package-diff additions. Root owns actual pack construction/full verify executions, live ID reservation and the final disposition. This review introduces no candidate, mathematical mechanism or novelty assertion; it therefore omits a new IDEAS read.

## Finding P1 — MAJOR: optional regeneration mismatches do not fail the verifier

`zenodo/verify-mz-sp.sh:44,46` prints `DIFFER` if a regenerated vector or witness payload disagrees with the archive, but neither branch sets `fail=1`, exits, or changes the final success message. With `--regenerate`, the script can return zero and print `ALL CHECKS AGREE` after all six identity comparisons fail. A platform-dependent source-vector discrepancy may intentionally be diagnostic because the archived-witness replay is the certificate. However the current unconditional final wording also implies successful payload regeneration, and the README describes this command as rebuilding and verifying the witnesses. No such distinction is preserved in the exit/result disposition.

An isolated Bash control actually executed the exact failure consequences and final disposition from this script. Expensive eigensolve/producer commands were replaced by `true` and each identity predicate by `false`; no numerical claim is made by that control. Result: six `DIFFER` lines, exit 0, `ALL CHECKS AGREE`. Reproduce with:

```sh
python topics/padua-mz-paper-20261113/audit-support/pack_verifier_control.py
```

Source SHA256: `d6d158ee6a05ae5f088e0fbe8916dd820da96f0f0d3320041719aad2468f95f7`.

Required response: either propagate regeneration-identity failures into the advertised all-checks/exit disposition, or explicitly split required archived-certificate verification from optional regeneration diagnostics and make its final report accurate. The unchanged archived-witness replay remains a valid certificate route; this finding does not invalidate PD-T376 or assert an actual mismatch in the supplied witnesses. It is a focused verifier defect, not grounds to rerun the whole mathematical audit. Fixing result-bearing verifier acceptance is material and belongs to development, not an auditor's MINOR wording fix.

## Finding P2 — MAJOR: the documented relative interpreter fails after the script changes directory

Both pack READMEs document `PY=venv/bin/python bash verify.sh` after creating the venv in the pack root. Both verifier scripts retain PY verbatim and then `cd "$HERE/repository"` before their first Python invocation (CC lines 8–16; SP lines 13–32). Consequently `venv/bin/python` is resolved relative to `repository/`, rather than the pack root, and the advertised invocation exits 127 even though the interpreter exists at the documented location. This is a verifier usability failure, not a scientific certificate failure.

The root auditor confirmed this on the actual uploaded CC pack with a valid relative symlink to the runtime interpreter: exit 127, `No such file or directory`, at the first Python command. This worker also executed the unchanged **both** verifier scripts in minimal temporary fixtures with a valid `venv/bin/python` symlink. The SP fixture supplies correctly hashed dummy payloads/norm files, so its shell-only identity precheck passes before reaching Python. Both executions fail 127 solely at relative interpreter resolution. No scientific computation is claimed for these fixtures. Reproduce:

```sh
python topics/padua-mz-paper-20261113/audit-support/pack_relative_python_control.py
```

Required response: resolve a relative PY to an absolute executable before changing directory, or document/use an absolute interpreter path such as `PY="$PWD/venv/bin/python"`. Verify the exact advertised command in a fresh extraction. Retain support for ordinary PATH names such as `python3`. The same repair applies to both README commands and/or both scripts; no theorem changes or expensive certificate repetitions are required merely to test interpreter resolution.

## Comparator inspection

Read all of `zenodo/compare_receipts.py` and both verifier scripts. The recursive walker compares dict-key unions and list lengths, so a missing or extra nonignored field fails. Compared fields include source/code hashes, exact arithmetic endpoints, `sign`, `accepted`, `strict_positive_lower`, `finite_threshold_pass`, `q_center`, `q_absolute_error`, exact inertia counts and strict-dominance margins. I executed direct `ignored(path)` probes confirming these remain significant.

The built-in ignore list is broader than timings alone: it skips versions/dependencies, commands/environment, paths, intermediate bulk descriptions, status prose, executable-binary hash, receipt hashes and gzip-container hash/size. Those omissions are consistent with replay portability at this scope: meaningful acceptance booleans/signs/enclosures remain compared, native source hashes remain compared, and decompressed payload identity is checked separately. `status` is not used as the proof acceptance predicate. The script does not independently establish the reference receipt's truth; that depends on the inspected producer/checker and audited source reduction. Arbitrary user-supplied `--ignore` regexes can intentionally suppress more fields, so the following actual invocations matter:

- Witness replay adds only `witness\.source_vector_sha256$`, because `--witness` has no input float proposal. The exact archived payload is separately hashed before replay. The normal built-in list does **not** skip source-vector identity on a producer-from-vector receipt.
- CC P4 adds `^protocol_sha256$` after checking the archived historical protocol against the receipt.
- SP P1 adds `^(protocol|reduction)_sha256$` after checking both archived historical documents. The N=8 and N=16 receipts use the same two identities.
- No actual verifier invocation ignores signs, mathematical endpoints, code hashes or the payload-identity comparison.

## Historical pin checks actually executed

`git show` of each original blob, SHA256 in Python, compared to committed receipt:

| Revision/path | SHA256 | Verdict |
|---|---|---|
| d03e74dc: sharp/attempts/P4.md | `101bc61acd673f71195b1e0c002101106f1e6d15dbc7b2b679eb614807d84a77` | matches P4 producer protocol |
| c1e6e59d: sharp/ideas/P1-numeric-protocol.md | `568fc2b9f2de6b328d4d2d69980302aba984cac425b43e8c09fd6c31c49d647f` | matches both P1 protocols |
| c1e6e59d: sharp/theory/P1-rectangle-certificate.md | `4cee5449c0b1634e4d868a41c474b0c938a5394bc87e8f45e197219508a911a9` | matches both P1 reductions |

Here `sharp/` abbreviates `topics/padua-mz-sharp-constants-20261106/`. This is an audit of existing historical pins, not a new prose-hashing requirement. Their archived copies and whole-zip integrity are for root's actual rebuild check.

## Manifest/source completeness

Parsed both committed manifests in full and compared all `repository/` members by `git show 90860ec:<path>` and SHA256:

- CC: 377 distinct manifest rows, 368 repository members; every repository hash matches.
- SP: 706 distinct rows, 678 repository members; every repository hash matches.
- Both manifests have exactly the expected set from `REPO_PATHS`, `DATA_FILES`, templates, verifier, comparator, requirements, LICENSE and the recorded verification log. No missing or extra member relative to the staging recipe. MANIFEST itself is intentionally outside its own list, giving the documented 378/707 total files.
- No `.cls` or `.bst` member appears in either manifest. CC explicitly excludes the two SIAM files; no other source exclusion was found.

The manuscript-named producer/checker paths, their runtime/hash dependencies, exact trial, small receipts, all three large witnesses/norms/source vectors, historical protocol files and the table/measurement outputs are represented. SP's longer P2 measurements are retained as scripts and receipts and are explicitly outside `verify.sh`; that limit is accurately documented. CC's removed SIAM build dependencies are accurately explained in its pack README and are unrelated to certificate execution.

`zenodo_pack.py` builds repository contents with `git archive REV`, applies exactly the declared SIAM exclusion, copies a finite declared external-data set and templates, then manifests every regular file except any file named MANIFEST-SHA256.txt. Its ZIP member ordering/timestamps/modes are fixed. The byte-level ZIP is also dependent on compression/runtime implementation; exact identity of a locally rebuilt ZIP is distinct from source/payload identity. Root's actual package verification is needed before claiming the data rows or delivered ZIP bytes were checked here.

## Licence and packaging-diff review

- Read root README licence notice, root LICENSE opening/end, pack README notices and the two new manuscript sentences. Root LICENSE and `zenodo/LICENSE` are byte-identical. The notices explicitly specify AGPL-3.0-or-later, as AC instructed. SIAM macros and source quotations keep their own terms; no attempt is made to relicense them. The unmodified SIAM class header indeed conditions redistribution on the complete eight-file package. Its remaining repository presence is AC's separately flagged decision, not resolved by this reviewer.
- `git diff ed385e9..90860ec` over all `REPO_PATHS` shows no result-bearing code, evidence or data change. Within packed repository content the only changes are the manuscript licence sentences; README/LICENSE templates changed and CC excludes the two SIAM files. The verifier scripts, comparator and pinned requirements are unchanged in that interval. The packer itself changed from tar/gzip to deterministic ZIP as documented, plus licence copy and exclusion handling. Thus the code/evidence represented by the manifests stays the verified staging's content.
- Both current availability statements say an evidence archive is *prepared for deposit* with a DOI placeholder; neither asserts that Zenodo already hosts it. The claim of prepared archive contents is consistent with the declared recipe/manifests, subject to root's actual rebuild. Physical delivery to AC's device is documented by Claude, not independently witnessed here.

## Limits

No archive ZIP was retrieved from AC's device, no full numerical verify run or producer was executed by this worker, and no external licence authority was queried. Executions were the isolated mismatch control, unchanged-script relative-interpreter controls, and the manifest/blob/path/hash/ignore probes described above. The root's independent numerical and packaging runs supply the separate science coverage. No finding beyond P1–P2 was identified in this bounded review.
