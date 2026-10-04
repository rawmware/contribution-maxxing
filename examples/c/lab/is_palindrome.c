#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    const char*s="level";int n=(int)strlen(s),ok=1;for(int i=0;i<n/2;i++)if(s[i]!=s[n-1-i])ok=0;const char*t="hello";int m=(int)strlen(t),ok2=1;for(int i=0;i<m/2;i++)if(t[i]!=t[m-1-i])ok2=0;printf("%d %d\n",ok,ok2);
    return 0;
}
