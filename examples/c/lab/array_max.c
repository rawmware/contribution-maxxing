#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int v[]={-4,7,2,0};int m=v[0];for(int i=1;i<4;i++)if(v[i]>m)m=v[i];printf("%d\n",m);
    return 0;
}
