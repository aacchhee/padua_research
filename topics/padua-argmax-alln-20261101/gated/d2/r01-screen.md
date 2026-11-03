# Direction 2, round 1: corner first-variation screen

Pre-registered before execution, 2026-11-02. Assigned Codex developer,
inherited gpt-6.1-sol xhigh; runtime metadata not independently exposed.
Rules/current administrative checkpoint supplied by the orchestrator:
`aa1883f2fd9a837bb931ce804cb4b210c7475886`; scientific base
`7d308b10d946b607ae0690454f6c0103690775a4`. Read current rules,
`gated/d2/r01-contract.md` and `theory/gated-codex-11-corner-phase-localization.md`.
This implements the existing registered D2 candidate, with no novelty claim,
new global certificate, Git operation, shared record or later-round work.

## Exact conventions and registered calculation

At the canonical nonnode corner c=(-1,-1), put m=n+1,
a_j=cos(j*pi/n), b_k=cos(k*pi/m), and retain even j+k physical nodes
with corrected kernel coefficients C_(n,0)=1 and ordinary coefficients
h_p h_q for p+q<=n. Weights are 2 eps_j eta_k/(nm).
Use T_p(-1)=(-1)^p and physical T'_p(-1)=-p^2(-1)^p.

The structural zero set is exactly k=0,j positive even; (0,0) is the
nonzero removable value L_00=(-1)^n/m. For k>0 the corner value is
`2*w*(-1)^(n+j)*(1-b_k)/(b_k-a_j)`, whose exact sign is
`(-1)^(n+j)*sign(m*j-n*k)`. Thus zero/nonzero classification and all
nonzero signs use integers, not floating values or zero thresholds.
The numerical gradient is computed from the corrected Chebyshev matrix.

Registered degrees: 2,3,4,5,8,12,16,24,32,48,64,96,128.
Registered inward directions: v=(t,1-t), t=0,1/4,1/2,3/4,1.
For every degree and direction retain
`D_v=sum_nonzero sign(L0)*(grad L dot v)+sum_zero |grad L dot v|`,
its two contributions, and normalizations by n^2*Lambda_c and by
`[t*n^2+(1-t)*m^2]*Lambda_c`. Retain the least-negative sampled direction,
axis margins, structural value/sign counts, zero-row gradients and
minimum nonzero absolute corner value. Numerical values are MEASURED.
There is no phase grid away from the corner or global optimization.

Before screening, reconstruct the n=2 rational cardinals using the
existing `finite_n2_exact.py` data/inverter. Verify exact axis slopes
-7/3 (x) and -14/3 (y), all five first variations, and match numerical
values/gradients to those rational controls. Also construct the outward
interval cardinals at n=3,4,8 using `finite_general.construct` and check
the structural zero/nonzero values, signs, and endpoint-gradient/first-
variation agreement. Retain small interval summaries, not full polynomials.
The constructor controls are diagnostics, not a new global certificate.

## Decision criterion and bounded scope

A wrong structural mask, sign or failed n=2 control blocks the screen.
A measured nonnegative axis derivative is a candidate failure flag, with
any refutation requiring a separate exact witness; preserve possible
higher-order behavior. Negative finite slopes alone do not establish a
uniform physical-radius theorem or justify a later round. Hope requires
the mathematical worker's exact structure plus a concrete bound on the
first variations and their perturbations that could give a radius
matching Direction 1's vanishing phase localization.

Budget: all specified degrees, expected under 60 CPU seconds, O(n^3)
matrix work; generated JSON plus stdout under 100 KB. No larger grids,
additional degree scans or future rounds are pre-authorized here.

## Registered command

`OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python topics/padua-argmax-alln-20261101/code/gated/d2_screen_r01.py topics/padua-argmax-alln-20261101/outputs/gated/d2_screen_r01.json > topics/padua-argmax-alln-20261101/outputs/gated/d2_screen_r01.out`

Independent replay and the required Claude audit remain pending until
actually performed. Outputs will retain versions and source hashes.

## Pre-execution structural diagnostic addition

The parallel mathematical worker supplied closed forms for both gradients
at these same nodes, including equal zero-row gradients
`gx=gy=-2*w*(-1)^(n+j)*n/(1-a_j)` and explicit removable (0,0)
derivatives. Compare these formulas with the coefficient matrix at the
registered degrees, retaining maximum absolute and relative discrepancies
and zero-row equality residuals. No new degree, direction or off-corner
grid is added. This diagnostic tests the proposed exact structure; the
mathematical derivation and its proof status remain the worker's scope.

## Supplementary energy diagnostic, registered before its execution

The initial screen completed in .387388101 CPU seconds, with frozen source
SHA-256 `1fb72190e9ea0ae53450ad5e379bfe2a74246520e8dd43ae50f7f6a65e0009d2`
and JSON SHA-256
`78dbf52b06c15d2ebae5f0fee5153236de28034ac8cc0fdf0d923de887ead5ad`.
After that run, the orchestrator requested the following new diagnostic,
which is registered here before execution on 2026-11-02. Reuse the frozen
`corner_matrix`/`variations` functions at the same thirteen degrees and
compute only over the structurally nonzero cardinals:
`E_x=sum gx^2/|L0|`, `E_y=sum gy^2/|L0|`,
`E_xy=sum gx*gy/|L0|`, and `W=E_x+E_y`.
Use the analytic corner magnitudes already returned as `known`, without
floating zero tests. Record each divided by `n^4*Lambda_c`.
No new degree grid, off-corner scan, radius claim or later round is added.
This diagnostic tests whether an aggregate sign-flip estimate could use
the scalar inequality
`|a+b|<=|a|+sign(a)*b+b^2/(2*|a|)`.

Documentation correction, 2026-11-02 (audit-01 N6): the original display
used the valid looser term `2*b^2/|a|`. The display now matches theorem13's
sharper `b^2/(2*|a|)` exactly. No measured value, code or premise changed.
The frozen main script and its original outputs will remain unchanged;
the additional small output is `outputs/gated/d2_screen_r01_weighted.json`.

## Completed results, MEASURED

The registered main command completed every specified degree and direction
in .387388101 process CPU seconds (.389104830 wall seconds), using Python
3.12.14 and NumPy 2.3.5. No randomness was used. The exact n=2 reconstruction
gave corner values `(1/3,-1/3,-2/3,2/3,0,1)` in physical-node order and
first variations `(-14/3,-49/12,-7/2,-35/12,-7/3)` in the registered ratio
order. Its maximum value/gradient disagreement with the floating matrix was
`8.049116928532385e-16`. The n=3,4,8 outward controls verified the structural
mask/signs and enclosed strictly negative first variations. These are
separate rational/outward diagnostics, not global certificates.

All thirteen degrees have strictly negative measured axis slopes and
negative values at all five ratios. No nonnegative-axis candidate flag
triggered. The table reports positive inward-descent margins; D_x,D_y
themselves have the opposite sign.

| n | `-D_x/(n^2 Lc)` | `-D_y/(m^2 Lc)` | `W/(n^4 Lc)` |
|---:|---:|---:|---:|
| 2 | .1944444444 | .1728395062 | .3831018519 |
| 3 | .2140246888 | .2049166624 | .3338448142 |
| 4 | .2317916419 | .2263367194 | .3150118860 |
| 5 | .2455500779 | .2417067741 | .3056462870 |
| 8 | .2721828352 | .2701872478 | .2958846014 |
| 12 | .2919557136 | .2907768763 | .2946712648 |
| 16 | .3042769600 | .3034610192 | .2963751401 |
| 24 | .3195578495 | .3190719881 | .3010635953 |
| 32 | .3291274811 | .3287914894 | .3054239523 |
| 48 | .3411085093 | .3409089145 | .3123812856 |
| 64 | .3486923017 | .3485543595 | .3176141604 |
| 96 | .3582869784 | .3582049274 | .3251084155 |
| 128 | .3644216213 | .3643647837 | .3303843693 |

For example, at n=128, Lc=17.3460568001,
D_x=-103567.8210693 and D_y=-105175.9830741.
The structural zero row contains floor(n/2) cardinals. Its x and y
gradients agree numerically within `1.3436821100221152e-13` over this
screen, consistent with the supplied formula that they are exactly equal.
The detailed rows and signed/absolute contributions are retained in JSON.

The closed-gradient formulas supplied by the mathematical worker agree
with the independent matrix expression to absolute error `9.58e-13` at
n=8. At n=128 the maximum absolute discrepancy is `1.16001e-5`, with
maximum relative discrepancy `1.19335e-7` after scaling each component by
max(1,|matrix gradient|). Small cosine differences make the rational closed
expressions numerically ill-conditioned there; the matrix gradients are
used for all reported slopes/energies. No exact-gradient identity is
proved by this comparison, and these discrepancies are not enclosures.

The supplementary energy calculation completed the same thirteen degrees
in .064039772 CPU seconds. At n=128,
`(E_x,E_y,E_xy)/(n^4 Lc)=(.1629668614,.1674175079,.1565503710)`.
W/(n^4 Lc) ranges from .2946712648 to .3831018519 in this finite set; its
late increase is preserved, and no boundedness or limiting constant is
inferred. The scalar sign-flip inequality and the equal zero gradients
make a concrete next analytic obligation: prove uniform constants c,C>0
for the inward slope margins and aggregate gradient energy, and control
the aggregate Hessian remainder. That would test a physical corner radius
kappa/n^2 (with the corresponding m scale in y). Such a fixed positive
scaled radius could match the already proved vanishing actual-corner
phases, since physical endpoint displacement is quadratic in angular
displacement. Empirical negativity or a fit alone does not provide that
radius, all-degree constants, thresholds or finite coverage.

## Executed supplementary command

The following command imported the unchanged frozen helper; it did not
alter or rerun the main output file.

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python - <<'PY'
import hashlib, importlib.util, json, time
from pathlib import Path
base=Path('topics/padua-argmax-alln-20261101')
source=base/'code/gated/d2_screen_r01.py'
spec=importlib.util.spec_from_file_location('d2_screen',source)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
start=time.process_time();rows=[]
for n in module.DEGREES:
 data=module.corner_matrix(n);nonzero=data['signs']!=0
 a=data['gx'][nonzero];b=data['gy'][nonzero];v=abs(data['known'][nonzero])
 ex=float((a*a/v).sum());ey=float((b*b/v).sum());exy=float((a*b/v).sum())
 lc=float(abs(data['known']).sum());scale=n**4*lc
 rows.append({'n':n,'E_x':ex,'E_y':ey,'E_xy':exy,'W':ex+ey,'E_x_over_n4_Lc':ex/scale,'E_y_over_n4_Lc':ey/scale,'E_xy_over_n4_Lc':exy/scale,'W_over_n4_Lc':(ex+ey)/scale})
result={'status':'MEASURED','arithmetic':'float64; structural nonzero mask and analytic magnitudes','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'preregistration_note_sha256':hashlib.sha256((base/'gated/d2/r01-screen.md').read_bytes()).hexdigest(),'degrees':rows,'cpu_seconds':time.process_time()-start}
out=base/'outputs/gated/d2_screen_r01_weighted.json';out.write_text(json.dumps(result,indent=2)+'\n')
for r in rows: print(r['n'],r['E_x_over_n4_Lc'],r['E_y_over_n4_Lc'],r['E_xy_over_n4_Lc'],r['W_over_n4_Lc'])
print('cpu',result['cpu_seconds'],'bytes',out.stat().st_size,'sha256',hashlib.sha256(out.read_bytes()).hexdigest())
PY
```

## Artifact identities and remaining checks

| File | Bytes | SHA-256 |
|---|---:|---|
| `code/gated/d2_screen_r01.py` | 12279 | `1fb72190e9ea0ae53450ad5e379bfe2a74246520e8dd43ae50f7f6a65e0009d2` |
| `outputs/gated/d2_screen_r01.json` | 72838 | `78dbf52b06c15d2ebae5f0fee5153236de28034ac8cc0fdf0d923de887ead5ad` |
| `outputs/gated/d2_screen_r01.out` | 17010 | `7b2ce3afb8a35510cf2351e70f714bec8c639795cbe4f661bf96c60e229ac1a7` |
| `outputs/gated/d2_screen_r01_weighted.json` | 4675 | `8250472c4d73a9ac9c8a74d2d587581fa2976e6f094efbe2829daab12b8dc43b` |

Generated outputs total 94523 bytes. Main and supplementary JSON retain
their pre-execution note identities; this completion append changes the
note hash intentionally. Other dependency identities are recorded in the
main JSON. Local artifacts await the orchestrator's evidence/storage
disposition; no cold-storage destination was invented.

Independent execution and required Claude audit are PENDING. The checker
should replay the main command and the supplementary calculation to new
output paths, compare non-time/non-argv values, and allow the completion
append's note-hash change. No future round, direction 3, new global
certificate or shared registry/log/handoff edit was performed here.
