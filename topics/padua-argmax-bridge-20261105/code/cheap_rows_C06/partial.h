#ifndef PADUA_C06_PARTIAL_H
#define PADUA_C06_PARTIAL_H
#include <flint/arb.h>
#ifdef __cplusplus
extern "C" {
#endif
// n in [2,2147483647], q in [0,n]. For q>0, entire finite input ball
// satisfies 0<y and y+q-1<n. Returns enclosure of sum cot(pi*(y+i)/n).
// q=0 returns zero. Return 1 and indeterminate output on invalid input.
// Arb160 operations, exact rational moments, Arb640 coefficient preparation.
int c06_partial_arb(long n,long q,const arb_t y,arb_t out);
// Diagnostic outward binary64 lower/upper, then full Arb radius; return 0 on success.
int c06_partial(long n,long q,const char*y,double*out);
#ifdef __cplusplus
}
#endif
#endif
