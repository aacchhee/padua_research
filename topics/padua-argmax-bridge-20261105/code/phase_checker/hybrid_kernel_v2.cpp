// Independent round-5 bounded R4-1 response. Derived from our frozen finite-polynomial
// checker, never from the producer arithmetic. Original arb_kernel.cpp preserved.
#include <flint/arb.h>
#include <vector>
#include <cmath>
#include <algorithm>
#include <stdexcept>
static constexpr slong P=160;
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
struct Jet {B v,a,b;};
static Jet add(const Jet&a,const Jet&b){return {a.v+b.v,a.a+b.a,a.b+b.b};}
// R_k(z) = [k odd] + 2 sum_{1<=j<k, j=k-1 mod 2} cos(jz).
// Direct Arb trig per harmonic avoids both quotient singularities and a
// correlated Chebyshev recurrence. These are finite exact identities.
static void ratios(const B&z,int n,B&r0,B&r1,B&d0,B&d1){
 r0=B((n%2)?1:0);r1=B(((n+1)%2)?1:0);d0=B(0);d1=B(0);
 for(int j=1;j<=n;j++){
  B t=z*B(j),s,c;arb_sin_cos(s.x,c.x,t.x,P);
  if((j-(n-1))%2==0 && j<n){r0=r0+B(2)*c;d0=d0-B(2*j)*s;}
  if((j-n)%2==0){r1=r1+B(2)*c;d1=d1-B(2*j)*s;}
 }
}
// Intersect independently valid enclosures. A quotient is valid on all of Z
// only when the outward sine ball excludes zero. Exact integer global bounds
// follow from the finite harmonics: sum |frequencies|=floor(k*k/2).
static bool refine_ratio(const B&z,int k,B&r,B&d){
 r=intersect(r,range(-k,k));
 const int cap=(k*k)/2;d=intersect(d,range(-cap,cap));
 B sz,cz;arb_sin_cos(sz.x,cz.x,z.x,P);
 if(!arb_is_finite(sz.x)||!arb_is_finite(cz.x)||arb_contains_zero(sz.x))return false;
 B sk,ck,kz=z*B(k);arb_sin_cos(sk.x,ck.x,kz.x,P);
 if(!arb_is_finite(sk.x)||!arb_is_finite(ck.x))return false;
 B denominator_square;arb_sqr(denominator_square.x,sz.x,P);
 if(!arb_is_finite(denominator_square.x)||arb_contains_zero(denominator_square.x))return false;
 B q=sk/sz;
 B dq=(B(k)*ck*sz-sk*cz)/denominator_square;
 return apply_optional_refinement(r,d,q,dq);
}
struct DualJet {Jet base,hybrid;};
static DualJet primitive(const B&u,const B&v,int n){
 B s=(u+v)/2,t=(u-v)/2,rs0,rs1,ds0,ds1,rt0,rt1,dt0,dt1;
 ratios(s,n,rs0,rs1,ds0,ds1);ratios(t,n,rt0,rt1,dt0,dt1);
 B z=u*B(n),sn,cn;arb_sin_cos(sn.x,cn.x,z.x,P);
 auto assemble=[&](){
  B ds=ds1*rt1+ds0*rt0,dt=rs1*dt1+rs0*dt0;
  return Jet{rs1*rt1+rs0*rt0-cn,((ds+dt)/2+B(n)*sn)/n,((ds-dt)/2)/(n+1)};
 };
 Jet baseline=assemble();
 refine_ratio(s,n,rs0,ds0);refine_ratio(s,n+1,rs1,ds1);
 refine_ratio(t,n,rt0,dt0);refine_ratio(t,n+1,rt1,dt1);
 return {baseline,assemble()};
}
struct Boards {std::vector<Jet> base,hybrid;};
static Boards board(int n,const B&a,const B&b){
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
 Sum S,C;
 for(int r=0;r<2*n;r++)for(int s=0;s<2*m;s++)if((r+s)%2){
  S.addterm(h[ix(r,s)],c[ix(r,s)]);
  Jet j=add(add(h[ix(r,s)],h[ix(-r,s)]),add(h[ix(r,-s)],h[ix(-r,-s)]));
  Jet k=add(add(c[ix(r,s)],c[ix(-r,s)]),add(c[ix(r,-s)],c[ix(-r,-s)]));C.addterm(j,k);
 }
 out[0]=upper(S.enclosure(ra,rb)/(2*N));out[1]=upper(C.enclosure(ra,rb)/(8*N));
 // Bound each projected triangle defect directly throughout the box.
 std::vector<B> qv(m+1),qh(n+1);
 for(int K=0;K<=m;K++)for(int r=0;r<2*n;r++)for(int s=0;s<2*m;s++)if((r+s)%2){
  const B&x=h[ix(r,s)].v;const B&y=h[ix(r,2*K-s)].v;
  qv[K]=qv[K]+absb(x)+absb(y)-absb(x+y);
 }
 for(int J=0;J<=n;J++)for(int r=0;r<2*n;r++)for(int s=0;s<2*m;s++)if((r+s)%2){
  const B&x=h[ix(r,s)].v;const B&y=h[ix(2*J-r,s)].v;
  qh[J]=qh[J]+absb(x)+absb(y)-absb(x+y);
 }
 B pi;arb_const_pi(pi.x,P);double pl=lower(pi),pu=upper(pi);
 double dl=INFINITY;
 for(int J=0;J<=n;J++)for(int K=0;K<=m;K++)if((J+K)%2){
  if((J==0||J==n)&&(K==0||K==m))continue;
  // Exclude only centers whose physical domain provably misses the box.
  // On these roots |phase|<=pi_hi, only endpoint inward signs matter.
  if((J==0&&ah<0)||(J==n&&al>0)||(K==0&&bh<0)||(K==m&&bl>0))continue;
  dl=std::min(dl,std::max({0.,lower(qv[K]/(4*N)),lower(qh[J]/(4*N))}));
 }
 out[2]=std::isfinite(dl)?dl:0.;
 B lc;
 for(int r=0;r<2*n;r++)for(int s=0;s<2*m;s++)if((r+s)%2)lc=lc+absb(z[ix(r,s)].v);
 lc=lc/(2*N);out[3]=lower(lc);out[4]=upper(lc);out[5]=pl;out[6]=pu;
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
 int e=collect_bounds(n,al,ah,bl,bh,h.base,c.base,z.base,out);
 if(e)return e;
 return collect_bounds(n,al,ah,bl,bh,h.hybrid,c.hybrid,z.hybrid,out+7);
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
  ratios(z,k,r,r1,d,d1);out[0]=lower(r);out[1]=upper(r);out[2]=lower(d);out[3]=upper(d);
  *used_quotient=refine_ratio(z,k,r,d)?1:0;
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
