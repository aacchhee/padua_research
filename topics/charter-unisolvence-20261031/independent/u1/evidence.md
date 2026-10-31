# Independent U1 execution evidence

Rules/base supplied by orchestrator: d36722823441dc40c6e19d69a174459348dd309c. Actual independent reviewer: Codex gpt-6-astra xhigh, 2026-10-31. No Git command was executed by this subagent. Cwd for commands: `/workspace/padua_research`.

This is a verification record, not a computer-assisted proof or a distinct general mathematical claim. The hand proofs are in the reconstruction files. No finite reduction from the universal theorem to the sampled cases is claimed.

## Independently written checker

Executed command:

```bash
python3 -u topics/charter-unisolvence-20261031/independent/u1/check_u1.py > topics/charter-unisolvence-20261031/independent/u1/check-output.txt
```

Exit status 0. Source SHA256 `227ecbb04e9130bf9fb06c5d15eb70bdc31b5fcdd3a478bca6799803967a2ce5`. Output SHA256 `6ad6130432037466c382e9b7c7842f31ef5364961d16fb46f6a5c1e2dcb01e4f`; size 11,439 bytes. CPython 3.12.14; Linux-6.18.57-x86_64-with-glibc2.41. Standard-library arithmetic only: `fractions.Fraction` for Q, integer arithmetic modulo primes, and polynomial-basis binary extensions. Random seed 20261031071. Each field/degree row in the output has a SHA256 digest of the exact ordered axis-pair stream. Inputs are generated deterministically by the frozen source.

Executed field/degree scopes:

| Field | Degrees m | Input coverage |
|---|---|---|
| F2 | 0 | all 4 labelled axis pairs |
| F3 | 0,1 | all 18 and 36 labelled axis pairs |
| F5 | 0,...,3 | all 7,200 pairs for m=2; 30 seeded pairs at each other degree |
| F7 | 0,...,5 | 30 seeded pairs at each degree |
| F11,F17 | 0,...,6 | 30 seeded pairs per field/degree |
| F4 | 0,1,2 | all 48,288,576 pairs |
| F8,F16 | 0,...,6 | 30 seeded pairs per field/degree |
| Q | 0,...,6 | 8 seeded pairs per degree; distinct integer nodes sampled in [−20,20] |

Binary extension moduli are t²+t+1 (bit encoding7), t³+t+1 (11), and t⁴+t+1 (19). Before testing, the checker verifies `x*inv(x)=1` for every nonzero element in every listed finite field. These finite arithmetic checks are explicitly executed and are not imported from the producer code.

Observed final result: `PASS axis pairs 9336 checkerboards 18672`. Each pair tests both parities, the exact all-characteristic squared determinant identity, the shortened iff, the original iff outside characteristic two, full alternation determinant one, complementary minors, powers-of-two normalization and central factor nonvanishing. Singular examples are included; notably exhaustive F5,m=2 has 2,400 singular axis pairs, and exhaustive F4,m=2 has 576 singular pairs. No assertion failed.

## Separate execution of the producer's finite checker

Executed after the independent proof and own checker were complete:

```bash
python3 topics/charter-unisolvence-20261031/directions/U1/exact_checker.py --samples 30 --seed 20261031072 --output topics/charter-unisolvence-20261031/independent/u1/producer-rerun-finite.json > /tmp/u1-producer-independent-finite.stdout
```

Exit status 0. Executed source SHA256 `a1ac30c35065c7fb54a29de40e5310303bb01ed7f00d91e036d51a2e7a07c8b5`. Output records CPython 3.12.14, Clang22.1.3. This uses a deliberately different deterministic seed, so it is a separate execution of the producer implementation, not a claim of bitwise replay of its original random stream.

Observed result: `all_assertions: PASS`. There are 1,650 seeded axis pairs /3,300 parity checks across 55 field/degree settings, plus all 288 F4,m=1 labelled pairs /576 parity checks. The explicit F4,m=1 example has determinants [2,2]; the explicit F8,m=2 example has determinants [6,4]. Both have false original quasi-definiteness and true corrected criterion, as asserted in the producer's negative record.

The producer's finite fields are F2,F3,F5,F7,F11,F13,F31 and binary extensions F4,F8,F16. Degrees run from0 through min(7,q−2). The complete settings, counts, explicit inputs and source hash are retained in `producer-rerun-finite.json`.

## Producer symbolic execution

Launched separately:

```bash
python3 topics/charter-unisolvence-20261031/directions/U1/exact_checker.py --symbolic --output topics/charter-unisolvence-20261031/independent/u1/producer-rerun-symbolic.json > /tmp/u1-producer-independent-symbolic.stdout
```

Observed status: ABORTED, not successful. The producer reported that its rational-expression expansion was stalling and was being replaced with factored assembly. At the orchestrator's request, this reviewer stopped its own matching symbolic process: exec session 4613, verified PID 2218 with output path in independent/u1. An interrupt was sent, then `kill -TERM 2218`; the resumed exec session returned exit 130. No completed symbolic JSON was produced by this attempt. This is retained as an executed unsuccessful attempt, not a pending or completed check.

The source computes full direct multivariate determinants only at m=2; for m=3,4 it factors the theorem-derived square and compares exact one-variable determinant slices. Those slices cannot by themselves establish the general m=3,4 multivariate determinant identity. The handwritten theorem supplies the general squared identity; sign normalization is fixed by the slice after polynomial squareness is justified. This distinction is preserved in the successful optimized execution recorded next.

## Final frozen producer replay — completed

Producer freeze source SHA256 `4216b9944c45345709ba11ffbb59b70799432329b646c0c44446da9be2cff56b`; orchestrator subsequently supplied commit `d5a5efbc6228ea21ef38b438ef976260f90ea83e`. Source hash was verified before and after the runs. The four theorem-content hashes remained identical to those in `report.md`. All nine entries and byte lengths in the producer's initial `frozen-hashes.json` were actually checked against disk.

Executed commands:

```bash
python3 topics/charter-unisolvence-20261031/directions/U1/exact_checker.py --samples 20 --seed 20261031 --output topics/charter-unisolvence-20261031/independent/u1/producer-final-finite.json > /tmp/u1-producer-independent-final-finite.stdout
python3 topics/charter-unisolvence-20261031/directions/U1/exact_checker.py --symbolic --output topics/charter-unisolvence-20261031/independent/u1/producer-final-symbolic.json > /tmp/u1-producer-independent-final-symbolic.stdout
```

Both exited 0. Python3.12.14, Clang22.1.3; symbolic mode SymPy1.14.0. Finite output: 1,100 seeded labelled axis pairs /2,200 parity checks, the same 55 settings as the earlier finite execution, plus 288 exhaustive F4,m1 axis pairs /576 parity checks and the two explicit counterexamples. All assertions PASS. Symbolic output: all six m2,3,4 parity cases PASS, with direct full multivariate determinants at m2 only and exact one-variable slice comparisons at all six settings. The complete factor expressions are retained in the JSON.

These final independent outputs were actually byte-compared with `/workspace/padua-cold/charter-unisolvence-20261031/U1/exact-fields.json` and `symbolic-factors.json`, respectively: **both byte-identical**. This is a separately executed exact replay, not merely inspection of producer output. No successful result is attributed to the aborted older implementation.

| Independent output | Bytes | SHA256 |
|---|---:|---|
| producer-final-finite.json | 10186 | 2e11931b57274e3444a93ea92755fac79b1cbd2d4d1fd24136760a9c4f3db937 |
| producer-final-symbolic.json | 18648 | df44efc4f554d14f825f6ec42eb917cd73b1e515e0da55193b8db52034728342 |

## Independent check of the compact symbolic summary — completed

The prose `directions/U1/symbolic-factors.md` adds compact A(H), B(H), Q(H) expressions and tables beyond the checker's raw strings. This reviewer separately wrote and executed:

```bash
python3 -u topics/charter-unisolvence-20261031/independent/u1/check_symbolic_summary.py > topics/charter-unisolvence-20261031/independent/u1/symbolic-summary-output.txt
```

Exit 0; SymPy1.14.0. Source SHA256 `6a090d79f85642794725d6dce4c3b96b9495ce5325721091b4f6272e50d32942`. Input is the final independently replayed symbolic JSON at SHA256 `df44efc4f554d14f825f6ec42eb917cd73b1e515e0da55193b8db52034728342`. Output SHA256 `3e55091a09a0d5dee9704f1dd8560bb39402123816b51b6642257116fe3d687b`, 642 bytes.

Observed: `PASS all 6 symbolic summary cases`. Every listed axis minor agrees identically with the compact formula, including `Q(H)=−(β²+αaβ−αγ+α²b)`. The exact determinant expressions agree with the signs and every difference/non-difference factor multiplicity for m2,3,4 and both parities. This verifies a readable summary against the independently generated symbolic expressions; it does not change the full-direct-versus-slice scope above.

## Input/rule provenance

The full AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, state/IDEAS.md (including obstruction and disposition tables), state/CURRENT.md, literature/INDEX.md and baseline-candidates.md were read. Initial literature coverage had records01–36; the later records37–40 and U1-COMPARISON.md were also inspected on producer comparison. The novelty-gate search used alternation, checkerboard, Hankel, quasi-definiteness, characteristic2 and Vandermonde across the idea registry, theory and literature, excluding producer U1 proof files until reconstruction was complete. No new research direction or novelty claim was generated. The shortlisted candidate remains U1a–c; the prior-axis-factor obstruction is preserved.

Rules-file SHA256 values checked during this work:

| File | SHA256 |
|---|---|
| AGENTS.md | 60bfe28edf232c69948efdd2f7a48edfd99af52644513a2fc378c866e742cb60 |
| agents/WORKFLOW.md | b1c1c14c83e02bf38283159f81ec278ae336ab56c95d0c026b9ada3314d1ffaa |
| agents/codex/CODEX.md | 28ca2976171a34860e2bf8d24292af6b92bee34ce22ba1e497891b366533083b |

The mutable registry snapshots are context, not executed mathematical input. No credentials were read. The cloud environment skill/status check reported current enforced restricted network; no network action was used in this reconstruction.

## Storage

The 11 KB main output and small JSON rerun outputs are necessary reproducibility evidence, individually below1 MB and collectively below5 MB. They are local review artifacts in the assigned directory; this subagent neither committed nor pushed them. The orchestrator controls retention and repository placement. AC's Windows cold-storage destination is known from CURRENT.md, but no delivery to it is claimed. Temporary stdout copies under `/tmp` duplicate the JSON outputs and are not evidence dependencies.

## Integration verification

After root's canonical path/ID migration, an actually executed Python command read `integration-impact.json` and `final-id-map.json`, checked the four integrated U1 hashes, reversed all exact final-ID substitutions in memory, and required that each resulting byte string recover the original reviewed hash. All four passed; output retained in `integration-check.txt`. No Git command was involved. This does not modify the historical execution commands above: their old paths are resolved by the source checkpoint and integration map.

Final artifact identities and sizes are listed in `manifest.json`. The two documentation findings in candidates.md are root-owned reference/status corrections, not mathematical or checker modifications, and are preserved in the final report for integration disposition.
