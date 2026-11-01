/* L5 R02 diagnostic: run the 'scheme' point-by-point Givens updating of VB-C 2010 in double and in long double (x87, 64-bit
 * mantissa) in lockstep from the same inputs; at checkpoints i report ||H_dbl - H_ld||_F over the active i x i blocks of (Hx, Hy)
 * relative to ||H_ld||_F, the max entry difference, the same restricted to the pivot structure (entries outside the band of
 * structural nonzeros are treated by the caller), and the number of rotations executed so far.
 * Both states form rotations from their own data (no shared angles).  Same operation order as givens_core.c.
 * Build: gcc -O2 -ffp-contract=off -shared -fPIC -o libgivens_dual.so givens_dual.c -lm
 * rule is fixed to 'scheme' (primary parent); rule 'largest' available with rule=1 for the double state only is NOT provided here.
 * out[3*c + {0,1,2}] = (relative Frobenius diff, max entry diff, nrot) for checkpoint c.
 */
#include <math.h>
#include <stdlib.h>
#include <string.h>

#define DEFSTATE(NAME, T, HYPOT) \
static void rot_##NAME(T *A, long M, int n, int j, int i, T c, T s) { \
    T *rj = A + (long)j * M, *ri = A + (long)i * M; \
    for (int k = 0; k < n; k++) { T a = rj[k], b = ri[k]; rj[k] = c * a + s * b; ri[k] = -s * a + c * b; } \
    for (int k = 0; k < n; k++) { T *row = A + (long)k * M; T a = row[j], b = row[i]; row[j] = c * a + s * b; row[i] = -s * a + c * b; } \
} \
static void step_##NAME(T *Hx, T *Hy, T *w, const T *x, const T *y, const T *v, long M, long i, \
                        const int *pi, const int *pv, long *nrot) { \
    w[i] = v[i]; Hx[i * M + i] = x[i]; Hy[i * M + i] = y[i]; int n = (int)i + 1; \
    for (int j = 0; j < (int)i; j++) { \
        T a, b; \
        if (j == 0) { a = w[0]; b = w[i]; } \
        else { int p = pi[j]; T *H = pv[j] == 0 ? Hx : Hy; a = H[(long)j * M + p]; b = H[i * M + p]; } \
        if (b == 0) continue; \
        T r = HYPOT(a, b), c = a / r, s = b / r; \
        rot_##NAME(Hx, M, n, j, (int)i, c, s); rot_##NAME(Hy, M, n, j, (int)i, c, s); \
        T wj = w[j], wi = w[i]; w[j] = c * wj + s * wi; w[i] = -s * wj + c * wi; (*nrot)++; \
    } \
}
DEFSTATE(d, double, hypot)
DEFSTATE(l, long double, hypotl)

int givens_dual(const double *x, const double *y, const double *v, long M, const int *pi, const int *pv,
                const long *ckpt, int nck, double *out)
{
    double *Hxd = calloc(M * M, sizeof(double)), *Hyd = calloc(M * M, sizeof(double)), *wd = calloc(M, sizeof(double));
    long double *Hxl = calloc(M * M, sizeof(long double)), *Hyl = calloc(M * M, sizeof(long double)), *wl = calloc(M, sizeof(long double));
    long double *xl = malloc(M * sizeof(long double)), *yl = malloc(M * sizeof(long double)), *vl = malloc(M * sizeof(long double));
    for (long k = 0; k < M; k++) { xl[k] = x[k]; yl[k] = y[k]; vl[k] = v[k]; }
    long nd = 0, nl = 0; int c = 0;
    wd[0] = v[0]; Hxd[0] = x[0]; Hyd[0] = y[0]; wl[0] = vl[0]; Hxl[0] = xl[0]; Hyl[0] = yl[0];
    for (long i = 1; i < M; i++) {
        step_d(Hxd, Hyd, wd, x, y, v, M, i, pi, pv, &nd);
        step_l(Hxl, Hyl, wl, xl, yl, vl, M, i, pi, pv, &nl);
        if (c < nck && i + 1 == ckpt[c]) {
            int n = (int)i + 1; long double sd = 0, sn = 0, mx = 0;
            for (int r = 0; r < n; r++) for (int q = 0; q < n; q++) {
                long double dx = (long double)Hxd[(long)r * M + q] - Hxl[(long)r * M + q];
                long double dy = (long double)Hyd[(long)r * M + q] - Hyl[(long)r * M + q];
                sd += dx * dx + dy * dy; sn += Hxl[(long)r * M + q] * Hxl[(long)r * M + q] + Hyl[(long)r * M + q] * Hyl[(long)r * M + q];
                long double a1 = fabsl(dx), a2 = fabsl(dy); if (a1 > mx) mx = a1; if (a2 > mx) mx = a2;
            }
            out[3 * c] = (double)sqrtl(sd / sn); out[3 * c + 1] = (double)mx; out[3 * c + 2] = (double)nd; c++;
        }
    }
    free(Hxd); free(Hyd); free(wd); free(Hxl); free(Hyl); free(wl); free(xl); free(yl); free(vl);
    return 0;
}
