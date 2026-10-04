#include <iostream>
#include <string>

int main() {
    int n=9876,sum=0;while(n){sum+=n%10;n/=10;}std::cout<<sum<<"\n";
    return 0;
}
