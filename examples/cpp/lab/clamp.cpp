#include <iostream>
#include <string>

int main() {
    int v[]={17,-9,4};int lo=-3,hi=10;for(int i=0;i<3;i++){int x=v[i];if(x<lo)x=lo;if(x>hi)x=hi;std::cout<<(i?" ":"")<<x;}std::cout<<"\n";
    return 0;
}
