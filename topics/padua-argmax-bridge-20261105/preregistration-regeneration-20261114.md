# Paper-supporting regeneration, 2026-11-14

New campaign ID: `padua-argmax-paper-regeneration-20261114`.
Input/rules head: `cc2f9ad10c2b5baf29af1887e681b851e9e9dc60`.
Developer: Codex, inherited runtime model/effort metadata as recorded by orchestrator.
This is evidence regeneration with no new mechanism or novelty claim, so the novelty gate does not apply. AC explicitly requested regeneration of missing paper-supporting evidence; historical ZIP/PDF identities are not reproduction targets.

The full machine preregistration is retained only at the output root. The small committed `code/regeneration_20261114/frozen-inputs.json` pins its exact identity. The full preregistration pins the unchanged runner, new wrapper, frozen source/data and trusted arithmetic bytes, helper sources, Python executable and trusted runtime manifest. Root must commit this machine preregistration identity and wrapper before any native action. The old runner's hardcoded historical preregistration function is not used; its `controls` and `run` functions are called unchanged.

From the repository root, the preparation already performed is:

```sh
python3 -E -B topics/padua-argmax-bridge-20261105/code/regeneration_20261114/campaign.py prepare --input-head cc2f9ad10c2b5baf29af1887e681b851e9e9dc60
```

After the orchestrator confirms the freeze commit, execute once in order:

```sh
python3 -E -B topics/padua-argmax-bridge-20261105/code/regeneration_20261114/campaign.py controls
python3 -E -B topics/padua-argmax-bridge-20261105/code/regeneration_20261114/campaign.py pilot
python3 -E -B topics/padua-argmax-bridge-20261105/code/regeneration_20261114/campaign.py remaining
```

Output is the exclusive directory `local-output/argmax-bridge-20261105/regeneration-20261114/`; controls use the separate exclusive sibling `regeneration-20261114-controls/`. Pilot is the actual n=320 primary/fresh pair, followed by n=321..510: 191 degrees and exactly 382 native engine passes. Each fresh pass consumes its own new primary certificate. No retry, rescue or resume is allowed. Stop admitting new cases on the first failure; allow active cases to terminate, record terminal accounting and preserve every unsuccessful attempt.

The restored trusted release is `local-output/argmax-bridge-20261105/compact-release-aea62883/padua30/`. Safe hash preflight authenticated all 13 frozen source/data rows and 180 arithmetic files. Observed resources are 4 CPU quota, 16 GiB memory and inherited affinity 0..4. The runner uses cores0..3, four workers, 2 GiB address-space and 260 CPU seconds per case; frozen engine cap120 CPU seconds per pass, wrapper wall cap1050 seconds. Historical estimate is approximately2700 CPU seconds and13 minutes wall with four workers; new timings remain observations.

Every pass receives full unchanged `validate_pass` validation, exact rational reconstruction, native/raw linkage and dependency checks. The original runner compares the retained primary/fresh proof fields and exact primary certificate linkage. Immutable artifacts may use byte-preserving hardlinks; no histories, logs, raw outputs, native sources, translation units, binaries, libraries, receipts or failed records will be pruned. Full histories and external dependency bytes will be included in an off-Git delivery artifact with inventory and checksums after completion.

Independent I25 reconstruction is a separate delegated execution with its own preregistration. New local campaign/result inventory and a separately reviewed reader/profile will identify this generation explicitly, without changing historical archive/default runner pins or using synthetic proof adapters. Mathematical adoption remains pending that independent reconstruction and review. Large outputs stay outside Git; only small necessary evidence summaries and manifests may be committed under workflow limits.

The freeze commit gate is an orchestrator operational requirement; the wrapper enforces the frozen identities without invoking Git.
