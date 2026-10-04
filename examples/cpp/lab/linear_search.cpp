#include <iostream>
#include <string>

int main() {
    int v[]={4,8,15,16,23,42},x=16,i=0;while(i<6&&v[i]!=x)i++;std::cout<<(i<6?i:-1)<<"\n";
    return 0;
}
