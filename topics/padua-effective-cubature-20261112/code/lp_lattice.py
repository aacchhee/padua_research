#!/usr/bin/env python3
"""Upper references M_lat(n) for the torus LP (Q1b).

M_lat(n) = min index [Z^3:L] of a sublattice L with L ∩ {0<|k|_1<=2n-2} = ∅.
  exhaust : exhaustive search over all Hermite normal forms of index d = m_n, m_n+1, ...
            (first admissible d is the EXACT minimum, since d >= m_n always).
  random  : seeded random HNF / rank-1 search for d = start, start+1, ... (UPPER bound only).
Every reported lattice is re-verified in Python (independent of the C search) by enumerating all
k with 0<|k|_1<=2n-2 and testing membership with exact integer arithmetic.
The inner search is C (compiled at run time with gcc -O2, source embedded below).
"""
import argparse, hashlib, json, os, platform, subprocess, sys, time, tempfile
import numpy as np
import scipy

CSRC = r"""
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
typedef long long ll;
static int NV; static int (*V)[3];
static int cmp(const void*a,const void*b){const int*x=a,*y=b;int nx=abs(x[0])+abs(x[1])+abs(x[2]),ny=abs(y[0])+abs(y[1])+abs(y[2]);return nx-ny;}
static void build(int r){ int cap=(2*r+1)*(2*r+1)*(2*r+1); V=malloc(sizeof(int[3])*cap); NV=0;
 for(int x=-r;x<=r;x++)for(int y=-r;y<=r;y++)for(int z=-r;z<=r;z++){ int s=abs(x)+abs(y)+abs(z); if(s==0||s>r)continue;
   /* half space: first nonzero coord positive */
   int f = x? x : (y? y : z); if(f<0)continue; V[NV][0]=x;V[NV][1]=y;V[NV][2]=z;NV++; }
 qsort(V,NV,sizeof(int[3]),cmp); }
/* returns 1 if lattice with HNF rows (a,b,c),(0,d2,e),(0,0,d3) has no nonzero vector of V */
static int admissible(int a,int b,int c,int d2,int e,int d3){
 for(int i=0;i<NV;i++){ ll k1=V[i][0],k2=V[i][1],k3=V[i][2];
   if(k1%a)continue; ll x1=k1/a; ll r2=k2-x1*b; if(r2%d2)continue; ll x2=r2/d2; ll r3=k3-x1*c-x2*e; if(r3%d3)continue; return 0; }
 return 1; }
static uint64_t rs; static uint64_t rnd(){ rs^=rs<<13; rs^=rs>>7; rs^=rs<<17; return rs; }
int main(int argc,char**argv){
 /* usage: mode r dmin dmax samples seed ; mode 0=exhaust 1=random HNF 2=random rank-1 */
 int mode=atoi(argv[1]); int r=atoi(argv[2]); int dmin=atoi(argv[3]); int dmax=atoi(argv[4]); ll samples=atoll(argv[5]); rs=atoll(argv[6])*2654435761ULL+88172645463325252ULL;
 build(r);
 for(int d=dmin; d<=dmax; d++){
  ll cnt=0; int found=0; int fa=0,fb=0,fc=0,fd2=0,fe=0,fd3=0;
  if(mode==0){
   for(int a=1;a<=d && !found;a++){ if(d%a)continue; int q=d/a;
    for(int d2=1;d2<=q && !found;d2++){ if(q%d2)continue; int d3=q/d2;
     for(int b=0;b<d2 && !found;b++)for(int c=0;c<d3 && !found;c++)for(int e=0;e<d3;e++){ cnt++;
       if(admissible(a,b,c,d2,e,d3)){found=1;fa=a;fb=b;fc=c;fd2=d2;fe=e;fd3=d3;break;} } } }
  } else if(mode==1){
   /* random factorisation (a,d2,d3) then random b,c,e */
   int nf=0; int (*F)[3]=malloc(sizeof(int[3])*(d+5)*40);
   for(int a=1;a<=d;a++){ if(d%a)continue; int q=d/a; for(int d2=1;d2<=q;d2++){ if(q%d2)continue; F[nf][0]=a;F[nf][1]=d2;F[nf][2]=q/d2;nf++; } }
   for(ll s=0;s<samples && !found;s++){ int*f=F[rnd()%nf]; int a=f[0],d2=f[1],d3=f[2];
     int b=rnd()%d2,c=rnd()%d3,e=rnd()%d3; cnt++;
     if(admissible(a,b,c,d2,e,d3)){found=1;fa=a;fb=b;fc=c;fd2=d2;fe=e;fd3=d3;} }
   free(F);
  } else {
   /* rank-1: L={k: k1 + A k2 + B k3 = 0 mod d}; basis HNF rows computed in python on output; here test directly */
   for(ll s=0;s<samples && !found;s++){ ll A=rnd()%d,B=rnd()%d; cnt++; int ok=1;
     for(int i=0;i<NV;i++){ ll t=(V[i][0]+A*V[i][1]+B*V[i][2])%d; if(t==0){ok=0;break;} }
     if(ok){found=1;fa=(int)A;fb=(int)B;} }
  }
  printf("%d %lld %d %d %d %d %d %d %d\n",d,cnt,found,fa,fb,fc,fd2,fe,fd3); fflush(stdout);
  if(found)break;
 }
 return 0; }
"""


def m_n(n):
    return (2 * n - 1) * (2 * n * n - 2 * n + 3) // 3


def compile_c(workdir):
    src = os.path.join(workdir, "lat.c"); exe = os.path.join(workdir, "lat")
    open(src, "w").write(CSRC)
    subprocess.check_call(["gcc", "-O2", "-o", exe, src])
    return exe


def verify_basis(n, B):
    """Exact check: B is 3x3 integer basis (rows). Returns (index, admissible). Pure-Python integers."""
    B = [[int(x) for x in row] for row in B]
    det = (B[0][0] * (B[1][1] * B[2][2] - B[1][2] * B[2][1]) - B[0][1] * (B[1][0] * B[2][2] - B[1][2] * B[2][0])
           + B[0][2] * (B[1][0] * B[2][1] - B[1][1] * B[2][0]))
    d = abs(det)
    assert d > 0
    # adjugate: x = k * B^{-1} integer iff k*adj(B) == 0 mod det
    adj = [[0] * 3 for _ in range(3)]
    def mnr(i, j):
        r = [x for x in range(3) if x != i]; c = [x for x in range(3) if x != j]
        return B[r[0]][c[0]] * B[r[1]][c[1]] - B[r[0]][c[1]] * B[r[1]][c[0]]
    for i in range(3):
        for j in range(3):
            adj[j][i] = ((-1) ** (i + j)) * mnr(i, j)  # adj = cofactor^T ; B^{-1} = adj/det
    R = 2 * n - 2
    bad = None
    for x in range(-R, R + 1):
        for y in range(-R + abs(x), R - abs(x) + 1):
            zr = R - abs(x) - abs(y)
            for z in range(-zr, zr + 1):
                if x == y == z == 0:
                    continue
                k = (x, y, z)
                # k = u B  =>  u = k B^{-1} = k adj / det
                if all(sum(k[i] * adj[i][j] for i in range(3)) % d == 0 for j in range(3)):
                    bad = k; break
            if bad: break
        if bad: break
    return d, bad is None, bad


def hnf_basis(a, b, c, d2, e, d3):
    return [[a, b, c], [0, d2, e], [0, 0, d3]]


def rank1_basis(M, A, B):
    # L = {k : k1 + A k2 + B k3 = 0 mod M}; basis (M,0,0), (-A,1,0), (-B,0,1)
    return [[M, 0, 0], [-A, 1, 0], [-B, 0, 1]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["exhaust", "random", "rank1"], required=True)
    ap.add_argument("--ns", type=int, nargs="+", required=True)
    ap.add_argument("--dmax-factor", type=float, default=1.3)
    ap.add_argument("--start-factor", type=float, default=1.0, help="start d at ceil(factor*m_n) (random modes)")
    ap.add_argument("--samples", type=int, default=2_000_000, help="samples per d (random modes)")
    ap.add_argument("--seed", type=int, default=12345)
    ap.add_argument("--out", required=True)
    ap.add_argument("--workdir", default="/tmp/claude-0/-workspace-padua-research/e2057052-bb3b-5345-abf7-4ff7dc19c8ac/scratchpad/lp")
    args = ap.parse_args()
    os.makedirs(args.workdir, exist_ok=True)
    exe = compile_c(args.workdir)
    receipt = dict(script_sha256=hashlib.sha256(open(__file__, "rb").read()).hexdigest(),
                   python=platform.python_version(), numpy=np.__version__, scipy=scipy.__version__,
                   gcc=subprocess.run(["gcc", "--version"], capture_output=True, text=True).stdout.splitlines()[0],
                   argv=sys.argv, args=vars(args), results=[])
    mode = {"exhaust": 0, "random": 1, "rank1": 2}[args.mode]
    for n in args.ns:
        t0 = time.time()
        m = m_n(n)
        r = 2 * n - 2
        dstart = m if mode == 0 else int(np.ceil(args.start_factor * m))
        dmax = int(args.dmax_factor * m) + 1
        proc = subprocess.run([exe, str(mode), str(r), str(dstart), str(dmax), str(args.samples), str(args.seed + n)],
                              capture_output=True, text=True, check=True)
        lines = [list(map(int, l.split())) for l in proc.stdout.strip().splitlines()]
        last = lines[-1]
        d, cnt, found = last[0], last[1], last[2]
        entry = dict(n=n, m_n=m, mode=args.mode, d_tried=[l[0] for l in lines][-1], searched_from=dstart,
                     hnf_or_samples_tested_last_d=cnt, seconds=round(time.time() - t0, 3))
        if found:
            if mode == 2:
                B = rank1_basis(d, last[3], last[4])
            else:
                B = hnf_basis(*[last[3], last[4], last[5], last[6], last[7], last[8]])
            idx, ok, bad = verify_basis(n, B)
            assert ok and idx == d, (n, B, idx, ok, bad)
            entry.update(M=idx, M_over_m=idx / m, basis=B, verified_exact=True,
                         kind=("EXACT minimum (all HNF of every index in [m_n, M-1] exhausted)" if mode == 0
                               else "UPPER bound only (random search)"))
        else:
            entry.update(M=None, kind="no admissible lattice found in range", verified_exact=False)
        receipt["results"].append(entry)
        print(json.dumps(entry), flush=True)
        json.dump(receipt, open(args.out, "w"), indent=1)


if __name__ == "__main__":
    main()
