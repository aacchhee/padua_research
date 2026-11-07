// Review-only forwarding shim; frozen C11 source remains unchanged.
#include "../cheap_rows_C11/partial.cpp"
static long review_fault_at=0,review_partial_calls=0;
static B review_partial(long n,long q,const B&y){
 ++review_partial_calls;
 if(review_fault_at<0||review_partial_calls==review_fault_at)
  throw std::runtime_error("C15 independent partial fault");
 return partial(n,q,y);
}
#define partial review_partial
