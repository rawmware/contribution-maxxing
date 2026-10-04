#include <iostream>
#include <string>

int main() {
    unsigned long long n=27;int steps=0;while(n!=1){n=n%2?3*n+1:n/2;steps++;}std::cout<<steps<<"\n";
    return 0;
}
