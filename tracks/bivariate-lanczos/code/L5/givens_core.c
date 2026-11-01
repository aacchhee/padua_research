/* L5: C port of the point-by-point Givens updating of Van Barel-Chesnokov 2010 (Algorithm 1),
 * mirroring givens() in code/inputs/f6_givens_vs_hl_deficit.py (real nodes), without the Q^T accumulation.
 * Operation order is the same as the Python/numpy version (row rotation then column rotation, both matrices).
 * Build: gcc -O2 -ffp-contract=off -shared -fPIC -o libgivens_core.so givens_core.c -lm
 *
 * rule: 0 = 'scheme' (primary parent), 1 = 'largest' (larger |pivot| among primary/alternative),
 *       2 = 'smaller' (diagnostic only: smaller |pivot|)
 * tol : rotation is skipped if |b| <= tol*scale (tol = 0 reproduces the input code: skip only if b == 0)
 * stats[0] = number of rotations applied, stats[1] = number skipped, stats[2] = number of alt-pivot choices taken
 */
#include <math.h>
#include <string.h>
#include <stdlib.h>

static void rot_rows_cols(double *A, long M, int n, int j, int i, double c, double s)
{
    double *rj = A + (long)j * M, *ri = A + (long)i * M;
    for (int k = 0; k < n; k++) {
        double a = rj[k], b = ri[k];
        rj[k] = c * a + s * b;
        ri[k] = -s * a + c * b;
    }
    for (int k = 0; k < n; k++) {
        double *row = A + (long)k * M;
        double a = row[j], b = row[i];
        row[j] = c * a + s * b;
        row[i] = -s * a + c * b;
    }
}

/* prim_idx/prim_var/alt_idx/alt_var: length M tables (alt_idx = -1 if no alternative); entry 0 unused */
int givens_run(const double *x, const double *y, const double *v, long M,
               const int *prim_idx, const int *prim_var, const int *alt_idx, const int *alt_var,
               int rule, double tol, double scale,
               double *Hx, double *Hy, double *stats)
{
    double *w = (double *)calloc(M, sizeof(double));
    long nrot = 0, nskip = 0, nalt = 0;
    memset(Hx, 0, sizeof(double) * M * M);
    memset(Hy, 0, sizeof(double) * M * M);
    w[0] = v[0]; Hx[0] = x[0]; Hy[0] = y[0];
    for (long i = 1; i < M; i++) {
        w[i] = v[i]; Hx[i * M + i] = x[i]; Hy[i * M + i] = y[i];
        int n = (int)i + 1;
        for (int j = 0; j < (int)i; j++) {
            double a, b;
            if (j == 0) { a = w[0]; b = w[i]; }
            else {
                int p = prim_idx[j]; double *H = prim_var[j] == 0 ? Hx : Hy;
                if (rule != 0 && alt_idx[j] >= 0) {
                    int pa = alt_idx[j]; double *Ha = alt_var[j] == 0 ? Hx : Hy;
                    double fa = fabs(Ha[(long)j * M + pa]), fp = fabs(H[(long)j * M + p]);
                    int take = (rule == 1) ? (fa > fp) : (fa < fp);
                    if (take) { p = pa; H = Ha; nalt++; }
                }
                a = H[(long)j * M + p]; b = H[i * M + p];
            }
            if (tol == 0.0 ? (b == 0.0) : (fabs(b) <= tol * scale)) { nskip++; continue; }
            double r = hypot(a, b), c = a / r, s = b / r;
            rot_rows_cols(Hx, M, n, j, (int)i, c, s);
            rot_rows_cols(Hy, M, n, j, (int)i, c, s);
            double wj = w[j], wi = w[i];
            w[j] = c * wj + s * wi; w[i] = -s * wj + c * wi;
            nrot++;
        }
    }
    stats[0] = (double)nrot; stats[1] = (double)nskip; stats[2] = (double)nalt;
    free(w);
    return 0;
}

/* R03 extension: pivot rules compared on the norm of the rotated pair.
 * rule 3 ('pairnorm'): use the alternative pivot pair (a_alt,b_alt) instead of the primary pair if
 *                      hypot(a_alt,b_alt) > kappa * hypot(a_prim,b_prim)   (kappa >= 1; kappa = inf reproduces 'scheme')
 * rule 4 ('pivot-kappa'): use the alternative if |a_alt| > kappa*|a_prim|   (kappa = 1 is 'largest')
 * stats as in givens_run; extra: stats[3] = number of rotations whose pair norm was < 1e-10 (noise-level rotations)
 */
int givens_run2(const double *x, const double *y, const double *v, long M,
                const int *prim_idx, const int *prim_var, const int *alt_idx, const int *alt_var,
                int rule, double kappa, double *Hx, double *Hy, double *stats)
{
    double *w = (double *)calloc(M, sizeof(double));
    long nrot = 0, nskip = 0, nalt = 0, nnoise = 0;
    memset(Hx, 0, sizeof(double) * M * M);
    memset(Hy, 0, sizeof(double) * M * M);
    w[0] = v[0]; Hx[0] = x[0]; Hy[0] = y[0];
    for (long i = 1; i < M; i++) {
        w[i] = v[i]; Hx[i * M + i] = x[i]; Hy[i * M + i] = y[i];
        int n = (int)i + 1;
        for (int j = 0; j < (int)i; j++) {
            double a, b;
            if (j == 0) { a = w[0]; b = w[i]; }
            else {
                int p = prim_idx[j]; double *H = prim_var[j] == 0 ? Hx : Hy;
                a = H[(long)j * M + p]; b = H[i * M + p];
                if (alt_idx[j] >= 0) {
                    int pa = alt_idx[j]; double *Ha = alt_var[j] == 0 ? Hx : Hy;
                    double aa = Ha[(long)j * M + pa], ba = Ha[i * M + pa];
                    int take = 0;
                    if (rule == 3) take = hypot(aa, ba) > kappa * hypot(a, b);
                    else if (rule == 4) take = fabs(aa) > kappa * fabs(a);
                    if (take) { a = aa; b = ba; nalt++; }
                }
            }
            if (b == 0.0) { nskip++; continue; }
            double r = hypot(a, b), c = a / r, s = b / r;
            if (r < 1e-10) nnoise++;
            rot_rows_cols(Hx, M, n, j, (int)i, c, s);
            rot_rows_cols(Hy, M, n, j, (int)i, c, s);
            double wj = w[j], wi = w[i]; w[j] = c * wj + s * wi; w[i] = -s * wj + c * wi;
            nrot++;
        }
    }
    stats[0] = (double)nrot; stats[1] = (double)nskip; stats[2] = (double)nalt; stats[3] = (double)nnoise;
    free(w);
    return 0;
}

/* R03: insert ONE point into an existing state (slot i = number of points already inserted; arrays are M x M row-major, zero
 * beyond the active block).  Same operations as one pass of the outer loop of givens_run (rule: 0 scheme, 1 largest, 3 pairnorm,
 * 4 pivot-kappa).  Returns in *minpiv the smallest |pivot| over the monomials j = 0..i after the chase
 * (|w_0| for j = 0, |V(j)[j,p(j)]| for j >= 1): the online non-unisolvence detector tested in R03. */
int givens_insert(double *Hx, double *Hy, double *w, long M, long i, double xi, double yi, double vi,
                  const int *prim_idx, const int *prim_var, const int *alt_idx, const int *alt_var,
                  int rule, double kappa, double *minpiv)
{
    w[i] = vi; Hx[i * M + i] = xi; Hy[i * M + i] = yi;
    int n = (int)i + 1;
    for (int j = 0; j < (int)i; j++) {
        double a, b;
        if (j == 0) { a = w[0]; b = w[i]; }
        else {
            int p = prim_idx[j]; double *H = prim_var[j] == 0 ? Hx : Hy;
            a = H[(long)j * M + p]; b = H[i * M + p];
            if (alt_idx[j] >= 0 && rule != 0) {
                int pa = alt_idx[j]; double *Ha = alt_var[j] == 0 ? Hx : Hy;
                double aa = Ha[(long)j * M + pa], ba = Ha[i * M + pa]; int take = 0;
                if (rule == 1) take = fabs(aa) > fabs(a);
                else if (rule == 3) take = hypot(aa, ba) > kappa * hypot(a, b);
                else if (rule == 4) take = fabs(aa) > kappa * fabs(a);
                if (take) { a = aa; b = ba; }
            }
        }
        if (b == 0.0) continue;
        double r = hypot(a, b), c = a / r, s = b / r;
        rot_rows_cols(Hx, M, n, j, (int)i, c, s);
        rot_rows_cols(Hy, M, n, j, (int)i, c, s);
        double wj = w[j], wi = w[i]; w[j] = c * wj + s * wi; w[i] = -s * wj + c * wi;
    }
    double mp = fabs(w[0]);
    for (int j = 1; j <= (int)i; j++) {
        double *H = prim_var[j] == 0 ? Hx : Hy; double q = fabs(H[(long)j * M + prim_idx[j]]);
        if (q < mp) mp = q;
    }
    *minpiv = mp;
    return 0;
}
