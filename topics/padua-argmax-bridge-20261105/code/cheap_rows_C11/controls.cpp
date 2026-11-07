#include "point.cpp"
#include <ctime>
// Immutable accepted exact-rational implementation, diagnostic namespace only.
#define c06_partial old_c06_partial
#define c06_partial_arb old_c06_partial_arb
#define c06_compare old_c06_compare
#define c06_budget old_c06_budget
namespace Old {
#include "../cheap_rows_C06/partial.cpp"
}
#undef c06_partial
#undef c06_partial_arb
#undef c06_compare
#undef c06_budget
static B directsum(long n,long q,const B&y){B sum,p;arb_const_pi(p.x,512);for(long i=0;i<q;i++){B x,c;arb_add_si(x.x,y.x,i,512);arb_mul(x.x,x.x,p.x,512);arb_div_si(x.x,x.x,n,512);arb_cot(c.x,x.x,512);arb_add(sum.x,sum.x,c.x,512);}return sum;}
extern "C" int c11_partial_control(long n,long q,const char*ys,double*out){try{B y;if(arb_set_str(y.x,ys,P))return 2;B a=partial(n,q,y),l,u;arf_t fl,fu;arf_init(fl);arf_init(fu);arb_get_lbound_arf(fl,y.x,512);arb_get_ubound_arf(fu,y.x,512);arb_set_arf(l.x,fl);arb_set_arf(u.x,fu);arf_clear(fl);arf_clear(fu);B rl=directsum(n,q,l),ru=directsum(n,q,u),ref;arb_union(ref.x,rl.x,ru.x,512);B old;Old::B oy;arb_set(oy.x,y.x);Old::B oa=Old::partial(n,q,oy);arb_set(old.x,oa.x);out[0]=arb_contains(a.x,ref.x);out[1]=arb_overlaps(a.x,old.x);out[2]=mag_get_d(arb_radref(a.x));out[3]=mag_get_d(arb_radref(old.x));return 0;}catch(...){return 1;}}
extern "C" int c11_moment_control(){int checks=0;for(long n:{2L,7L,33L,64L})for(long q:{1L,n}){B y;arb_set_si(y.x,1);arb_mul_2exp_si(y.x,y.x,-1);auto m=moments(n,q,y);for(int d=0;d<=33;d++){Q total;for(long i=0;i<q;i++){Q z=(Q(1)/Q(2)+Q(i))/Q(n)-Q(1)/Q(2);total=total+powerq(z,d);}if(!arb_contains_fmpq(m[d].x,total.x))return -1;checks++;}}return checks;}
