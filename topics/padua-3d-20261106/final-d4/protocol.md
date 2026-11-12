# Final D4 protocol — preregistered before execution

Rules/input: 04ef28b (full SHA supplied by the orchestrator's work log).
Developer: Codex D4 worker; assigned gpt-6.1-sol high. Runtime model
identifier is not exposed to this worker.
Authority: approved handoff19 and full handoff18 D4, maximum two rounds.
Ownership: final-d4/, code/fd4_*.py, evidence/fd4-*.json only.

No experiment has run when this protocol was written. The orchestrator must
publish it, the code and the gate before starting any experiment. Numerical
quality is not a general Riesz-basis or asymptotic claim.

## Inputs and gate

The fixed approved mechanisms are C3 and C4 of frontier-assessment; aliases
IDEA?padua-3d-20261106-claude-03/04 are retained, not new final IDs.
Closest existing mechanisms: IDEA-027 (maxvol/norm optimization), IDEA-058
(certified spectra), IDEA-120 (3-D cubature/joint-spectrum target), topic
U2 and S3, and R08 HNF reduction/minima. The mechanism is a known diagnostic
and a finite certificate transfer, not a proposed new construction.
The elementary double-sphere argument removes an imported theorem from
n4..7 determinant minima only; it does not change other lattice objectives.
The complete-registry gate record is in gate.md, completed before execution.

Read handoffs18/19, late-Nov8 LOG, audit04 and A1, frontier-assessment, S3,
R08 reduction/minima, and the source code. Primary mesh statement is being
checked by D5 against Białas-Cież–Kenne–Sommariva–Vianello,
arXiv2311.18656v1, Lemma1/Proposition1 pp3–4. Dependence remains explicit;
if exact statement/normalization/application are not checked, the resulting
whole-cube transfer is CONDITIONAL, never bare PROVED.

Measured read-only input inventory before registration: all source U2
scratch directories in u2-admissible, holdout, transfer14 and heldout16 are
absent from this workspace. Only the optimized n12 (455-node) exact dyadic
coordinate payload is committed. The n4..16 fallback is explicitly a fresh
regeneration of QR on the inherited (2n+1)^3 tensor Lobatto candidate grid;
its basis order is the fd4 lexicographic order. It is not identified with a
historical optimized set. QR coordinates are exact dyadics in this run.
Historical lower-sample rankings do not certify a global best set.

## Round 1 (one research round)

Run the double-sphere restart from q=88,170,292,462 to the known witnesses
q=92,178,304,486 for n=4,5,6,7. Compile and execute unchanged producer and
unchanged independent audit04 enumerator. Each subprocess cap120 wall
seconds; compile cap60 seconds. Both count every HNF in each determinant
window. Store exact per-q counts and all minimizer HNFs under32KiB.
No 18/19 bound, source table optimality label or packing import is used.
Check anticode cardinality and diameter exactly as a sanity check; durable
proof is separate. No global folded/full-rank minimum is inferred.

Run Gram diagnostics and m=2 whole-cube certificates on n4..16 QR fallback
sets; run the committed optimized n12 payload with m=2. Each certificate
has cap120 wall seconds with a check between128-point blocks. Stop that
set at the first cap and record the actual partial mesh coverage and time.
No new optimizer or source-endpoint search is permitted. Seeds: none;
OPENBLAS_NUM_THREADS=OMP_NUM_THREADS=1.

Certificate arithmetic: scale2^24 fixed-point quantizations, guarded exact
int64 matrix multiplication and sum (each potential overflow checked),
exact Fraction residual/Neumann and error bounds, mpmath interval60dps
for scalar Chebyshev mesh coordinates and c_m upper bound. β is proved
from the binary64 evaluation recurrence and rounded UP to2^-40. Matrix
and mesh claims use exact integers/rationals, not measured eigenvalues.
The Gram spectrum and Gram-derived upper expression are MEASURED only.
The continuum mesh factor is dimension-independent c_m, for TOTAL degree
n, as in the named source, applied to the interpolation projector.

## Round 2 (one research round; ceiling, not quota)

If round1 passes inverse/overflow guards, tighten the retained n12 payload
certificate to m=3, same cap120 and arithmetic. No other fit or optimization.
Request an independent execution of consequential code with pinned inputs;
return a mathematically checkable reduction and receipts. If any certificate
fails its guards or cap, record measured infeasibility at that precise
boundary; do not enlarge the round/time budgets or infer impossibility.
The required n4..16 historical-best optimized-set table remains unavailable
where coordinate identity cannot be recovered; the fallback table and its
separate scope must remain explicit.

## Frozen commands and identities

From repository root, unique scratch directories:

```
python topics/padua-3d-20261106/code/fd4_lee.py --scratch /tmp/padua-fd4-lee-r1 --output topics/padua-3d-20261106/evidence/fd4-lee.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/fd4_certify.py --family qr --degrees 4 5 6 7 8 9 10 11 12 13 14 15 16 --m 2 --scratch /tmp/padua-fd4-qr-r1 --output topics/padua-3d-20261106/evidence/fd4-qr.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/fd4_certify.py --family payload12 --degrees 12 --m 2 --scratch /tmp/padua-fd4-payload-r1 --output topics/padua-3d-20261106/evidence/fd4-payload-m2.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-3d-20261106/code/fd4_certify.py --family payload12 --degrees 12 --m 3 --scratch /tmp/padua-fd4-payload-r2 --output topics/padua-3d-20261106/evidence/fd4-payload-m3.json
```

fd4_certify.py SHA256:
1bd5d1eb1183e11e4c89f3d303f280b7b6776d429d8b6f2316312b9e8351a8d2.
fd4_lee.py SHA256:
acc2328ddafeec1cc90c76e0f97ffb7257f1f5dfa74282076f8a34eaa0f2b69e.
Producer enumerator:
e07ad9e51d5b883e7c6d813d396ef32ea0ac24eda253a73f6137f8b8f86feaa4.
Auditor enumerator:
d39563b9340bb0e8384031dac36e2050efb0ab6953c64e165e4006eaca9be503.

Generated receipts≤32KiB each, repository allowance10MB. Retain each QR
set as a lossless base85 binary64 payload in evidence/fd4-qr-nN-nodes.json
(each≤32KiB), so exact finite witnesses remain inspectable. Scratch regenerate
only; identities retained. Do not split files to evade size limits. No
shared registries, Git, handoffs or other-topic files are worker-owned.
