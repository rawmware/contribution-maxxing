#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int a=240,b=46,old_r=a,r=b,old_s=1,s=0,old_t=0,t=1;while(r){int q=old_r/r;int z=old_r-q*r;old_r=r;r=z;z=old_s-q*s;old_s=s;s=z;z=old_t-q*t;old_t=t;t=z;}printf("%d %d %d\n",old_r,old_s,old_t);
    return 0;
}
