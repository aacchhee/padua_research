// Independent auditor kernel (Claude audit05 D4).  int128 exact arithmetic.
// mode "res": reads N, Vint (N*N int64, rows=nodes, cols=basis), Wint (N*N int64,
//   rows=basis, cols=nodes); prints max_i sum_j |2^SH*delta_ij - (V W)_ij| (exact).
// mode "mesh": reads N, n, m, KC, table C[0..mn] (int64), basis exps (a,b,c)*N, Wint;
//   for every (i,j,k) in [0,mn]^3, P_alpha = round(C[fa]C[fb]C[fc] / 2^(2KC)) where
//   fa = fold(a*i mod 2mn); prints max over mesh of sum_j |sum_alpha P_alpha W_alpha,j|.
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <string>
#include <omp.h>
typedef __int128 i128; typedef long long ll;
static std::string s128(i128 v){ if(v==0) return "0"; bool neg=v<0; if(neg) v=-v; std::string s; while(v>0){ s.push_back('0'+(int)(v%10)); v/=10;} if(neg) s.push_back('-'); return std::string(s.rbegin(),s.rend()); }
static i128 ab(i128 v){ return v<0?-v:v; }
static void rd(const char*f, std::vector<ll>&v, size_t cnt){ FILE*F=fopen(f,"rb"); if(!F){perror(f);exit(1);} v.resize(cnt); if(fread(v.data(),8,cnt,F)!=cnt){fprintf(stderr,"short %s\n",f);exit(1);} fclose(F);}
static int bitlen(ll x){ unsigned long long u = x<0 ? (unsigned long long)(-(x+1))+1 : (unsigned long long)x; int b=0; while(u){b++;u>>=1;} return b; }
int main(int argc,char**argv){
  std::string mode=argv[1];
  if(mode=="res"){
    int N=atoi(argv[2]); int SH=atoi(argv[3]); std::vector<ll> V,W; rd(argv[4],V,(size_t)N*N); rd(argv[5],W,(size_t)N*N);
    int bv=0,bw=0; for(ll x:V) bv=std::max(bv,bitlen(x)); for(ll x:W) bw=std::max(bw,bitlen(x));
    int bn=0; while((1<<bn)<N) bn++;
    if(bv+bw+bn>=125 || SH>=125){fprintf(stderr,"guard fail res %d %d %d\n",bv,bw,bn);return 2;}
    i128 best=0; i128 maxabs=0;
    #pragma omp parallel for schedule(dynamic,4)
    for(int i=0;i<N;i++){
      std::vector<i128> acc(N,0);
      for(int k=0;k<N;k++){ i128 v=V[(size_t)i*N+k]; if(!v) continue; const ll* w=&W[(size_t)k*N]; for(int j=0;j<N;j++) acc[j]+=v*(i128)w[j]; }
      acc[i]-=((i128)1)<<SH;
      i128 s=0,mx=0; for(int j=0;j<N;j++){ i128 a=ab(acc[j]); if(a>mx) mx=a; s+=a; }  // |acc|<2^126, N<2^10 -> but s bounded below
      #pragma omp critical
      { if(s>best) best=s; if(mx>maxabs) maxabs=mx; }
    }
    // overflow safety for s: each |acc_j| < 2^(bv+bw+bn)+2^SH <= 2^125, but residual entries are tiny; verify explicitly
    if(maxabs > (((i128)1)<<115)){fprintf(stderr,"residual entry too large for safe row sum\n");return 3;}
    printf("RES %s MAXENTRY %s BITS %d %d %d\n",s128(best).c_str(),s128(maxabs).c_str(),bv,bw,bn);
    return 0;
  }
  if(mode=="mesh"){
    int N=atoi(argv[2]), n=atoi(argv[3]), m=atoi(argv[4]), KC=atoi(argv[5]); int G=m*n;
    std::vector<ll> C,E,W; rd(argv[6],C,G+1); rd(argv[7],E,(size_t)3*N); rd(argv[8],W,(size_t)N*N);
    int bw=0; for(ll x:W) bw=std::max(bw,bitlen(x)); int bc=0; for(ll x:C) bc=std::max(bc,bitlen(x));
    int bn=0; while((1<<bn)<N) bn++;
    if(3*bc>=126 || KC>40 || bc>KC+1 || (KC+1)+bw+2*bn>126){fprintf(stderr,"guard fail mesh %d %d %d\n",bc,bw,bn);return 2;}
    // fold table: idx(l) for l in [0,2G): cos(l pi/G) = cos(fold pi/G)
    auto fold=[&](ll l)->int{ l%= (2*G); return (int)(l<=G? l : 2*G-l); };
    i128 best=-1; long long bi=-1,bj=-1,bk=-1; long long count=0;
    const i128 half=((i128)1)<<(2*KC-1);
    #pragma omp parallel for schedule(dynamic,1) reduction(+:count)
    for(int i=0;i<=G;i++){
      std::vector<ll> P(N); std::vector<i128> acc(N);
      i128 lb=-1; long long lj=-1,lk=-1;
      for(int j=0;j<=G;j++) for(int k=0;k<=G;k++){
        for(int al=0;al<N;al++){
          i128 pr=(i128)C[fold(E[3*al]*i)]*(i128)C[fold(E[3*al+1]*j)]; pr*= (i128)C[fold(E[3*al+2]*k)];
          P[al]=(ll)((pr+half)>>(2*KC));    // floor(x/2^(2KC)+1/2): arithmetic shift (GCC)
        }
        for(int c=0;c<N;c++) acc[c]=0;
        for(int al=0;al<N;al++){ i128 p=P[al]; if(!p) continue; const ll* w=&W[(size_t)al*N]; for(int c=0;c<N;c++) acc[c]+=p*(i128)w[c]; }
        i128 s=0; for(int c=0;c<N;c++) s+=ab(acc[c]);
        count++;
        if(s>lb){lb=s;lj=j;lk=k;}
      }
      #pragma omp critical
      { if(lb>best || (lb==best && i<bi)){best=lb;bi=i;bj=lj;bk=lk;} }
    }
    printf("MESH %s ARG %lld %lld %lld COUNT %lld BITS %d %d %d\n",s128(best).c_str(),bi,bj,bk,count,bc,bw,bn);
    return 0;
  }
  return 1;
}
