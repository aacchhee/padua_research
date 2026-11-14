# Synthetic controls01: stopped on fixture failure

Executed once at published source `4787aea51b041317ae359090d8d4daaab437adf8`
with exact command in PREREGISTRATION.md. Direct tool observation: initial
session82529, final output chunk f002d8, **exit1**. Candidate and harness
hashes matched their preregistration. No retry or source mutation.

Raw output remains `/workspace/p02c`; receipt SHA256
`3c062a9d588e43929b81f358ba12cc2fa33858047502b6222998e76ada0548d5`.
All stdout/stderr and fixture trees remain retained there, off Git. Cold
storage is pending, not claimed. Serving metadata remains unexposed;
reviewer requested/API-accepted gpt-6-astra medium.

| Case | Exit | Wall seconds | Observed result |
|---|---:|---:|---|
| status7 | 0 | 0.123 | Actual exit7 preserved. |
| ignored | 0 | 0.070 | Refused, normalized, original SIG_IGN in stderr. |
| echild | 0 | 0.069 | Missing actual status raises, never exit0. |
| hup | 0 | 0.422 | Dispatcher cleans fake worker descendants. |
| quit | 0 | 0.422 | Dispatcher cleans fake worker descendants. |
| parentdeath | 1 | 12.178 | Fixture failed before fake engine started. |

Failure diagnosis from parentdeath.stderr: the harness imposed hard
RLIMIT_CPU12, then the unchanged real worker attempted its configured
RLIMIT_CPU260 and Python raised `ValueError: not allowed to raise maximum
limit`. This is a reviewer-authored fixture incompatibility, not evidence
that the candidate's parent-death handling failed. The observer killed/reaped
one retained sleeping fake supervisor, PID214901. Parent-death behavior
remains untested. Reboot, preflight, deletion, partial, ZIP bounds and pin
cases were not reached. No compiler, native oracle or scientific execution.

The focused continuation is preregistered separately in PREREGISTRATION-02.md:
only parentdeath and the six unreached cases, fresh output, with only that
fixture's wrapper CPU profile reduced to10. Original harness/output and actual
candidate260 limit remain unchanged. Publication/root release required.
