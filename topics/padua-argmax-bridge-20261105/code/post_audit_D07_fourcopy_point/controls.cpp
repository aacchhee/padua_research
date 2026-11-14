// Independent finite divided-difference reference; not a production fallback.
#include "point.cpp"
static B reference_cos7(const Q&t){B p,x,v;arb_const_pi(p.x,512);arb_set_fmpq(x.x,t.x,512);arb_mul(x.x,x.x,p.x,512);arb_cos(v.x,x.x,512);return v;}
static bool collision7(const Q&u,const Q&v){Q a=(u-v)/Q(2),b=(u+v)/Q(2);return fmpz_is_one(fmpq_denref(a.x))||fmpz_is_one(fmpq_denref(b.x));}
static B reference_g7(long n,const Q&u,const Q&v){
 B x=reference_cos7(u),y=reference_cos7(v),tn,tm,un,um,p,q,a,b,out;
 if(collision7(u,v)){
  arb_chebyshev_u_ui(un.x,n-1,y.x,512);arb_chebyshev_u_ui(um.x,n,y.x,512);
  arb_mul_si(p.x,un.x,n,512);arb_mul_si(q.x,um.x,n+1,512);arb_add(out.x,p.x,q.x,512);
 }else{
  arb_chebyshev_t_ui(tn.x,n,x.x,512);arb_chebyshev_t_ui(tm.x,n+1,x.x,512);arb_add(p.x,tn.x,tm.x,512);
  arb_chebyshev_t_ui(tn.x,n,y.x,512);arb_chebyshev_t_ui(tm.x,n+1,y.x,512);arb_add(q.x,tn.x,tm.x,512);
  arb_sub(a.x,p.x,q.x,512);arb_sub(b.x,x.x,y.x,512);if(arb_contains_zero(b.x))throw std::runtime_error("reference separated denominator unresolved");arb_div(out.x,a.x,b.x,512);
 }
 arb_chebyshev_t_ui(tn.x,n,x.x,512);arb_sub(out.x,out.x,tn.x,512);return out;
}
static B reference_lambda7(long n,const Q&xi,const Q&ze){B total;
 for(long r=0;r<=n+1;r++)for(long j=1-r%2;j<=n;j+=2){B four,term;for(long sig:{-1L,1L})for(long tau:{-1L,1L}){term=reference_g7(n,xi+Q(sig*j)/Q(n),ze+Q(tau*r)/Q(n+1));arb_add(four.x,four.x,term.x,512);}arb_abs(four.x,four.x);arb_div_si(four.x,four.x,(r==0||r==n+1?2:1)*(j==0||j==n?2:1),512);arb_add(total.x,total.x,four.x,512);}
 arb_div_si(total.x,total.x,2*n*(n+1),512);if(!arb_is_finite(total.x))throw std::runtime_error("reference nonfinite");return total;
}
extern "C" int d07_reference(long n,const char*x,const char*z,double*out){try{if(n<2||n>128)return 2;Q xi=parse7(x),ze=parse7(z);B ref=reference_lambda7(n,xi,ze);export7(ref,out);return 0;}catch(...){return 1;}}
extern "C" int d07_compare(long n,const char*x,const char*z,double*out,long*counts){try{if(n<2||n>128)return 2;Q xi=parse7(x),ze=parse7(z);Count7 st;B value=lambda7(n,xi,ze,st),ref=reference_lambda7(n,xi,ze);out[0]=arb_overlaps(value.x,ref.x);out[1]=arb_contains(value.x,ref.x);out[2]=arb_contains(ref.x,value.x);export7(value,out+3);export7(ref,out+6);long v[]={st.rows,st.eta,st.fallback,st.rootfail,st.signfail,st.direct,st.blocks,st.partials,st.roots,st.axis,st.node,st.corner,st.maxdirect};for(int i=0;i<13;i++)counts[i]=v[i];return 0;}catch(...){return 1;}}
