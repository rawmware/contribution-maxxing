#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    unsigned long long n=27;int steps=0;while(n!=1){n=n%2?3*n+1:n/2;steps++;}printf("%d\n",steps);
    return 0;
}
