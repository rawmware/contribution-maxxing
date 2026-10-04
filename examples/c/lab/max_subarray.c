#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int v[]={-2,1,-3,4,-1,2,1,-5,4},best=v[0],cur=v[0];for(int i=1;i<9;i++){cur=cur>0?cur+v[i]:v[i];if(cur>best)best=cur;}printf("%d\n",best);
    return 0;
}
