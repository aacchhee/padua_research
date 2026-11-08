# P-audit referee checks (journal paper), Claude Opus 5.5 xhigh, 2026-11-08

Read-only checks against branch head f366535e1fa4ede566cb83bdc554220c12b307cf.
All results are MEASURED numerical sanity checks (float64 / mpmath 30-40 digits,
mpmath 1.3.0, numpy 2.5.3, Python 3.13); none is a proof. Run from this directory:

    PYTHONPATH=<audit3>/pylib python3 check_corner.py      # Sections 2-3 (7 CPU-s)
    PYTHONPATH=<audit3>/pylib python3 check_constants.py   # Section 4 rational bounds (9 CPU-s)
    PYTHONPATH=<audit3>/pylib python3 check_floors.py      # Lemma 4.6 floors vs actual projections (63 CPU-s)
    PYTHONPATH=<audit3>/pylib python3 check_regions.py     # lambda_n corner descent, noncorner charts (32 CPU-s)
    (check_regions2.py: S_n regional scan with collision-safe offsets, driven as in p-paper.md; 25 CPU-s)
    PYTHONPATH=<audit3>/pylib python3 check_geometry.py    # (ul:outer-geometry), (uc:weighted-C), Lemma 4.1 (7 CPU-s)

Outputs: the matching `*.out` files. Total about 2.4 CPU-minutes.

Key results:
- Lemma 2.1 matches an independent Vandermonde solve (n=1..8, 1e-15); (cu:positive),
  both identities (cu:exact), (cu:square) and the midpoint form of L_n agree to 1e-39.
- (cu:deform): max |diff|*2l^2/(pi^2 n) = 0.20 (bound 1), n <= 1000.
- kappa = 0.91971011838849253510 by the integral and by the (uc:kappa-series), K=64.
  K=5 partial sum + stated tail gives kappa in [0.919599, 0.919785] (interval check),
  which already implies 9/10<kappa<23/25 and C_*<1847/1000.
- (cu:cancel), S_u, psi(1/2) identities hold to 1e-40.
- Expansion residual r_n*N^2/log N = 0.21, 0.12, 0.063, 0.022, -0.0075, -0.030, -0.049,
  -0.063, -0.075, -0.085 for n = 8..4096 (doubling): bounded, consistent with O(log N/N^2).
- H(0) computed directly as a finite part equals kappa/2+(2k_0/pi^2)log(2/pi) to 1e-31
  (uc:origin-identity); H(w)<=H(0) on a grid; scalar f bounds hold with wide margins.
- Every displayed rational bound checked at n=320 (near/annulus/wide/outer), 256 (corner),
  192 (far): all hold; F_h, F_w coefficients recomputed exactly equal the displayed A_h,B_h,A_w,B_w;
  E_64-1/64 and E_160-1/32 exact; far192 anchor = 79/2000 exactly.
- Outer gate G-A^2/(4K) increases from 0.069 at n=320; it is 0.064 at 319 and negative at 300.
- Lemma 4.6 floors are 5.5x (n=320) to 54x (n=41) below the smallest actual eligible projection
  on the sampled phases.
- Regional scan (n=192,320, 72x72 grid): S_n-Lambda_c-P(rho) <= -0.018 on rho<=1; outer and far
  gaps hold with margins >1.6; corner descent lambda <= Lambda_c-(A^2+B^2)/30 holds on a 9x9 grid
  (true descent coefficient near the corner is about L^2/pi^2 ~ 3.4).
- (ul:outer-geometry) holds on a 1201^2 grid, but the stated route "x>=1 via u>=11/48" alone
  gives only p0+eta*sqrt(11/48-u1)=0.970<1; the E13 two-case argument is needed.
