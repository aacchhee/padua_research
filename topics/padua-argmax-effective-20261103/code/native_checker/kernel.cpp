// Independent GMP reconstruction of PD-T101/PD-T210. No producer code linked.
#include <gmpxx.h>
#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <vector>
#include <string>
#include <stdexcept>
using Z=mpz_class; using Q=mpq_class;
const Z S=Z(1)<<192;
struct I { Z l=0,h=0; };
Z down(Q x){x.canonicalize(); Z z;mpz_fdiv_q(z.get_mpz_t(),x.get_num_mpz_t(),x.get_den_mpz_t());return z;}
Z up(Q x){return -down(-x);}
Z floor_pow2(Z x,unsigned bits){Z out;mpz_fdiv_q_2exp(out.get_mpz_t(),x.get_mpz_t(),bits);return out;}
Z ceil_pow2(Z x,unsigned bits){Z out;mpz_cdiv_q_2exp(out.get_mpz_t(),x.get_mpz_t(),bits);return out;}
I grid(Q x){return {down(x*S),up(x*S)};}
I add(I a,I b){return {a.l+b.l,a.h+b.h};}
I scale(I a,Z k){return k>=0?I{a.l*k,a.h*k}:I{a.h*k,a.l*k};}
I mul(I a,I b){std::vector<Z> v={a.l*b.l,a.l*b.h,a.h*b.l,a.h*b.h};return {floor_pow2(*std::min_element(v.begin(),v.end()),192),ceil_pow2(*std::max_element(v.begin(),v.end()),192)};}
Q ratio(Z a,Z b){Q q(a,b);q.canonicalize();return q;}
Q frac(long a,long b){Q q(a,b);q.canonicalize();return q;}
std::pair<std::pair<Q,Q>,int> atanb(int d){Q t=frac(1,d),sum=0,x2=frac(1,d*d),tol=Q(1,S<<32);int k=0;for(;;){Q v=t/(2*k+1);sum+=(k%2?-v:v);++k;t*=x2;Q r=t/(2*k+1);if(r<tol){Q o=sum+(k%2?-r:r);return {{std::min(sum,o),std::max(sum,o)},k};}}}
std::pair<Q,Q> cosb(Q x){Q t=1,sum=1,tol=Q(1,S<<32);int k=0;for(;;){++k;t*=x*x/((2*k-1)*(2*k));sum+=(k%2?-t:t);Q r=t*x*x/((2*k+1)*(2*k+2));if(r<tol){Q o=sum+(k%2?r:-r);return {std::min(sum,o),std::max(sum,o)};}}}
std::vector<I> axis(int n,Q pl,Q ph){I seed={grid(cosb(ph/n).first).l,grid(cosb(pl/n).second).h};std::vector<I> v={{S,S},seed};for(int j=2;j<=n;++j)v.push_back(add(scale(mul(seed,v.back()),2),scale(v[j-2],-1)));v[0]={S,S};v[n]={-S,-S};if(n%2==0)v[n/2]={0,0};return v;}
I mode(const std::vector<I>&v,int j,int p){int n=v.size()-1,r=j*p%(2*n);return v[std::min(r,2*n-r)];}
Z choose(int n,int k){if(k<0||k>n)return 0;Z z;mpz_bin_uiui(z.get_mpz_t(),n,k);return z;}
using Table=std::vector<I>;using Coeff=std::vector<Table>;
I linear(const std::vector<I>&v,const std::vector<Q>&w){Q l=0,h=0;for(size_t i=0;i<v.size();++i){l+=w[i]*(w[i]>=0?v[i].l:v[i].h);h+=w[i]*(w[i]>=0?v[i].h:v[i].l);}return {down(l),up(h)};}
std::pair<Coeff,Coeff> split(const Coeff&c,int n,int axis){int m=n+1;Coeff a=c,b=c;for(size_t z=0;z<c.size();++z)for(int f=0;f<m;++f){std::vector<I> row;for(int t=0;t<m;++t)row.push_back(c[z][axis==0?t*m+f:f*m+t]);for(int d=0;d<m;++d){a[z][axis==0?d*m+f:f*m+d]=row.front();b[z][axis==0?(n-d)*m+f:f*m+n-d]=row.back();for(int j=0;j<n-d;++j){row[j]={floor_pow2(row[j].l+row[j+1].l,1),ceil_pow2(row[j].h+row[j+1].h,1)};}row.pop_back();}}return {a,b};}
Z absmax(I x){Z a=abs(x.l),b=abs(x.h);return std::max(a,b);}
std::set<std::string> frontier,ancestors;
void walk(const Coeff& c,int n,Z threshold,std::string p,int flags){
 if(frontier.count(p)){std::vector<Z> b((n+1)*(n+1));for(auto&t:c)for(size_t i=0;i<b.size();++i)b[i]+=absmax(t[i]);Z mx=*std::max_element(b.begin(),b.end());if(mx<threshold){std::cout<<"{\"path\":\""<<p<<"\",\"kind\":\"bound\",\"upper\":"<<mx<<"}\n";return;}
 int corners[2][2]={{-1,-1},{n%2?-1:1,n%2?1:-1}};
 for(auto&e:corners){int fx=e[0]<0?1:2,fy=e[1]<0?4:8;if((flags&fx)&&(flags&fy)){int index=(e[0]<0?0:n)*(n+1)+(e[1]<0?0:n);Z other=0;for(size_t i=0;i<b.size();++i)if((int)i!=index)other=std::max(other,b[i]);if(other<threshold){std::cout<<"{\"path\":\""<<p<<"\",\"kind\":\"corner\",\"corner\":["<<e[0]<<","<<e[1]<<"],\"upper_away_from_vertex\":"<<other<<"}\n";return;}}}
 std::cout<<"{\"path\":\""<<p<<"\",\"kind\":null}\n";return;
 }
 if(!ancestors.count(p))throw std::runtime_error("uncovered partition");auto halves=split(c,n,p.size()%2);int axis=p.size()%2;walk(halves.first,n,threshold,p+"0",flags&~(axis==0?2:8));walk(halves.second,n,threshold,p+"1",flags&~(axis==0?1:4));
}
int main(int argc,char**argv){try{if(argc!=2)throw std::runtime_error("degree required");int n=std::stoi(argv[1]);if(n<2||n>100)throw std::runtime_error("degree outside supported range");auto a=atanb(5),b=atanb(239);Q pl=16*a.first.first-4*b.first.second,ph=16*a.first.second-4*b.first.first;auto x=axis(n,pl,ph),y=axis(n+1,pl,ph);int m=n+1;std::vector<std::vector<Z>> t(m,std::vector<Z>(m));t[0][0]=1;t[1][1]=1;for(int p=2;p<=n;++p)for(int i=0;i<=n;++i)t[p][i]=(i?2*t[p-1][i-1]:Z(0))-t[p-2][i];
 std::vector<std::vector<Q>> w(m,std::vector<Q>(m));for(int k=0;k<=n;++k)for(int i=0;i<=n;++i)for(int r=0;r<=std::min(k,i);++r)w[k][i]+=ratio(choose(i,r)*choose(k,r)*(Z(1)<<r)*( ((i-r)%2)?-1:1),choose(n,r));
 Coeff coeff;I cb[2];for(int j=0;j<=n;++j)for(int k=0;k<=n+1;++k)if((j+k)%2==0){Table poly(m*m);Q weight=frac(2,n*(n+1));if(j==0||j==n)weight/=2;if(k==0||k==n+1)weight/=2;for(int p=0;p<=n;++p)for(int q=0;q<=n-p;++q){int h=(p?2:1)*(q?2:1);if(p==n&&q==0)h=1;I z=mul(mul(mode(x,j,p),mode(y,k,q)),grid(weight*h));for(int u=0;u<=p;++u)if(t[p][u]!=0)for(int v=0;v<=q;++v)if(t[q][v]!=0)poly[u*m+v]=add(poly[u*m+v],scale(z,t[p][u]*t[q][v]));}
 for(int e=0;e<2;++e){I z;int cx=(e&&n%2==0)?1:-1,cy=(e&&n%2)?1:-1;for(int u=0;u<=n;++u)for(int v=0;v<=n;++v)z=add(z,scale(poly[u*m+v],((cx<0&&u%2)^(cy<0&&v%2))?-1:1));Z low=(z.l>0?z.l:(z.h<0?-z.h:Z(0)));cb[e].l+=low;cb[e].h+=absmax(z);}
 Table mid(m*m),out(m*m);for(int v=0;v<=n;++v){std::vector<I> vals;std::vector<int> powers;for(int u=0;u<=n;++u)if(poly[u*m+v].l!=0||poly[u*m+v].h!=0){vals.push_back(poly[u*m+v]);powers.push_back(u);}for(int r=0;r<=n;++r){std::vector<Q> weights;for(int u:powers)weights.push_back(w[r][u]);mid[r*m+v]=linear(vals,weights);}}for(int r=0;r<=n;++r){std::vector<I> vals;for(int v=0;v<=n;++v)vals.push_back(mid[r*m+v]);for(int s=0;s<=n;++s)out[r*m+s]=linear(vals,w[s]);}coeff.push_back(std::move(out));}
 Z low=std::max(cb[0].l,cb[1].l),high=std::min(cb[0].h,cb[1].h);if(!(S<low&&low<=high))throw std::runtime_error("invalid threshold");std::cout<<"{\"n\":"<<n<<",\"precision\":192,\"scale\":"<<S<<",\"threshold_interval\":["<<low<<","<<high<<"],\"pi_interval\":[\""<<pl<<"\",\""<<ph<<"\"],\"machin_terms\":["<<a.second<<","<<b.second<<"],\"x_cosine_seed\":["<<x[1].l<<","<<x[1].h<<"],\"y_cosine_seed\":["<<y[1].l<<","<<y[1].h<<"],\"cardinals\":"<<coeff.size()<<"}\n";
 std::string p;while(std::getline(std::cin,p)){if(p=="-")p="";if(p.size()>100||p.find_first_not_of("01")!=std::string::npos)throw std::runtime_error("invalid path");if(!frontier.insert(p).second)throw std::runtime_error("duplicate path");for(size_t i=0;i<p.size();++i)ancestors.insert(p.substr(0,i));}for(auto&p:frontier)if(ancestors.count(p))throw std::runtime_error("prefix overlap");if(frontier.empty())throw std::runtime_error("empty frontier");walk(coeff,n,low,"",15);return 0;
 }catch(const std::exception&e){std::cerr<<e.what()<<"\n";return 1;}}
