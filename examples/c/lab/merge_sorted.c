#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int a[]={0,2,7},b[]={1,3,8},o[6],i=0,j=0,k=0;while(i<3&&j<3)o[k++]=a[i]<b[j]?a[i++]:b[j++];while(i<3)o[k++]=a[i++];while(j<3)o[k++]=b[j++];for(i=0;i<6;i++)printf("%s%d",i?" ":"",o[i]);puts("");
    return 0;
}
