#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int v[]={17,-9,4};int lo=-3,hi=10;for(int i=0;i<3;i++){int x=v[i];if(x<lo)x=lo;if(x>hi)x=hi;printf("%s%d",i?" ":"",x);}puts("");
    return 0;
}
