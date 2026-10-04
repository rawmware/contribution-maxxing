#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    int v[]={4,8,15,16,23,42},x=16,i=0;while(i<6&&v[i]!=x)i++;printf("%d\n",i<6?i:-1);
    return 0;
}
