#include <iostream>
#include <string>

int main() {
    long long base=7,exp=128,mod=1000,result=1;while(exp){if(exp&1)result=result*base%mod;base=base*base%mod;exp>>=1;}std::cout<<result<<"\n";
    return 0;
}
