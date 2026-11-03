# Scientific checker optimization hardening — preparation N1

2026-11-03. Developer Codex, configured/requested `gpt-6.1-sol` high; serving metadata unavailable. Source/rules input `cdb12257af24ea2542de707b9730f8278d69a168`. Parent assigned this bounded task under handoff11; AC subsequently requested finalization without another Claude round. Independent final review belongs to the parent's distinct Astra checker, not this developer record. No new mathematics, numerical scan, degree or proof claim is introduced.

## Acceptance boundary

Seven current proof/check-control entry modules now refuse optimization before imports or scientific execution, including when imported under an optimized interpreter:

```python
if not __debug__:
    raise RuntimeError("Scientific verification requires Python assertions; do not use -O or PYTHONOPTIMIZE.")
```

This preserves the existing asserted predicates for ordinary execution and prevents `python -O`, `python -OO`, or `PYTHONOPTIMIZE=1` from producing unchecked success. The guarded modules are the standalone n2 proof, n8-field checker, general-certificate checker, general controls, exact O-Lt checker, independent O-Lt reconstruction and D3 checker. No archived certificate, receipt, audit/support script or mathematical producer/arithmetic body is modified.

Numeric screen/producer scripts remain source-pinned historical producers, not proof acceptance interfaces; finite producers still set `accepted=False`. The arithmetic library's standalone self-test and numerical sanity assertions are not promoted to optimized proof evidence. `d2_symbolic_r01.py` already computes booleans and explicitly exits nonzero on failure, independent of assertion optimization. Frozen independent harnesses remain immutable historical artifacts; those importing current guarded acceptance modules abort under optimization. No claim is made that every historical script in the repository was rewritten.

## Frozen source pins and the precise compatibility rule

The frozen general certificates pin `finite_n2_exact.py` as a producer dependency. D3 additionally pins its own checker source. Editing these sources solely to add early refusal would otherwise reject all those unchanged certificates. The new [proof_runtime.py](../code/part3/proof_runtime.py) handles only this explicit source-version metadata delta:

1. A recorded source map equal to the complete actual current map is accepted as before.
2. Otherwise require exactly one occurrence of the exact guard byte block in current n2; verify its actual file SHA matches the actual map; remove only that block and compute the historical n2 SHA.
3. For D3 only, verify the checker's actual SHA and require exactly one occurrence each of its guard, the literal helper-import line and the literal four-line compatibility call. Reverse those exact three edits to the original one-line source-map assertion, then compute its historical SHA.
4. Compare the complete resulting historical map to the recorded map. Every other source key/value remains exact. Extra edits, duplicate blocks/imports and mathematical predicate changes fail against the frozen historical pin. No AST normalization, ignored key or generic source bypass is used.

This is an explicit metadata compatibility change. Mathematical acceptance assertions, arithmetic, partitions, bounds, witness tests and field/source constructors are unchanged. [source-compat-controls.py](source-compat-controls.py) reconstructs all seven original files **byte-for-byte** from the enumerated changes and compares them to the actual input Git blobs; for the two metadata adapters it reverses only the documented exact edits. Thus predicate preservation is checked more strongly than a visual claim.

The historical n2 SHA is `a5f00e6039d6ec76660cac90fb5720e0d6721348ed34c9e62775e1125d3e87c2`; historical D3-checker SHA is `5f43f69a427c415542848f8ae9e337c69b3a5b8f822e78db38e095a0a2c9a358`. No certificate source pin is rewritten. The n8 field certificate does not pin n2 and needs no metadata adapter.

## Source identities

| Topic-relative file | Input SHA-256 | Current SHA-256 |
|---|---|---|
| `code/part3/finite_n2_exact.py` | `a5f00e6039d6ec76660cac90fb5720e0d6721348ed34c9e62775e1125d3e87c2` | `8c74170cadee19cfd805734c13182e47734958d7495a8a0109c582631fc7cab0` |
| `code/part3/finite_bernstein_check.py` | `096e60475252ebeff871efd3b87eab8029fef0971c0f3b94bfd1ad83a71f6fa1` | `687eb644a314e2488bfed99deb3a8519b353235282a670ceacdb4fb36ef66988` |
| `code/part3/finite_general_check.py` | `f9d33648eb05f9539f32c7d8f9003ed61410c7acfff9095bf7ea665989ac8281` | `d2edd6bc5c1ef1193ad44a8fb5decd859e92d960717e1a696743e43c77f337cb` |
| `code/part3/finite_general_controls.py` | `c850f635736882de65134465279744c9e4990f08361824c8b13498e0136c030b` | `81022c0a1477454f177e99665fe0b720f5bacb35c2fd1a826fd591eccf77e884` |
| `code/part3/pairing_exact_check.py` | `39a701f79f60052272a7af6fadbe021761e3becd33793c1e1746033eb4705098` | `80e822f19283603da728c5e3a787ff386654b0d075380730b24192452ddcaf8c` |
| `code/part3/pairing_independent_reconstruction.py` | `cc3edb6dd23279ba623ab891de2dac0b7b65df6467322998dc8622b41a51a83b` | `2fbac4abfde35917ba7a9896c8fafd8c041d11c5dcc4120ce8ecbe53d3512aee` |
| `code/gated/d3_edge_check.py` | `5f43f69a427c415542848f8ae9e337c69b3a5b8f822e78db38e095a0a2c9a358` | `09165fcf6b05de17667db1e109ab06d09c1bea600649ec6d404342ea085e0308` |

New metadata helper SHA256: `6c998078e373c1281bac1dfc11078135dfe036d28c8718dbbec45606e8789e9f`.

## Executions and scratch discipline

Commands from the repository root:

```text
python -B topics/padua-argmax-alln-20261101/prep-support/source-compat-controls.py
python -B topics/padua-argmax-alln-20261101/prep-support/checker-replay.py
```

The compatibility command executes seven cases, including extra n2 text, doubled guard, changed D3 mathematical comparison, doubled adapter import and an unrelated forged source pin; intended historical maps pass and every mutation is refused. It also verifies exact old-source recovery for all seven entry files.

The replay command creates a fresh scratch mirror preserving source bytes and repository-relative imports, copies the frozen certificates and only required materialized dependency trees, and retrieves the single cold-stored historical pairing input by its pinned Git blob identity. It never writes old evidence into the source checkout. It executes all21optimization refusal cases, ordinary standalone n2, the field n8 certificate, every general n8–16 certificate, general/field/independent mutation controls, exact pairing and independent reconstruction, D3 with17malformed controls, and two additional forged-n2-source-pin CLI controls. All destinations and generated results remain in the owned scratch mirror. Normal checker result metadata records new checker SHAs; mathematical predicates and frozen inputs remain unchanged.

An initial complete run reached all checks, then its too-broad final monitor noticed concurrent authorized theory/LOG edits by other workers. That was a harness-monitor failure, not a scientific checker failure. The corrected harness monitors scientific code/evidence/dependency inputs and excludes the parent's packaging metadata; it is rerun in full. Source checkers did not change between those executions.

Final corrected run: **PASS**, 40 subprocess invocations in 160.933s on Python3.12.14/Linux. All21optimization refusals pass; n2 and all10existing field/general certificates replay;14general,5field,4independent-general and17D3malformed controls reject; exact pairing/reconstruction pass; D3 verifies10pairs and8witnesses; two forged n2 pins reject. All242monitored scientific input files retain their byte hashes. The seven exact-source compatibility probes also pass. The receipt normalizes only temporary path/executable prefixes through explicit command aliases; omitted stdout hashes are explicitly the empty-output hash. Source identities and arguments are retained.

The final compact receipt is [checker-hardening.json](checker-hardening.json). Full raw stdout/stderr are ephemeral scratch logs named in that receipt by SHA, not new claimed permanent proof evidence. Independent final audit must assess the exact metadata adapter and test its refusals; this developer does not self-approve it. The existing accepted finite proofs and mathematical audit scopes are retained without assigning stronger status.
