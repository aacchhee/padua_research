# D02 far joint completion: derivation and limits

Rules/input 084a64f6465956f9c75b5538f83752c30318f151. Parent assigned hard
mathematical development at requested Astra ultra after the prospective
LOG justification; serving metadata unexposed. Root owns Git and shared
records. This worker owns only D02-far-joint idea/attempt and D02-far theory.

## Analytic outcome

Three separate substantive developer-PROVED records are written:

- D02-far-bias-identity.md: continuous full-phase finite part C_infty and
  exact signed bias beta_(R,delta)=E_infty-E_R+integral_strips(B-S0)/pi.
- D02-far-uniform-limit.md: identification with the uniform limit of
  S_n-B0 log²n-b_full log n, plus an explicit auxiliary-parameter finite-n
  contract with the actual n>=ceil(2pi R/delta) geometry condition.
- D02-far-boundary-identity.md: on every a=0 phase beta=p*b_delta and
  S_n-M_far=p[b_delta+(2/pi)log(1+1/n)]+e, |e|<=7/(12[n(n+1)]²).

The original practical C(phase)(1+L)/n goal remains OPEN separately in
D02-far-joint-target.md. The general bound retains E_n's O(a/R) floor,
the old finite-row R²/n growth and a strip Q charge. It is not a solved
joint cancellation estimate and does not improve the global onset.
The sharp target is not relabeled PARTIAL by its supporting lemmas.

The exact limit is nevertheless identified uniformly at a=0, axes and
all collision transitions, rather than defined by an unproved asymptotic
symbol. A phase-relative comparison can now use the exact S_n(0)=Lambda_c
without inserting a crude separate corner constant. This does not supply
the missing sharp error-side estimate for a validated phase-cover run.

## Candidate dispositions

The declared bias-completed constant survives the exact separation test:
its paired endpoint tail and omitted strip integral are both retained,
and its midpoint restriction equals the independent D01/PD-T365 oracle.
The sharp finite-h joint estimate is unresolved. A fitted first-order
correction and reducing delta alone were not pursued. No new negative
result or rejection of the true residual is asserted.

## Preregistered scalar reuse check (at most 60 CPU-seconds)

Before execution, the sole proposed diagnostic is a scalar recombination
of existing D01 outputs at (1.45,1.45): use the raw t1c.json model values
and its already computed strip integral over [1e-7,.01], compute
E_infty-E64 from exact formulas with binary64 digamma, and add those two
numbers. Print Q(P,1e-7) as an analytic bound for the omitted endpoint
interval, plus the three existing n512/2048/8192 S-M values after this
estimated bias subtraction. This is MEASURED arithmetic, not validated
quadrature; the existing floating integration/roundoff remains unbounded
by an interval checker. No new point evaluation, board sum, quadrature,
phase, degree or fit. A discrepancy with the exact midpoint sign/formula
would stop interpretation. The mathematical proofs above use no run.

Input identities: existing evidence/d01-far.json and raw
local-output/argmax-bridge-20261105/post-audit-D01/far/t1c.json; the latter's
existing SHA256 is 08407e19b8a7a7600ae1c4b8aa00800242dbc2a3f1be6e06dec9a6e1b3ff2d5a.
The execution command and result will be recorded below if actually run.

## Review and remaining work

Distinct Astra review is requested via root on frozen file hashes, with
special attention to the delta-dependent BV constants, special-row
accounting, uniform limit order and boundary normalization. Formal Claude
final audit remains pending. No self-approval or usable new onset claimed.

## Executed scalar check

Executed 2026-11-06 from /workspace/padua_research, Python 3.12.14,
SciPy 1.17.0. Process CPU from resource.getrusage(RUSAGE_SELF), including
imports: 0.808157 seconds; no child process or new quadrature. The raw
input hash was asserted before use. No output artifact was generated;
these scalar observations are recorded here and are not proof premises.

Command: `python -` with the following exact body:

```python
import json, math, hashlib, resource, sys
import scipy
from scipy.special import digamma
from pathlib import Path
raw=Path('local-output/argmax-bridge-20261105/post-audit-D01/far/t1c.json')
assert hashlib.sha256(raw.read_bytes()).hexdigest()=='08407e19b8a7a7600ae1c4b8aa00800242dbc2a3f1be6e06dec9a6e1b3ff2d5a'
x=json.loads(raw.read_text())[0]; v=x['model']; pi=math.pi
alpha=beta=1.45; td=.5+(alpha-beta)/(2*pi); te=.5+(alpha+beta)/(2*pi)
C=lambda t:-digamma(t)-digamma(1-t)
Einf=v['a']/3+v['a']*C(td)*C(te)/pi**2
D0=v['U']/pi+v['B0']*math.log(pi); kap=math.log(.01/pi)
ER=v['endpoint_rows']+v['mesh_constant']-v['B0']*kap**2-2*D0*kap
bias=float(Einf-ER+x['strip_residual_partial_integral'])
eta=1e-7; P=v['p']+v['q']; missing=(2*eta/pi)*(7+P/pi*(5+2*math.log(4*pi/eta)))
old=json.loads(Path('topics/padua-argmax-bridge-20261105/evidence/d01-far.json').read_text())
res=[{'n':r['n'],'old_residual':r['S_minus_M'],'bias_subtracted':r['S_minus_M']-bias} for r in old['results'] if r['phase']==2]
r=resource.getrusage(resource.RUSAGE_SELF)
print(json.dumps({'status':'MEASURED','E_infty':float(Einf),'E64':float(ER),'endpoint_tail':float(Einf-ER),'partial_strip':x['strip_residual_partial_integral'],'estimated_bias':bias,'omitted_strip_analytic_bound':missing,'old_strip_quadrature_estimate':x['strip_residual_partial_estimate'],'results':res,'python':sys.version.split()[0],'scipy':scipy.__version__,'CPU_seconds':r.ru_utime+r.ru_stime},indent=2))
```

Observed E_infty=1.342661167066038, E64=1.342661516840213;
the signed endpoint-tail difference is -3.49774174957e-7. Adding the
existing partial strip integral .000960616234574709 gives the bias
estimate .000960266460399752. The omitted (0,1e-7) analytic envelope is
2.14742493327e-6; the earlier floating quadrature error estimate was
1.22910791417e-10. The latter and roundoff are not rigorous enclosures,
so the displayed decimal bias is MEASURED, not a certified interval.

| Existing n | Existing S-M_far | After estimated bias subtraction |
|---:|---:|---:|
| 512 | .001009722030579141 | .0000494555701793893 |
| 2048 | .0008985712407465485 | -.0000616952196532032 |
| 8192 | .0009264135899851311 | -.0000338528704146206 |

This identifies the size and sign of the two contributions under the
proved formula; it does not fit a rate or estimate a uniform constant.
No analytic upper is inferred from the three samples. The exact midpoint
control was reconstructed analytically and no midpoint value was rerun.
The unused diagnostic budget remains unused.
