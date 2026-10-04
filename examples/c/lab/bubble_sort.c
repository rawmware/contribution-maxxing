#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int v[]={5,1,4,2,8};for(int i=0;i<5;i++)for(int j=0;j<4-i;j++)if(v[j]>v[j+1]){int t=v[j];v[j]=v[j+1];v[j+1]=t;}for(int i=0;i<5;i++)printf("%s%d",i?" ":"",v[i]);puts("");
    return 0;
}
