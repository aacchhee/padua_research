#include "point.cpp"
#include <utility>
// Independent direct cosine reference copied from C07 reviewer.
static B direct_board(long n,const Q&a,const Q&b){
 constexpr long RP=512;B p,sum;arb_const_pi(p.x,RP);
 for(long r=0;r<2*(n+1);r++)for(long j=0;j<2*n;j++)if((j+r)%2){
  Q uf=(Q(j)+a)/Q(n),vf=(Q(r)+b)/Q(n+1);B u,v,t,g;
  arb_set_fmpq(u.x,uf.x,RP);arb_mul(u.x,u.x,p.x,RP);
  arb_set_fmpq(v.x,vf.x,RP);arb_mul(v.x,v.x,p.x,RP);
  std::vector<B>cu(n+1),cv(n+1);
  for(long k=0;k<=n;k++){
   arb_mul_si(t.x,u.x,k,RP);arb_cos(cu[k].x,t.x,RP);
   arb_mul_si(t.x,v.x,k,RP);arb_cos(cv[k].x,t.x,RP);
  }
  for(long k=0;k<=n;k++)for(long l=0;l<=n-k;l++){
   arb_mul(t.x,cu[k].x,cv[l].x,RP);arb_mul_si(t.x,t.x,(k?2:1)*(l?2:1),RP);arb_add(g.x,g.x,t.x,RP);
  }
  arb_sub(g.x,g.x,cu[n].x,RP);arb_abs(g.x,g.x);arb_add(sum.x,sum.x,g.x,RP);
 }
 arb_div_si(sum.x,sum.x,2*n*(n+1),RP);return sum;
}
// One valid pilot call only: original S assembly, plus exact full-radius gate.
extern "C" int c23_point_audit(long n,const char*as,const char*bs,double*out,long*counts){try{
 if(n!=2048)return 2;Q a,b;if(fmpq_set_str(a.x,as,10)||fmpq_set_str(b.x,bs,10))return 2;
 fmpq_canonicalise(a.x);fmpq_canonicalise(b.x);
 if(!fmpq_equal(a.x,(Q(1)/Q(12)).x)||!fmpq_equal(b.x,(Q(1)/Q(16)).x))return 2;
 Stats st;B ans=pointS(n,a,b,st),rad,limit=qb(Q(1)/Q(100000));arf_t t;arf_init(t);
 // A mag is an exact dyadic upper radius. No nearest binary64 comparison.
 arf_set_mag(t,arb_radref(ans.x));arb_set_arf(rad.x,t);out[3]=arb_le(rad.x,limit.x);
 arb_get_lbound_arf(t,ans.x,P);out[0]=arf_get_d(t,ARF_RND_FLOOR);
 arb_get_ubound_arf(t,ans.x,P);out[1]=arf_get_d(t,ARF_RND_CEIL);
 out[2]=mag_get_d(arb_radref(ans.x));arf_clear(t);
 long v[]={st.retained,st.direct,st.blocks,st.maxdirect,st.maxblocks,st.ordinary};for(int i=0;i<6;i++)counts[i]=v[i];return 0;
 }catch(...){return 1;}}
static B direct_partial(long n,long q,const B&y){B p,sum,x,t;arb_const_pi(p.x,512);for(long i=0;i<q;i++){
 arb_add_si(x.x,y.x,i,512);arb_mul(x.x,x.x,p.x,512);arb_div_si(x.x,x.x,n,512);arb_cot(t.x,x.x,512);arb_add(sum.x,sum.x,t.x,512);
 }return sum;}
extern "C" int c23_partial_control(long n,long q,const char*ys,double*out){try{
 B y;if(arb_set_str(y.x,ys,P))return 2;B ans=partial(n,q,y),lo,hi,ref;arf_t l,u;arf_init(l);arf_init(u);
 arb_get_lbound_arf(l,y.x,512);arb_get_ubound_arf(u,y.x,512);arb_set_arf(lo.x,l);arb_set_arf(hi.x,u);arf_clear(l);arf_clear(u);
 B rl=direct_partial(n,q,lo),rh=direct_partial(n,q,hi);arb_union(ref.x,rl.x,rh.x,512);
 out[0]=arb_contains(ans.x,ref.x);out[1]=mag_get_d(arb_radref(ans.x));return 0;
 }catch(...){return 1;}}
extern "C" int c23_moment_control(){int checks=0;for(auto nq:std::vector<std::pair<long,long>>{{7,1},{7,7},{16,9}}){
 long n=nq.first,q=nq.second;B y;arb_one(y.x);arb_mul_2exp_si(y.x,y.x,-1);auto values=moments(n,q,y);
 for(int d=0;d<=5;d++){Q exact;for(long i=0;i<q;i++)exact=exact+powerq((Q(1)/Q(2)+Q(i))/Q(n)-Q(1)/Q(2),d);
 if(!arb_contains_fmpq(values[d].x,exact.x))return -1;checks++;}}return checks;}
extern "C" int c23_reference(long n,const char*as,const char*bs,double*out){try{
 if(n!=8&&n!=16)return 2;Q a,b;if(fmpq_set_str(a.x,as,10)||fmpq_set_str(b.x,bs,10))return 2;
 fmpq_canonicalise(a.x);fmpq_canonicalise(b.x);Stats st;B ans=pointS(n,a,b,st),ref=direct_board(n,a,b);
 out[0]=arb_contains(ans.x,ref.x);out[1]=arb_is_exact(ans.x)&&arb_contains(ref.x,ans.x);out[2]=mag_get_d(arb_radref(ans.x));return 0;
 }catch(...){return 1;}}
