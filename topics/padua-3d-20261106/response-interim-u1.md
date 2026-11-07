# U1 response to interim audit01

2026-11-07. Developer Codex, assigned gpt-6.1-sol high technical/mathematical
continuation; runtime model/effort is not independently exposed. Rules and
execution input: `97c323bfae15cf3c76f40802c3ebabedceeb0c60`.
Root owns Git/publication and the combined response. This response does not
supply independent approval or replace the pending formal Claude audit.

## U1-M1 — fixed, material operational change

`parity_fit` now converts values with `np.asarray`, checks rank is exactly
one or two and checks axis0 has exactly the canonical M observations before
any weighted multiplication. Clear `ValueError` messages reject scalar,
wrong-length and rank>2 input. Valid vectors become explicit columns for
multiplication and return vectors; valid matrices retain their RHS dimension.
No cast to real, new finite-value restriction, node change or solver change
was introduced. Existing complex numeric behavior is retained.

Executed developer regression [u1c_api_check.py](code/u1c_api_check.py):
14 cases, both parity families at n1/3/4/7/8/12/16; 112 malformed rejections,
including the two observed silent broadcasts, scalar, short/long vectors,
short/transposed matrices and rank3 data. Valid list, vector, one-column,
three-column and complex paths pass. Every orthonormal basis column is
reproduced, including the corrected top x mode; maximum matrix infinity
residual2.8705208e−14. The separately seeded79query points verify valid
prediction paths. Receipt: [u1c-api.json](evidence/u1c-api.json).

Executed original complete valid-input science replay under the patched
producer identity using the preserved `uc12_replay_u1.py`: all24cases of
original U1 rounds1/2 at n4/8/12/16 match; maximum saved-array delta0.
Receipt: [u1c-science-replay.json](evidence/u1c-science-replay.json).
Original receipts and their historical source hashes were preserved. The
receipt's historical `protocol_commit` names the original science protocol;
`execution_input_head` and working-tree disclosure identify this new run.
The invocation is developer verification, even though the preserved checker
was originally written for an independent supplement. Its receipt status
was explicitly labelled accordingly after execution.

Commands actually executed, one BLAS/OpenMP thread:

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/u1c_api_check.py --raw /tmp/padua-u1c-api-20261107a --out topics/padua-3d-20261106/evidence/u1c-api.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 python topics/padua-3d-20261106/code/uc12_replay_u1.py --scratch /tmp/padua-u1c-replay-20261107a --output topics/padua-3d-20261106/evidence/u1c-science-replay.json
```

This repair and its checks consume zero research rounds. Root will record
the distinct review of the patch; no self-approval is asserted here.

## U1-N1/N2/N3 — accepted scope and continuation response

Retain every auditor outcome: stronger stored U2 noise comparator;
higher-degree QR deterministic wins inside the parity site allowance;
feasible integer replication and heteroscedastic reversal of the optional
iid OLS benefit. No universal budget, target, measure or noise superiority
is claimed. New [continuation protocol](u1-continuation-protocol.md) fixes
an expressly assumed application scenario and evaluates total expected
squared error, with feasible degree choices and every retained target.
The assumptions are illustrative research choices, not facts about AC.
