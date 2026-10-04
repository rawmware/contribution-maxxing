#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int a[3][3]={{1,2,3},{4,5,6},{7,8,9}},sum=0;for(int i=0;i<3;i++)sum+=a[i][i];printf("%d\n",sum);
    return 0;
}
