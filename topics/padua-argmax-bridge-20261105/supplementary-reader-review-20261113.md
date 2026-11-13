# Supplementary reader review — 2026-11-13

**Disposition:** the inspected E4-01..04 repair passes the synthetic and source-level checks below after one material correction. This is a distinct Codex supplementary review, not the required Claude handoff. A subsequently supplied original compact return passed the actual data-only rerun recorded below. The canonical onset-512 ZIP was unavailable for this review. Its compatibility with the new member allowlist and complete trusted runtime remains untested.

Reviewer: Codex, assigned `gpt-6-astra`, high; serving metadata are not independently exposed. Rules read at `2f87ee65f93ba056cf9fb3f9a737a362e864e755`: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md`. Input instructions: handoff 31, audit-04 E4 findings and evidence report, and its `rb_controls.py`. Reviewed the relevant working-tree delta against `941aa335e60ca7058c8a0113faa76e31217f4753`. Only this report was written in the repository; no mutable Git operation, code repair, native campaign, or scientific status change was performed. Novelty gate is inapplicable: this review introduces no new mathematical claim or mechanism.

## Identified source bytes

Paths below are relative to this topic. These hashes identify the reviewed working files independently of later orchestration commits.

| File | SHA-256 |
|---|---|
| `code/local_onset512_campaign/return_bundle.py` | `5e25c8a47115e114d20e64fa6ac7b2afb30dde0bfebef371f1e709857795ae2e` |
| `code/local_onset512_campaign/runner.py` | `a198b65182590be13cb91110ff976d90e7e885c778180e59699fbe9b067ccdad` |
| `code/local_onset512_campaign/check_reader_repairs.py` | `0a11ce4c2ee01e79609767bbc0f18f6b1f34a595394d31c07aaa8ed3e7078634` |
| `compact_pack/verify_compact.py` | `2d26886fa38089815712edcceccd4ac893fea9d8e6092afbd4c0faac7b569cef` |
| `code/independent_phase_checker/runtime_probe.py` | `18801fb898de0ad9d32745d1e684ace55bc9d1661bbf0f87abb33183f3fb8820` |
| `code/independent_phase_checker/controls.py` | `c1810bd1dc6ddcbb3501c0589f099c89fa50fd6bd2e79b77f06030d8cc114bd1` |
| `code/independent_phase_checker/check.py` | `1501ce9435a17e9cc4b0954f3ce90f47450252d58027e08468ce905528fdc8be` |
| `zenodo-deposit/README.md` | `f1a58efa9e0caa48f966383f7029eb68150bcfd9d0deac00fa6b636216d02bc4` |
| `zenodo-deposit/RECHECK-SMALL-BUNDLE.md` | `88a163d4b2343da93d84fd0e4a124a00315c085e5b4746c86aefe092d013f621` |
| `zenodo-deposit/MANIFEST.json.in` | `21ca6fa317dd1b50c0b8222c2b7da801806a6351c5e911c913c91d2c67e6e376` |
| `local-onset512-summary.md` | `0f044119ba5d2cae64e1f2a9da57587602919f181a7ae520c782ae3a28ab0e29` |

Later purely administrative changes to README/manifest review status do not inherit a new content hash from this table.

## Finding and material recheck

**SR-01, material parser-path gap — fixed and rechecked.** Initial inspection found `return_bundle.strict` recursively enforced scalar types, but production `evidence.Access.json` used `common.strict`, which rejects duplicate keys and JSON nonfinite constants without enforcing those scalar types. The initial regression's `SyntheticAccess.json` instead used the stronger reader parser, masking that difference. I sent this finding to the developer and orchestrator without editing the code. The developer added a local `CheckedAccess` subclass whose `json` method invokes `strict(self.data(name))`, and changed the test adapter to ordinary JSON parsing so the production subclass is essential. Independent checks preserving inherited real `Access.data/json` then rejected all tested malformed scalars, duplicate keys, and NaN. The repaired file identity is the reader hash above.

No other unresolved code finding was identified within this limited scope. Missing payloads remain a verification obligation, not a waived finding or evidence of success.

## Executed checks and results

Working directory was `/workspace/padua_research`; Python `3.12.14` (Clang 22.1.3), NumPy `2.3.5`. Synthetic choices use the committed fixture's deterministic seed; there is no scientific sampling or native engine execution.

1. `python3 -E -B topics/padua-argmax-bridge-20261105/code/local_onset512_campaign/check_reader_repairs.py` — exit 0, **40 controls PASS** on the final test hash. This separately executed the developer's suite. Its positive case adapts checker arithmetic and sampled closure and therefore is not a certificate proof. It covers computed counts, former transport categories, pins, namespaces, linkage/types, optimization, and compact coverage. Large-size controls patch declared metadata rather than allocate multi-GiB ZIPs. Symlink-typed ZIP entries are data, never extracted; the test checks inventory handling, not a claim of blanket symlink metadata rejection.
2. `python3 -E -B /tmp/padua_reader_independent.py` — exit 0. The independent script below has SHA-256 `943b927cb86c0000952c2a582055c250d4c8b7a15a4f37ed5150a09d195753c2`. It reuses fixture data but preserves real inherited `Access.data/json`; only construction, checker arithmetic, and sampled native closure are adapted. One positive baseline reported 191 pairs / 382 proofs. **18 negative controls rejected**: boolean CPU, float cap/degree/exit, boolean exit, integer boolean fields, false cleanup list, failed status, wrong summary identity, duplicate key, NaN, an unlisted archive member, three rehashed extra namespaces, wrong external manifest, and failed source pin. The latter two never reached checker construction.
3. A separately constructed 203-byte ZIP containing only `COMPACT.json` with `files={}`, empty degrees, and empty selection was submitted in child processes to the reader and runner. For each script, `-O -B`, environment `PYTHONOPTIMIZE=1` with `-B`, and `-E -O -B` exited **1** with `optimized Python is unsupported`, no acceptance text, and no runner output-directory creation. The ephemeral ZIP SHA was `52692f2c4cc7ef8615b1f82a064fd1d9636661d0f7b30d7f554eb91eb5c5acf6`; ZIP timestamps mean regenerated bytes can differ. Construction was `ZipFile(...,'w').writestr('COMPACT.json', json.dumps({'files':{},'root':'/forged','output':'out','degrees':[],'selection':{}}))`. The committed 40-control script also preserves reproducible subprocess optimization tests. AST traversal reported **zero `ast.Assert` nodes** in both repaired reader and runner.
4. `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -E -B topics/padua-argmax-bridge-20261105/code/independent_phase_checker/runtime_probe.py` — exit 0, **31 arithmetic controls** and all four finite probes true: ties-even-down, ties-even-up, gradual underflow, smallest subnormal. This does not establish universal IEEE conformance or replay a witness.
5. Parsed `zenodo-deposit/MANIFEST.json.in` and compared its three current code hashes to `sha256sum` and the README: all agree. `git diff --check` on the reader, compact verifier, and deposit paths exited 0. Searched the repaired reader/runner and current deposit recipes for `assert`; the remaining mention is explanatory prose about the historical defect, not an executable guard.

## Scope conclusions

- **E4-01:** source-level fail-open mechanism removed; explicit optimization refusal occurs before operational imports; printed counts accumulate from checked records. Runner pin checks now raise errors. Recipes use `-E` and explain correctly that it ignores Python environment variables, not full isolation. The export-generated README also uses `-E`; the historical canonical ZIP's internal README was not rewritten or inspected here.
- **E4-02:** reader externally defaults to canonical archive `da63280a7e4aec86fa52e3f8384620fbf07939006ab5f6f70222fa2485816e7e` and independently pins trusted manifest `5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16`. Trusted asset bytes and `R.pins()` are checked before `CheckedAccess` constructs/imports the frozen checker. Explicit `--archive-sha` is an operator-selected external pin for other archives; it does not disable manifest authentication.
- **E4-03:** inspection and adapted controls cover the added summary-receipt/fresh-input linkage, attempt completion status, historical preregistered runner identity, registered member namespaces, and strict scalar/boolean checks. The allowlist was inferred from frozen producer writes. Real canonical member compatibility and all sampled native-closure reads remain untested.
- **E4-04:** both compact wrapper/pass return codes require actual integer zero; adapted malformed boolean exits reject. Output now states `expect_plan` and `coverage_mode`, and the test rejects an incomplete requested plan. The subsequently supplied original compact return passed the actual rerun below.
- **Recipes:** the small-bundle pin checks now raise before importing its separately trusted checker, exact 942 proof-member coverage is enforced, and the proposed full serial cap is 7,200 CPU-s. Historical timing calibration is explicitly historical. No new timing fit, small-I25 replay, full serial recheck, canonical onset ZIP run, or 942-proof cross-archive comparison is claimed.

The canonical actual-return run required by handoff 31, small-I25 representative degrees 320/384/458/510, proof-byte comparisons, native-history custody decision, and substantive Claude re-review remain separate obligations. No historical acceptance is attributed to the repaired reader. Newly supplied artifacts require identity checks and a dated addendum or separate record before changing these execution limits.

## Supplied original compact return: independent actual rerun, 2026-11-13

After the synthetic review, AC supplied the old package and split return. I independently rehashed the reconstructed return (36,045,486 bytes; SHA-256 `b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a`), the 54,003-byte manifest (`5b89fa66…`, full pin above), and all **250** extracted package members against that manifest. The current repository verifier was rehashed to `2d26886f…` before invocation; the package's historical verifier was not executed.

A separate preregistration at `/tmp/padua-independent-compact-recheck/preregistration.json` fixed one read-only data check, **180 CPU-s / 240 wall-s** caps, no native campaign. The child used `RLIMIT_CPU=(180,180)` inside an outer `timeout --kill-after=5s 240s` wrapper. Exact verifier command from the repository root:

```sh
python3 -I -S -B topics/padua-argmax-bridge-20261105/compact_pack/verify_compact.py \
  local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz \
  --package local-output/argmax-bridge-20261105/compact-release-aea62883/padua30 \
  --manifest-sha 5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16 \
  --expect-plan all
```

Result: **exit 0**, 5.349221 child CPU-s / 5.350634 wall-s, empty stderr. Output reports `expect_plan=all`, `coverage_mode=complete_plan`, **280 rationally checked pairs**, exact degrees **41..319 plus 511**, sampled full histories **199,238**. Stdout SHA-256: `3f6605da9c09eaa69f7a9daf30c6cfdf0ff6ef424369cf420527e246ed841767`; scratch output is `/tmp/padua-independent-compact-recheck/stdout.json`. These are local session outputs, not a cold-storage custody receipt.

This closes the independent actual old-return check for the repaired compact verifier at its recorded hash. It does not check onset degrees 320..510, the still-missing I25 ZIP, or perform fresh native sample reruns.

## Independent harness

Save the following as `/tmp/padua_reader_independent.py` and run the command above. It is a metadata-control harness, not a substitute for actual archives.

```python
import contextlib, copy, hashlib, io, json, sys, tempfile, zipfile
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
sys.path.insert(0, '/workspace/padua_research/topics/padua-argmax-bridge-20261105/code/local_onset512_campaign')
import check_reader_repairs as C
B=C.B
from evidence import Access as RealAccess
rows=[]
with tempfile.TemporaryDirectory(prefix='independent-reader-') as td:
    t=Path(td); release=t/'release'; release.mkdir()
    asset=b'{}'; manifest=B.encoded({'files':{'asset_provenance.json':{'bytes':2,'sha256':B.sha(asset)}}})
    (release/'asset_provenance.json').write_bytes(asset); (release/'runtime_manifest.json').write_bytes(manifest)
    docs, inv, pins=C.fixture(); docs['TRUSTED_RUNTIME_MANIFEST.json']=manifest; docs['TRUSTED_ASSET_PROVENANCE.json']=asset
    inv['trusted_manifest']=B.R.identity(release/'runtime_manifest.json')
    events=[]
    class DataAccess(RealAccess):
        def __init__(self, package, root, read_bytes):
            events.append('checker'); self.reader=read_bytes
            self.checker=SimpleNamespace(verify_essential=lambda proof,freeze:proof['verification'])
    def pincheck(): events.append('pins'); return pins
    def run(files, inventory=None, extra=None):
        inventory=copy.deepcopy(inv if inventory is None else inventory)
        inventory['files']={n:{'bytes':len(d),'sha256':B.sha(d)} for n,d in files.items()}
        archive=t/'case.zip'
        with zipfile.ZipFile(archive,'w') as z:
            for n,d in files.items(): z.writestr(n,d)
            if extra: z.writestr(extra,b'{}')
            z.writestr('COMPACT.json',B.encoded(inventory))
        with contextlib.redirect_stdout(io.StringIO()) as out: B.verify(archive,B.sha(archive.read_bytes()))
        return json.loads(out.getvalue())
    def rejection(label,call):
        try: call()
        except Exception as e: rows.append({'test':label,'result':'REJECT','reason':str(e)})
        else: rows.append({'test':label,'result':'ACCEPT_UNEXPECTED'})
    with patch.object(B.R,'RELEASE',release),patch.object(B,'MANIFEST_SHA',B.sha(manifest)),patch.object(B.R,'pins',pincheck),patch.object(B,'Access',DataAccess),patch.object(B,'validate_pass',lambda *a:None):
        baseline=run(docs); rows.append({'test':'adapted baseline, real inherited Access.json/data','pairs':baseline['pairs'],'proofs':baseline['proofs']})
        if events != ['pins','checker']: raise RuntimeError(events)
        for label,name,key,val in [
          ('false CPU','out/jobs/320/produce/final-accounting.json','total_CPU_through_summary',False),
          ('float cap','out/jobs/320/produce/final-accounting.json','hard_aggregate_cap',120.0),
          ('float degree','out/jobs/320/attempt.json','n',320.0),
          ('boolean exit','out/jobs/320/produce-exit.json','observed_returncode',False),
          ('float exit','out/jobs/320/wrapper-exit.json','observed_returncode',0.0),
          ('integer terminal','out/jobs/320/attempt.json','terminal',1),
          ('integer ECHILD','out/jobs/320/produce-exit.json','ECHILD',1),
          ('false cleanup','out/jobs/320/attempt.json','cleanup_killed',False),
          ('failed attempt','out/jobs/320/attempt.json','status','failed'),
          ('wrong summary receipt','out/jobs/320/produce/summary.json','essential_receipt',{}),
        ]:
            files=dict(docs); doc=json.loads(files[name]); doc[key]=val; files[name]=B.encoded(doc)
            rejection(label,lambda:run(files))
        for label,old,new in [('duplicate keys',b'"terminal": true',b'"terminal": true, "terminal": true'),('nonfinite',b'"n": 320',b'"n": NaN')]:
            files=dict(docs); name='out/jobs/320/attempt.json'; files[name]=files[name].replace(old,new); rejection(label,lambda:run(files))
        rejection('unlisted archive member',lambda:run(docs,extra='unlisted.json'))
        for name in ['out/jobs/999/attempt.json','out/jobs/320/produce/surprise.json','out/surprise.json']:
            files=dict(docs); files[name]=b'{}'; rejection('rehashed extra '+name,lambda:run(files))
        for label,operation in [('manifest',lambda:patch.object(B,'MANIFEST_SHA','0'*64)),('source pin',lambda:patch.object(B.R,'pins',side_effect=ValueError('independent source pin refusal')))]:
            events.clear()
            with operation(): rejection(label+' before checker import',lambda:run(docs))
            if 'checker' in events: raise RuntimeError('checker imported after '+label+' refusal')
print(json.dumps({'controls':rows,'scope':'synthetic metadata only; fixture data reused, independent adapter preserves Access.data/json; checker arithmetic and sampled closure explicitly stubbed'},indent=2))
if any(r.get('result')=='ACCEPT_UNEXPECTED' for r in rows): raise SystemExit(1)
```

## J3-04 positive controls — supplementary recheck, 2026-11-13

**Accepted at the stated one-tree scope.** Independently inspected and executed `code/independent_phase_checker/accept_controls.py`, SHA-256 `c0ab77e611b78c840c8ac02cad1431c20bb018be9a2770605f2aeae450a4e908`. Before execution I rehashed this source, frozen `check.py` and `controls.py` against their full hashes above, and the authenticated original return against `b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a`. The script also independently checks that archive pin, then reads the unique regular n=41 primary receipt as data, with a 16-KiB member limit.

Command from `/workspace/padua_research`:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -E -B \
  topics/padua-argmax-bridge-20261105/code/independent_phase_checker/accept_controls.py \
  local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz
```

A local preregistration at `/tmp/padua-independent-accept-controls/preregistration.json` fixed one baseline plus three endpoint substitutions, **60 CPU-s / 90 wall-s** caps, no native engine. The script enforces `RLIMIT_CPU=(60,60)` and the run used an outer `timeout --kill-after=5s 90s` wrapper. Observed **exit 0**, 1.316975 child CPU-s / 1.318031 wall-s; stderr empty. All three controls accepted: raise `S_upper_rows`, raise `lambda_upper_rows`, lower stored origin. Stdout SHA-256 `97546337aece8476ba2c66ca1aa1d93fbf14eddea00f34b286518a0de86e3a97`; local output `/tmp/padua-independent-accept-controls/stdout.json`.

Correctness inspection: each variant deep-copies the baseline and changes only its designated endpoint field. Raising each stored upper by 1 and lowering the stored origin to zero preserves the checker's direction-specific consistency tests. Its mathematical results use freshly calculated independent intervals. The shared cache contains only those independent intervals, keyed by `(kind,n,a,b)`; all certificate structure and comparison predicates rerun for each variant. The comparison excludes only the two documented endpoint-containment diagnostics, while requiring equality of all other returned fields. These controls therefore test successful substituted-bound recertification, not validation of the altered native endpoints.

An additional data-only inspection identified `outputs/all/jobs/41/produce/essential-receipt.json`: 6,425 bytes, SHA-256 `20adb3487797c7e89edef744d73a22de14e138c8cd3c194a393bd08fe3a585b4`, degree 41, **64 S rows / 3 lambda rows**, stored origin `0x1.8070af6899f92p+3`. Every +1 substitution strictly raises its original endpoint and the zero origin strictly lowers it; none of the three cases is an empty-field or unchanged-data control. Scope remains one authenticated old-return tree and three positive substitutions. No new degree campaign, newer onset-512/I25 replay, or universal arithmetic claim follows.
