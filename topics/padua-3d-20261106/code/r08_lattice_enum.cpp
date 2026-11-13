// Exact unrestricted row-HNF enumeration, round08; stdlib only.
// Port of audit03 T10 window_search.py and T9 k_complement_probe.py.
#include <algorithm>
#include <chrono>
#include <climits>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;
struct H { int a,b,c,d,e,f; };
long long mod(long long x,long long q){ x%=q; return x<0?x+q:x; }
long long dist(long long x,int f){ x=mod(x,f); return min(x,f-x); }
int floordiv(int x,int d){ int v=x/d,r=x%d; return v-(r<0); }
int ceildiv(int x,int d){ return -floordiv(-x,d); }
bool pair_short(int d,int e,int f,int R){
    for(int v=1;v*d<R;++v) if(v*d+dist(1LL*e*v,f)<R) return true;
    return false;
}
bool full_short(const H &h,int R){
    for(int u=1;u*h.a<R;++u){
        int rx=R-1-u*h.a;
        for(int v=ceildiv(-rx-u*h.b,h.d);v<=floordiv(rx-u*h.b,h.d);++v)
            if(u*h.a+abs(u*h.b+v*h.d)+dist(1LL*u*h.c+1LL*v*h.e,h.f)<R) return true;
    }
    return false;
}
// Return exact count when <=cap; otherwise return cap+1 after a certified lower bound.
int fold(const H &h,int cap){
    int q=h.a*h.d*h.f;
    unordered_set<uint64_t> seen; seen.reserve(min(q,cap+1)*2+1);
    for(int j3=0;j3<h.f;++j3) for(int j2=0;j2<h.d;++j2) for(int j1=0;j1<h.a;++j1){
        long long t=-1LL*h.e*j3+1LL*j2*h.f;
        long long z=mod(1LL*j3*h.a*h.d,q), y=mod(1LL*h.a*t,q);
        long long x=mod(-1LL*h.b*t-1LL*h.c*j3*h.d+1LL*j1*h.d*h.f,q);
        x=min(x,q-x); y=min(y,q-y); z=min(z,q-z);
        seen.insert((x*q+y)*q+z);
        if((int)seen.size()>cap) return cap+1;
    }
    return seen.size();
}
void print_h(ostream &o,const H &h){ o<<'['<<h.a<<','<<h.b<<','<<h.c<<','<<h.d<<','<<h.e<<','<<h.f<<']'; }
int main(int argc,char**argv){
    if(argc!=7){ cerr<<"usage: enum MODE n det_lo det_hi fold_cap output.jsonl\n"; return 2; }
    string mode=argv[1]; int n=stoi(argv[2]),lo=stoi(argv[3]),hi=stoi(argv[4]),cap=stoi(argv[5]);
    if((mode!="min"&&mode!="complement")||n<1||lo<1||hi<lo||cap<0) return 2;
    ofstream out(argv[6]); if(!out) return 3;
    const int R=2*n; long long all=0,tested=0,admissible=0,small=0; int best=INT_MAX,bestq=0; H besth{};
    auto start=chrono::steady_clock::now();
    for(int q=lo;q<=hi;++q){
        long long qc=0,qt=0,qg=0,qs=0; vector<H> goods;
        for(int a=1;a<=q;++a) if(q%a==0) for(int d=1;d<=q/a;++d) if(q/a%d==0){
            int f=q/(a*d); qc+=1LL*d*f*f;
            if(f<R) continue; // Pure third-axis vector.
            for(int b=0;b<d;++b) for(int e=0;e<f;++e){
                if(pair_short(d,e,f,R)) continue; // Complete u=0 test, shared by all c.
                for(int c=0;c<f;++c){
                    ++qt; H h{a,b,c,d,e,f}; if(full_short(h,R)) continue;
                    ++qg;
                    if(mode=="min") { goods.push_back(h); continue; }
                    int threshold=(best==INT_MAX?q:max(cap,best-1));
                    int m=fold(h,threshold);
                    if(m<best){ best=m; bestq=q; besth=h; }
                    if(m<=cap){ ++qs; out<<"{\"type\":\"small\",\"q\":"<<q<<",\"fold\":"<<m<<",\"hnf\":";print_h(out,h);out<<"}\n"; }
                }
            }
        }
        all+=qc;tested+=qt;admissible+=qg;small+=qs;
        double sec=chrono::duration<double>(chrono::steady_clock::now()-start).count();
        out<<"{\"type\":\"q\",\"q\":"<<q<<",\"hnf_total\":"<<qc<<",\"after_axis_pair_prune\":"<<qt<<",\"admissible\":"<<qg<<",\"small\":"<<qs<<",\"elapsed_seconds\":"<<sec<<"}\n";out.flush();
        if(mode=="min"&&qg){
            for(auto h:goods){ out<<"{\"type\":\"minimizer\",\"q\":"<<q<<",\"fold\":"<<fold(h,q)<<",\"hnf\":";print_h(out,h);out<<"}\n"; }
            bestq=q;break;
        }
    }
    double sec=chrono::duration<double>(chrono::steady_clock::now()-start).count();
    out<<"{\"type\":\"summary\",\"mode\":\""<<mode<<"\",\"n\":"<<n<<",\"det_lo\":"<<lo<<",\"det_hi_requested\":"<<hi<<",\"fold_cap\":"<<cap<<",\"hnf_total\":"<<all<<",\"after_axis_pair_prune\":"<<tested<<",\"admissible\":"<<admissible<<",\"small_count\":"<<small<<",\"min_det\":"<<(mode=="min"?bestq:0)<<",\"min_fold\":"<<(best==INT_MAX?0:best)<<",\"min_fold_det\":"<<(mode=="complement"?bestq:0)<<",\"min_fold_hnf\":";print_h(out,besth);out<<",\"elapsed_seconds\":"<<sec<<"}\n";
    cerr<<"n="<<n<<" mode="<<mode<<" q="<<bestq<<" minfold="<<(best==INT_MAX?0:best)<<" seconds="<<sec<<"\n";
}
