// Review-only forwarding shim. The frozen box source includes this file.
// Normal controls forward unchanged; fault controls exercise its row catch.
#include "../cheap_rows_C11/partial.cpp"
static long review_fault_at=0,review_partial_calls=0;
static B review_partial(long n,long q,const B&y){
 ++review_partial_calls;
 if(review_fault_at<0||review_partial_calls==review_fault_at)
  throw std::runtime_error("review injected partial failure");
 return partial(n,q,y);
}
#define partial review_partial
