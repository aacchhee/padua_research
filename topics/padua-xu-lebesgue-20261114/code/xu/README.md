# code/xu — X1 (Xu interpolation Lebesgue function)

Conventions: `literature-xu-mp.md` section 1 (K_{n+1} kernel, unscaled T_n, flags F1-F3). Points are passed as angles
(x = (cos th, cos ph)). Environment: python 3.x, numpy, scipy, mpmath 1.4.1, python-flint 0.9.0 (versions are
recorded inside every evidence JSON). 2 cores. Everything is deterministic (seed 20261114).

| file | role |
|---|---|
| `xu_exact.py` | Path A: arb (python-flint, 256 bit) Vandermonde solve in the product Chebyshev basis; Lagrange enclosures, determinant, interpolation check |
| `xu_kernel.py` | Path B: mpmath kernel (orthonormal sum, compact D_n form, K*, l_xi, lambda, closed-form vertex value) and vectorised float64 `XuFloat` for screening |
| `g0_check.py` | G0 checks, writes `evidence/xu-g0.json` |
| `g1_screen.py` | G1 screen n = 2..60, writes `evidence/xu-g1-summary.json` (+ raw `/tmp/xu-runs/g1_raw_n*.json`) |
| `vertex_values.py` | lambda_n(v), v in V*, even n <= 400 and odd n <= 401, `evidence/xu-vertex-values.json` |

## Reproduction (run from the topic directory; wall times on 2 cores, measured)
```
python3 code/xu/g0_check.py --nmax 12            # 3 min 6 s  -> evidence/xu-g0.json   (G0_PASS true)
python3 code/xu/g1_screen.py --nmin 2 --nmax 60  # ~1.5 min   -> evidence/xu-g1-summary.json, /tmp/xu-runs/g1_raw_n*.json
python3 code/xu/vertex_values.py                 # ~12 min (even 393 s, odd 322 s) -> evidence/xu-vertex-values.json
```
Options: `g0_check.py --npts 200 --skip-lambda`; `g1_screen.py --ns 20,21 --digits 40 --summary PATH --raw DIR`.
Run G1 only after G0 (gates.md); the G1 run reported here was done after a passing G0.

## Method notes
* Path B kernel: K_d = sum of four D_d terms, D_d(a,b) = 1/2[cos((d-1/2)a)cos(a/2) - cos((d-1/2)b)cos(b/2)]/(cos a - cos b);
  the removable singularity (|cos a - cos b| < 1e-8) is evaluated by the defining finite trigonometric sum
  D_d = sum_{i+j<=d-1} w_i w_j cos(ia)cos(jb), w_0 = 1/2. Also checked against the orthonormal sum (G0 C4).
* Vertex closed form (xu_kernel.vertex_value): at x = (1,1), 1/2(K_n+K_{n+1})(x, x_{r,s}) =
  [(-1)^r(1+cos a) - (-1)^s(1+cos b)]/(cos a - cos b), a = r pi/n, b = s pi/n (O(1) per node); other vertices by T_l(-1) = (-1)^l
  (index reflection). Verified against the generic path B at all four vertices for n <= 12 and n = 34, and against path A (n <= 12).
* Screen kernel: lambda(th,ph) = sum_xi w_xi |sum_{k+l<=n} Q_kl eps_k eps_l cos k th cos l ph cos(k pi r/n) cos(l pi s/n) + extra|,
  Q = 1 (k+l<=n-1), 1/2 (k+l=n); evaluated by BLAS products per node row. Float64 error about 1e-13 (path A grid cross-check n <= 12: max 7e-15).
* Maxima of lambda sit at smooth points (|.| kinks are convex), so the polish freezes the signs of all l_xi at the refined point,
  forms the cosine polynomial sum C_kl cos(k th) cos(l ph) in arb (>= 40 digits, 192 bit, 60 digits for g_n < 1e-6), does Newton on the face
  and re-checks signs; the reported lambda is a direct arb enclosure of sum |l_xi| at the polished point.
  `signs_ok` and `converged` are recorded; Hessian sign gives `locmax_Q` (true local maximum of lambda on Q).
* Symmetry reduction: Lemma S only (even n: 8 elements; odd n: swap and central reflection). Edges theta=0, theta=pi, phi=0, phi=pi are
  equivalent under these groups (even and odd), so `e_th0`/`e_ph0` labels in the output are the same family.
* Grid maxima: 8-neighbourhood in the interior, 1-D along edges (an edge point need not beat its interior neighbour), corners always.
  Beyond the pre-registered 0.9*max V* threshold the screen also refines (i) up to 6 non-vertex orbits if fewer exist, (ii) the 3 best
  interior orbits, for the structure report; cap 80 orbits per n. n = 2 has a plateau lambda = 1 (flat interior), Newton is skipped there
  (`converged` false, value taken at the float point).
