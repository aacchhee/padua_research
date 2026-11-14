// C03 distinct Arb endpoint/centered ratio tightness prototype; C01 preserved.
// Generated initially from preserved independent v3; no producer arithmetic.
// Original finite boards, derivatives and natural profiles remain unchanged.
// Pair lower bounds follow the independent real-rectangle lemma; no MPFR arithmetic.
#include <flint/arb.h>
#include <vector>
#include <cmath>
#include <algorithm>
#include <stdexcept>
static constexpr slong P=160;
static double counts[8]={};static double extra[4]={};static int variant=2;
extern "C" int c03_variant(int v){if(v<0||v>2)return 1;variant=v;return 0;}
extern "C" void c03_counts(double*out){for(int i=0;i<8;i++){out[i]=counts[i];counts[i]=0;}for(int i=0;i<4;i++){out[i+8]=extra[i];extra[i]=0;}}
extern "C" void c01_counts(double*out){for(int i=0;i<8;i++){out[i]=counts[i];counts[i]=0;}}
struct B {
 arb_t x;
 B(){arb_init(x);} B(double d):B(){arb_set_d(x,d);} B(const B&o):B(){arb_set(x,o.x);}
 B&operator=(const B&o){arb_set(x,o.x);return *this;} ~B(){arb_clear(x);}
};
static B operator+(const B&a,const B&b){B c;arb_add(c.x,a.x,b.x,P);return c;}
static B operator-(const B&a,const B&b){B c;arb_sub(c.x,a.x,b.x,P);return c;}
static B operator-(const B&a){B c;arb_neg(c.x,a.x);return c;}
static B operator*(const B&a,const B&b){B c;arb_mul(c.x,a.x,b.x,P);return c;}
static B operator/(const B&a,long b){B c;arb_div_si(c.x,a.x,b,P);return c;}
static B operator/(const B&a,const B&b){B c;arb_div(c.x,a.x,b.x,P);return c;}
// Optional refinements may be indeterminate and must then leave the finite
// baseline untouched. A finite contradiction is always an error.
static bool finite_intersection(B&out,const B&a,const B&b){
 if(!arb_is_finite(a.x)||!arb_is_finite(b.x))return false;
 if(!arb_intersection(out.x,a.x,b.x,P))throw std::runtime_error("empty finite valid intersection");
 return arb_is_finite(out.x);
}
static B intersect(const B&a,const B&b){
 B out;if(!finite_intersection(out,a,b))throw std::runtime_error("nonfinite baseline/global intersection");return out;
}
static bool apply_optional_refinement(B&r,B&d,const B&q,const B&dq){
 // Stage both results: never commit a value refinement if the derivative
 // candidate/intersection is indeterminate (or conversely).
 if(!arb_is_finite(q.x)||!arb_is_finite(dq.x))return false;
 B refined_r,refined_d;
 if(!finite_intersection(refined_r,r,q)||!finite_intersection(refined_d,d,dq))return false;
 r=refined_r;d=refined_d;return true;
}
static B absb(const B&a){B c;arb_abs(c.x,a.x);return c;}
static B hull(const B&a,const B&b){B c;arb_union(c.x,a.x,b.x,P);return c;}
static B range(double lo,double hi){return hull(B(lo),B(hi));}
static double upper(const B&a){arf_t z;arf_init(z);arb_get_ubound_arf(z,a.x,P);double d=arf_get_d(z,ARF_RND_CEIL);arf_clear(z);return d;}
static double lower(const B&a){arf_t z;arf_init(z);arb_get_lbound_arf(z,a.x,P);double d=arf_get_d(z,ARF_RND_FLOOR);arf_clear(z);return d;}
static B maxabs(const B&a){arf_t z;arf_init(z);arb_get_abs_ubound_arf(z,a.x,P);B r;arb_set_arf(r.x,z);arf_clear(z);return r;}
// A point-valued Arb object storing a lower bound, not an enclosure of d.
// d(x,y)=|x|+|y|-|x+y| is nonnegative. On opposite-sign balls it equals
// 2 min(|x|,|y|); otherwise zero is a valid lower bound.
static B positive_pair_lower(const B&x,const B&y){
 if(!arb_is_finite(x.x)||!arb_is_finite(y.x))throw std::runtime_error("nonfinite pair input");
 B out(0);
 if(!((arb_is_positive(x.x)&&arb_is_negative(y.x))||
      (arb_is_negative(x.x)&&arb_is_positive(y.x))))return out;
 B ax=absb(x),ay=absb(y);
 arf_t lx,ly;arf_init(lx);arf_init(ly);
 arb_get_lbound_arf(lx,ax.x,P);arb_get_lbound_arf(ly,ay.x,P);
 if(arf_cmp(lx,ly)>0)arf_set(lx,ly);
 // Multiplication by two is an exact exponent shift, including large values.
 arf_mul_2exp_si(lx,lx,1);arb_set_arf(out.x,lx);
 arf_clear(lx);arf_clear(ly);return out;
}
struct Jet {B v,a,b;};
static Jet add(const Jet&a,const Jet&b){return {a.v+b.v,a.a+b.a,a.b+b.b};}
// Fixed J32 rational sinc jet, independent of degree. No library sinc call.
static void sincjet(const B&x,B&s,B&d){
 static const std::vector<B> co=[](){std::vector<B> v(33);fmpz_t f;fmpz_init(f);
  for(int j=0;j<=32;j++){fmpz_fac_ui(f,2*j+1);B one((j%2)?-1:1);arb_div_fmpz(v[j].x,one.x,f,P);}fmpz_clear(f);return v;}();
 B xx;arb_sqr(xx.x,x.x,P);s=co[32];d=co[32]*B(64);
 for(int j=31;j>=0;j--){s=s*xx+co[j];if(j>=1)d=d*xx+co[j]*B(2*j);}
 d=d*x;
 fmpz_t f;fmpz_init(f);fmpz_fac_ui(f,67);
 B ax=maxabs(x),e0,e1;arb_pow_ui(e0.x,ax.x,66,P);arb_div_fmpz(e0.x,e0.x,f,P);
 arb_pow_ui(e1.x,ax.x,65,P);e1=e1*B(66);arb_div_fmpz(e1.x,e1.x,f,P);fmpz_clear(f);
 arb_add_error(s.x,e0.x);arb_add_error(d.x,e1.x);
 s=intersect(s,range(-1,1));d=intersect(d,range(-.5,.5));
 B local=maxabs(x)/3;d=intersect(d,hull(-local,local));
}
static bool quotient_pair(const B&z,int k,B&r,B&d){
 B sz,cz;counts[1]++;arb_sin_cos(sz.x,cz.x,z.x,P);
 if(!arb_is_finite(sz.x)||!arb_is_finite(cz.x)||arb_contains_zero(sz.x))return false;
 B sk,ck,kz=z*B(k);counts[1]++;arb_sin_cos(sk.x,ck.x,kz.x,P);
 if(!arb_is_finite(sk.x)||!arb_is_finite(ck.x))return false;
 B sq;arb_sqr(sq.x,sz.x,P);if(!arb_is_finite(sq.x)||arb_contains_zero(sq.x))return false;
 return apply_optional_refinement(r,d,sk/sz,(B(k)*ck*sz-sk*cz)/sq);
}
static void ratio_base(const B&z,int k,B&r,B&d){
 if(k<1||k>513||!arb_is_finite(z.x))throw std::runtime_error("invalid fixed ratio input");
 counts[0]++;r=range(-k,k);int c1=k*k/2;d=range(-c1,c1);if(k==1){r=B(1);d=B(0);return;}
 if(quotient_pair(z,k,r,d))return;
 // Rounded midpoint only proposes an exact turn; correctness uses literal guards.
 double mid=arf_get_d(arb_midref(z.x),ARF_RND_NEAR);
 if(!std::isfinite(mid)||std::abs(mid)>100.){counts[3]++;return;}
 long ell=std::lround(mid/3.14159265358979323846);B pi;arb_const_pi(pi.x,P);
 B a=z-pi*B(ell),ka=a*B(k);
 if(upper(maxabs(a))>1.5||upper(maxabs(ka))>4.){counts[3]++;return;}
 B sr,dr,sk,dk;sincjet(a,sr,dr);sincjet(ka,sk,dk);sr=intersect(sr,range(.625,1));
 B sq;arb_sqr(sq.x,sr.x,P);int eps=((ell%2)!=0&&k%2==0)?-1:1;
 B value=B(eps*k)*sk/sr,deriv=B(eps*k)*(B(k)*dk*sr-sk*dr)/sq;
 if(apply_optional_refinement(r,d,value,deriv))counts[2]++;
 else counts[3]++;
}
// No recursion: all point jets below call the preserved C01 base evaluator.
static bool endpoint_chart(const B&z,int k,B&r,B&d){
 double mid=arf_get_d(arb_midref(z.x),ARF_RND_NEAR);
 if(!std::isfinite(mid)||std::abs(mid)>100.)return false;
 long ell=std::lround(mid/3.14159265358979323846);B pi;arb_const_pi(pi.x,P);
 B a=z-pi*B(ell);if(upper(maxabs(a))>1.5||upper(maxabs(a*B(k)))>4.)return false;
 arf_t lo,hi;arf_init(lo);arf_init(hi);arb_get_abs_lbound_arf(lo,a.x,P);arb_get_abs_ubound_arf(hi,a.x,P);
 B l,u;arb_set_arf(l.x,lo);arb_set_arf(u.x,hi);arf_clear(lo);arf_clear(hi);
 // Extracted outward dyadics themselves must obey the admitted chart.
 if(lower(l)<0||upper(u)>1.5||upper(u*B(k))>4.)return false;
 B vl,dl,vu,du;if(arb_is_zero(l.x)){vl=B(k);dl=B(0);}else ratio_base(l,k,vl,dl);
 if(arb_equal(l.x,u.x)){vu=vl;du=dl;}else ratio_base(u,k,vu,du);
 arf_t bottom,top;arf_init(bottom);arf_init(top);arb_get_lbound_arf(bottom,vu.x,P);arb_get_ubound_arf(top,vl.x,P);
 B image;arb_set_interval_arf(image.x,bottom,top,P);arf_clear(bottom);arf_clear(top);
 int eps=(ell%2!=0&&k%2==0)?-1:1;if(eps<0)image=-image;
 B sign=d;int cap=k*k/2;
 if(arb_is_nonnegative(a.x))sign=intersect(sign,eps>0?range(-cap,0):range(0,cap));
 if(arb_is_nonpositive(a.x))sign=intersect(sign,eps>0?range(0,cap):range(-cap,0));
 bool used=apply_optional_refinement(r,d,image,sign);if(used)extra[1]++;return used;
}
static void ratio_fixed(const B&z,int k,B&r,B&d){
 // Base validates first, including k1/nonfinite inputs. Successful quotient
 // must not skip independently valid endpoint or centered candidates.
 extra[0]++;ratio_base(z,k,r,d);if(k==1)return;
 endpoint_chart(z,k,r,d);if(variant==0||arb_is_exact(z.x))return;
 B center;arb_set_arf(center.x,arb_midref(z.x));B t=z-center,h=maxabs(t),vc,dc;ratio_base(center,k,vc,dc);
 long c2=(long)k*((long)k*k-1)/3;B curvature(c2);
 if(variant==2){
  B sn,cs;counts[1]++;arb_sin_cos(sn.x,cs.x,z.x,P);
  if(arb_is_finite(sn.x)&&arb_is_finite(cs.x)&&!arb_contains_zero(sn.x)){
   B ode=B(1-k*k)*r-B(2)*(cs/sn)*d;
   if(arb_is_finite(ode.x)){B ab=maxabs(ode);if(upper(ab)<c2){curvature=ab;extra[3]++;}}
  }
 }
 B h2;arb_sqr(h2.x,h.x,P);B ev=curvature*h2/2,ed=curvature*h;
 B tv=vc+dc*t+hull(-ev,ev),td=dc+hull(-ed,ed);
 if(apply_optional_refinement(r,d,tv,td))extra[2]++;
}
static void ratios(const B&z,int n,B&r0,B&r1,B&d0,B&d1){ratio_fixed(z,n,r0,d0);ratio_fixed(z,n+1,r1,d1);}
static bool refine_ratio(const B&z,int k,B&r,B&d){(void)z;(void)k;(void)r;(void)d;return false;}
struct DualJet {Jet base,hybrid;};
static DualJet primitive(const B&u,const B&v,int n){
 B s=(u+v)/2,t=(u-v)/2,rs0,rs1,ds0,ds1,rt0,rt1,dt0,dt1;
 ratios(s,n,rs0,rs1,ds0,ds1);ratios(t,n,rt0,rt1,dt0,dt1);
 B z=u*B(n),sn,cn;counts[1]++;arb_sin_cos(sn.x,cn.x,z.x,P);
 auto assemble=[&](){
  B ds=ds1*rt1+ds0*rt0,dt=rs1*dt1+rs0*dt0;
  return Jet{rs1*rt1+rs0*rt0-cn,((ds+dt)/2+B(n)*sn)/n,((ds-dt)/2)/(n+1)};
 };
 Jet result=assemble();return {result,result};
}
struct Boards {std::vector<Jet> base,hybrid;};
static Boards board(int n,const B&a,const B&b){
 counts[7]++;
 B pi;arb_const_pi(pi.x,P);int m=n+1;
 Boards h{std::vector<Jet>(4*n*m),std::vector<Jet>(4*n*m)};
 for(int r=0;r<2*n;r++)for(int s=0;s<2*m;s++)if((r+s)%2){
  DualJet j=primitive((pi*B(r)+a)/n,(pi*B(s)+b)/m,n);
  h.base[r*(2*m)+s]=j.base;h.hybrid[r*(2*m)+s]=j.hybrid;
 }
 return h;
}
static B signedgrad(const B&v,const B&g){
 if(arb_is_positive(v.x))return g;
 if(arb_is_negative(v.x))return -g;
 B z=maxabs(g);return hull(-z,z);
}
struct Sum {B natural,center,ga,gb;
 void addterm(const Jet&j,const Jet&c){natural=natural+absb(j.v);center=center+absb(c.v);ga=ga+signedgrad(j.v,j.a);gb=gb+signedgrad(j.v,j.b);}
 B enclosure(const B&ra,const B&rb){B mv=center+ra*maxabs(ga)+rb*maxabs(gb);return B(std::min(upper(natural),upper(mv)));}
};
// Returns S upper, corner-orbit upper, all-admissible-center projected lower,
// Lc lower, Lc upper, pi lower, pi upper. 0 on success; no acceptance here.
static int collect_bounds(int n,double al,double ah,double bl,double bh,
 const std::vector<Jet>&h,const std::vector<Jet>&c,const std::vector<Jet>&z,double*out){
 if(n<2||n>512||!std::isfinite(al)||!std::isfinite(ah)||!std::isfinite(bl)||!std::isfinite(bh)||al>ah||bl>bh)return 1;
 B a=range(al,ah),b=range(bl,bh),ac=(B(al)+B(ah))/2,bc=(B(bl)+B(bh))/2;
 B ra=(B(ah)-B(al))/2,rb=(B(bh)-B(bl))/2;
 int m=n+1,N=n*m;
 auto ix=[&](int r,int s){return ((r%(2*n)+2*n)%(2*n))*(2*m)+(s%(2*m)+2*m)%(2*m);};
 B lc;for(int r=0;r<2*n;r++)for(int s=0;s<2*m;s++)if((r+s)%2)lc=lc+absb(z[ix(r,s)].v);
 lc=lc/(2*N);B pi;arb_const_pi(pi.x,P);double pl=lower(pi),pu=upper(pi);
 out[3]=lower(lc);out[4]=upper(lc);out[5]=pl;out[6]=pu;
 Sum S,C;
 for(int r=0;r<2*n;r++)for(int s=0;s<2*m;s++)if((r+s)%2)S.addterm(h[ix(r,s)],c[ix(r,s)]);
 out[0]=upper(S.enclosure(ra,rb)/(2*N));
 if(out[0]<out[3]){out[1]=out[0];out[2]=0;counts[4]++;return 0;}
 for(int r=0;r<2*n;r++)for(int s=0;s<2*m;s++)if((r+s)%2){
  Jet j=add(add(h[ix(r,s)],h[ix(-r,s)]),add(h[ix(r,-s)],h[ix(-r,-s)]));
  Jet k=add(add(c[ix(r,s)],c[ix(-r,s)]),add(c[ix(r,-s)],c[ix(-r,-s)]));C.addterm(j,k);
 }
 out[1]=upper(C.enclosure(ra,rb)/(8*N));
 // Approved C01 allclass theorem applies to the entire outward box only.
 B rho=B(std::max(std::abs(al),std::abs(ah)))+B(std::max(std::abs(bl),std::abs(bh)));
 if(n>=64&&upper(rho)<=.5){out[2]=1./2048;counts[5]++;return 0;}
 counts[6]++;
 // Bound each projected triangle defect directly throughout the box.
 std::vector<B> qv(m+1),qh(n+1),positive_v(m+1),positive_h(n+1);
 for(int K=0;K<=m;K++)for(int r=0;r<2*n;r++)for(int s=0;s<2*m;s++)if((r+s)%2){
  const B&x=h[ix(r,s)].v;const B&y=h[ix(r,2*K-s)].v;
  qv[K]=qv[K]+absb(x)+absb(y)-absb(x+y);
  positive_v[K]=positive_v[K]+positive_pair_lower(x,y);
 }
 for(int J=0;J<=n;J++)for(int r=0;r<2*n;r++)for(int s=0;s<2*m;s++)if((r+s)%2){
  const B&x=h[ix(r,s)].v;const B&y=h[ix(2*J-r,s)].v;
  qh[J]=qh[J]+absb(x)+absb(y)-absb(x+y);
  positive_h[J]=positive_h[J]+positive_pair_lower(x,y);
 }
 double dl=INFINITY;
 for(int J=0;J<=n;J++)for(int K=0;K<=m;K++)if((J+K)%2){
  if((J==0||J==n)&&(K==0||K==m))continue;
  // Exclude only centers whose physical domain provably misses the box.
  // On these roots |phase|<=pi_hi, only endpoint inward signs matter.
  if((J==0&&ah<0)||(J==n&&al>0)||(K==0&&bh<0)||(K==m&&bl>0))continue;
  dl=std::min(dl,std::max({0.,lower(qv[K]/(4*N)),lower(qh[J]/(4*N)),lower(positive_v[K]/(4*N)),lower(positive_h[J]/(4*N))}));
 }
 out[2]=std::isfinite(dl)?dl:0.;
 for(int i=0;i<7;i++)if(!std::isfinite(out[i]))return 2;
 return 0;
}
// Both scalar enclosures remain valid even if Arb ball conversion means
// interval endpoints are not literally nested. Min upper / max lower retains
// the baseline guarantees without relying on monotonicity of ball radii.
static int all_bounds(int n,double al,double ah,double bl,double bh,double*out){
 if(n<2||n>512||!std::isfinite(al)||!std::isfinite(ah)||!std::isfinite(bl)||!std::isfinite(bh)||al>ah||bl>bh)return 1;
 B a=range(al,ah),b=range(bl,bh),ac=(B(al)+B(ah))/2,bc=(B(bl)+B(bh))/2;
 Boards h=board(n,a,b),c=board(n,ac,bc),z=board(n,B(0),B(0));
 int e=collect_bounds(n,al,ah,bl,bh,h.hybrid,c.hybrid,z.hybrid,out);
 if(e)return e;for(int i=0;i<7;i++)out[i+7]=out[i];return 0;
}
extern "C" int phase_bounds_pair(int n,double al,double ah,double bl,double bh,double*out){
 try{return all_bounds(n,al,ah,bl,bh,out);}catch(const std::exception&){return 3;}
}
extern "C" int phase_bounds(int n,double al,double ah,double bl,double bh,double*out){
 try{
  double both[14];int e=all_bounds(n,al,ah,bl,bh,both);if(e)return e;
  for(int i=0;i<7;i++)out[i]=(i==2||i==3||i==5)?std::max(both[i],both[i+7]):std::min(both[i],both[i+7]);
  if(out[3]>out[4]||out[5]>out[6])return 3;
  return 0;
 }catch(const std::exception&){return 3;}
}
// Diagnostic entry: rigorous primitive at exact pi rational mesh plus exact
// binary64 phase offsets; exposes value and both phase derivatives.
extern "C" int phase_term(int n,int r,int s,double a,double b,double*out){
 try{
 if(n<2||n>512||!std::isfinite(a)||!std::isfinite(b))return 1;
 B pi;arb_const_pi(pi.x,P);
 Jet j=primitive((pi*B(r)+B(a))/n,(pi*B(s)+B(b))/(n+1),n).hybrid;
 out[0]=lower(j.v);out[1]=upper(j.v);out[2]=lower(j.a);out[3]=upper(j.a);out[4]=lower(j.b);out[5]=upper(j.b);
 for(int i=0;i<6;i++)if(!std::isfinite(out[i]))return 2;
 return 0;
 }catch(const std::exception&){return 3;}
}

// Bounded diagnostic: z=turn*pi+[lo,hi], exact integer turn and binary64
// offsets. Output baseline value/derivative then hybrid value/derivative.
extern "C" int phase_ratio(int k,int turn,double lo,double hi,double*out,int*used_quotient){
 try{
  if(k<1||k>513||turn< -4||turn>4||!std::isfinite(lo)||!std::isfinite(hi)||lo>hi)return 1;
  B pi;arb_const_pi(pi.x,P);B z=pi*B(turn)+range(lo,hi),r,r1,d,d1;
  double before=counts[2],fallback_before=counts[3];ratio_fixed(z,k,r,d);out[0]=lower(r);out[1]=upper(r);out[2]=lower(d);out[3]=upper(d);
  *used_quotient=(counts[2]>before)?2:((counts[3]>fallback_before)?0:1);
  out[4]=lower(r);out[5]=upper(r);out[6]=lower(d);out[7]=upper(d);
 for(int i=0;i<8;i++)if(!std::isfinite(out[i]))return 2;
 return 0;
 }catch(const std::exception&){return 3;}
}
extern "C" int phase_disjoint_intersection_control(){
 try{B x=intersect(B(0),B(1));(void)x;return 0;}catch(const std::exception&){return 3;}
}

// Directly exercise the fallback branch without depending on a particular
// Arb overestimation pattern. Finite inconsistent candidates still throw.
extern "C" int phase_nonfinite_refinement_control(int which,double*out){
 try{
  B r(1),d(0),q(1),dq(0);
  if(which==0)arb_indeterminate(q.x);
  else if(which==1)arb_indeterminate(dq.x);
  else if(which==2)q=B(2);
  else return 1;
  bool used=apply_optional_refinement(r,d,q,dq);
  if(used)return 4;
  out[0]=lower(r);out[1]=upper(r);out[2]=lower(d);out[3]=upper(d);
  for(int i=0;i<4;i++)if(!std::isfinite(out[i]))return 2;
  return 0;
 }catch(const std::exception&){return 3;}
}

// Bounded diagnostic entry: interval inputs are exact binary64 endpoints.
// Return the positive lower-bound point, old natural enclosure, and maximum
// lower bound. This entry performs no certificate acceptance.
extern "C" int phase_pair_defect(double al,double ah,double bl,double bh,double*out){
 try{
  if(!std::isfinite(al)||!std::isfinite(ah)||!std::isfinite(bl)||!std::isfinite(bh)||al>ah||bl>bh)return 1;
  B x=range(al,ah),y=range(bl,bh),p=positive_pair_lower(x,y);
  B natural=absb(x)+absb(y)-absb(x+y);
  out[0]=lower(p);out[1]=upper(p);out[2]=lower(natural);out[3]=upper(natural);
  out[4]=std::max({0.,out[0],out[2]});
  for(int i=0;i<5;i++)if(!std::isfinite(out[i]))return 2;
  return 0;
 }catch(const std::exception&){return 3;}
}
