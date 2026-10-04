#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int v[]={1,2,3,4,5},sum=0;for(int i=0;i<5;i++)sum+=v[i];printf("%d\n",sum);
    return 0;
}
