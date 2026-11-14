// Independent512-bit finite cosine reference, used only by bounded controls.
#include "global.cpp"
static void ref_ratio12(arb_t out,long k,const arb_t z){arb_zero(out);arb_t a,c;arb_init(a);arb_init(c);for(long j=0;j<k;j++){arb_mul_si(a,z,k-1-2*j,512);arb_cos(c,a,512);arb_add(out,out,c,512);}arb_clear(a);arb_clear(c);}
extern "C" int c12_reference(long n,const char*as,const char*bs,double*out){try{if(n<2||n>32)return 1;Q a=parse12(as),b=parse12(bs);if(fmpq_sgn(a.x)<0||fmpq_sgn(b.x)<0||fmpq_cmp_si((a+b).x,1)>0)return 1;arb_t pi,a0,b0,u,v,s,t,x,y,z,w,g,c,total;arb_ptr vars[]={pi,a0,b0,u,v,s,t,x,y,z,w,g,c,total};for(auto q:vars)arb_init(q);arb_const_pi(pi,512);arb_set_fmpq(a0,a.x,512);arb_set_fmpq(b0,b.x,512);arb_zero(total);
 for(long r=0;r<2*(n+1);r++){long delta=(1-r)%2;if(delta<0)delta+=2;for(long k=0;k<n;k++){
  arb_add_si(u,a0,delta+2*k,512);arb_mul(u,u,pi,512);arb_div_si(u,u,n,512);arb_add_si(v,b0,r,512);arb_mul(v,v,pi,512);arb_div_si(v,v,n+1,512);arb_add(s,u,v,512);arb_mul_2exp_si(s,s,-1);arb_sub(t,u,v,512);arb_mul_2exp_si(t,t,-1);
  ref_ratio12(x,n+1,s);ref_ratio12(y,n+1,t);ref_ratio12(z,n,s);ref_ratio12(w,n,t);arb_mul(g,x,y,512);arb_mul(c,z,w,512);arb_add(g,g,c,512);arb_mul_si(c,u,n,512);arb_cos(c,c,512);arb_sub(g,g,c,512);arb_mul_2exp_si(g,g,-1);arb_abs(g,g);arb_add(total,total,g,512);
 }}arb_div_si(total,total,n*(n+1),512);arf_t f;arf_init(f);arb_get_lbound_arf(f,total,512);out[0]=arf_get_d(f,ARF_RND_FLOOR);arb_get_ubound_arf(f,total,512);out[1]=arf_get_d(f,ARF_RND_CEIL);arf_clear(f);for(auto q:vars)arb_clear(q);return 0;}catch(...){return 1;}}
// Direct root-family edge controls use exact dyadic artificial coefficients.
extern "C" int c12_root_control(long n,long c,long p,long delta,const char*al,const char*ah,long*out){try{B a=range12(qb12(parse12(al)),qb12(parse12(ah)))*pi();std::set<long>D,cuts{0,n},E;numerator12(B(c),B(p),n,delta,a,D,cuts,E);out[0]=E.size();out[1]=cuts.size();return 0;}catch(...){return 1;}}
