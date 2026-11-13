# Reader repair execution, 2026-11-13

This records data checks, not a new native campaign. Rules read at
941aa335e60ca7058c8a0113faa76e31217f4753. Codex coordinates under AC's
gpt-6-astra high request; gpt-6.1-sol medium developed the reader repairs;
a distinct gpt-6-astra high reviewed them and independently reran the actual
original return. The [supplementary review](supplementary-reader-review-20261113.md)
records its own commands, parser finding and correction.

## Authenticated inputs

AC uploaded `padua30.zip` and two return parts. They were read as data;
no instructions or launch scripts from the archive were followed. Joining
part-aa then part-ab produces the recorded original return, not the new
onset-512 return.

| File | Bytes | SHA-256 |
|---|---:|---|
| padua30.zip | 25111335 | aac08e5f25bd27b2710de22039efd229b4ee67d8c1e3ffef9456af200e1f74d2 |
| part-aa | 25165824 | 9b202cb653e06c12b80492049c509671aabaaf3b6ce2f8e4502d418ca98f03bd |
| part-ab | 10879662 | 983c70084c5fe4674827bc1d045f4c8f64a1d5392a054d765f7806cbc0bb0b6a |
| joined return.tar.gz | 36045486 | b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a |
| runtime_manifest.json | 54003 | 5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16 |

The ZIP CRC passes. Safe regular-file extraction was bounded; all 250 runtime
manifest members match byte lengths and hashes. The 180 authenticated
arithmetic assets were also restored to the manifest's repository-relative
local-output paths. The supplied package contains a historical unrepaired
verifier; execution below uses the repaired repository verifier, SHA-256
`2d26886fa38089815712edcceccd4ac893fea9d8e6092afbd4c0faac7b569cef`.

## Root's actual rerun

A prospective local record caps this one data-only run at 180 CPU-seconds
and 240 wall-seconds, with no retry. From the repository root:

```sh
python3 -E -B topics/padua-argmax-bridge-20261105/audit-04/code/e4-code/observe.py root-compact local-output/argmax-bridge-20261105/audit04-response-20261113 240 -- prlimit --cpu=180:180 python3 -I -S -B topics/padua-argmax-bridge-20261105/compact_pack/verify_compact.py local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz --package local-output/argmax-bridge-20261105/compact-release-aea62883/padua30 --manifest-sha 5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16 --expect-plan all
```

Observed exit 0, no timeout, child CPU 5.536 seconds, wall 5.542 seconds,
maximum RSS 172916 KiB, ECHILD after reaping, empty stderr. Output enforces
`complete_plan`, `expect_plan: all`, all 280 pairs (560 certificates), exactly
degrees 41..319 plus 511, sampled full histories 199 and 238. There was no
native fresh evaluation. Unsampled full histories retain the existing
server-validation scope. Independent replay is in the supplementary review.

Local output directory:
`local-output/argmax-bridge-20261105/audit04-response-20261113/`.
The prospective record is 737 bytes, SHA-256
`55c4c0c3bcc0db027a8762c64165707216f0ec4fd8f9b50659bed2eacc3c1fb0`;
root observation 671 bytes,
`9e23b0a7e2fff9a8626e82e01e57d16072244abc8a545f9bcdbe0f0a54c9d1e0`;
stdout 2781 bytes,
`3f6605da9c09eaa69f7a9daf30c6cfdf0ff6ef424369cf420527e246ed841767`.
These are local working outputs; durable external custody is not claimed.

## Supplementary controls

`python3 -E -B topics/padua-argmax-bridge-20261105/code/local_onset512_campaign/check_reader_repairs.py`
passes all 40 developer controls. The synthetic positive fixture adapts
arithmetic and sampled closure and therefore supplies no actual onset-512
certificate evidence. The distinct reviewer adds independent strict-parser,
type, duplicate, pin-order and malformed-member controls.

`python3 -E -B topics/padua-argmax-bridge-20261105/code/independent_phase_checker/runtime_probe.py`
passes all 31 frozen arithmetic controls plus four finite runtime probes
under Python 3.12.14 / NumPy 2.3.5. This does not prove universal IEEE behavior.

`python3 -E -B topics/padua-argmax-bridge-20261105/code/independent_phase_checker/accept_controls.py local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz`
passes three positive substitution controls at the authenticated old n=41
witness: raise stored S uppers, raise stored lambda uppers, lower the stored
origin lower. The mathematical result is unchanged; endpoint-containment
diagnostics may change. No frozen historical source or input is modified.

## Runs still needed

The actual canonical onset-512 reader run, new-range I25 data checks and
cross-archive witness comparisons in audit-04/WHEN-INPUTS-ARRIVE.md remain
unexecuted. The newly supplied files do not contain those missing archives.
Neither the 632 MiB unsampled histories nor historical PDF bytes are present.
AC requests retention and transfer if the prior workspace is reachable;
there is no connected tool exposing that workspace's filesystem. No custody
gap is silently accepted and no replacement native campaign is authorized.
