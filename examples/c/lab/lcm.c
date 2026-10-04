#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int a=21,b=6,x=a,y=b;while(y){int r=x%y;x=y;y=r;}printf("%d\n",a/x*b);
    return 0;
}
