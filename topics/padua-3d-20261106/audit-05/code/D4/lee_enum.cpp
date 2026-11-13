// Fresh auditor enumerator (Claude audit05 D4). Every row-HNF sublattice L of Z^3
// with det q in [qlo,qhi]; admissible iff no nonzero v in L with ||v||_1 <= 2n-1.
// Membership via dual forms: v in L  <=>  v * adj(B) == 0 (mod q), adj = q B^{-1}.
// Fold: |{(min(h_i,q-h_i))_i : h in H}|, H = closure of the columns of adj mod q.
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <array>
#include <set>
#include <algorithm>
#include <omp.h>
typedef long long ll;
struct V3{int x,y,z;};
static ll md(ll a, ll q){ ll r=a%q; return r<0?r+q:r; }
int main(int argc,char**argv){
  int n=atoi(argv[1]); ll qlo=atoll(argv[2]), qhi=atoll(argv[3]); int R=2*n-1;
  std::vector<V3> half;  // nonzero v with ||v||1<=R, one of each +-pair, sorted by norm
  for(int x=-R;x<=R;x++)for(int y=-R;y<=R;y++)for(int z=-R;z<=R;z++){
    int s=abs(x)+abs(y)+abs(z); if(s==0||s>R) continue;
    bool pos = x>0 || (x==0 && (y>0 || (y==0 && z>0)));
    if(pos) half.push_back({x,y,z});
  }
  std::stable_sort(half.begin(),half.end(),[](const V3&a,const V3&b){return abs(a.x)+abs(a.y)+abs(a.z)<abs(b.x)+abs(b.y)+abs(b.z);});
  fprintf(stderr,"half-ball size %zu\n",half.size());
  for(ll q=qlo;q<=qhi;q++){
    // list all (a,d,f) with a*d*f=q, then all b<d, c<f, e<f
    std::vector<std::array<ll,3>> diag;
    for(ll a=1;a<=q;a++) if(q%a==0) for(ll d=1;d<=q/a;d++) if((q/a)%d==0) diag.push_back({a,d,q/a/d});
    ll total=0, adm=0; std::vector<std::array<ll,7>> found;
    for(auto&t:diag){
      ll a=t[0],d=t[1],f=t[2];
      total += d*f*f;
      #pragma omp parallel for schedule(dynamic,1) reduction(+:adm)
      for(ll b=0;b<d;b++){
        for(ll c=0;c<f;c++) for(ll e=0;e<f;e++){
          ll B[3][3]={{a,b,c},{0,d,e},{0,0,f}};
          // adjugate via generic cofactors: adj[i][j] = (-1)^{i+j} M_{ji}
          ll adj[3][3];
          for(int i=0;i<3;i++)for(int j=0;j<3;j++){
            int r0=(j+1)%3,r1=(j+2)%3,c0=(i+1)%3,c1=(i+2)%3;
            adj[i][j]=B[r0][c0]*B[r1][c1]-B[r0][c1]*B[r1][c0];
          }
          // sanity: B*adj = q I
          bool good=true;
          for(int i=0;i<3;i++)for(int j=0;j<3;j++){ll s=0;for(int k=0;k<3;k++)s+=B[i][k]*adj[k][j]; if(s!=(i==j?q:0)) good=false;}
          if(!good){fprintf(stderr,"adj fail\n");exit(2);}
          ll A[3][3]; for(int i=0;i<3;i++)for(int j=0;j<3;j++) A[i][j]=md(adj[i][j],q);
          bool admissible=true;
          for(const V3&v:half){
            bool in=true;
            for(int j=0;j<3&&in;j++){ ll s=(ll)v.x*A[0][j]+(ll)v.y*A[1][j]+(ll)v.z*A[2][j]; if(s%q!=0) in=false; }
            if(in){admissible=false;break;}
          }
          if(admissible){
            adm++;
            // fold via group closure of adj columns mod q
            std::vector<char> seen((size_t)q*q*q,0); std::vector<std::array<ll,3>> st, all;
            st.push_back({0,0,0}); seen[0]=1;
            while(!st.empty()){auto h=st.back();st.pop_back();all.push_back(h);
              for(int j=0;j<3;j++){ std::array<ll,3> g={(h[0]+A[0][j])%q,(h[1]+A[1][j])%q,(h[2]+A[2][j])%q};
                size_t key=(g[0]*q+g[1])*q+g[2]; if(!seen[key]){seen[key]=1;st.push_back(g);} } }
            std::set<std::array<ll,3>> fold;
            for(auto&h:all) fold.insert({std::min(h[0],q-h[0]),std::min(h[1],q-h[1]),std::min(h[2],q-h[2])});
            // also check every h annihilates every row of B (h in L^perp)
            for(auto&h:all) for(int i=0;i<3;i++){ ll s=B[i][0]*h[0]+B[i][1]*h[1]+B[i][2]*h[2]; if(s%q){fprintf(stderr,"dual fail\n");exit(3);} }
            #pragma omp critical
            found.push_back({a,b,c,d,e,f,(ll)all.size()*1000000+ (ll)fold.size()});
          }
        }
      }
    }
    std::sort(found.begin(),found.end());
    printf("Q %lld %lld %lld\n",q,total,adm);
    for(auto&h:found) printf("H %lld %lld %lld %lld %lld %lld %lld group=%lld fold=%lld\n",q,h[0],h[1],h[2],h[3],h[4],h[5],h[6]/1000000,h[6]%1000000);
    fflush(stdout);
  }
}
