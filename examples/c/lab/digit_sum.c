#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int n=9876,sum=0;while(n){sum+=n%10;n/=10;}printf("%d\n",sum);
    return 0;
}
