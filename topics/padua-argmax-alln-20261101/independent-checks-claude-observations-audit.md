# Codex audit of Claude's original measured observation records

Auditor: independent Codex subagent, actual model `gpt-6-astra`, high
reasoning effort, 2026-11-01. Rules and pinned source:
`328be35e55143013047ec03a70e9906e82b95353`.
Role: Codex mathematical/source audit of Claude development. This report
is separate from the required later Claude audit of new Codex part-3 work.
No Git operation or developer/evidence-file edit was performed.

## Decision and exact coverage

**Accept the six-script-covered observations as MEASURED, subject to the
explicit strip-domain clarification below.** No blocking mathematical or
implementation finding was found in that finite scope. This acceptance
is neither a certificate of an exact maximum nor an asymptotic statement.
One minor wording correction is recorded as C-01; the narrower precise
claim is the claim accepted here. The original files are preserved.

Read both complete Claude theory records, all seven source files listed
below, the complete `independent-checks-claude-records.md` execution report,
its comparison JSON and the relevant stored outputs. Independently
recomputed equality of the six developer/replay stdout byte strings and
their SHA256 hashes. The separate replay worker actually executed the six
scripts; this auditor does not claim to have executed those six original
commands again. This auditor did execute the additional targeted central
optimizer-coordinate check described below.

Coverage accepted:

- Record01 kernel comparison at n=3,4; all 13 reported majorant-excess
  rows; six reported central-box local-search gaps at n=8,12,16,24,32,48.
- Record02 four-edge profiles at n=12,24,48,96; one-cell strip-band
  searches at n=24,48 under C-01; n=2 four-edge 4001-point scans.

Residual execution scope: standalone `maj.py 3 4 5 6 8 12 16 24` and
`maj.py 2` whole-square 161×161 scans were **not** independently executed
in the six-script replay or by this auditor. Record01's coarse-grid part
and record02's whole-square n2-scan portion remain developer-measured
claims outside independent execution coverage. They are not promoted by
this audit. `maj.py` was inspected and exercised as an imported evaluator.

## Findings and dispositions

**C-01 — minor, strip-domain wording.** Record02 Statement 3 says
"strips 1–5 cells wide adjacent to" an edge. The actual `strips.py` domains
are one-cell-thick bands at offsets i=0,…,5, not expanding adjacent strips:
for a vertical band, theta∈[iπ/n,(i+1)π/n], phi∈[0,π]; for a horizontal
band, phi∈[iπ/(n+1),(i+1)π/(n+1)], theta∈[0,π]. The quoted positive gaps
1.09–2.49 concern i=1,…,5. An expanding strip adjoining x=+1 contains a
maximal non-node corner and would instead have gap zero. Action: use the
one-cell-thick offset-band wording in any integrated report or corrected
source record; do not infer the quoted gaps for expanding adjacent strips.
The accepted measured observation is precisely the offset-band version.
The parent was notified; no frozen source record was silently changed.

**C-02 — checked implementation limitation, no observed violation.**
`interior.py` initializes Nelder–Mead inside the specified grid box but
does not constrain its subsequent iterates. A future run could leave that
box. A targeted independent check of the six central runs confirmed that
all final points in the reported cases remain inside the central box and
that each optimizer reports success. Thus this source limitation does not
invalidate those six measured values. No claim about a globally optimal
point, or about the unreported secondary box's optimizer coordinates,
is accepted. Future box searches should enforce or verify containment.

Other finite-search limitations are already disclosed and retained:
`cell.py` has an unconstrained local search, and periodicity permits its
majorant point to be moved to a fundamental cell; it supplies a sampled
excess witness, not a global maximum enclosure. `edgeprofile.py` refines
around the sampled grid winner and uses the local optimizer's result,
without certifying other branches; it uses 25 endpoint-inclusive points
(24 subintervals) per cell. `strips.py` penalizes leaving its actual band
and retains the larger of the grid value and local-search result. Its
printed coordinates have only two decimals in units of pi; they are
numerical boundary-location evidence, not an exact boundary theorem.

## Kernel and status reconstruction

PD-T101 §1, read in full during this audit session's part-3 work, derives
unisolvence, positive endpoint weights and the corrected cardinal kernel
for these exact even-checkerboard nodes. `maj.setup` implements precisely
w_jk=2 epsilon_j eta_k/[n(n+1)], with endpoint half factors and zero weights
on the odd board. Its coefficient matrix has h_a h_b on a+b≤n except
(n,0), whose coefficient is 1. This exceptional x mode is correct.

Applying the elementary cosine product identity separately in each
coordinate gives the four reflected kernel copies implemented in
`maj.lam`. Taking the absolute value after their average yields the
cardinal Lebesgue sum; taking it before the average yields the triangle
majorant. All weights are nonnegative. At a corner the reflected copies
coincide. Reflection of endpoint-weighted physical nodes produces the
uniform periodic checkerboard: each node orbit has 4 epsilon_j eta_k
members and the torus has 2n(n+1) sites. This verifies the equivalence
between the code's reflected weighted majorant and the shifted-lattice
sum used in the observation record. It is a routine verification against
the existing exact cardinal identity, not a newly registered result.

The Vandermonde driver independently forms the full total-degree
Chebyshev evaluation matrix and computes its inverse numerically. Printed
agreement at n=3,4 checks those values only; it is not the reason the
all-degree algebraic identity is valid and does not establish rigorous
floating-point error bounds at other degrees.

IDEA?argmax-alln-claude-01's disposition remains a **MEASURED failure of
the specified stand-alone majorant-at-coset mechanism**. The observed
excesses (roughly 9e-5 to 1.4e-3) reproduce, but no outward error bound
was computed. They must not be relabeled a certified counterexample or
an obstruction to the original Padua argmax target. No global negative
theorem, priority or literature claim is accepted here. The complete
state/IDEAS.md was already read for the accompanying part-3 audit,
including all obstruction/disposition tables; this check proposes no
new candidate and adds no novelty assertion.

## Executed targeted check

Reason for execution: the unconstrained optimizer raised a concrete
possible mismatch with the claimed central domain. Environment:
Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0; no seed. Ran from the snapshot
root with `OPENBLAS_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1`:

```python
import sys, json, numpy as np
from scipy.optimize import minimize
sys.path.insert(0, 'topics/padua-argmax-alln-20261101/code')
import maj
for n in (8,12,16,24,32,48):
    S = maj.setup(n)
    lo, hi = np.pi/4, 3*np.pi/4
    M = int(6*n*(hi-lo)/np.pi)+2
    T = np.linspace(lo,hi,M)
    X,Y = np.meshgrid(T,T,indexing='ij')
    values,_ = maj.lam(n,X.ravel(),Y.ravel(),S)
    i = values.argmax()
    f = lambda z: -maj.lam(n,[z[0]],[z[1]],S)[0][0]
    r = minimize(f,(X.ravel()[i],Y.ravel()[i]),method='Nelder-Mead')
    print(n, r.x/np.pi, bool(np.all(r.x>=lo) and np.all(r.x<=hi)),
          bool(r.success), -r.fun)
```

Exit 0. Actual final coordinates (theta/pi,phi/pi), all inside the box and
all successful:

| n | theta/pi | phi/pi | Found lambda |
|---|---:|---:|---:|
| 8 | 0.5000003925414894 | 0.33667459208480616 | 4.418776960411907 |
| 12 | 0.5845364040925995 | 0.3067356057027929 | 5.576974187168945 |
| 16 | 0.4370665913843738 | 0.3516636642029268 | 6.56384208180237 |
| 24 | 0.45850655798769796 | 0.3188346394421985 | 8.085255044438998 |
| 32 | 0.46882286170681237 | 0.6675082863868027 | 9.24490359958667 |
| 48 | 0.291738495709917 | 0.5510957239857817 | 10.940878402925971 |

These numbers are measurements, not enclosures. They are retained directly
in this new report because the orchestrator froze the existing output
artifacts during upload. No existing output or manifest was modified.

## Audited identities

Paths below are relative to this topic. SHA256 of the two original records
and the separate execution receipt:

| File | SHA256 |
|---|---|
| `theory/argmax-alln-claude-01-measured-observations.md` | `c93593e0530f80cd4b7ede1803f959f9ffbe49dcd6c319ad2eb0aed8a2c67be2` |
| `theory/argmax-alln-claude-02-measured-edge-profile.md` | `05852443203822c3aa311064f6c4ff04cbba30f4d40cc397b22858dc483aaf16` |
| `independent-checks-claude-records.md` | `daa0355dc91b200c2f84df4b53a68f10ae4cf4118b0a7cf465a0bc1c73a43b96` |
| `code/maj.py` | `705139a65f225f66ed30f5c7f197cda9f54137c42fb10c8b6f452ab83c78909c` |
| `code/check.py` | `a2be104c3aa3e7c792d69d7fae61f0bd23cab1e4cebae5ed376678720604ea5d` |
| `code/cell.py` | `f163fa22d6a591e66aa2dc243566f15a914c313d8b9af16b721c620cfdb58341` |
| `code/interior.py` | `f826871ebaa0f69b9efa852057198f9fe0087a1405a1d777bdbdf710d1f296cf` |
| `code/edgeprofile.py` | `6fe6dd72883701c05da03de2b97853193e022d60da24dfa573cca5f8c5b8e7e7` |
| `code/strips.py` | `5ea3ba36837b8b9af7bc78320fd5312f168aefc3592bacf8338d5865114ed11f` |
| `code/n2_edges.py` | `69b6fcddc3e89e6dd3596204cbc54538fd7c997d426d136c3ef126f051d19557` |

Independently recalculated reference/replay equality and hashes for each
six-script output; all byte strings match. Full commands, versions,
timings and identities for that worker's actual executions remain in
`independent-checks-claude-records.md` and `outputs/codex-replay/`.
This audit does not repeat or silently expand that execution coverage.

## Response review — C-01 resolved

2026-11-01, same independent Codex auditor (`gpt-6-astra`, high).
Re-read the complete revised Claude record02 after the developer's
response. Statement 3 now specifies one-cell-thick angle bands at offsets
i=1,…,5, between consecutive mesh lines, with i=0 separately printed.
This matches the unchanged source and output. The History preserves the
old wording and explains the correction; no numerical claim or epistemic
status was upgraded. The replay paragraph correctly separates completed
edgeprofile/strips/n2_edges replay coverage from the unrerun standalone
whole-square scan.

**Disposition: C-01 resolved; accept the revised covered claims as
MEASURED with the existing execution and optimization limits.** No
mathematical source or evidence change requires a rerun. At this review,
revised record02 SHA256 was
`e113a1dc82ad946ff88367983892f1dfb7cc9b3a4afd06c0caf4f06fbac82091`.
Its History called this finding `F1`; the developer has identified that
as a reference typo and will change it to `C-01`. That identifier-only
correction is covered by this disposition and has no scientific impact.
All earlier hashes remain the identities of the earlier audited versions.
Only this new audit file was appended by the auditor.
