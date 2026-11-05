# Supplementary independent mathematical check — C2/C3

2026-11-05. Checker: separate Codex agent, assigned `gpt-6-astra`, high.
The actual model identifier is supplied by the parent allocation; no
separate runtime model attestation API was available. This is an
independent reconstruction and finite check, **not the required Claude
audit**, which remains pending. The checker initially changed only this record and
`code/independent_odd_check.py`. At the parent's later explicit request,
the checker updated completion metadata in the three checked theory
files. No proof was changed and no mutable Git operation was performed.

Rules read at full head `ad503cb0603fc017444b0aa732240981eefa4d24`:
AGENTS.md, agents/WORKFLOW.md, agents/codex/CODEX.md, and handoff 01.
Initial accepted base: `21dbfc90257b952d8923f6d01739d12aa8d6e0a1`.
The parent subsequently integrated main's PR22; at final input hashing
the workspace head was `ef9723bef6dd061109db1237f3338626093e1052`.
The following file hashes, rather than a moving working-tree head,
identify the checked mathematical candidate.

## Verdict and findings

**PASS within scope; no unresolved mathematical finding.** The odd-m
fixed-node weight limit, whole-grid majorant, two carriers, all-parity
divergence, and exact continuous norms have complete analytic arguments
under the written assumptions. The new one-sided spectral constants
are valid. No sharp spectral limit, matching opposite bound, effective
onset, or finite negative witness is established by these records.

One input issue was identified independently and communicated to the
developer before completion: handoff C3's `1/9` and `1/36` optimize
unnormalized sampled-energy coefficients. They are not justified as
spectral constants without division by continuous squared norm. The
submitted growth record correctly repairs this. The corresponding
limiting squared norms at the selected carrier parameters are about
3.75098821137026 and 2.17372444063582; neither is one. The resulting
proved one-sided constants are approximately 0.02962182359686 and
0.01277888643956. They are not claimed optimal even in the normalized
carrier family. No accepted predecessor proof needed alteration.

## Pinned candidate

Paths below are relative to this topic.

| File | SHA-256 |
|---|---|
| theory/odd-weight-asymptotic.md | `7e5ae87461abd0270479f3a4513201db7a5a414b9cf682c8160db5c075f0711a` |
| theory/odd-carriers.md | `490672447af2c4999e50aab7ecd4636c29a9f1a09d401db6adc7757ea95fe39d` |
| theory/growth-carrier-bounds.md | `0e72d4276677791182dbb6d767a9f5a4d169caca3b90d4f0313a0af1cd4ca594` |
| novelty-gate-math.md | `c071baaa2a382413846eef9ec3ce4ad435b036dce370c349a5773367c529ab8e` |
| code/independent_odd_check.py | `2590f394b64e469a968c5d0e899dc3b66eea7fd8cd17b30fc0d25c211855cec2` |

Accepted proof dependencies read in full and reconstructed within the
needed scope:

| Repository-relative file | SHA-256 |
|---|---|
| topics/padua-mz-2d-frontier-20261105/theory/f12-local-weight-asymptotic.md | `0cb69640bb49b5a4f58f9932504479c4982e7e3513db40db8715a1b9832d4703` |
| topics/padua-mz-2d-frontier-20261105/theory/f12-eventual-negative-carrier.md | `bf7c8e41fa18cb4d0fe97d751410fd3f82025da5473083b9688f65f90bf7d4ba` |
| topics/padua-mz-2d-frontier-20261105/theory/f12-eventual-upper-carrier.md | `029609ea0a9bec77a34d83ae11a8692be7a1762eccab981c99e79bbf6def1d14` |
| topics/padua-mz-2d-frontier-20261105/theory/f3-fixed-ratio-threshold.md | `ce4e1f764b2274e2cdbddd09636b823f863e099104b39415f2b7bd0b27a9edec` |
| tracks/mz-constants/theory/mz2d-lower-corner-weights.md | `38e730b7f8a11eea7265dc02d3163d128d7092a1a9cd9a38e8b6742daf87b56a` |
| topics/padua-mz-2d-20261101/definitions.md | `4ac0e391859a14e4d6f752f1244df0701e99d9b3d8ab8570bd632520f517c7db` |

The accepted cardinal identity PD-T101 is taken in the exact normalization
quoted by PD-T111; this check does not re-audit PD-T101's full upstream
proof. Independent small-m moment-system solves below test that
normalization without using the cardinal identity as their constructor.

## Analytic reconstruction

For odd m, integration removes the exceptional x term exactly, because
h_m=0. It does not exchange the exceptional coordinate. With
R=(m-1)/2, the same rectangle-minus-triangle identity holds for every
integer R. Both high-frequency phases converge to their indicated
integer multiples of pi, although neither is exactly that multiple.
The logarithmic contribution from the two thin corners is therefore
unchanged. The order of limits R first and then strip width is valid.
The numerical constant 8192 in the uniform bound safely dominates the
displayed coefficients for R>=2. The j=k=0 limit is -4 and agrees with
the independently accepted both-parity corner formula.

The odd-m carrier uses the **actual even mesh m+1 in y**. Its degree
overhead is 1/2, absorbed by a strict parameter margin; floors cannot
invalidate eventual admissibility. The negative carrier selects even
k exactly. The positive cosine difference is polynomial, selects odd
k exactly, and its envelope modulation has degree 4r<m+1. The finite
constant coefficients are D_r and D_r/2-1/[2(r+1)^2], with the latter
factor checked independently by rational Chebyshev convolution. The
unmodulated x-factor's alternating sum vanishes under 2s<m. All factors
are normalized by m, including those on mesh m+1; the written m+1/m
factors converge to one. This yields the asserted -16ab/9 and +8ab/9.

The majorant dominates the full signed summand by a summable product
of inverse cubes. It is strong enough both for moving endpoints and for
the infinite parity sums. No negative-corner-only inference is used.
Positive norm upper bounds have the correct inequality direction for
negative numerators. Eventual conclusions on both parities imply the
all-integer statements. At theta<=1/2, 2floor(theta m)<=m proves exact
Gram identity; above one half the strict degree budgets leave room for
both carriers on both parities.

For the norm calculation, L=r+1 and u=Lt give the Jacobian factor
L sin(u/L), not sin(u/L) or L^2 sin(u/L). The integrable majorant
u min(1,pi^4/u^4) is uniform, and the unmodulated mass is independent
of its fixed positive degree ratio. The modulated limits are integrals
of u sinc^4(u/2) times cos^2(u/(2a)) or
sin^2(u/(2a))sin^2 u; each is strictly positive.

I independently obtained the same cosine transform before reading the
completed growth proof. In the written proof H=O(u^4) at zero follows
from both sum c_t=0 and sum c_t t^2=0. Twice integrating by parts gives
integral 2H/u^3 = integral H''/u with a **positive** sign and no missing
factor two. Every boundary term vanishes; zero frequencies contribute
zero after two derivatives. Subtracting cos u is legitimate by the
second cancellation identity. The damped logarithm and its ordinary
improper limit give exactly the displayed C(q), including q=0,1,2 by
the stated continuous zero convention. Expanding the carrier squares
then gives the two J formulas.

Finally, fixing a=1/4 or a=1/8 and approaching b=1/4 from below gives
valid one-sided bounds by taking a scalar supremum after the m-limit.
There is no reliance on an inadmissible boundary polynomial family or
interchange of an uncontrolled pair of limits.

## Executed independent checks

Working directory: `/workspace/padua_research`. Python 3.12.14,
mpmath 1.3.0; deterministic, no random seed or expensive computation.
The committed checker imports no developer or predecessor numerical
code. Actual commands included:

```text
python topics/padua-mz-cleanup-20261105/code/independent_odd_check.py
sha256sum topics/padua-mz-cleanup-20261105/theory/odd-weight-asymptotic.md topics/padua-mz-cleanup-20261105/theory/odd-carriers.md topics/padua-mz-cleanup-20261105/theory/growth-carrier-bounds.md topics/padua-mz-cleanup-20261105/novelty-gate-math.md topics/padua-mz-cleanup-20261105/code/independent_odd_check.py state/IDEAS.md
git diff 21dbfc9 aff30e8 -- state/IDEAS.md
git diff 21dbfc9 aff30e8 -- AGENTS.md agents/WORKFLOW.md agents/codex/CODEX.md
git rev-parse HEAD
```

The checker was executed once before adding continuous-norm checks and
again after that addition. Its **final execution passed** in about three
seconds. Small stdout is reproduced by the command; this record retains
the consequential results without a second generated receipt file.

- **Exact rational:** 176 carrier constant-coefficient and alternating
  mesh-sum checks, odd m=3,5,...,31 and every included r satisfying the
  required bandwidth constraint. Chebyshev products use exact
  `Fraction` arithmetic and the elementary finite cosine-sum functional.
- **75-digit floating diagnostic:** independently solve the complete
  interpolation moment equations at m=2,3,4,5,7,9 (6,10,15,21,36,55
  nodes) and compare all weights with the integrated triangular formula.
  Maximum absolute discrepancy was `4.5093619e-76`; masses were four
  within `1e-60`. This is not outward-rounded certification.
- The same moment solves matched exact rational node-corner weights
  `0,-1/18,-2/225,-7/675,-29/8820,-97/70875` in that order.
- **Exact rational finite norms:** construct the carrier coefficients
  independently, square them with Chebyshev product-to-sum, and integrate
  every coefficient using 2/(1-k^2) for even k. With b=1/5, the negative
  a=1/4 squared norms at m=32,64,128 were
  3.701402707413481, 3.731642871157386, 3.743021013865303; at odd
  m=33,65,129 they were 3.716128337710115, 3.739014148585302,
  3.746266969718412. Positive a=1/8 norms in the same even sequence
  were 2.390485857526717, 2.299904960232930, 2.238572023278200;
  in the odd sequence, 2.391399274002171, 2.300659551761518,
  2.238751447467700. Only final display rounding is floating. These
  samples are checks of normalization, not proof of the norm limit.

A separate 60-digit mpmath evaluation of the explicit formulas printed
`A Jminus=3.75098821137025988438496345466`,
`A Jplus=2.17372444063582269455493722827`,
`cminus=0.0296218235968599630799708634092`, and
`cplus=0.0127788864395583976450879898078`. This duplicates formula
evaluation only; the independent norm construction above uses a distinct
finite algebraic path. None of these executions supplies an asymptotic
proof premise or certifies a large-m negative witness.

## Novelty and coverage limits

Read all 955 lines of the initial state/IDEAS.md, including every
obstruction/disposition table, in bounded slices. Initial oversized
outputs were truncated; missing ranges were reread before treating the
read as complete. Full shortlisted candidate bodies read: the original
2D directions/ideas-d3.md (IDEA-215–218), frontier ideas-f12.md
(IDEA-384–390), and ideas-f3.md (IDEA-391–394), together with the full
supporting theory listed above and the developer's new gate. Targeted
`rg` searches covered odd carriers/weights, growth constants, and
carrier normalization in IDEAS, MZ tracks/topics and literature/INDEX.md.
No primary literature was opened, and this check makes no historical
novelty, attribution, or exhaustive-priority assertion.

The retained mechanisms are accurately classified as parity completion
and quantitative normalization of existing packets. The closest failed
degree and negative-corner-only mechanisms retain their scopes; no
existing obstruction is silently declared overcome without the full
signed calculation. The new gate candidly qualifies its source-reading
timing rather than claiming retrospective preregistration.

After main advanced, I read the entire IDEAS diff `21dbfc9..aff30e8`:
IDEA-117's changed disposition and new IDEA-376–379 concern NN-MOP
reconstruction and are unrelated to these MZ mechanisms. Rule-file diff
was empty. The resulting full registry SHA-256 was
`60d5dbcd4e216926c23202ae08998da2643f3acf3e59c88b2b517b041543728e`.

Not checked here: the manuscript, C1 large finite witness certification,
spectral scans and slope fits, allocation/PR preparation, or storage
delivery. Material changes to the three pinned proofs require a new
impact check. Required Claude mathematical audit remains pending.

## Completion-metadata impact check

At the parent's explicit request after the mathematical check, updated
only current completion metadata in the three theory files: links now
identify this finished supplementary check while required Claude audit
remains pending. No statement, definition, assumption, proof, constant,
or numerical code changed. The candidate table above contains the new
SHA-256 values. The original checked hashes, in weight/carrier/growth
order, were `02aa460b220a884770a20b1d812ba038e2d32d2b35820177df31714e01b29976`,
`1aabd0e28e62dce56ca59ea83246c0b0a2eb50d003f23feaf1d99131cfd93051`, and
`2af168f14ed591cfb30f1d933104813072514c05fa739e90c13df2b4248eec03`.
This metadata-only diff was inspected and `git diff --check` passed.
No mathematical rerun was needed or performed for this update.
