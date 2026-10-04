#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int a[]={1,2,3},b[]={4,5,6},sum=0;for(int i=0;i<3;i++)sum+=a[i]*b[i];printf("%d\n",sum);
    return 0;
}
