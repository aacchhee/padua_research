# Independent technical check — actual compact return

Date: 2026-11-07. Rules read at
`9847ee1ce5433f1f58718ec66095015c2d93f328`:
AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md; handoff12 and recent
LOG read. Role: supplementary independent technical reviewer, requested
Codex gpt-6-astra medium; serving metadata unexposed. Scope contains no new
ideas, novelty or mathematical development, so the novelty gate is inapplicable.
This check supplements the pending substantive Claude audit; it grants no
readiness and does not independently reprove the analytic reductions.

## Inputs and actual independent execution

Actual return at
`local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz`:
36,045,486 bytes, independently rehashed SHA256
`b00fd57f85ce6d96a6c1fa01e2307abd815088bb8fcb28b1587657ef142b109a`.
Trusted package is `local-output/argmax-bridge-20261105/compact-release-aea62883/padua30`,
manifest `5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16`.
The released source/checker was used; no archive code was executed.

Executed once, separately from developer verification:

```sh
python3 -I -S -B topics/padua-argmax-bridge-20261105/compact_pack/verify_compact.py local-output/argmax-bridge-20261105/actual-return-20261107/return.tar.gz --package local-output/argmax-bridge-20261105/compact-release-aea62883/padua30 --manifest-sha 5b89fa66e742952497f99a49110a965ada2828b1861917268d3074af0eb22a16
```

Direct exit0, execution session66571/completion1840e3. Output is
`local-output/argmax-bridge-20261105/independent-actual-return-20261107/verification.json`,
SHA256 `ef09be693b89362067fe147aeed4158b7bc553ac6497e8d0faf1f5c921335f93`;
stderr empty. This independently checks all 280 rational certificate pairs,
exactly41–319 and511: all273 residual degrees and seven controls
41,42,63,64,159,160,511. No omitted, unfinished or never-started degree remains.
The 4,323 payload inventory, hashes, source binding, accounts, exits and
certificate links passed. Seed
`7c79b8e401d9a32f8233f8371c441cd28d82dedd60e46e7c73d211ab099d01d2`
reproduces ordered sample[199,238] from the exact273 residual population.
Both sampled original full produce/verify histories passed native endpoint,
compiled source, binary, translation-unit, header/toolchain, mapped arithmetic
and runtime closure checks. The other full histories were validated on
Syvert by the released collector; their raw bytes were not independently
inspected here and are not claimed to be retained in cold storage.

Sample primary identities (also independently rehashed extracted files):

| Degree | Bytes | SHA256 |
| --- | ---: | --- |
|199|5680|`4e58080f60980a94c485e0d8a25558ed2997f38d35ccdb7718533c66ca9becfd`|
|238|5681|`52f26a6ff367112122acb5acfd0f0e00b5f061c8a1849cc69383bbf4b2e53043`|

## Fresh native verification: preregistration and result review

Before either fresh engine call, read the complete developer runner and
preregistration, checked their hashes and sample identities, and inspected
strict Popen/default SIGCHLD/cleanup implementation and unchanged engine caps.
Runner SHA256 `c281852c1dc91268af384d164034bfba71cec8bc3d09158430cf00248252287e`;
preregistration SHA256 `23f16a7c29c82f62a9552bb15dcab6a2fcf2f066527d6e5d5575c9a5607f3c2f`.
The commands specify exactly two sequential verify-only calls, exclusive new
outputs, returned primary inputs and the pinned offline arithmetic libraries.
The wrapper resource-limit difference is disclosed canonically in [LOG.md](LOG.md).
The pre-call review did not catch that difference; the root raised it after
review, but both calls had finished before the developer received the request.
No retry or retrospective alteration was performed.

The developer executed the two calls; this reviewer executed **zero** native
engine calls. Both directly observed engine exits were0, SIGCHLD default,
ECHILD established, no cleanup victims, complete final accounting and no
first failure. Fresh results:

|n|CPU through summary (s)|Observed wrapper wall (s)|Native calls|Nodes/leaves|
|---|---:|---:|---|---|
|199|10.162178|10.163065|45 S + 3 lambda|51/26|
|238|11.856834|11.763267|45 S + 3 lambda|51/26|

Independently ran the released `validate_pass` on each actual fresh result,
using a read-only local-path adapter. It rehashed301 distinct identity paths,
reconstructed rational proof fields, checked completed native-call endpoints,
source/build/translation-unit/dependency/runtime/arithmetic closures, stage
accounting, descendant completion, final120CPU bounds and original certificate
linkage. All substantive proof fields exactly equal the corresponding returned
primary: tree, pi bracket, S upper rows, origin lower bound, lambda upper rows,
norm, floor, corner, analytic far claim, and full rational verification result.
Each fresh pass has positive strict margins and the same accepted analytic
and exact-arithmetic dependencies as its primary.

Fresh receipt SHA256:

- 199: `2bc59c54cabc399244403705fe68ac6d78f7db8bc49d7a7134f71a8d58b445fa`.
- 238: `de740bcb43442864fad9eab033d3948367a9f1212e30433a9b6e1565a542c198`.

The independent data check lives in the above independent-output directory:
`check_fresh02.py` SHA256
`55f337ccbe0d5cfeffdeb2f630d0e371c31ce3767ac599d1eaec0262029a1c5e`,
run with `python3 -I -S -B`; direct exit0/session22962/completion66c923.
Output `fresh-check02.json` SHA256
`3623e7805e87c8e37537201c7b8510197e02b5c4e08f0200e670a71899b80ccd`.
First adapter `check_fresh.py` is preserved: it failed at an embedded original
certificate's Syvert absolute path, not a proof check. The02 adapter resolves
those old identities from the already validated archive/trusted package;
all fresh identities are checked against actual current files. No native
rerun was involved in either data-only adapter execution.

## Returned workload observations and limits

From the returned280 complete accounts per mode, produce CPU through summary
ranges10.441089–23.217470s (median16.9790065), verify10.097595–22.497275s
(median16.0150165). Their sums are4758.151296 and4536.896717 CPU seconds;
these exclude subsequent return work and are not the campaign elapsed time.
The supervisor records10496.346196 waited-descendant CPU seconds plus
12.181273 self CPU seconds. Per-pass wall maxima are26.153328s produce and
24.753369s verify. Trees range51–101nodes and retained S premises43–64;
retained premises are not a claim about all discovery calls. No actual peak
memory measurement was established from these compact records, so none is
inferred from worker count or caps. Statistics are retained in the independent
output directory as `statistics.json`.

**Finding/disposition:** no unresolved scientific-data discrepancy found in
this technical scope. Operational conformity is limited by the canonical
wrapper-cap disclosure. Evidence supports the completed compact checks and
two fresh retained-witness verifications; theorem scope and readiness remain
subject to their distinct mathematical review and Claude audit. Exact source,
compiler, arithmetic and interval-kernel trust assumptions remain explicit;
sampled re-execution is not independent re-execution of all273 degrees.
