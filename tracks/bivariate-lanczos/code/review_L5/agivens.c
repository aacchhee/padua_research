/* L5 adversarial reconstruction (auditor's own code; written from Van Barel-Chesnokov 2010, Numer. Algor. 55,
 * Sect. 4, Algorithm 1 and the 6x6 example pp. 391-395; NOT derived from the developer's givens_core.c).
 *
 * D = [w | X | Y] (M x (2M+1)), real nodes.  Point i (0-based) is appended with w_i = v_i, X_ii = x_i, Y_ii = y_i;
 * then for j = 0..i-1 the element D[i, pi(j)] is annihilated by a Givens rotation built on the pivot D[j, pi(j)]
 * (pi(0) = the w column; for j >= 1 a column of the X or Y part fixed by the downside-up scheme (12), or for
 * rule 'largest' the larger of the two candidate pivots of a doubly-parented monomial).  The rotation acts on rows j,i
 * of D and, as a similarity, on columns j,i of the X and Y parts.  Optionally Q^T is accumulated (rows j,i of Qt).
 *
 * Precision: REAL = double (default) or long double (-DAG_LD).
 * Build:  gcc -O2 -ffp-contract=off -shared -fPIC -o libagivens.so agivens.c -lm
 *         gcc -O2 -ffp-contract=off -DAG_LD -shared -fPIC -o libagivens_ld.so agivens.c -lm
 * Interface arrays are double; long-double builds take/return long double arrays (numpy.longdouble).
 *
 * piv_part[j]: 0 = w, 1 = X, 2 = Y;  piv_col[j]: column inside that part.  alt_part[j] = -1 if no alternative.
 * rule: 0 scheme (primary pivot), 1 largest (larger |pivot| of primary/alternative; tie -> primary).
 * stats[0] executed rotations, stats[1] skipped (b == 0), stats[2] alternative pivots taken.
 */
#include <math.h>
#include <stdlib.h>
#include <string.h>

#ifdef AG_LD
typedef long double REAL;
#define HYPOT hypotl
#define FABS fabsl
#else
typedef double REAL;
#define HYPOT hypot
#define FABS fabs
#endif

static inline REAL *part(REAL *w, REAL *X, REAL *Y, int p) { return p == 0 ? w : (p == 1 ? X : Y); }

/* apply G = [[c, s], [-s, c]] to rows r1 < r2 (first n entries), row-major, leading dimension M */
static void rows2(REAL *A, long M, long n, long r1, long r2, REAL c, REAL s)
{
    REAL *u = A + r1 * M, *v = A + r2 * M;
    for (long k = 0; k < n; k++) { REAL a = u[k], b = v[k]; u[k] = c * a + s * b; v[k] = c * b - s * a; }
}
/* apply G to columns c1 < c2 (first n rows) */
static void cols2(REAL *A, long M, long n, long c1, long c2, REAL c, REAL s)
{
    for (long k = 0; k < n; k++) {
        REAL *r = A + k * M; REAL a = r[c1], b = r[c2];
        r[c1] = c * a + s * b; r[c2] = c * b - s * a;
    }
}

int ag_run(long M, const REAL *x, const REAL *y, const REAL *v,
           const int *piv_part, const int *piv_col, const int *alt_part, const int *alt_col,
           int rule, REAL *X, REAL *Y, REAL *w, REAL *Qt, double *stats)
{
    long nrot = 0, nskip = 0, nalt = 0;
    memset(X, 0, sizeof(REAL) * M * M); memset(Y, 0, sizeof(REAL) * M * M); memset(w, 0, sizeof(REAL) * M);
    if (Qt) memset(Qt, 0, sizeof(REAL) * M * M);
    for (long i = 0; i < M; i++) {
        w[i] = v[i]; X[i * M + i] = x[i]; Y[i * M + i] = y[i]; if (Qt) Qt[i * M + i] = 1;
        long n = i + 1;
        for (long j = 0; j < i; j++) {
            int pp = piv_part[j]; long pc = piv_col[j];
            REAL a, b;
            if (pp == 0) { a = w[j]; b = w[i]; }
            else {
                REAL *P = part(w, X, Y, pp);
                a = P[j * M + pc];
                if (rule == 1 && alt_part[j] >= 0) {
                    REAL *A2 = part(w, X, Y, alt_part[j]); REAL a2 = A2[j * M + alt_col[j]];
                    if (FABS(a2) > FABS(a)) { P = A2; pc = alt_col[j]; a = a2; nalt++; }
                }
                b = P[i * M + pc];
            }
            if (b == 0) { nskip++; continue; }
            REAL r = HYPOT(a, b), c = a / r, s = b / r;
            /* rows j,i of D = [w | X | Y] */
            { REAL a0 = w[j], b0 = w[i]; w[j] = c * a0 + s * b0; w[i] = c * b0 - s * a0; }
            rows2(X, M, n, j, i, c, s); rows2(Y, M, n, j, i, c, s);
            /* similarity: columns j,i of the X and Y parts */
            cols2(X, M, n, j, i, c, s); cols2(Y, M, n, j, i, c, s);
            if (Qt) rows2(Qt, M, n, j, i, c, s);
            nrot++;
        }
    }
    stats[0] = (double)nrot; stats[1] = (double)nskip; stats[2] = (double)nalt;
    return 0;
}
