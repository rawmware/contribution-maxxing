#include <stdio.h>
#include <string.h>
#include <stddef.h>

int main(void) {
    const char*s="polyglot";size_t n=0;while(s[n])n++;printf("%s %zu\n",s,n);
    return 0;
}
