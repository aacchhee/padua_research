// D01: positive finite sums on exactly C07's regular odd board.
// Long-double diagnostics; mathematical scope and envelope are in SPEC.md.
#include <cmath>
#include <iomanip>
#include <iostream>
#include <array>
#include <algorithm>
#include <cstdlib>
#include <fstream>
using R=long double;
using V=std::array<R,4>;
V term(long n,long j,long r){
 R s=j+r-R(1)/6,g=std::fabs(R(j-r)+R(j)/n)-R(1)/6;
 if(!(s>0&&g>0)) std::abort();
 return {1/(s*g*g*g),1/(s*s*s*g),1/(s*s*g*g),1/(g*g)};
}
int main(int argc,char**argv){
 if(const char* p=std::getenv("D01_MAPS")){std::ifstream in("/proc/self/maps");std::ofstream out(p);out<<in.rdbuf();}
 if(argc!=4)return 2;
 long n=std::stol(argv[1]),D=std::stol(argv[2]),mode=std::stol(argv[3]),m=n+1;
 if(n<2||D<1||!(D%2)||mode<0||mode>1)return 2;
 V low{},tail{};unsigned long long count=0,omitted=0;
 if(mode==1){
  for(long j=0;j<=n;++j)for(long r=0;r<=m;++r){
   if((j+r)%2==0||(r==j+1&&2*j>=n))continue;
   auto x=term(n,j,r);for(int k=0;k<4;++k)low[k]+=x[k];++count;
  }
 }
 for(long l=1;mode==0&&l<=m;l+=2) for(int sign:{1,-1}){
  long lo=sign>0?l:0,hi=sign>0?n:std::min(n,m-l);
  if(sign<0&&l==1)hi=(n-1)/2;
  if(lo>hi)continue;
  if(l<=D||mode==1){
   for(long j=lo;j<=hi;++j){long r=j-sign*l;auto x=term(n,j,r);
    for(int k=0;k<4;++k)low[k]+=x[k];++count;}
  }else{
   // Each positive summand <= product of the separate denominator minima.
   R s=R(2*lo-sign*l)-R(1)/6;
   R g=sign>0?R(l)+R(lo)/n-R(1)/6:R(l)-R(hi)/n-R(1)/6;
   R q=hi-lo+1;
   V x={q/(s*g*g*g),q/(s*s*s*g),q/(s*s*g*g),q/(g*g)};
   for(int k=0;k<4;++k)tail[k]+=x[k];omitted+=hi-lo+1;
  }
 }
 R b20=0,c20=0;unsigned long long board=0;
 for(long s=1;s<=2*n+1;s+=2){
  long lo=std::max(0L,s-m),hi=std::min(n,s),q=std::max(0L,hi-lo+1),j=(s-1)/2;
  if(j>=lo&&j<=hi&&2*j>=n)--q;
  board+=q;b20+=R(q)/std::pow(R(s)-R(1)/6,2);
  c20+=R(q)/std::pow(R(2*n+1-s)-R(1)/6,2);
 }
 if(board!=count+omitted)return 3;
 // Alternative uniform diagonal tails supplied by the analytic partner.
 if(!mode&&D<m){R q=R(D+2)-R(7)/6;
  auto H=[&](int p){return std::pow(q,-p)+std::pow(q,1-p)/(2*(p-1));};
  V uniform={2*H(4)+std::log(1+R(2)*n/q)*H(3),2*H(4)+H(3)/2,2*H(4)+H(3),R(2)*(n+1)*H(2)};
  for(int k=0;k<4;++k)tail[k]=std::min(tail[k],uniform[k]);
 }
 std::cout<<std::setprecision(24)<<"{\"n\":"<<n<<",\"D\":"<<D<<",\"full\":"<<(mode?"true":"false")<<",\"enumerated\":"<<count<<",\"omitted\":"<<omitted<<",\"board\":"<<board<<",\"sums_low\":[";
 for(int k=0;k<4;++k)std::cout<<(k?",":"")<<low[k];
 std::cout<<"],\"tail_upper\":[";
 for(int k=0;k<4;++k)std::cout<<(k?",":"")<<tail[k];
 std::cout<<"],\"B20\":"<<b20<<",\"C20\":"<<c20<<"}\n";
}
