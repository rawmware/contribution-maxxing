#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int n=123456,rev=0;while(n){rev=rev*10+n%10;n/=10;}printf("%d\n",rev);
    return 0;
}
