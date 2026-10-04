#include <iostream>
#include <string>

int main() {
    int v[]={-4,7,2,0};int m=v[0];for(int i=1;i<4;i++)if(v[i]>m)m=v[i];std::cout<<m<<"\n";
    return 0;
}
