# D1 round ledger

Input/rules: `04ef28b6139ad15b8cfc31f865c7bb9ba0d56d9b`; Codex, assigned gpt-6.1-sol xhigh; 2026-11-12.

| Round | Prospective record | Publication / go | Actual work / outcome |
|---|---|---|---|
| 1 | protocol.md | Published f9ab1c6; root GO | Completed finite-frame.md; exact seven-case controls pass in 0.50 s measured; independent rerun requested |
| 2 | protocol.md, dated R2 section | Published db8c3cc; root GO | Completed stationary-limit.md: separated stationary orthogonal local limit, intensity preserved; completeness still pending |
| 3 | protocol.md, dated R3 section | Published 613735e; root GO | complete-law.md proves completeness; spectral-obstruction.md gives source-dependent fixed excess; final consistency reconstruction remains |
| 4 | protocol.md, dated R4 section | Published f7caf42; root GO | Completed reconstruction.md; exact all-n Padua spectrum calibration; actual disk/sphere/closest-prior primary comparison; bounded weight corollary proved and general doubling retained OPEN at H1/H2 |
| 5–6 | Ceiling headroom only after local-limit closure by round 4 | Not requested | NOT RUN |

Consumed research rounds: 4/6. Local-limit completeness closed in the written R3 proof and survived R4 reconstruction. Stop successfully; 2 ceiling slots unused, no round5/6 run. Original Chebyshev consequence and bounded inverse-polynomial weight corollary: PROVED with explicit LITERATURE dependency. General doubling extension: OPEN, not rejected. Supplemental independent review [d1-audit.md](../final-check/d1-audit.md) now records PASS for R1–R4, including the fixed inverse-polynomial corollary and conditional H1/H2 route; it leaves general doubling explicitly OPEN. Formal Claude acceptance remains a separate orchestrator handoff.

Actual controls command: `python topics/padua-3d-20261106/code/fd1_controls.py --output topics/padua-3d-20261106/evidence/fd1-controls.json`; 0.49734 seconds measured; Python3.12.14/SymPy1.14.0, deterministic/no seed. Root separately ran the same command with output `/tmp/padua-fd1-controls-root.json`, seven identical rows. Independent Astra actually ran `python -B topics/padua-3d-20261106/code/fd1_controls.py --output topics/padua-3d-20261106/evidence/fdc-d1-controls.json`, seven identical rows, 0.48733 seconds measured; receipt SHA256 `dae51951071a74afa8ef452fcf138e6080d9281cd30e0cf4f7dee4bcea79d74e`, 3261 bytes. Reading those outputs is not another independent run. All finite checks are verification controls; no numerical premise proves the asymptotic theorem.
