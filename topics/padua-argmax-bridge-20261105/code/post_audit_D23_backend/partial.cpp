// C10 partial-cotangent research backend derived from frozen C06. C02 (1)--(3), no point-S assembly.
#include <flint/arb.h>
#include <flint/fmpq.h>
#include <vector>
#include <stdexcept>
static constexpr slong P=160, CP=640;
static constexpr int J=2,K=8,LH=4,WD=16;
struct B {arb_t x; B(){arb_init(x);} B(long a):B(){arb_set_si(x,a);} B(const B&a):B(){arb_set(x,a.x);} B&operator=(const B&a){arb_set(x,a.x);return *this;} ~B(){arb_clear(x);}};
static B operator+(const B&a,const B&b){B c;arb_add(c.x,a.x,b.x,P);return c;}
static B operator-(const B&a,const B&b){B c;arb_sub(c.x,a.x,b.x,P);return c;}
static B operator*(const B&a,const B&b){B c;arb_mul(c.x,a.x,b.x,P);return c;}
static B operator/(const B&a,const B&b){B c;arb_div(c.x,a.x,b.x,P);return c;}
static B power(const B&a,unsigned k){B c;arb_pow_ui(c.x,a.x,k,P);return c;}
static B pi(){B c;arb_const_pi(c.x,P);return c;}
static B logb(const B&a){B c;arb_log(c.x,a.x,P);return c;}
static B absolute(const B&a){B c;arb_abs(c.x,a.x);return c;}
static const std::vector<B>& co(){static std::vector<B> v=[](){
 std::vector<B> r(WD+1); std::vector< fmpq*> t(WD+1);
 for(auto &p:t){p=new fmpq;fmpq_init(p);} fmpq_one(t[0]); fmpq_t tmp;fmpq_init(tmp);
 B pc,term,a,b;arb_const_pi(pc.x,CP);
 for(int j=0;j<=WD;j++){
  if(j){for(int k=0;k<j;k++){fmpq_mul(tmp,t[k],t[j-1-k]);fmpq_add(t[j],t[j],tmp);}fmpq_set_si(tmp,2*j+1,1);fmpq_div(t[j],t[j],tmp);}
  arb_one(a.x);arb_mul_2exp_si(a.x,a.x,2*j+3);arb_div(a.x,a.x,pc.x,CP);
  arb_pow_ui(b.x,pc.x,2*j+1,CP);arb_set_fmpq(term.x,t[j],CP);arb_mul(b.x,b.x,term.x,CP);arb_sub(r[j].x,a.x,b.x,CP);
 }
 fmpq_clear(tmp);for(auto p:t){fmpq_clear(p);delete p;}return r;}();return v;}
// W remains stable across its removable zeros using Arb's entire sinc.
static B W(const B&x){B p=pi(),y=x; if(arb_gt(x.x,(p/B(2)).x))y=p-x;B s;arb_sinc(s.x,y.x,P);return logb(s/(p-y));}
// Globally convergent residual series; derivative tail explicitly enclosed.
static B wp(const B&x){B p=pi(),z=x/p-B(1)/B(2),zz=z*z,a=co()[WD]*B(2*WD+1);
 for(int j=WD-1;j>=0;j--)a=a*zz+co()[j]*B(2*j+1);
 a=a/p; B tail=B(16)/(B(9)*p*p)*power(B(1)/B(4),WD+1)*(B(2*WD+3)*B(4)/B(3)+B(8)/B(9));arb_add_error(a.x,tail.x);return a;}
static B harmonic(long q,const B&y){B s;long prefix=q<K?q:K;for(long i=0;i<prefix;i++)s=s+B(1)/(y+B(i));
 if(q<=K)return s;B x=y+B(K),z=y+B(q);s=s+logb(z/x)+(B(1)/x-B(1)/z)/B(2);
 for(int r=1;r<=LH;r++){B b;arb_bernoulli_ui(b.x,2*r,P);s=s+b/B(2*r)*(B(1)/power(x,2*r)-B(1)/power(z,2*r));}
 B eta;arb_bernoulli_ui(eta.x,2*LH,P);eta=absolute(eta)/B(2*LH)/power(B(K),2*LH);arb_add_error(s.x,eta.x);return s;}
// Exact rational moment construction at the input midpoint. Its input-ball
// dependence is bounded separately by |d/dy sum z_i^d| <= d*q*2^(1-d)/n.
struct Q {fmpq_t x;Q(){fmpq_init(x);}Q(long v):Q(){fmpq_set_si(x,v,1);}Q(const Q&a):Q(){fmpq_set(x,a.x);}Q&operator=(const Q&a){fmpq_set(x,a.x);return *this;}~Q(){fmpq_clear(x);}};
static Q operator+(const Q&a,const Q&b){Q c;fmpq_add(c.x,a.x,b.x);return c;}
static Q operator-(const Q&a,const Q&b){Q c;fmpq_sub(c.x,a.x,b.x);return c;}
static Q operator*(const Q&a,const Q&b){Q c;fmpq_mul(c.x,a.x,b.x);return c;}
static Q operator/(const Q&a,const Q&b){Q c;fmpq_div(c.x,a.x,b.x);return c;}
static Q powerq(const Q&a,unsigned d){Q c;fmpq_pow_si(c.x,a.x,d);return c;}
// Same exact-midpoint recurrence with every arithmetic operation explicit640.
// No global160-bit B operator is used until final input-radius propagation.
static std::vector<B> moments(long n,long q,const B&y){
 constexpr slong MP=640;B ym,left,right,step,half,term,binom,den;
 arb_set_arf(ym.x,arb_midref(y.x));arb_one(step.x);arb_div_si(step.x,step.x,n,MP);arb_mul_2exp_si(half.x,step.x,-1);
 arb_mul_2exp_si(term.x,B(1).x,-1);arb_sub(left.x,ym.x,term.x,MP);arb_div_si(left.x,left.x,n,MP);arb_sub(left.x,left.x,term.x,MP);
 arb_add_si(right.x,ym.x,q,MP);arb_sub(right.x,right.x,term.x,MP);arb_div_si(right.x,right.x,n,MP);arb_sub(right.x,right.x,term.x,MP);
 std::vector<B> work(2*J+2),out(2*J+2),lp(2*J+3),rp(2*J+3),hp(2*J+2);lp[0]=B(1);rp[0]=B(1);hp[0]=B(1);
 for(int k=1;k<=2*J+2;k++){arb_mul(lp[k].x,lp[k-1].x,left.x,MP);arb_mul(rp[k].x,rp[k-1].x,right.x,MP);if(k<=2*J+1)arb_mul(hp[k].x,hp[k-1].x,half.x,MP);}
 work[0]=B(q);out[0]=B(q);B yr;arf_set_mag(arb_midref(yr.x),arb_radref(y.x));
 for(int d=1;d<=2*J+1;d++){
  arb_sub(work[d].x,rp[d+1].x,lp[d+1].x,MP);arb_mul_si(den.x,step.x,d+1,MP);arb_div(work[d].x,work[d].x,den.x,MP);arb_one(binom.x);
  for(int k=1;k<=d;k++){arb_mul_si(binom.x,binom.x,d-k+1,MP);arb_div_si(binom.x,binom.x,k,MP);if(k%2==0){arb_mul(term.x,binom.x,hp[k].x,MP);arb_div_si(term.x,term.x,k+1,MP);arb_mul(term.x,term.x,work[d-k].x,MP);arb_sub(work[d].x,work[d].x,term.x,MP);}}
  arb_set_round(out[d].x,work[d].x,P);B error=B(d)*B(q)/B(n)*power(B(1)/B(2),d-1)*yr;arb_add_error(out[d].x,error.x);
 }return out;
}
static B partial(long n,long q,const B&y){if(n<2||n>2147483647L||q<0||q>n)throw std::runtime_error("invalid integer input");if(!q)return B();
 if(!arb_is_positive(y.x)||!arb_is_positive((B(n)-y-B(q-1)).x))throw std::runtime_error("nonpositive pole distance");
 B p=pi(),h=p/B(n),s=B(1)/B(n),zl=(y-B(1)/B(2))/B(n)-B(1)/B(2),zr=(y+B(q)-B(1)/B(2))/B(n)-B(1)/B(2);
 // Exact centered-cell moment recurrence, degree <=2J+1; no q-sized sum.
 std::vector<B> mom=moments(n,q,y);
 B ps,integ,deriv;for(int j=0;j<=J;j++){int d=2*j+1;ps=ps+co()[j]*mom[d];integ=integ+co()[j]*(power(zr,d+1)-power(zl,d+1))/B(d+1);deriv=deriv+co()[j]*B(d)*(power(zr,d-1)-power(zl,d-1));}
 B left=p*(zl+B(1)/B(2)),right=p*(zr+B(1)/B(2));
 B ans=(harmonic(q,y)-harmonic(q,B(n)-y-B(q-1)))/h+ps+(W(right)-W(left)-p*integ)/h-h/B(24)*(wp(right)-wp(left)-deriv/p);
 B mj=B(389120)/(B(19683)*power(p,5))*power(B(2*J+3),4)*power(B(1)/B(4),J),err=B(7*q)*power(h,4)/B(5760)*mj;
 arb_add_error(ans.x,err.x);if(!arb_is_finite(ans.x))throw std::runtime_error("nonfinite result");return ans;
}
extern "C" int c06_partial(long n,long q,const char*ystr,double*out){try{B y; if(arb_set_str(y.x,ystr,P))return 2;B a=partial(n,q,y);arf_t t;arf_init(t);arb_get_lbound_arf(t,a.x,P);out[0]=arf_get_d(t,ARF_RND_FLOOR);arb_get_ubound_arf(t,a.x,P);out[1]=arf_get_d(t,ARF_RND_CEIL);out[2]=mag_get_d(arb_radref(a.x));arf_clear(t);return 0;}catch(...){return 1;}}
// Independent small reference only: never called from production partial().
extern "C" int c06_compare(long n,long q,const char*ystr,double*out){try{B y;if(arb_set_str(y.x,ystr,P))return 2;B a=partial(n,q,y);B ref,yr,pp,angle,c;arb_set_str(yr.x,ystr,512);arb_const_pi(pp.x,512);for(long i=0;i<q;i++){arb_add_si(angle.x,yr.x,i,512);arb_mul(angle.x,angle.x,pp.x,512);arb_div_si(angle.x,angle.x,n,512);arb_cot(c.x,angle.x,512);arb_add(ref.x,ref.x,c.x,512);}out[0]=arb_overlaps(a.x,ref.x);out[1]=arb_contains(a.x,ref.x);out[2]=mag_get_d(arb_radref(a.x));return 0;}catch(...){return 1;}}

extern "C" void c06_budget(long n,long q,double*out){B p=pi(),h=p/B(n),mj=B(389120)/(B(19683)*power(p,5))*power(B(2*J+3),4)*power(B(1)/B(4),J),smooth=B(7*q)*power(h,4)/B(5760)*mj,eta;arb_bernoulli_ui(eta.x,2*LH,P);eta=absolute(eta)/B(2*LH)/power(B(K),2*LH);B harmonic_error=q>K?B(2)*eta/h:B(); B derivative_tail=B(16)/(B(9)*p*p)*power(B(1)/B(4),WD+1)*(B(2*WD+3)*B(4)/B(3)+B(8)/B(9));B tails[]={smooth,harmonic_error,h/B(12)*derivative_tail};arf_t a;arf_init(a);for(int i=0;i<3;i++){arb_get_ubound_arf(a,tails[i].x,P);out[i]=arf_get_d(a,ARF_RND_CEIL);}arf_clear(a);}
// Native integration entry: preserves the full Arb ball instead of binary64 bounds.
extern "C" int c06_partial_arb(long n,long q,const arb_t y,arb_t out){try{B input;arb_set(input.x,y);B a=partial(n,q,input);arb_set(out,a.x);return 0;}catch(...){arb_indeterminate(out);return 1;}}
