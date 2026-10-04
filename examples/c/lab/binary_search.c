#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int v[]={1,3,5,7,9};int lo=0,hi=4,x=5,ans=-1;while(lo<=hi){int mid=lo+(hi-lo)/2;if(v[mid]==x){ans=mid;break;}if(v[mid]<x)lo=mid+1;else hi=mid-1;}printf("%d\n",ans);
    return 0;
}
