// Independent exact fixed-point interval corner verification; no MPFR kernel.
#include <gmpxx.h>
#include <algorithm>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using Z=mpz_class;
using Q=mpq_class;
constexpr unsigned PREC=512;
const Z SCALE=Z(1)<<PREC;
Z down(const Z&a,const Z&b){if(b<=0)throw std::runtime_error("nonpositive divisor");Z q;mpz_fdiv_q(q.get_mpz_t(),a.get_mpz_t(),b.get_mpz_t());return q;}
Z up(const Z&a,const Z&b){if(b<=0)throw std::runtime_error("nonpositive divisor");Z q;mpz_cdiv_q(q.get_mpz_t(),a.get_mpz_t(),b.get_mpz_t());return q;}
struct I{
 Z l,h;
 I(long x=0):l(Z(x)*SCALE),h(l){}
 I(Z a,Z b):l(a),h(b){if(l>h)throw std::runtime_error("reversed interval");}
 static I rat(Q q){q.canonicalize();return I(down(Z(q.get_num()*SCALE),q.get_den()),up(Z(q.get_num()*SCALE),q.get_den()));}
};
I operator+(const I&a,const I&b){return I(Z(a.l+b.l),Z(a.h+b.h));}
I operator-(const I&a){return I(Z(-a.h),Z(-a.l));}
I operator-(const I&a,const I&b){return a+(-b);}
I operator*(const I&a,const I&b){Z x[]={Z(a.l*b.l),Z(a.l*b.h),Z(a.h*b.l),Z(a.h*b.h)};return I(down(*std::min_element(x,x+4),SCALE),up(*std::max_element(x,x+4),SCALE));}
I inverse(const I&a){if(a.l<=0&&a.h>=0)throw std::runtime_error("division through zero");if(a.h<0)return -inverse(-a);return I(down(Z(SCALE*SCALE),a.h),up(Z(SCALE*SCALE),a.l));}
I operator/(const I&a,const I&b){return a*inverse(b);}
I sq(const I&a){if(a.l<=0&&a.h>=0)return I(Z(0),up(std::max(Z(a.l*a.l),Z(a.h*a.h)),SCALE));Z x=a.l*a.l,y=a.h*a.h;return I(down(std::min(x,y),SCALE),up(std::max(x,y),SCALE));}
I abs_i(const I&a){if(a.l>=0)return a;if(a.h<=0)return -a;return I(Z(0),std::max(Z(-a.l),a.h));}
Q lo(const I&a){Q q(a.l,SCALE);q.canonicalize();return q;}
Q hi(const I&a){Q q(a.h,SCALE);q.canonicalize();return q;}
// atan(1/d): even number of alternating terms is lower; next positive term bounds remainder.
std::pair<Q,Q> atan_bounds(unsigned d){constexpr unsigned terms=240;Z power=d,dd=Z(d)*d;Q s=0;for(unsigned k=0;k<terms;k++){Q t(1,Z(power*(2*k+1)));if(k%2)s-=t;else s+=t;power*=dd;}Q next(1,Z(power*(2*terms+1)));return {s,s+next};}
I pi_bounds(){auto a=atan_bounds(5),b=atan_bounds(239);Q l=16*a.first-4*b.second,h=16*a.second-4*b.first;return I(I::rat(l).l,I::rat(h).h);}
I cosine(unsigned j,unsigned n,const I&pi){
 if(j==0)return I(1);
 if(j==n)return I(-1);
 if(2*j==n)return I(0);
 // Evaluate cos(j*pi/n) directly. Taylor degree 201 has tail <=4^202/202!.
 I x=pi*I::rat(Q(j,n));if(x.l<0||x.h>4*SCALE)throw std::runtime_error("angle bound");
 I x2=sq(x),term(1),sum(1);
 for(unsigned k=1;k<=100;k++){term=term*x2*I::rat(Q(1,Z(2*k)*Z(2*k-1)));if(k%2)sum=sum-term;else sum=sum+term;}
 Z fac=1,pow4=1;for(unsigned k=1;k<=202;k++){fac*=k;pow4*=4;}
 I err=I::rat(Q(pow4,fac));return I(Z(sum.l-err.h),Z(sum.h+err.h));
}
std::string qs(Q x){x.canonicalize();return x.get_str();}
void field(const char*name,const Q&q,bool comma=true){std::cout<<"  \""<<name<<"\": \""<<qs(q)<<"\""<<(comma?",":"")<<"\n";}
void degree(unsigned n){
 if(n<2||n>10000)throw std::runtime_error("degree domain");
 unsigned m=n+1;
 I pi=pi_bounds();if(pi.l<=3*SCALE||pi.h>=4*SCALE)throw std::runtime_error("pi enclosure");
 std::vector<I>a,b;for(unsigned j=0;j<=n;j++)a.push_back(cosine(j,n,pi));for(unsigned k=0;k<=m;k++)b.push_back(cosine(k,m,pi));
 // Explicit removable 00 cardinal and PHYSICAL gradients (squares remove parity sign).
 I mass=I::rat(Q(1,m));I gx00=I::rat(Q(-(2L*n*n+1),6L*m));I gy00=I::rat(Q(-(2L*n+1),6));
 I energy=(sq(gx00)+sq(gy00))/mass;unsigned kept=1,omitted=0;
 for(unsigned j=0;j<=n;j++)for(unsigned k=0;k<=m;k++){
  if((j+k)%2||(j==0&&k==0))continue;
  if(k==0){if(j%2||j==0)throw std::runtime_error("zero mask");omitted++;continue;}
  I aa=a[j],bb=b[k],C=I(1)-bb,d=bb-aa;
  const long sign_index=long(m)*j-long(n)*k;
  if((sign_index>0&&d.l<=0)||(sign_index<0&&d.h>=0)||!sign_index)throw std::runtime_error("denominator sign");
  Q two_w(4,Z(n)*m);two_w.canonicalize();if(j==0||j==n)two_w/=2;if(k==0||k==m)two_w/=2;
  I pref=I::rat(two_w),d2=sq(d),d3=d2*d;
  I value=pref*C/d;
  // Expanded T227 brackets, NOT producer's normalized q_x,q_y calculation.
  I common=I(long(n))*(aa*bb-I(1))/d2;
  I gx=pref*(-I::rat(Q(Z(n)*n,2))*C/d+common-C*aa/d2+I(2)*C*(I(1)-sq(aa))/d3);
  I gy=pref*(-I::rat(Q(Z(m)*m,2))*C/d+common+C*(I(1)+I(2)*bb)/d2+I(2)*C*(I(1)-sq(bb))/d3);
  I v=abs_i(value);if(v.l<=0)throw std::runtime_error("nonzero cardinal not separated");
  mass=mass+v;energy=energy+(sq(gx)+sq(gy))/v;kept++;
 }
 unsigned c=0;Z power=1;while(power<n+1){power*=2;c++;}
 Q ell=lo(mass),E=hi(energy),u=110L*(1+c)*(1+c);if(ell<=0)throw std::runtime_error("mass lower bound");
 Q bnorm=E/(Q(Z(n)*n*n*n)*ell),K=u/ell;
 Q kap=1/(8*(bnorm+3*K));if(kap>1)kap=1;
 Q phase=Q(1,128*128)*(1+Q(Z(n)*n,Z(m)*m))/2;
 if(!(kap>Q(1,12500)&&phase<=Q(1,12500)))throw std::runtime_error("target radius not proved");
 if(kept+omitted!=(n+1)*(n+2)/2||omitted!=n/2)throw std::runtime_error("mask/cardinality");
 std::cout<<"{\n  \"degree\": "<<n<<",\n  \"precision_bits\": "<<PREC<<",\n  \"nonzero_cardinals\": "<<kept<<",\n  \"zero_cardinals_omitted\": "<<omitted<<",\n";
 field("pi_lower",lo(pi));field("pi_upper",hi(pi));field("corner_lower",ell);field("corner_upper",hi(mass));field("energy_lower",lo(energy));field("energy_upper",E);field("global_norm_upper",u);field("normalized_energy_upper",bnorm);field("kappa",kap);field("scaled_phase_requirement",phase);field("certified_common_kappa",Q(1,12500),false);std::cout<<"}\n";
}
int main(int argc,char**argv){try{if(argc!=2)throw std::runtime_error("usage: check_corner_exact degree");degree(std::stoul(argv[1]));return 0;}catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}}
