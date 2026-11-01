# Supplementary adversarial mathematical audit

Date: 2026-11-01. Auditor: Codex `/root/supplementary_audit`, allocated
`gpt-6-astra`, xhigh, under the repository's adversarial mathematical audit
row. This is supplementary Codex review of Codex development. It is **not**
the required final Claude Opus 5.5 xhigh audit and does not authorize PR
readiness or merging.

Rules read: `AGENTS.md`, `agents/WORKFLOW.md`, `agents/codex/CODEX.md` at
`806cc7b4509fd93bae652f9545d32d95529f8281`, supplied by the orchestrator;
the rule files are reported byte-identical to the preceding campaign base
`cf89b140530d5838bdb208a8c28f3e7aa676ace3`. Branch:
`codex/padua-mz-2d-20261101`. No Git operation or developer proof/code edit
was performed by this auditor. The sole owned repository output is this
report; temporary execution output is under `/tmp`.

## Current verdict and coverage

**Supplementary review complete: no unresolved mathematical finding within
the declared D1--D7 scope.** Both returned findings were accepted and
resolved by developer changes, then independently rechecked: S1 records
the failure of the two D5 uniform majorants while preserving the OPEN
actual-norm target; S2 consolidates the repeated pointwise negative-node
obstruction under the D2 record. The frozen D7 exact tensor-control
theorem and its endpoint/fixed-ratio consequences also pass this review.
The required final Claude audit remains pending. Final-ID integration
still requires the mechanical impact check specified at the end.

Read the complete `state/IDEAS.md`, including the canonical, historical,
MZ, lattice, programme and bivariate-Lanczos obstruction/disposition
tables. Long/truncated reads were followed with smaller overlapping
reads. Read the campaign D1--D5 candidate records; the full shortlisted
M1/M3 candidate entries; the D7 gate as available; the campaign definitions;
and all final scientific `tracks/mz-constants/theory/mz2d-*.md` files. Read the
MZ/Padua-relevant literature index rows and the whole campaign
`literature.md`. Relevant predecessor IDs include IDEA-053/055/056,
060--076, 205/208; PD-T013/017/018/021--025/101. Inspected the current
CC foundation, endpoint lower bound, fixed-ratio lower/upper proofs and
their exact assumptions. No new historical priority claim is made.

Primary-source PDFs were **not** opened by this auditor. Source
normalization and attribution were reviewed through their inspectable
local records, without inheriting another reader's fulltext inspection as
our own. The source distinction is consistent: positive normalized
Chebyshev cubature, signed mass-four Lebesgue interpolation quadrature,
and Xu/MPX node families are different objects. No literature statement is
used in this audit as an unproved substitute for a local mathematical
argument.

## Findings delivered before developer changes

### S1 — P2: D5 uniform absolute-majorant routes are already ruled out

Location at initial hash `188b5271...`: `mz2d-hyperinterpolation-uniform-open.md`,
lines 42--47; related resumption wording in `ideas-d5.md`, candidate 33,
and the end of `mz2d-hyperinterpolation-absolute.md`.

The initial text treated a uniform bound on `tau_m beta_abs(m,m-1)` or a
uniform bound on negative leverage `chi_m` as unresolved sufficient
routes. D3's proved corner formula and Christoffel calculation already
give, for either actual negative node corner `c`,

\[
 \beta_{\rm abs}(m,m-1)\ge |w_c|K_{m-1}(c,c)
 =\tfrac16\log m+O(1)\longrightarrow\infty,
 \qquad \chi_m\ge |w_c|K_{m-1}(c,c).
\]

The first inequality follows because the absolute Gramian contains that
positive rank-one summand; the second is the definition of `chi_m`.
Also `tau_m>=|sum w|=4`. Thus both specified uniform majorants are
impossible. The absolute-norm identity and its finite-m upper estimates
are valid; the actual `C->L2` operator norm may still be uniformly bounded.
In particular a single corner contributes `|w_c|sqrt(K)` to the relevant
weighted L1 functional, not `|w_c|K`; divergence of the latter is not
operator-norm divergence.

Requested correction: mark these exact uniform sufficient mechanisms as
failed consequences of the D3 result; preserve degree-dependent upper
bounds as possible, and keep the exact operator-norm target OPEN with a
different direct weighted-L1 or cancellation argument. Root accepted the
finding and reassigned the D5 developer to a written response.

### S2 — P2: consolidate the repeated pointwise negative-node obstruction

Locations: `mz2d-fixed-ratio-energy-conversion-obstruction.md`, statement
and proof; `ideas-d4.md`, candidate 41; compared with
`mz2d-upper-sign-obstruction.md`, proof section 3.

At the orchestrator's request, compared the exact mathematical claims.
D2 already proves the actual `m=3` corner weight `-1/18` and failure of
positive nodal Cauchy--Schwarz on arbitrary data. D4 repeats the same
cardinal polynomial and integral, then tests a data vector supported at
that corner against any positive reference weights. The extra implication
`w_c<0` prevents `w_c>=c v_c>0` is routine. Its application to M3's final
energy-conversion step is useful, but supplies no distinct mathematical
mechanism or obstruction requiring another final negative-result ID.

Recommended correction: preserve the D4 derivation and candidate history
as an application/alias of the D2 negative record; retain the failed
positive-floor transfer disposition and identify the duplicate
mathematics explicitly. D3's continuous-metric obstruction is different:
it proves divergence on the restricted polynomial space, whereas the
D2/D4 corner-data argument concerns arbitrary nodal values. No negative
statement about restricted-degree Padua coercivity follows from S2.

## Independent mathematical reconstruction

- **D1 aliases and structure.** Folding each coordinate and applying the
  checkerboard complement gives total degrees summing to `2m+1`, so
  exactly one representative lies in `Pi_m`. The explicit degree-`m+1`
  y mode establishes exactness precisely m. Reconstructed all five
  nontrivial moment regions, including their integer boundaries. The
  pullback into sum/difference sectors needs at most 160 tensor terms.
  The unitary Fourier integral proves the claimed `1+log(8n+1)` mask
  bound in Chebyshev coefficient norm. It supplies no hidden estimate in
  the continuous mass metric, and the files correctly leave that gap open.
- **D2.** The `1,T2(x),T2(y)` three-cycle has invariant positive sign
  product, including the special `m=3` alias, so no diagonal sign switch
  gives a Z-matrix. Checked the two `m=4` defect entries and the exact
  `m=2` tensor nodal ratio three. The open block-Schur formulation
  explicitly requires positive diagonal blocks before inverse square
  roots; no unproved positivity is silently assumed.
- **D3.** Reconstructed the telescoping triangular moment sum and partial
  fractions for the corner weight, both parity cases, m=2 zero, m>=3
  negativity and the coefficient `-4 log(m)/m^4`. Independently summed
  the total-degree endpoint Legendre Christoffel function to
  `m(m+1)(m^2+m+1)/24`. Hence the rank-one norm is `(log m)/6+O(1)`.
  This invalidates the stated fixed continuous-metric subtraction only.
  The tensor packet degree obstruction is exact and the positive tensor
  fixed-ratio bound is not claimed for signed Padua. The rhombus packet's
  ordered-pair formula correctly cancels sine terms and respects total
  degree; its measured failure was replayed separately below.
- **D4.** Parity projection retains exactly equal-parity diagonal-angle
  frequency pairs and gives multiplier `kappa(a+b)kappa(a-b)`. The
  plateau includes its boundary; support is the radius-(m-1) diamond.
  The checkerboard annihilator's shortest nonzero l1 length is 2m, above
  the maximum input/output difference `n+m-1<=2m-2`. This reconstructs
  the full stated trigonometric space, including n=0,m=1. Reconstructed
  the rectangular transfer's spurious coefficient
  `1/[4(m-n)(m+1-n)]` for input xy. These facts repair aliasing only;
  the signed energy and sharp upper-bound gaps remain explicit.
- **D5.** For distinct nodes, disjoint continuous tents attain arbitrary
  bounded nodal signs. Finite-dimensional duality therefore gives exactly
  `sup_{||p||2=1} sum |w_i||p(z_i)|`, and Cauchy--Schwarz must use the
  absolute Gramian. `A=G+2G_-` and the trace bound prove the stated finite
  estimates. Product degree proves reproduction when `n+r<=m,r<=n`.
  At n=m-1 the odd/even quadratic witnesses have nonzero defects
  `h_(m-1)-h_(m+1)` and `h_m`, respectively. Thus the maximal complete
  reproduced degree is one for m>=3, without implying failure of
  fixed-function convergence. S1 concerns only their proposed next route.
- **D6 finite reduction.** Positive-denominator clearing and exact strict
  diagonal dominance certify nonsingularity along the off-diagonal
  homotopy. This both counts signs and proves the proposed integer
  congruence invertible. Sylvester inertia and continuous positive mass
  then prove the strict open eigenvalue brackets. Numerical eigenvectors
  select proposals only. The explicit stored m30 witness requires only
  its two rational quadratic forms, independently of all interval
  certificates. The measured D0 data and computer-assisted finite
  conclusions are properly separated from universal targets.

The substantive PROVED supporting results are split from the genuinely
OPEN spectral and operator targets. None of the negative statements
reviewed above refutes a broader spectral theorem merely because a proof
route fails. The final Claude audit must retain this scope distinction.

## Executions actually performed by this auditor

Environment: Python 3.12.14, NumPy 2.3.5, SciPy 1.17.0, SymPy 1.14.0,
python-flint 0.9.0. Deterministic; no random seed was required for the
selected checks. Set `OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1`.

Pinned inputs:

| Input | SHA-256 |
|---|---|
| `mz2d_exact.py` | `5d1f005e2307d3a26badc9c1a44ce313dc9126625a49fba5d59430c151cf9c70` |
| `mz2d_independent_check.py` | `5e455d747dc5dca84c883ed900095ff4a2bb40767f4ebcb3261d7d583df7bdfc` |
| `mz2d_spectra.py` | `623acdf06e4ad1c50c3c0562f47f037b8efa15fcc332c2f1ee7a7d0f88ee8b76` |
| `evidence/exact-spectra.json` | `5456917afe8fea69b0a776270ef3ae79fdc33deb02d27f89648fc342f78b93de` |
| `evidence/independent-exact-spectra.json` | `18c8623442664aa119d3581b701d200315d454071d6b8f6c89cbaf540fe34d9c` |
| `evidence/independent-additional-checks.json` | `2da16fa5c8f2f480ab7c12270b8c9b95ec49028f9df6b1cf4062af4f11897717` |
| `definitions.md` | `4ac0e391859a14e4d6f752f1244df0701e99d9b3d8ab8570bd632520f517c7db` |

From repository root, executed successfully:

```sh
PYTHONPATH=/tmp/padua-flint OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python tracks/mz-constants/code/mz2d_exact.py --m 10 --output /tmp/padua-supplementary-m10.json
```

All m10 result fields matched the producer receipt after removing only
nested `seconds`. The temporary replay receipt SHA-256 is
`16469a481c50e6aa80168b0136578783b5527b142a6e3c8f54f324d6937332b5`.
That local output is not a durable external archive. This auditor did
**not** rerun the full m20/m30/m40 inertia producer; its separate-agent
replay was inspected as already existing evidence, not claimed as ours.

Then executed the following selected functions from the independently
written checker, avoiding its main function's write to someone else's
receipt:

```sh
PYTHONPATH=/tmp/padua-flint OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python - <<'PY'
import importlib.util,json,hashlib,sys
from pathlib import Path
path=Path('tracks/mz-constants/code/mz2d_independent_check.py')
spec=importlib.util.spec_from_file_location('audit_check',path)
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
data=json.loads((a.TOP/'evidence/exact-spectra.json').read_text())
w,bad=a.stored_witness(data)
print(json.dumps({'python':sys.version,'sympy':a.sp.__version__,'flint':a.p.flint.__version__,'stored_witness':w,'rejection_controls':a.rejection_controls(data,bad),'regions':a.region_checks()}))
x=json.loads(Path('/tmp/padua-supplementary-m10.json').read_text())
assert a.normalize(x['results'][0])==a.normalize(data['results'][0])
print('m10 exact replay fields match after removing only seconds')
print('m10 receipt SHA256',hashlib.sha256(Path('/tmp/padua-supplementary-m10.json').read_bytes()).hexdigest())
PY
```

All 225 stored coefficients reproduced the advertised exact forms and
strict positive `b-4a`; all six malformed-certificate controls rejected.
All 1,221 moment region comparisons passed, with counts
`L=451,C=385,X0=150,X1=70,Y0=95,Y1=70`. This is a new execution of that
checker, not a claim that this auditor authored it. The small cyclotomic
nodal regressions were inspected but not rerun here.

The independent replay of the D3 finite rhombus measurement used the
following complete inline command. It imports only the frozen weight
routine; constructs the witness independently from the written definition;
and also compares the coordinate harmonic witness on its actual mesh.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python - <<'PY'
import importlib.util,hashlib,json
from pathlib import Path
import numpy as np
from numpy.polynomial.chebyshev import chebvander,chebval
from numpy.polynomial.legendre import leggauss
path=Path('tracks/mz-constants/code/mz2d_spectra.py')
spec=importlib.util.spec_from_file_location('measured',path)
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
print('source SHA256',hashlib.sha256(path.read_bytes()).hexdigest(),'numpy',np.__version__,'scipy',a.scipy.__version__)
expected=[.8816982072230825,.888410221048749,.9049194670876055,.9238661857810373,.9419610544549483]
for m,target in zip([8,16,32,64,128],expected):
    u=np.zeros(m)
    for k in range(1,(m-1)//2+1):
        u[m-1-2*k]+=1/k;u[m-1]-=(1-2*k/m)/k
    c=np.array([2*sum(u[r::2]) for r in range(m)]);c[0]/=2
    C=np.zeros((m,m))
    for r in np.flatnonzero(c):
        for s in np.flatnonzero(c):
            C[(r+s)//2,abs(r-s)//2]+=c[r]*c[s]/2
            C[abs(r-s)//2,(r+s)//2]+=c[r]*c[s]/2
    assert not any(C[i,j] for i in range(m) for j in range(m) if i+j>m-1)
    x,y,w=a.padua_weights(m)
    values=chebvander(x,m-1)@C@chebvander(y,m-1).T
    q=np.sum(w*values**2)
    z,gw=leggauss(m);V=chebvander(z,m-1)
    b=np.sum(np.outer(gw,gw)*(V@C@V.T)**2)
    rq=q/b
    coord=np.dot(a.cc_weights(m),chebval(x,c)**2)/np.dot(gw,chebval(z,c)**2)
    assert abs(rq-target)<1e-10 and rq>coord
    print(json.dumps({'m':m,'Q':q,'continuous':b,'packet_quotient':rq,'coordinate_quotient':coord,'reference_difference':rq-target}))
PY
```

| m | rhombus quotient, this replay | coordinate quotient, this replay |
|---:|---:|---:|
| 8 | 0.8816982072230825 | 0.7605246113989627 |
| 16 | 0.8884102210487492 | 0.6306811036758154 |
| 32 | 0.9049194670876055 | 0.5154150866922251 |
| 64 | 0.9238661857810373 | 0.42168944079447956 |
| 128 | 0.9419610544549483 | 0.34782866596256884 |

Maximum difference from the five recorded rhombus quotients was
`2.220446049250313e-16`. These remain float64 measurements, not rigorous
enclosures or an asymptotic impossibility theorem.

## Focused rechecks and final disposition

**S1 RESOLVED.** Read the new
`mz2d-hyperinterpolation-absolute-obstruction.md` at SHA-256
`201f3a3347b3716c7ace06024535e2b9571987b58e59bc9f0dd61ca3069bd3e7`
and revised `mz2d-hyperinterpolation-uniform-open.md` at
`b9fd1371f19d9c1088546581485447e50240684251712776cd87deef860d4ee3`.
Reconstructed their rank-one lower bounds, mass-four floor, constant-mode
Rayleigh floor, and divergence of both sufficient majorants. The
single-corner weighted-L1 term tends to zero as stated. The candidate
record now distinguishes failed mechanisms from the unchanged OPEN
actual-norm target. The valid finite-degree norm and reproduction
theorem bytes are unchanged. The developer's response is
[response-d5.md](response-d5.md); its final receipt was read.

**S2 RESOLVED scientifically; final alias insertion remains mechanical.**
Read the corrected candidate disposition and live D4 references. The
canonical obstruction is the existing `PD-N?mz2d-codex-10` section 3;
historical `PD-N?mz2d-codex-41` is its alias/application, not a separately
allocated claim. An executed Python check recovered exactly 4,450 bytes
from offset 2,255 of
`directions/d4-positive-floor-verification.md`; their SHA-256 is the
original `bcecd47698bea9679f6b734a26f8afb0fd85874a51b414ad75cf9ac650e98903`.
It also checked that the duplicate theory path is absent, diamond and
rectangular proof hashes are unchanged, and all 13 local Markdown links
in the four selected live D4 files resolve. The separate worker's count
of 16 covers a different file set. The archived body is expressly
verification/provenance only. Read [response-d4.md](response-d4.md),
including its final focused-review receipt. Do not rewrite its frozen
archived body or the frozen peer reports during ID allocation.

**D7 PASS.** Read the complete frozen exact tensor-control theorem at
`7a652720ed5ca88d4bd9c3da6b1c1296957928c2f8436283f12400da627e0741`
and its detailed candidate/gate records. Independently derived:

1. A nonzero mixed coordinate defect needs `a+c>m,b+d>m+1`, inconsistent
   with `a+b+c+d<=2n<=2m-2`.
2. A nonzero x-defect row needs `a-b>m-n`; a nonzero y-defect row needs
   `b-a>m+1-n`. These wedges are disjoint, and symmetry gives the same
   column supports. Thus the two remaining defects annihilate each other.
3. Each fixed-other-coordinate active block is a principal submatrix of
   its one-dimensional full degree-n Gram matrix after identity rows are
   removed. The two full coordinate polynomial spaces are invariant, so
   both coordinate spectra actually occur. These facts prove equality of
   the full extrema with the minimum/maximum of the two coordinate extrema;
   this is stronger than a generic product bound or one-sided compression.
4. The fixed-ratio interval follows from PD-T022/023 without multiplying
   their constants. Monotonicity of the explicit harmonic `K_N` gives
   the endpoint lower bound `1/K_(m+1)`; PD-T018's all-N statement gives
   `128000/log^2(m)` above the minimum. The upper endpoint stays below two.
   Therefore the minimum has logarithmic-square order and eta tends to one.
   No eta-deficit rate, signed Padua theorem, or sharp constant is inferred.

The Chebyshev pencil identity is consistent with this orthonormal proof:
the omitted product of the two Hankel defects vanishes by the same degree
count. All statement ranges include m=2 and n=0 correctly. These are
analytic proofs with accepted one-dimensional dependencies; no numerical
test supplies an all-degree inference.

Also rechecked the late fixed-theta corollary in
`mz2d-lower-corner-subtraction-obstruction.md` at
`282bc22de3a15056bef406ddc6a3aa4f268a62b4c54a2574b82208e8240a63a1`.
Replacing m by n+1 in the endpoint finite sum gives
`K_n=(n+1)(n+2)(n^2+3n+3)/24`. With n=floor(theta m), multiplication by
the proved corner weight gives `theta^4 log(m)/6+O_theta(1)` for each fixed
theta>0. For theta<=1/2, `2n<=m` gives exactly `G=I`; hence the growing
positive and negative parts cancel. This is a correct warning against
inferring signed spectral failure from a growing negative subform.

### Additional executed D7 diagnostic

Executed the following independent bounded regression after the analytic
review. Its source input is the same frozen `mz2d_spectra.py` hash listed
above; environment unchanged. It passed **104 cases**, every n=0,...,m-1
for m=2,...,14. Maximum extreme discrepancy was
`1.5543122344752192e-15`, at (m,n)=(6,5). These float64 comparisons are
diagnostic only.

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python - <<'PY'
import importlib.util,hashlib
from pathlib import Path
import numpy as np
from scipy.linalg import eigvalsh
path=Path('tracks/mz-constants/code/mz2d_spectra.py')
spec=importlib.util.spec_from_file_location('tensor_check',path)
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
count=0;worst=0.;where=None
for m in range(2,15):
    for n in range(m):
        scale=np.sqrt((2*np.arange(n+1)+1)/2)
        x=np.cos(np.pi*np.arange(m+1)/m)
        y=np.cos(np.pi*np.arange(m+2)/(m+1))
        vx=np.polynomial.legendre.legvander(x,n)*scale
        vy=np.polynomial.legendre.legvander(y,n)*scale
        gx=vx.T@(a.cc_weights(m)[:,None]*vx)
        gy=vy.T@(a.cc_weights(m+1)[:,None]*vy)
        idx=a.indices(n)
        full=np.array([[gx[i,k]*gy[j,l] for k,l in idx] for i,j in idx])
        ex=eigvalsh(gx);ey=eigvalsh(gy);ev=eigvalsh(full)
        delta=max(abs(ev[0]-min(ex[0],ey[0])),abs(ev[-1]-max(ex[-1],ey[-1])))
        assert delta<2e-13,(m,n,delta)
        if delta>worst:worst=delta;where=(m,n)
        count+=1
print('PASS',count,'all-degree cases m2..14; max extreme discrepancy',worst,'at',where)
print('source SHA256',hashlib.sha256(path.read_bytes()).hexdigest(),'numpy',np.__version__,'scipy',a.scipy.__version__)
PY
```

## Final scientific input pins before final-ID mapping

All theory paths below are relative to `tracks/mz-constants/theory/`.
These pins identify the reviewed mathematical content independently of
concurrent orchestration commits. The orchestrator reports scientific
checkpoint `c682164`, followed by metadata work including `1f3530b`;
the hashes, rather than those abbreviated reported commit locators,
define this audit's exact scientific scope.

| File | SHA-256 |
|---|---|
| `mz2d-aliasing.md` | `ca22c888e00b46c2caf569dd9221b9c490367a5f16384460b27b111ef3229947` |
| `mz2d-certified-spectra.md` | `81986b6379adedf3393173cf75388a99211d5c3330b34254e7d48d87cc7af795` |
| `mz2d-defect-structure.md` | `25bc96aa605afdfa9e16d6f05baf9a5e44a1800c1b56c0323272d936e2e47eec` |
| `mz2d-endpoint-rhombus-packet.md` | `308206c521f1182f8c18634835a062f686008a7854f08565c91f8bbd1a7b6f2a` |
| `mz2d-endpoint-tensor-obstruction.md` | `c20da3825a1a28535763ac5a5b1ec9bdc0dd82a45875896ed7867969659543a2` |
| `mz2d-eta-counterexample.md` | `ae52a472871b8ee4d9bf22f787bb417cb23e88dcedc041ed53360091e246d6e1` |
| `mz2d-fixed-ratio-diamond-reconstruction.md` | `8d517cc6435a7936f4eb3572089e9990659e1a02b560ae602059c394b78ac4d5` |
| `mz2d-fixed-ratio-rectangular-obstruction.md` | `777046f5b57d853db12e2df8470ba5b14624fbe3eb35f96bc3e6a30b9ca4dfbd` |
| `mz2d-fixed-ratio.md` | `a4eca46fd8d312ff09ceee74dd3a66fcf4cfe5ddde7c000a9bc54da5c3ff48e8` |
| `mz2d-hyperinterpolation-absolute-obstruction.md` | `201f3a3347b3716c7ace06024535e2b9571987b58e59bc9f0dd61ca3069bd3e7` |
| `mz2d-hyperinterpolation-absolute.md` | `1bcea644be34a797d90b282287ad77c61d679da369f644107bdcadc4eb162b8b` |
| `mz2d-hyperinterpolation-reproduction-obstruction.md` | `b728d3d30b1ab1bb3ab26f661d1c0fa7875ba91f667f527466c124e991a8c451` |
| `mz2d-hyperinterpolation-reproduction.md` | `59de128f347330316d7eae26091db255740477d1b6d65d1e1b58456556ded0b1` |
| `mz2d-hyperinterpolation-signed-obstruction.md` | `b5dbb0f05752fb6484f4fda4896b327f3f17467cf1e508612c59f1ef843e523c` |
| `mz2d-hyperinterpolation-uniform-open.md` | `b9fd1371f19d9c1088546581485447e50240684251712776cd87deef860d4ee3` |
| `mz2d-lower-corner-subtraction-obstruction.md` | `282bc22de3a15056bef406ddc6a3aa4f268a62b4c54a2574b82208e8240a63a1` |
| `mz2d-lower-corner-weights.md` | `3c763e54a5758db7f444917c46d07312bc97c411f400b4c85f6a59af7232dc07` |
| `mz2d-measured-spectra.md` | `292d4b91c1135a2e47adae09aecb5c604cbe16afc6f4da5b748bf62925f54ca9` |
| `mz2d-tensor-control.md` | `7a652720ed5ca88d4bd9c3da6b1c1296957928c2f8436283f12400da627e0741` |
| `mz2d-upper-open.md` | `482c2126cda6348539abfa6b1ffecd529b4f12327424e1e5d50cb9d919e024f0` |
| `mz2d-upper-sign-obstruction.md` | `e26df8e8f302d3ba8d6e4006cb2c488131e0f4ded9285a391f34493c6a630a2d` |
| `mz2d-upper-tensor-obstruction.md` | `c861784adce7fff04e3cd886969bd29489846688c8d5e0296ecfa42fc7a65ed8` |

Additional final response/retention pins, relative to this topic:

| File | SHA-256 |
|---|---|
| `response-d4.md` | `d82134f46294ee8a33afdf313b6b5786d10275e8c832046cd3e26d34f4c78f4b` |
| `response-d5.md` | `a870b46d925e6226a829810782fb1830af5fee33151ae2d7b793c438a7f041fa` |
| `ideas-d4.md` | `82b9a33d86edb6c68d1fb454a7da8b1b769e0ba490407fcc97722fe8d8d0400a` |
| `ideas-d5.md` | `5ea1a0dd640d59950cbf565c82271ab0630ec564c367533ddd8d6a6814343550` |
| `directions/D7.md` | `03672c9219946e3dcdf716de102b679e4793646a6d0a36412df4dea834a68e0e` |
| `directions/ideas-d7.md` | `db118eb9206dce527b3866cb60d7a106b9e4524655b0a0e48855f726956cd245` |
| `directions/d4-positive-floor-verification.md` | `7cde49ddb70e36c070891247d41e436ac1a12a853843299089ad92698efe0b5f` |

## Remaining integration obligations and residual risk

Final-ID mapping is owned by the orchestrator. After mapping, check
canonical IDs, all split/dependency links, the duplicate N41-to-N10 alias
disposition, and preservation of theorem statements/statuses against these
pins. Preserve this audit and the frozen verification bodies unchanged;
record the mechanical transformation in a separate impact receipt. A
mechanical ID rewrite is not a new proof audit; any material mathematical
change needs focused reinspection. New/changed shared registries have not
been audited here because final integration was still pending.

The full large floating D0 spectra were inspected, not independently rerun;
their MEASURED scope is retained. The full four-case exact replay belongs
to the recorded other agent; this auditor's actual execution scope is
specified above. No new primary-source PDF reading, exhaustive literature
clearance, signed Padua universal spectral bound, or exact signed-operator
norm asymptotic is claimed. Existing accepted one-dimensional and cardinal
results remain named proof dependencies. The required Claude Opus 5.5
xhigh handoff remains pending independently of this supplementary review.
