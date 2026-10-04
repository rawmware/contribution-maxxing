#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int v[]={9,3,7,-1,3};for(int i=1;i<5;i++){int x=v[i],j=i;while(j>0&&v[j-1]>x){v[j]=v[j-1];j--;}v[j]=x;}for(int i=0;i<5;i++)printf("%s%d",i?" ":"",v[i]);puts("");
    return 0;
}
