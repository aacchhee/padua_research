# PD-T234 (PD-T?argmax-alln-prep-codex-03) — Finite axis-row formula comparison grid

Final registration: **PD-T234**, 2026-11-03. The provisional identifier in the title remains an alias; mathematical statement and historical evidence are unchanged.

ID kind: PD-T.
Aliases: D1 round6;380row comparisons;binary64 cotangent/collision checks.
Split from: numerical checks in gated/d1/r06-row-sum.md; the analytic identities remain gated-codex-12.
Split into: none.

## Statement

On exactly n=2,3,4,8,16 and alpha=0,+.17,-.17,+.4,-.4,beta=0,the existing deterministic Python binary64 script compares380periodic second-row cases. Maximum absolute discrepancies are1.6928680679484387e-12 for cotangent terms versus finite kernel,8.86402062860725e-13 for complete signed rows versus the exact formula,and8.526512829121202e-13 for sign-interval/endpoint absolute rows versus the finite kernel. These are finite implementation checks.

## Definitions

Each degree/phase pair checks all2(n+1)periodic second rows and their nparity first points. Collision values use the finite Fourier kernel according to [r06-row-sum](../gated/d1/r06-row-sum.md); the source numerical collision threshold is a diagnostic convention,not a proof device.

## Assumptions

Python3.12.14 binary64 math,deterministic finite grids,no optimizer,fit,extra phase or outward rounding. The analytic collision completions and pi-row harmonic bound are not established by these finite samples.

## Status by part

Overall status: **MEASURED**.

| Mathematical part | Status | Evidence / remaining gap |
|---|---|---|
| 380formula comparisons | MEASURED | Only the registered25degree/phase pairs |

Candidate / claim disposition: none; this is a finite evidence record.

## Depends on

PD-T101 corrected finite kernel and the separately PROVED gated-codex-12 row identities. Its analytic proof covers general collision parameters; this numerical record is not its premise.

## Checks

Original and separate replay command: `python topics/padua-argmax-alln-20261101/code/gated/d1_rows_r06.py > <scratch>/d1_rows_r06.json`. Frozen producer3,490B SHA256`a9decfcd7293bcfd50ec474b9adb72f16854cf9d24d3aa9979c9fcaf9f394329`. Independent Astra xhigh [round6 check](../gated/checks/d1-r06.md) actually reran it and obtained byte-identical parsed/raw JSON without exclusions. No execution occurred during this rehoming.

## Sources

No external theorem, literature priority or new mechanism is claimed.
This is the durable rehoming required by audit-01 F11 and accepted
response-review-01, not a new scientific run.

## Proof or evidence

Claude [audit-01](../audit-01.md) accepted the numerical claims at their recorded finite scopes; its F11 requested these durable homes. Committed[output](../outputs/gated/d1_rows_r06.json),6,507B,SHA256`560e2677d04a3ab6a2a6d0bbaa6e57ca5ab3e97835fefd15abb7d2e2c0ffb9dc`. All380cases agree to the displayed measured discrepancies. The original note's no-independent-rerun wording is historical; the separate round6 report supplies the completed replay.

## Scope

Formula and collision implementation checks on this finite grid. No general partial-sum inequality,uniform estimate,asymptotic rate or independent numerical verification of the pi-row harmonic bound is asserted.

## Open items

The uncontrolled interior negative partial cotangent sums remain an OPEN quantitative obligation. Direction1 stopped after round6; these comparisons do not authorize another scan or round.

## History

2026-11-03, Codex gpt-6.1-sol high (configured; serving metadata not
independently exposed), preparation input `cdb12257af24ea2542de707b9730f8278d69a168`.
Created from the already recorded finite observations and independent
checks cited above. No new measurement, criterion, bound or source output
was produced; no historical evidence was split or recommitted. This
record separates the measured claim from supporting PROVED theory and
from unresolved all-degree targets.
