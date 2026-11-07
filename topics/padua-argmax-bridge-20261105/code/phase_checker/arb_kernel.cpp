// Independent replay kernel: Arb balls, finite cosine polynomial, no producer imports.
#include <flint/arb.h>
#include <vector>
#include <cmath>
#include <algorithm>
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
static Jet primitive(const B&u,const B&v,int n){
 B s=(u+v)/2,t=(u-v)/2,rs0,rs1,ds0,ds1,rt0,rt1,dt0,dt1;
 ratios(s,n,rs0,rs1,ds0,ds1);ratios(t,n,rt0,rt1,dt0,dt1);
 B z=u*B(n),sn,cn;arb_sin_cos(sn.x,cn.x,z.x,P);
 B ds=ds1*rt1+ds0*rt0,dt=rs1*dt1+rs0*dt0;
 return {rs1*rt1+rs0*rt0-cn,((ds+dt)/2+B(n)*sn)/n,((ds-dt)/2)/(n+1)};
}
static std::vector<Jet> board(int n,const B&a,const B&b){
 B pi;arb_const_pi(pi.x,P);int m=n+1;
 std::vector<Jet> h(4*n*m);
 for(int r=0;r<2*n;r++)for(int s=0;s<2*m;s++)if((r+s)%2)
  h[r*(2*m)+s]=primitive((pi*B(r)+a)/n,(pi*B(s)+b)/m,n);
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
extern "C" int phase_bounds(int n,double al,double ah,double bl,double bh,double*out){
 if(n<2||n>512||!std::isfinite(al)||!std::isfinite(ah)||!std::isfinite(bl)||!std::isfinite(bh)||al>ah||bl>bh)return 1;
 B a=range(al,ah),b=range(bl,bh),ac=(B(al)+B(ah))/2,bc=(B(bl)+B(bh))/2;
 B ra=(B(ah)-B(al))/2,rb=(B(bh)-B(bl))/2;
 auto h=board(n,a,b),c=board(n,ac,bc);int m=n+1,N=n*m;
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
 auto z=board(n,B(0),B(0));B lc;
 for(int r=0;r<2*n;r++)for(int s=0;s<2*m;s++)if((r+s)%2)lc=lc+absb(z[ix(r,s)].v);
 lc=lc/(2*N);out[3]=lower(lc);out[4]=upper(lc);out[5]=pl;out[6]=pu;
 for(int i=0;i<7;i++)if(!std::isfinite(out[i]))return 2;
 return 0;
}
// Diagnostic entry: rigorous primitive at exact pi rational mesh plus exact
// binary64 phase offsets; exposes value and both phase derivatives.
extern "C" int phase_term(int n,int r,int s,double a,double b,double*out){
 if(n<2||n>512||!std::isfinite(a)||!std::isfinite(b))return 1;
 B pi;arb_const_pi(pi.x,P);
 Jet j=primitive((pi*B(r)+B(a))/n,(pi*B(s)+B(b))/(n+1),n);
 out[0]=lower(j.v);out[1]=upper(j.v);out[2]=lower(j.a);out[3]=upper(j.a);out[4]=lower(j.b);out[5]=upper(j.b);return 0;
}
