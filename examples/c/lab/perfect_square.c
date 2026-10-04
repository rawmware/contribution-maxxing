#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int v[]={0,49,50},out[3];for(int k=0;k<3;k++){int i=0;while(i*i<v[k])i++;out[k]=(i*i==v[k]);}printf("%d %d\n",out[1],out[2]);
    return 0;
}
