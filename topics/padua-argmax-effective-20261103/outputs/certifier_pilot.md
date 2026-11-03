# Certifier pilot summary (MEASURED; Claude, 2026-11-03)

Unchanged PD-T210 producer `topics/padua-argmax-alln-20261101/code/part3/finite_general_run.py` at main `440d107`, run as `--n N --seconds 1500`. Single process in a shared cloud container. Certificates are regenerable and kept in scratch only (not committed). No independent replay.

| n | complete | leaves (bound+corner) | max depth | visited | producer wall time | checker |
|---|---|---|---|---|---|---|
| 17 | true | 106 (104+2) | 8 | 211 | 35.0 s | accepted, complete partition, 32.4 s; certificate sha256 2f07c866…6c08 |
| 20 | true | 132 (130+2) | 10 | 263 | 87.0 s | not run |
| 24 | true | 154 (152+2) | 10 | 307 | 229.6 s | not run |
| 32 | PENDING | | | | | not run |
