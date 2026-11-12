// Auditor brute-force cross-check for small q: lattice vectors by box
// enumeration, dual group by brute force over (Z/q)^3, fold by direct set.
// usage: aud_brute n qmax cap  -> per-q lines "q all admissible small" and small HNFs
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;
static long long pm(long long x,long long m){ long long r=x%m; return r<0?r+m:r; }
int main(int argc,char**argv){
    int n=atoi(argv[1]), qmax=atoi(argv[2]), cap=atoi(argv[3]); int R=2*n;
    for(int q=1;q<=qmax;++q){
        long long all=0,adm=0,small=0;
        for(int a=1;a<=q;++a) if(q%a==0) for(int d=1;d<=q/a;++d) if((q/a)%d==0){ int f=q/(a*d);
            for(int b=0;b<d;++b) for(int c=0;c<f;++c) for(int e=0;e<f;++e){
                ++all; int mn=1<<30;
                for(int u=-R;u<=R;++u) for(int v=-2*R;v<=2*R;++v) for(int w=-4*R;w<=4*R;++w){
                    if(!u&&!v&&!w) continue;
                    int k1=a*u,k2=b*u+d*v,k3=c*u+e*v+f*w; int l=abs(k1)+abs(k2)+abs(k3); if(l<mn) mn=l; }
                if(mn<R) continue; ++adm;
                vector<char> fs((size_t)q*q*q,0); int fold=0;
                for(int x=0;x<q;++x) for(int y=0;y<q;++y) for(int z=0;z<q;++z)
                    if(pm(1LL*a*x+1LL*b*y+1LL*c*z,q)==0 && pm(1LL*d*y+1LL*e*z,q)==0 && pm(1LL*f*z,q)==0){
                        int fx=min(x,q-x)%q,fy=min(y,q-y)%q,fz=min(z,q-z)%q; size_t id=((size_t)fx*q+fy)*q+fz; if(!fs[id]){fs[id]=1;++fold;} }
                if(fold<=cap){ ++small; printf("S %d %d %d %d %d %d %d %d\n",q,fold,a,b,c,d,e,f); }
            }
        }
        printf("Q %d %lld %lld %lld\n",q,all,adm,small);
    }
}
