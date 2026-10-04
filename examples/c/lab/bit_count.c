#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    unsigned int x=0xB5u;int n=0;while(x){n+=(int)(x&1u);x>>=1;}printf("%d\n",n);
    return 0;
}
