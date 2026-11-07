// C12 actual whole-box S upper. Explicitly released C11 CP640/J16 partial; full returned tail retained.
#include "partial.cpp"
#include <set>
#include <algorithm>
#include <climits>
#include <cmath>
static B qb12(const Q&q){B b;arb_set_fmpq(b.x,q.x,P);return b;}
static B sin12(const B&a){B b;arb_sin(b.x,a.x,P);return b;}
static B cos12(const B&a){B b;arb_cos(b.x,a.x,P);return b;}
static B point12(double d){B b;arb_set_d(b.x,d);return b;}
static B range12(const B&a,const B&b){B c;arb_union(c.x,a.x,b.x,P);return c;}
static B meet12(const B&a,const B&b){B c;if(!arb_is_finite(a.x)||!arb_is_finite(b.x)||!arb_intersection(c.x,a.x,b.x,P))throw std::runtime_error("finite intersection");return c;}
static B up12(const B&a){arf_t x;arf_init(x);arb_get_ubound_arf(x,a.x,P);B b;arb_set_arf(b.x,x);arf_clear(x);if(!arb_is_finite(b.x))throw std::runtime_error("nonfinite upper");return b;}
static double upper12(const B&a){arf_t f;arf_init(f);arb_get_ubound_arf(f,a.x,P);double d=arf_get_d(f,ARF_RND_CEIL);arf_clear(f);return d;}
static B max12(const B&a,const B&b){B c;arb_max(c.x,up12(a).x,up12(b).x,P);return up12(c);}
static B min12(const B&a,const B&b){B c;arb_min(c.x,up12(a).x,up12(b).x,P);return up12(c);}
struct Stats12{long retained=0,direct=0,regular=0,blocks=0,fallback=0,ordinary=0,maxD=0,maxE=0,maxBlocks=0,ratioFallback=0;};
// Valid degree-independent full-ball ratio image; no point substitution.
static B ratio12(long k,const B&z,Stats12&st){
 B out=range12(B(-k),B(k));if(k==1)return B(1);B sn=sin12(z);
 if(arb_is_finite(sn.x)&&!arb_contains_zero(sn.x)){B q=sin12(z*B(k))/sn;if(arb_is_finite(q.x))out=meet12(out,q);}
 double mid=arf_get_d(arb_midref(z.x),ARF_RND_NEAR);if(!std::isfinite(mid)||std::abs(mid)>100){st.ratioFallback++;return out;}
 long turn=std::lround(mid/3.14159265358979323846);B a=z-pi()*B(turn),ka=a*B(k);
 if(upper12(absolute(a))>1.5||upper12(absolute(ka))>4){st.ratioFallback++;return out;}
 B sr,sk;arb_sinc(sr.x,a.x,P);arb_sinc(sk.x,ka.x,P);sr=meet12(sr,range12(point12(.625),B(1)));
 int eps=(turn%2!=0&&k%2==0)?-1:1;out=meet12(out,B(eps*k)*sk/sr);
 // C03 exact folded dyadic endpoints; guard the actual extracted values.
 arf_t l,u;arf_init(l);arf_init(u);arb_get_abs_lbound_arf(l,a.x,P);arb_get_abs_ubound_arf(u,a.x,P);B lo,hi;arb_set_arf(lo.x,l);arb_set_arf(hi.x,u);arf_clear(l);arf_clear(u);
 if(upper12(hi)<=1.5&&upper12(hi*B(k))<=4){
  auto val=[&](const B&r){if(arb_is_zero(r.x))return B(k);B s,t;arb_sinc(s.x,(r*B(k)).x,P);arb_sinc(t.x,r.x,P);t=meet12(t,range12(point12(.625),B(1)));return B(k)*s/t;};
  B vl=val(lo),vh=val(hi),image;arf_t b,t;arf_init(b);arf_init(t);arb_get_lbound_arf(b,vh.x,P);arb_get_ubound_arf(t,vl.x,P);arb_set_interval_arf(image.x,b,t,P);arf_clear(b);arf_clear(t);if(eps<0)arb_neg(image.x,image.x);out=meet12(out,image);
 }
 return out;
}
static B finite12(long n,long r,long k,const B&af,const B&bf,Stats12&st){
 long m=n+1,delta=(1-r)%2;if(delta<0)delta+=2;B u=pi()*(B(delta+2*k)+af)/B(n),v=pi()*(B(r)+bf)/B(m),s=(u+v)/B(2),t=(u-v)/B(2);
 B g=ratio12(m,s,st)*ratio12(m,t,st)+ratio12(n,s,st)*ratio12(n,t,st)-cos12(u*B(n));return g*B(delta?-1:1)/B(2);
}
static std::pair<long,long> integers12(const B&x){
 if(!arb_is_finite(x.x))throw std::runtime_error("nonfinite band");arf_t l,u;arf_init(l);arf_init(u);arb_get_lbound_arf(l,x.x,P);arb_get_ubound_arf(u,x.x,P);fmpz_t a,b;fmpz_init(a);fmpz_init(b);arf_get_fmpz(a,l,ARF_RND_CEIL);arf_get_fmpz(b,u,ARF_RND_FLOOR);
 if(!fmpz_fits_si(a)||!fmpz_fits_si(b)){arf_clear(l);arf_clear(u);fmpz_clear(a);fmpz_clear(b);throw std::runtime_error("band integer overflow");}long cl=fmpz_get_si(a),fu=fmpz_get_si(b);arf_clear(l);arf_clear(u);fmpz_clear(a);fmpz_clear(b);return {cl,fu};
}
static void narrow12(const B&x){arf_t l,u;arf_init(l);arf_init(u);arb_get_interval_arf(l,u,x.x,P);B a,b;arb_set_arf(a.x,l);arb_set_arf(b.x,u);arf_clear(l);arf_clear(u);if(!arb_lt((b-a).x,B(1).x))throw std::runtime_error("root band width");}
static void directcut12(long k,long n,std::set<long>&cuts,std::set<long>&direct){if(k>=0&&k<n){direct.insert(k);cuts.insert(k);cuts.insert(k+1);}}
static void poleband12(const B&x,long n,std::set<long>&cuts,std::set<long>&direct){narrow12(x);B buffered=x+range12(B(-1),B(1));auto band=integers12(buffered);if(band.second-band.first>2)throw std::runtime_error("wide buffered integer band");for(long k=std::max(0L,band.first);k<=std::min(n-1,band.second);k++)directcut12(k,n,cuts,direct);}
static void rootband12(const B&x,long n,const std::set<long>&actual,std::set<long>&cuts,std::set<long>&regular){
 narrow12(x);auto band=integers12(x);if(band.second-band.first>0)throw std::runtime_error("wide vertex band");if(band.first<=band.second){long k=band.first;if(k>=0&&k<n&&!actual.count(k))directcut12(k,n,cuts,regular);}else if(band.first>0&&band.first<n)cuts.insert(band.first);
}
static std::vector<B> endpoints12(const B&x,long lower,long upper){
 arf_t l,u;arf_init(l);arf_init(u);arb_get_interval_arf(l,u,x.x,P);if(arf_cmp_si(l,lower)<0)arf_set_si(l,lower);if(arf_cmp_si(u,upper)>0)arf_set_si(u,upper);if(arf_cmp(l,u)>0){arf_clear(l);arf_clear(u);throw std::runtime_error("coefficient endpoints");}B a,b;arb_set_arf(a.x,l);arb_set_arf(b.x,u);arf_clear(l);arf_clear(u);if(arb_equal(a.x,b.x))return {a};return {a,b};
}
static B asin12(const B&x){
 arf_t l,u;arf_init(l);arf_init(u);arb_get_interval_arf(l,u,x.x,P);if(arf_cmp_si(l,-1)<0)arf_set_si(l,-1);if(arf_cmp_si(u,1)>0)arf_one(u);B a,b,aa,bb;arb_set_arf(a.x,l);arb_set_arf(b.x,u);arf_clear(l);arf_clear(u);arb_asin(aa.x,a.x,P);arb_asin(bb.x,b.x,P);return range12(aa,bb);
}
static void numerator12(const B&c,const B&p,long n,long delta,const B&alpha,const std::set<long>&actual,std::set<long>&cuts,std::set<long>&regular){
 if(arb_is_zero(p.x))return;if(arb_gt(absolute(c).x,p.x))return;B theta;
 if(arb_equal(c.x,p.x))theta=pi()/B(2);else {B negp;arb_neg(negp.x,p.x);if(arb_equal(c.x,negp.x))theta=B(-1)*pi()/B(2);else theta=asin12(c/p);}
 for(const B&angle:std::vector<B>{theta,pi()-theta,theta+B(2)*pi()})rootband12((B(n)*angle-alpha-B(delta)*pi())/(B(2)*pi()),n,actual,cuts,regular);
 if(regular.size()>3)throw std::runtime_error("too many vertex direct samples");
}
static long wrap12(const B&y,long n){B turns=y/B(n);fmpz_t z;fmpz_init(z);arf_get_fmpz(z,arb_midref(turns.x),ARF_RND_FLOOR);if(!fmpz_fits_si(z)){fmpz_clear(z);throw std::runtime_error("wrap overflow");}long a=fmpz_get_si(z);fmpz_clear(z);return a;}
static B vertex12(long n,long r,const B&af,const B&bf,const B&amid,const B&bmid,const B&c,const B&p,const std::set<long>&actual,const std::set<long>&dcuts,Stats12&st){
 if(arb_is_zero(c.x)&&arb_is_zero(p.x))return B();long m=n+1,delta=(1-r)%2;if(delta<0)delta+=2;B alpha=pi()*af,v=pi()*(B(r)+bf)/B(m),sv=sin12(v);if(arb_contains_zero(sv.x))throw std::runtime_error("ordinary sinv zero");
 B C=(p-c/sv)/B(4),D=(p+c/sv)/B(4),lambda=(B(delta)+af)/B(2),vf=(B(r)+bf)/B(m);std::set<long>cuts=dcuts,regular;numerator12(c,p,n,delta,alpha,actual,cuts,regular);st.maxE=std::max(st.maxE,(long)regular.size());
 B result;for(long k:regular){B u=pi()*(B(delta+2*k)+af)/B(n),den=cos12(u)-cos12(v);if(arb_contains_zero(den.x))throw std::runtime_error("regular vertex denominator");result=result+absolute((c-p*sin12(u))/(B(2)*den));st.regular++;}
 std::vector<long>edges(cuts.begin(),cuts.end());long rowblocks=0;
 for(size_t j=0;j+1<edges.size();j++){long a=edges[j],b=edges[j+1]-1;if(a>b||actual.count(a)||regular.count(a))continue;
  B um=pi()*(B(delta+2*a)+amid)/B(n),vm=pi()*(B(r)+bmid)/B(m),num=c-p*sin12(um),den=cos12(um)-cos12(vm);int sign=0;
  if((arb_is_positive(num.x)&&arb_is_positive(den.x))||(arb_is_negative(num.x)&&arb_is_negative(den.x)))sign=1;
  if((arb_is_negative(num.x)&&arb_is_positive(den.x))||(arb_is_positive(num.x)&&arb_is_negative(den.x)))sign=-1;
  if(!sign)throw std::runtime_error("unresolved vertex core sign");B channel[2];
  for(int ch=0;ch<2;ch++){B y=B(a)+lambda+B(ch?1:-1)*B(n)*vf/B(2);long wrap=wrap12(y,n);y=y-B(n)*B(wrap);if(!arb_is_positive(y.x)||!arb_is_positive((B(n)-y-B(b-a)).x))throw std::runtime_error("whole-ball wrap/pole guard");channel[ch]=partial(n,b-a+1,y);st.blocks++;rowblocks++;if(rowblocks>24)throw std::runtime_error("vertex block cap");}
  result=result+B(sign)*(C*channel[0]+D*channel[1]);
 }
 st.maxBlocks=std::max(st.maxBlocks,rowblocks);if(!arb_is_finite(result.x))throw std::runtime_error("vertex result nonfinite");return result;
}
static B box12(long n,const Q&al,const Q&ah,const Q&bl,const Q&bh,Stats12&st,B&deltaMax,B&tail){
 if(sizeof(long)<8||n<2||n>4096L||fmpq_sgn(al.x)<0||fmpq_sgn(bl.x)<0||fmpq_cmp(al.x,ah.x)>0||fmpq_cmp(bl.x,bh.x)>0||fmpq_cmp_si((ah+bh).x,1)>0)throw std::runtime_error("whole rational triangle domain");
 if(fmpq_equal(al.x,ah.x)&&fmpq_equal(bl.x,bh.x)&&((!fmpq_cmp_si(al.x,1)&&fmpq_is_zero(bl.x))||(!fmpq_cmp_si(bl.x,1)&&fmpq_is_zero(al.x))))return B(1);
 B af=range12(qb12(al),qb12(ah)),bf=range12(qb12(bl),qb12(bh)),amid=qb12((al+ah)/Q(2)),bmid=qb12((bl+bh)/Q(2)),alpha=pi()*af,beta=pi()*bf,p=sin12(alpha),A=cos12(alpha)+cos12(beta),q=sin12(beta),total;long m=n+1;B N=B(n)*B(m),rowcap=B(n)*N;
 for(long r=0;r<2*m;r++){
  if(r==0||r==2*m-1||r==m-1||r==m){B row;for(long k=0;k<n;k++){row=row+absolute(finite12(n,r,k,af,bf,st));st.retained++;}total=total+min12(row,rowcap);continue;}
  st.ordinary++;try{
   long delta=(1-r)%2;if(delta<0)delta+=2;B vf=(B(r)+bf)/B(m),v=pi()*vf;std::set<long>cuts{0,n},actual;
   poleband12((B(n)*v-alpha-B(delta)*pi())/(B(2)*pi()),n,cuts,actual);poleband12((B(n)*(B(2)*pi()-v)-alpha-B(delta)*pi())/(B(2)*pi()),n,cuts,actual);directcut12(0,n,cuts,actual);directcut12(n-1,n,cuts,actual);
   if(actual.size()>8)throw std::runtime_error("actual buffered cap");st.maxD=std::max(st.maxD,(long)actual.size());B row;
   for(long k:actual){row=row+absolute(finite12(n,r,k,af,bf,st));st.direct++;}
   if((long)actual.size()==n){total=total+min12(row,rowcap);continue;}
   B c=A*(B(1)+cos12(v))+q*sin12(v);auto ce=endpoints12(c,-5,5),pe=endpoints12(p,0,1);deltaMax=max12(deltaMax,(ce.back()-ce.front())+(pe.back()-pe.front()));B largest;
   for(const B&cv:ce)for(const B&pv:pe)largest=max12(largest,vertex12(n,r,af,bf,amid,bmid,cv,pv,actual,cuts,st));
   total=total+min12(row+largest,rowcap);
  }catch(const std::exception&){st.fallback++;total=total+rowcap;}
 }
 double budget[3];c06_budget(n,n,budget);B H=B(1)+logb(B(n));tail=(point12(budget[0])+B(12)*point12(budget[1])+B(12)*point12(budget[2]))*(B(1)+B(5)*H)/B(n);
 B answer=min12(total/N,B(2)*N);if(!arb_is_finite(answer.x))throw std::runtime_error("final upper nonfinite");return answer;
}
static Q parse12(const char*s){Q q;if(!s||fmpq_set_str(q.x,s,10)||fmpz_is_zero(fmpq_denref(q.x)))throw std::runtime_error("rational parse");fmpq_canonicalise(q.x);return q;}
extern "C" int c12_box(long n,const char*al,const char*ah,const char*bl,const char*bh,double*out,long*counts){try{Stats12 st;B delta,tail;B ans=box12(n,parse12(al),parse12(ah),parse12(bl),parse12(bh),st,delta,tail);B H=B(1)+logb(B(n)),relax=B(2)/pi()*delta*H*H;out[0]=upper12(ans);out[1]=upper12(relax);out[2]=upper12(tail);out[3]=upper12(delta);long vals[]={st.retained,st.direct,st.regular,st.blocks,st.fallback,st.ordinary,st.maxD,st.maxE,st.maxBlocks,st.ratioFallback};for(int j=0;j<10;j++)counts[j]=vals[j];return 0;}catch(...){return 1;}}
