# Independent compiled checker route

Rules read: `8a1f394739293953e1566fd24a0a193cc78ff26f`.
Base: `440d1079e42c3ef21c40d1cf8870f5b206410c6a`.
Agent: Codex, gpt-6.1-sol medium, explicitly tool-configured by the
orchestrator with fork_turns=none; runtime internals beyond that tool
configuration are unexposed.
Role: delegated independent checker implementation; no Git authority.

Scope: independently port the historical PD-T210 finite-general verifier
into a compiled GMP arithmetic path. No new mechanism, literature,
priority or novelty claim is proposed, so this bounded implementation
work does not require an additional ideas gate. The topic orchestrator
owns the campaign gate and mathematical status records.

Plan (before execution, sent to orchestrator): independently implement
Machin/Taylor, outward 192-bit integer constructor, exact rational tensor
Bernstein conversion, recursive subdivision and leaf predicates in C++;
use Python only for strict JSON, provenance, prefix cover and receipts.
Crossvalidate historical n9–16 and new producer n9–24; reject every
historical corruption case and malformed inputs. Kill criterion: any
metadata or leaf-bound mismatch blocks all finite-range extension claims
until explained and fixed. CPU work stays inside the authorized ~30 min
round; no external dependencies or network access needed.

Independence: read historical reference checker, `finite_general.py`,
`finite_bernstein.py`, `finite_general_controls.py`, provenance guard and
PD-T210 theorem. Did not inspect or import producer-agent arithmetic.
Shared inputs are mathematical formulas, certificate schema, prescribed
rounding sequence and source compatibility convention. Implemented all
arithmetic separately using C++ GMP mpz/mpq. See `code/native_checker/README.md`.

Executed validation of the frozen final candidate:

- Built with `g++ -O3 -std=c++17 .../kernel.cpp -lgmpxx -lgmp`.
- Historical certificates n9–16 all accepted with exact metadata and
  every integer leaf verdict reproduced. n12 historical input has basename
  `finite_n12_pilot.json.gz`; the others use `finite_nN_general.json.gz`.
- New native producer n9–25 all accepted with exact reconstructed
  metadata and integer leaf verdicts. Required overlap n9–24 is complete.
  n24 has 152 bound and 2 corner leaves, 153 splits; its final replay took
  76.029 s under concurrent campaign load. n25 has 162 bound+2 corner
  leaves, 163 splits; 92.300 s. These are wall measurements under shared
  load, not isolated benchmarks.
- All 14 historical corruptions rejected on n9 and n17. Added 22 malformed
  JSON, strict-type, frontier, and compiled-protocol negatives: 36 rejected
  in total on each degree. Complete positives were accepted; genuinely
  partial positives were verified with accepted=false. Receipts:
  `controls-n9.json`, `controls-n17.json`.
- Repeated all 36 n9 controls under `PYTHONOPTIMIZE=1`; every negative
  remained rejected and both positive behaviors were preserved. Driver
  validation uses explicit exceptions, so optimization cannot remove it.
- Compiled signed-floor/ceiling, mixed-sign multiplication, negative
  rational transform, de Casteljau, Machin bracket and exact cosine-axis
  identity controls passed via `unit.cpp`; receipt `unit.json`.

External evidence root: `/workspace/padua-work/checker/`.
Source candidate hashes: kernel
`ae4f20b69c5e676a5d2fefa55c903c8b3efd87a5807a5c5617ca21390a1cab3d`,
driver `b6c7320db2f7cfebf27fe33aa38ffdd45ff719870e3d23e15f845b6e8026eb2e`.

Pending: orchestrator extended the requested replay through n32 when
certificates become available; n26+ is currently running. Different-worker
replay/review is assigned to the independent worker. No theorem status
upgrade is made in this implementation record.

Implementation refinement: the independent reviewer identified avoidable
rational normalization in subdivision. Replaced half-averages and
scaled-product rounding by GMP direct integer floor/ceiling shifts,
without changing the arithmetic result; repeated unit controls passed.
All required n9–24 production and n9–16 historical replays were regenerated
with the final source and binary hashes. Earlier receipts are superseded.

Provenance-final artifact transition: producer subsequently froze native
source provenance and wrote authoritative certificates under
`/workspace/padua-work/producer/final/`. Earlier top-level artifacts have
identical mathematical payloads through n24 but different raw hashes.
Explicit fresh replays of those final-path artifacts are underway; their
receipts use `nN-final-producer.json` and `controls-nN-final.json`. Earlier
`nN-producer.json` receipts remain historical and are not the authoritative
final-provenance receipts.
