// C07 research point-only row assembly; frozen C06 included unchanged.
#include "partial.cpp"
#include <set>
#include <algorithm>
static B qb(const Q&q){B b;arb_set_fmpq(b.x,q.x,P);return b;}
static long floorq(const Q&q){fmpz_t f;fmpz_init(f);fmpz_fdiv_q(f,fmpq_numref(q.x),fmpq_denref(q.x));long a=fmpz_get_si(f);fmpz_clear(f);return a;}
static B sinb(const B&a){B b;arb_sin(b.x,a.x,P);return b;}
static B cosb(const B&a){B b;arb_cos(b.x,a.x,P);return b;}
static B cotb(const B&a){B b;arb_cot(b.x,a.x,P);return b;}
static B maxzero(const B&a){B b;arb_max(b.x,a.x,B().x,P);return b;}
// Exact polynomial sine ratio, including removable integer-pi turns.
static B ratio(const Q&turn,long k){long ell=floorq(turn+Q(1)/Q(2));Q reduced=turn-Q(ell);B x=pi()*qb(reduced),a,b;arb_sinc(a.x,(x*B(k)).x,P);arb_sinc(b.x,x.x,P);return B((ell%2&&k%2==0)?-k:k)*a/b;}
static B finiteF(long n,long r,long k,const Q&af,const Q&bf){long m=n+1,delta=(1-r)%2;if(delta<0)delta+=2;Q u=(Q(delta+2*k)+af)/Q(n),v=(Q(r)+bf)/Q(m),s=(u+v)/Q(2),t=(u-v)/Q(2);B g=ratio(s,m)*ratio(t,m)+ratio(s,n)*ratio(t,n)-cosb(pi()*qb(u)*B(n));return g*B(delta?-1:1)/B(2);}
struct Stats {long retained=0,direct=0,blocks=0,maxdirect=0,maxblocks=0,ordinary=0;};
static void rootcut(const B&turn,long n,const B&sigma,std::set<long>&cuts,std::set<long>&direct){B x=turn*B(n)-sigma;arf_t l,u;arf_init(l);arf_init(u);arb_get_lbound_arf(l,x.x,P);arb_get_ubound_arf(u,x.x,P);fmpz_t a,b;fmpz_init(a);fmpz_init(b);arf_get_fmpz(a,l,ARF_RND_CEIL);arf_get_fmpz(b,u,ARF_RND_FLOOR);long cl=fmpz_get_si(a),fu=fmpz_get_si(b);arf_clear(l);arf_clear(u);fmpz_clear(a);fmpz_clear(b);
 if(fu<0||cl>=n)return;if(cl<=fu){if(fu-cl>0)throw std::runtime_error("wide root cluster");direct.insert(cl);cuts.insert(cl);cuts.insert(cl+1);}else cuts.insert(cl);
}
static B asinb(const B&a){B b;arb_asin(b.x,a.x,P);return b;}
// Root candidates include possible threshold roots, conservatively clamped.
static void sinecuts(const B&threshold,long n,const B&sigma,std::set<long>&cuts,std::set<long>&direct){
 if(arb_gt(threshold.x,B(1).x)||arb_lt(threshold.x,B(-1).x))return;
 // Evaluate asin separately at exact outward endpoints after clamping.
 // A ball formed by min/max may itself overhang +/-1 and is not a safe asin input.
 arf_t fl,fu;arf_init(fl);arf_init(fu);arb_get_lbound_arf(fl,threshold.x,P);arb_get_ubound_arf(fu,threshold.x,P);if(arf_cmp_si(fl,-1)<0)arf_set_si(fl,-1);if(arf_cmp_si(fu,1)>0)arf_one(fu);B lp,up,al,au,a;arb_set_arf(lp.x,fl);arb_set_arf(up.x,fu);arb_asin(al.x,lp.x,P);arb_asin(au.x,up.x,P);arb_union(a.x,al.x,au.x,P);arf_clear(fl);arf_clear(fu);a=a/(B(2)*pi());B b=B(1)/B(2)-a;
 if(!arb_is_finite(a.x))throw std::runtime_error("asin root failure");for(long shift=-1;shift<=1;shift++){rootcut(a+B(shift),n,sigma,cuts,direct);rootcut(b+B(shift),n,sigma,cuts,direct);}
}
static B pointS(long n,const Q&af,const Q&bf,Stats&stats){if(n<2||n>2147483647L||fmpq_sgn(af.x)<0||fmpq_sgn(bf.x)<0||fmpq_cmp_si((af+bf).x,1)>0)throw std::runtime_error("phase domain");
 if(!fmpq_cmp_si(af.x,1)||!fmpq_cmp_si(bf.x,1))return B(1);
 long m=n+1;B alpha=pi()*qb(af),beta=pi()*qb(bf),p=fmpq_is_zero(af.x)?B():sinb(alpha),q=fmpq_is_zero(bf.x)?B():sinb(beta),A=fmpq_equal_si((af+bf).x,1)?B():cosb(alpha)+cosb(beta),total;
 for(long r=0;r<2*m;r++){
  if(r==0||r==2*m-1||r==m-1||r==m){for(long k=0;k<n;k++){total=total+absolute(finiteF(n,r,k,af,bf));stats.retained++;}continue;}
  stats.ordinary++;long delta=(1-r)%2;if(delta<0)delta+=2;Q sig=(Q(delta)+af)/Q(2),vf=(Q(r)+bf)/Q(m);B sigma=qb(sig),v=pi()*qb(vf),cv=cosb(v),sv=sinb(v),c=A*(B(1)+cv)+q*sv;if(fmpq_is_zero(af.x)&&fmpq_equal(vf.x,(Q(1)+bf).x))c=B();
  std::set<long>cuts{0,n},direct;
  Q d=fmpq_cmp_si(vf.x,1)<=0?vf/Q(2):Q(1)-vf/Q(2);rootcut(qb(d),n,sigma,cuts,direct);rootcut(qb(Q(1)-d),n,sigma,cuts,direct);
  if(!fmpq_is_zero(af.x))sinecuts(c/p,n,sigma,cuts,direct);
  // Seam sample is direct only when it actually occurs on this grid.
  if(fmpq_is_zero(sig.x)){direct.insert(0);cuts.insert(1);}
  if(direct.size()>5)throw std::runtime_error("too many direct samples");stats.maxdirect=std::max(stats.maxdirect,(long)direct.size());stats.direct+=direct.size();
  B cotv=cotb(v/B(2)),C=(p-q-A*cotv)/B(4),D=(p+q+A*cotv)/B(4),row=B(n)*((cosb(alpha)+cosb(beta))/B(2)-q/B(2)*cotv);long rowblocks=0;
  std::vector<long>edges(cuts.begin(),cuts.end());for(size_t i=0;i+1<edges.size();i++){long lo=edges[i],hi=edges[i+1]-1;if(lo>hi||direct.count(lo))continue;
   B u=pi()*qb((Q(2*lo)+Q(delta)+af)/Q(n)),num=c-p*sinb(u),den=cosb(u)-cv;
   bool negative=(arb_is_negative(num.x)&&arb_is_positive(den.x))||(arb_is_positive(num.x)&&arb_is_negative(den.x));
   bool positive=(arb_is_positive(num.x)&&arb_is_positive(den.x))||(arb_is_negative(num.x)&&arb_is_negative(den.x));
   if(!negative&&!positive){if(arb_is_zero(p.x)&&arb_is_zero(c.x))continue;throw std::runtime_error("unresolved core sign");}if(!negative)continue;
   B channel[2];for(int ch=0;ch<2;ch++){Q y=Q(lo)+sig+(ch?Q(1):Q(-1))*Q(n)*vf/Q(2);long wrap=floorq(y/Q(n));y=y-Q(wrap)*Q(n);channel[ch]=partial(n,hi-lo+1,qb(y));rowblocks++;}
   row=row-B(2)*C*channel[0]-B(2)*D*channel[1];
  }
  if(rowblocks>24)throw std::runtime_error("too many blocks");stats.maxblocks=std::max(stats.maxblocks,rowblocks);stats.blocks+=rowblocks;
  for(long k:direct)row=row+B(2)*maxzero(B()-finiteF(n,r,k,af,bf));total=total+row;
 }
 B answer=total/(B(n)*B(m));if(!arb_is_finite(answer.x))throw std::runtime_error("nonfinite S");return answer;
}
extern "C" int c07_point(long n,const char*astr,const char*bstr,double*out,long*counts){try{Q a,b;if(fmpq_set_str(a.x,astr,10)||fmpq_set_str(b.x,bstr,10))return 2;if(fmpz_is_zero(fmpq_denref(a.x))||fmpz_is_zero(fmpq_denref(b.x)))return 2;fmpq_canonicalise(a.x);fmpq_canonicalise(b.x);Stats st;B ans=pointS(n,a,b,st);arf_t f;arf_init(f);arb_get_lbound_arf(f,ans.x,P);out[0]=arf_get_d(f,ARF_RND_FLOOR);arb_get_ubound_arf(f,ans.x,P);out[1]=arf_get_d(f,ARF_RND_CEIL);out[2]=mag_get_d(arb_radref(ans.x));arf_clear(f);long values[]={st.retained,st.direct,st.blocks,st.maxdirect,st.maxblocks,st.ordinary};for(int i=0;i<6;i++)counts[i]=values[i];return 0;}catch(...){return 1;}}

extern "C" int c07_point_arb(long n,const char*astr,const char*bstr,arb_t out){try{Q a,b;if(fmpq_set_str(a.x,astr,10)||fmpq_set_str(b.x,bstr,10)||fmpz_is_zero(fmpq_denref(a.x))||fmpz_is_zero(fmpq_denref(b.x)))throw std::runtime_error("rational parse");fmpq_canonicalise(a.x);fmpq_canonicalise(b.x);Stats st;B answer=pointS(n,a,b,st);arb_set(out,answer.x);return 0;}catch(...){arb_indeterminate(out);return 1;}}
