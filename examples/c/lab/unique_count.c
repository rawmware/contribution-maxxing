#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int v[]={2,1,2,3,1,4},n=6,count=0;for(int i=0;i<n;i++){int seen=0;for(int j=0;j<i;j++)if(v[j]==v[i])seen=1;if(!seen)count++;}printf("%d\n",count);
    return 0;
}
