// Diagnostic side channel only. Generated point_rows.cpp is the frozen C11
// point.cpp with two assignment-only row captures; arithmetic is unchanged.
#include "point_rows.cpp"
extern "C" int d01_rows(long n,const char*astr,const char*bstr,double*out,double*total){
 try { Q a,b;if(fmpq_set_str(a.x,astr,10)||fmpq_set_str(b.x,bstr,10))return 2;
  fmpq_canonicalise(a.x);fmpq_canonicalise(b.x);
  std::vector<B> rows(2*(n+1));d01_capture=&rows;Stats st;
  B answer=pointS(n,a,b,st);d01_capture=nullptr;
  arf_t l,u;arf_init(l);arf_init(u);
  for(long r=0;r<2*(n+1);r++){
   B x=rows[r]/(B(n)*B(n+1));
   arb_get_lbound_arf(l,x.x,P);arb_get_ubound_arf(u,x.x,P);
   out[2*r]=arf_get_d(l,ARF_RND_FLOOR);out[2*r+1]=arf_get_d(u,ARF_RND_CEIL);
  }
  arb_get_lbound_arf(l,answer.x,P);arb_get_ubound_arf(u,answer.x,P);
  total[0]=arf_get_d(l,ARF_RND_FLOOR);total[1]=arf_get_d(u,ARF_RND_CEIL);
  arf_clear(l);arf_clear(u);return 0;
 }catch(...){d01_capture=nullptr;return 1;}
}
static B d01_cotnorm(long n,const Q&y){
 Q t=y-Q(floorq(y));if(fmpq_is_zero(t.x))throw std::runtime_error("collision cotnorm");
 Q q=Q(n)/Q(2)-t;long count=floorq(q);if(fmpz_cmp_si(fmpq_denref(q.x),1)!=0)count++;
 B positive=partial(n,count,qb(t)),negative=partial(n,n-count,qb(t+Q(count)));
 return positive-negative;
}
extern "C" int d01_poles(long n,const char*astr,const char*bstr,double*out,int*kinds){
 try {Q af,bf;if(fmpq_set_str(af.x,astr,10)||fmpq_set_str(bf.x,bstr,10))return 2;
 fmpq_canonicalise(af.x);fmpq_canonicalise(bf.x);long m=n+1;
 B alpha=pi()*qb(af),beta=pi()*qb(bf),p=sinb(alpha),q=sinb(beta),a=(cosb(alpha)+cosb(beta))/B(2);
 arf_t l,u;arf_init(l);arf_init(u);
 for(long r=0;r<2*m;r++){
  long delta=(1-r)%2;if(delta<0)delta+=2;
  Q sigma=(Q(delta)+af)/Q(2),vf=(Q(r)+bf)/Q(m);
  Q ym=sigma-Q(n)*vf/Q(2),yp=sigma+Q(n)*vf/Q(2);
  bool collision=fmpz_is_one(fmpq_denref(ym.x))||fmpz_is_one(fmpq_denref(yp.x));
  int kind=(r<64||r>=2*m-64)?1:collision?2:(r==m-1||r==m)?3:0;kinds[r]=kind;
  if(kind){out[2*r]=out[2*r+1]=0;continue;}
  B v=pi()*qb(vf),cotv=cotb(v/B(2)),C=(p-q-B(2)*a*cotv)/B(4),D=(p+q+B(2)*a*cotv)/B(4);
  B value=(absolute(C)*d01_cotnorm(n,ym)+absolute(D)*d01_cotnorm(n,yp))/(B(n)*B(m));
  arb_get_lbound_arf(l,value.x,P);arb_get_ubound_arf(u,value.x,P);
  out[2*r]=arf_get_d(l,ARF_RND_FLOOR);out[2*r+1]=arf_get_d(u,ARF_RND_CEIL);
 }
 arf_clear(l);arf_clear(u);return 0;
 }catch(...){return 1;}
}
